def fib(n):
    a, b = 0, 1
    fib_list = []
    while len(fib_list) < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

 print(fib(10))


