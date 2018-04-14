# read the first line
input
n,q  = list (map( int ,  input ().split() ) )

# n is number of seconds callcenter is open eahc day
# q is #of queries

"""
The  next  line  contains n
integers,  each  between  0  and  100.

Consecutive  integers  will  be
separated by a single space.
The ith integer on this line indicates how many new calls were
received by your call centre yesterday in the ith second of operation
"""

what = list (map( int ,  input ().split() ) )

cumsum={0:0}
# for i in range(1,n+1):
#     cumsum[i]=sum(what[:i])
      #still too slow RIP

for i in range(1,n+1):
    cumsum[i]= what[i-1] + cumsum[i-1]
    #FINALLY 0x6675636b this
    
# for x in cumsum.items():
#     print(x)
for i in range(q):
    s,t = list (map( int ,  input ().split() ) )
    #print(sum(what[s-1:t])) too slow
    print(cumsum[t]-cumsum[s-1])



# for x in out:
#     print(x)
# read the calls

# read and process each query
