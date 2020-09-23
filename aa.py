def myPow(x, n, p):
    if n == 0:
        return 1
    if n < 0:
        return 1 / myPow(x, -n, p)
    else:

        if n % 2 == 1:
            return myPow(x * x % p, n // 2,p) * x % p
        else:
            return myPow(x * x % p, n // 2,p)


a = list(map(int, input().split()))
print(myPow(a[0], a[1], a[2]))
