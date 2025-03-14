from collections import defaultdict

def caching_fibonacci(n):
    #make defaultdict for keeping results
    cache = defaultdict(int)
    def fibonacci(n):
        #make results for variants 1 or 0
        if n<=0:
            return 0
        if n==1:
            return 1
        if n in cache:
            return cache[n]
        #make rekurcy from n to smaller numbers
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    return fibonacci(n)

fib = caching_fibonacci()
print(fib(10))
print(fib(15))
