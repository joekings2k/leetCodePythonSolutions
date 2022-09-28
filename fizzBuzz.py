def fizzBizz(n):
    finbizz = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            finbizz.append("fizzbuzz")
        elif i % 3== 0:
            finbizz.append("fizz")
        elif i % 5 == 0:
            finbizz.append("buzz")
        else:
            finbizz.append(i)
    return finbizz

p=3 
print(fizzBizz(p))