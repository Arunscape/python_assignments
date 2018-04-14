import sys

for line in sys.stdin:

    if line.strip(): # if line not empty
        # cnt=0
        chars = set() #only one item of each type in a set
        line=line.lower().strip()
        for c in line:
            if c in 'vkjxqz':
                # print('yep')
                chars.add(c)
        cnt=len(chars)
        if cnt > 4:
            print('BAD')

        elif cnt < 5:
            print('OK')
