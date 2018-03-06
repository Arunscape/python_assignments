import sys
import traceback

"""
Simple compiler for expression-based calculator, with variables.
The expression language is pecisely defined by the ExprParser class.
In general, it is the usual arithmetic formulas, with the additional
ability to bind variable names to values, and use the value a variable is bound to.

The result of a successful compile is Python3 code that,
when executed, should return the same value as the calculator program.

Run the doctests with
    python3 compiler.py
"""

from exprparser import ExprParser

class Compiler():
    """
    A Compiler is a service for taking sequences of strings that
    represent formulas and compiling them into sequences of Python3 code.
    """

    def __init__(self):
        """
        Build an expression parser to get the AST for the input string

        Side Effect:
        This will generate, if not present and up-to-date,
        the parse tables:
            parser.out, parsetab.py
        in the current directory.

        If self.debug is set,
        debugging info must be printed during compilation.
        """

        self.parser = ExprParser()
        self.debug = False


    def compile(self, expr_str, code):
        """
        Compile the expression given by expr_string into a Python code fragment
        that when executed will achieve the same effect as evaluating the expression.
        It means that the result of executing the sequence of statements is the same
        as if they were processed by the calculator program.

        Inputs:
            expr_str - a string in the expression language
            code - prior lines of code to which this compile is appended.
                It is a list of strings,
                each string being a single-line Python statement.
                All lines have an equal indentation of 0 spaces.

        Outputs:
            Returns:
                Normally returns None.
                It returns a diagnostic string when there is a problem.

            code - is updated by appending the newly added code.
                If there was an error in code generation parsing,
                this will be unchanged.
                During code generation, the code list will grow;
                we should remember its initial lenght
                and roll back any changes if we encounter an error.

                At some point in the code is the statement
                    _result = expr...
                which binds _result to the value of the expression being calculated.
                After that there are lines of cleanup code that remove
                any intermediate variable generations and ensure that
                the actual variable is updated.

        Example:
            the expression
                (x = 2) + (y = (x + 1)) + (x = y + x)
            results in the code list containing

                # code for:
                # (x = 2) + (y = (x + 1)) + (x = y + x)
                _x_1 = 2
                _y_1 = (_x_1 + 1)
                _x_2 = (_y_1 + _x_1)
                _result = ((_x_1 + _y_1) + _x_2)
                # Update and cleanup x
                x = _x_2
                del(_x_1)
                del(_x_2)
                # Update and cleanup y
                y = _y_1
                del(_y_1)

            and if you want to actually print the value of the expression
            you can add this to the end:
                print(_result)

        """

        # Evaluation proceeds in two steps.  First parse the string into
        # an AST, represented by a ValueTree.
        # Then traverse the AST converting it into one or more lines of
        # Python3 code.

        # The parser normally should not raise any execeptions,
        # if it does we want to die with a proper traceback.
        (errors, ast) = self.parser.parse(expr_str)

        if len(errors) > 0:
            return "Parsing generated errors:\n{}".format(
                    "\n".join(errors))

        if ast is None:
            return None

        if self.debug:
            print("Initial ast:", ast.tree_to_valshape())

        # Variable generation dictionary,
        # maps variable name to current generation number.
        var_dict = {}

        # Remember the initial length of the code
        # in case we need to rollback any changes.
        initial_code_len = len(code)

        code.append("# code for:")
        code.append("# {}".format(expr_str))

        try:
            last_expr = self.compile_ast(ast, var_dict, code)
            # we need to save the value of the last expression
            # in the special variable _result.
            code.append("{} = {}".format('_result', last_expr))
        except ValueError as e:
            # roll back the changes to code, and return the error message
            if len(code) > initial_code_len:
                code[:] = code[0:initial_code_len]
            return e


        # Also emit Python code to set variables back to their
        # generation number and delete generations other than 0.
        # This should leave var_dict in a state of each variable being
        # associated with generation 0

        def key_fn(t):
            # sort by identifier name, grouping the _ versions after
            # the gen 0 name.
            return "_"+t[0] if t[0][0:1] != "_" else t[0]

        for v, gen in sorted(var_dict.items(), key=key_fn):
            if gen is not None and gen > 0:
                code.append("# Update and cleanup {}".format(v))
                v_gen_name = self.make_gen_name(v, gen)
                code.append("{} = {}".format(v, v_gen_name))
                var_dict[v] = 0

                # Delete all previous generations > 0 from the
                # execution context.
                for g in range(1,gen+1):
                    code.append("del({})".format(self.make_gen_name(v, g)))

        # All OK!
        return None


    def make_gen_name(self, name, gen_num):
        """
        When multiple assignments to a variable are made
        in an expression we need to create generation numbers.
        See compile_ast below for the format of names.
        """

        if gen_num > 0:
            return "_{}_{}".format(name, str(gen_num))
        return name

    def compile_ast(self, ast, var_dict, code = None):
        """
        Traverse the AST, and return the line of code that evaluates the
        expression, adding additional instructions as required to the code list.
        Normally an expression translates directly into one line of Python.

        When there are no assignment operations (i.e., =) in the expression,
        it is translated directly into a single executable line of Python.
        This is the unparse operation we are familiar with.

        But if the expression contains assignment operations like
            4 + (y = (x = 2) + 3)
        it is not legal Python, and a single line of code is insufficient.
        In this case we need to break the expression up into parts,
        compute each part with a Python statement, and combine the parts.
        This additional code is added to the code list to compute the assignment,
        and we just return the name of an intermediate variable that holds
        the value of the sub expression.
        For example, the above requires adding these two statements to code:
            _x_1 = 2
            _y_1 = (_x_1 + 3)
        before returning this line of code:
            (4 + _y_1)

        This case is relatively simple, but if a variable is mentioned many times,
        then the assignments operate from left to right, and
        many generations of a variable are needed to compute the final result.

        So, when there are assignment operations, then every time an assignment is performed,
        we need to introduce a temporary variable to capture the value of that expression
        in order to properly evaluate in left to right order. For example in
            (x = 1) + (x = x + 2) + (x = x + 42)
        we have to make sure that the x on the rhs of x = x + 2 is
        the x in the first term (x = 1), and the x on the rhs of
        x = x + 42 refers to the value of x after the x = x + 2
        term in the middle is executed.
        The final value of the expression is clearly not
            x + x + x
        It is these added to code:
            _x_1 = 1
            _x_2 = (_x_1 + 2)
            _x_3 = (_x_2 + 42)
        with this returned:
            ((_x_1 + _x_2) + _x_3)

        Note that
            (x = 2 + (x = 3) + (x = 4) + (x = 5))
        and
            (x = 2) + (x = 3) + (x = 4) + (x = 5)
        are very different expressions!  They both evaluate to 14,
        but x = 15 in the first, and x = 5 in the second.

        The added code for the first is
            _x_1 = 3
            _x_2 = 4
            _x_3 = 5
            _x_4 = (((2 + _x_1) + _x_2) + _x_3)
        returning
            _x_4
        which is the most current value of x


        and the added code for the second is
            _x_1 = 2
            _x_2 = 3
            _x_3 = 4
            _x_4 = 5
        returning
            (((_x_1 + _x_2) + _x_3) + _x_4)
        with _x_4 again the most current value of x

        As expressions are traversed, each time a variable is assigned
        we introduce a new "generation" of that variable.
        Later references to that variable (further to the right or down in the expression)
        will reference not "x" but the "current generation" of x.
        The purpose of var_dict is to map a variable name to the current
        generation number of that variable.
        Generation 0 of x is just the name x,
        while for generation n > 0, the name is _x_n, (as in _x_1, _x_2, ...)

        Returns:

        A string s that is the Python expression that evaluates the expression in the ast,
        assuming that all the statements in code are evaluated prior to evaluating s.

        """
        if code is None:
            code = []

        ntype = ast.get_value()
        children = ast.get_children()

        if ntype == 'const':
            code_str = str(children[0].get_value())

        elif ntype == 'get':
            # Reference to a variable
            # Make sure that the current generation is referenced.
            # If the variable is not in the var_dict,
            # it means that it has not been assigned to yet.
            # But, we don't consider this an error,
            # as it might be properly assigned by some code
            # that is pre-pended to the code list later.

            name = children[0].get_value()

            # get the latest generation number of name,
            # and if not present set to 0.
            gen_num = var_dict.get(name, 0)
            code_str = self.make_gen_name(name, gen_num)

        elif ntype == 'set':
            # bind name to value, finish off the current expression and start a new one.
            # The rhs needs to be output to the code list, and
            # the lhs appears as a name in the current expresion being built.


            code_str = ""
            name =children[0].get_value()

            #get value to assign
            val =self.compile_ast(children[1],var_dict,code)
            
            #get position in code list
            pos= var_dict.get(name,0)
            #increment each time
            var_dict[name]=pos+1

            #update name
            name=self.make_gen_name(name,var_dict[name])

            #add code
            # code += '{}={}'.format(name,val) #doesn't play nice with lists
            code.append('{} = {}'.format(name,val))

            #finally, generate python code
            code_str += str(name)

        elif ntype == 'apply':
            # Attempt to unparse the AST into something that python can understand.
            # Binary operations have 3 children, neg (i.e. unary minus)
            # and sqr() have 2 children, and anything else looks like a function call.
            op = children[0].get_value()

            code_str = ""
            if op in {'+','-','/','*'}:
                leftval = self.compile_ast(children[1],var_dict,code)
                rightval= self.compile_ast(children[2],var_dict,code)

                #          (2  +  2)
                #          (l  op r)
                code_str= '({} {} {})'.format(leftval,op,rightval)


            elif op == 'sqr':
                #x^2 = x**2
                code_str= '({} ** 2)'.format(self.compile_ast(children[1], var_dict,code))

            elif op == 'neg':
                #neg(x)=-x
                code_str= '(-{})'.format(self.compile_ast(children[1], var_dict,code))

            else:
                #treat like function = op(args)

                #children[1:] contains the args but those are valuetree objects,
                #so compile again to get strings
                args=[self.compile_ast(c,var_dict) for c in children[1:]]
                code_str+= '{}({})'.format(op,','.join(args))

        else:
            # anything else, seriously wrong state.
            raise ValueError(
                "Evaluation internal error, AST node type '{}' not implemented".
                format(ntype))

        return code_str


