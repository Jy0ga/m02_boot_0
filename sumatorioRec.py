
def sumatorio(n):
    if n > 0:
        return n + sumatorio (n-1)
    else:
        return 0
    
print(sumatorio(4))



def fact(n):
    if n > 0:
        return n * fact(n-1)
    else:
        return 1

print(fact(5))
