#fibonacci
def fibonacciG(n):
    a,b,counter = 0,1,0
    while True:
        if (counter>n): return
        yield a
        a, b = b, a+b
        counter+=1
n = int(input('Which fibonacci number would you like? '))
f = fibonacciG(n)
f=list(f)
print(f[n])