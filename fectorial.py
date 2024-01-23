def fec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fec(n-1)
def sum1(num):
    sum = 0
    while num > 0:
        digit = num%10
        sum += digit
        num = num//10
    return sum
    
n = int(input("enter the number"))
res = fec(n)
sum1 = sum1(res)
print(f"the fectorial of {n} is {res} and the aum of digits is {sum1}")
