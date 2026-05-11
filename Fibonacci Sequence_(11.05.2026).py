
# --------
# Coding Fibonacci
# --------

n0 = 0
n1 = 1
n2 = 1
i = 0
FibSequence = [n0, n1, n2]

while i < 25: 
    
    #print (n0, "+", n1,"=", n2)
    n0 = n1
    n1 = n2
    n2 = n1 + n0
    FibSequence.append(n2)
    i = i + 1

print (FibSequence)
print ('done')