def do_test(s):
    """
    Helper function for doc test generation
    """
    comp = Compiler()
    code = []
    error = comp.compile(s, code)
    return (error, code)


def tests():
    """
    Doctests - not even remotely complete.

    >>> do_test("1")
    (None, ['# code for:', '# 1', '_result = 1'])

    >>> do_test("-1")
    (None, ['# code for:', '# -1', '_result = (-1)'])

    >>> do_test("sqr(2)")
    (None, ['# code for:', '# sqr(2)', '_result = (2 ** 2)'])

    >>> do_test("1 / 0")
    (None, ['# code for:', '# 1 / 0', '_result = (1 / 0)'])

    >>> do_test("(x = 1) + (x = x + 2) + (x = x + 42)")
    (None, ['# code for:', '# (x = 1) + (x = x + 2) + (x = x + 42)', '_x_1 = 1', '_x_2 = (_x_1 + 2)', '_x_3 = (_x_2 + 42)', '_result = ((_x_1 + _x_2) + _x_3)', '# Update and cleanup x', 'x = _x_3', 'del(_x_1)', 'del(_x_2)', 'del(_x_3)'])

    >>> do_test("x + - + 1")
    ("Parsing generated errors:\\nSyntax error at '+'", [])

    >>> do_test("1 + 2")
    (None, ['# code for:', '# 1 + 2', '_result = (1 + 2)'])

    >>> do_test("y = x + 1")
    (None, ['# code for:', '# y = x + 1', '_y_1 = (x + 1)', '_result = _y_1', '# Update and cleanup y', 'y = _y_1', 'del(_y_1)'])

    >>> do_test("y + y = 1")
    (None, ['# code for:', '# y + y = 1', '_y_1 = 1', '_result = (y + _y_1)', '# Update and cleanup y', 'y = _y_1', 'del(_y_1)'])

    >>> do_test("(x = 2) + 1")
    (None, ['# code for:', '# (x = 2) + 1', '_x_1 = 2', '_result = (_x_1 + 1)', '# Update and cleanup x', 'x = _x_1', 'del(_x_1)'])

    >>> do_test("(x = 1) + (y = x + 1)")
    (None, ['# code for:', '# (x = 1) + (y = x + 1)', '_x_1 = 1', '_y_1 = (_x_1 + 1)', '_result = (_x_1 + _y_1)', '# Update and cleanup x', 'x = _x_1', 'del(_x_1)', '# Update and cleanup y', 'y = _y_1', 'del(_y_1)'])

    >>> do_test("x=1 + (y=2) + (z=x)")
    (None, ['# code for:', '# x=1 + (y=2) + (z=x)', '_y_1 = 2', '_z_1 = x', '_x_1 = ((1 + _y_1) + _z_1)', '_result = _x_1', '# Update and cleanup x', 'x = _x_1', 'del(_x_1)', '# Update and cleanup y', 'y = _y_1', 'del(_y_1)', '# Update and cleanup z', 'z = _z_1', 'del(_z_1)'])

    >>> do_test("(x=1) + (y=2) + (z=x)")
    (None, ['# code for:', '# (x=1) + (y=2) + (z=x)', '_x_1 = 1', '_y_1 = 2', '_z_1 = _x_1', '_result = ((_x_1 + _y_1) + _z_1)', '# Update and cleanup x', 'x = _x_1', 'del(_x_1)', '# Update and cleanup y', 'y = _y_1', 'del(_y_1)', '# Update and cleanup z', 'z = _z_1', 'del(_z_1)'])

    >>> do_test("(x=1) + (y=2) + (x=y+3)")
    (None, ['# code for:', '# (x=1) + (y=2) + (x=y+3)', '_x_1 = 1', '_y_1 = 2', '_x_2 = (_y_1 + 3)', '_result = ((_x_1 + _y_1) + _x_2)', '# Update and cleanup x', 'x = _x_2', 'del(_x_1)', 'del(_x_2)', '# Update and cleanup y', 'y = _y_1', 'del(_y_1)'])

    >>> do_test("((x0 + y0) + x1)")
    (None, ['# code for:', '# ((x0 + y0) + x1)', '_result = ((x0 + y0) + x1)'])

    >>> do_test("(x = (x = ( x = (x = 42))))")
    (None, ['# code for:', '# (x = (x = ( x = (x = 42))))', '_x_1 = 42', '_x_2 = _x_1', '_x_3 = _x_2', '_x_4 = _x_3', '_result = _x_4', '# Update and cleanup x', 'x = _x_4', 'del(_x_1)', 'del(_x_2)', 'del(_x_3)', 'del(_x_4)'])

    >>> do_test("x = 1 + (y = (x = (x - - - - 3) + - - - - y))")
    (None, ['# code for:', '# x = 1 + (y = (x = (x - - - - 3) + - - - - y))', '_x_1 = ((x - (-(-(-3)))) + (-(-(-(-y)))))', '_y_1 = _x_1', '_x_2 = (1 + _y_1)', '_result = _x_2', '# Update and cleanup x', 'x = _x_2', 'del(_x_1)', 'del(_x_2)', '# Update and cleanup y', 'y = _y_1', 'del(_y_1)'])

    """
    pass


def _test():
    print("Running doctests ...")
    import doctest
    doctest.testmod()
    print("... done.")

if __name__ == "__main__":
    _test()
