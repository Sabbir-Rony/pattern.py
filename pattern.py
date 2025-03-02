def patn(n):
    if(n==1):
        return 1
    print("*" * n)
    patn(n-1)
patn(5)
