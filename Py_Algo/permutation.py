def nCr(n,r):
    result = 1 
    for i in range(1, r+1):
        result = result * ( n-i +1)/ i
    return result

m , n = 10,3
print(nCr(m , n))
