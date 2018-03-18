"""
>>> from avl_dict import AVLDict
>>> d = AVLDict()
>>> d["arrival"] = "hello"
>>> d["departure"] = "goodbye"
>>> d.ith_key(0)
'arrival'
>>> d.ith_key(1)
'departure'
>>> d["cancel"] = "cancelled"
>>> d.ith_key(1)
'cancel'
>>> d.ith_key(2)
'departure'
>>> del d["arrival"]
>>> d.ith_key(0)
'cancel'
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
