import cProfile
import timeit
from functools import cache
from functools import lru_cache
import sys
sys.setrecursionlimit(2500)

def recursiveMethod(n):
    if n<=1:
        return n
    return recursiveMethod(n-1)+recursiveMethod(n-2)

@cache
def cachedMethod(n):
    if n<=1:
        return n
    return cachedMethod(n-1)+cachedMethod(n-2)

@lru_cache(maxsize=7)
def lrucachedMethod(n):
    if n<=1:
        return n
    return cachedMethod(n-1)+cachedMethod(n-2)

globalCache = {}
def manualMethod(n):
    if n<=1:
        return n
    if n in globalCache.keys():
        return globalCache[n]
    value = manualMethod(n-1)+manualMethod(n-2)
    globalCache[n] = value
    # if n==280:
    #     print(value)
    return value

def iterativeMethod(n):
    if n<=1:
        return n
    n2 = 1
    n1 = 1
    #n = 1
    for i in range(2,n):
        n0 = n1 + n2
        
        n2 = n1
        n1 = n0
    # print(n)
    return n

if len(sys.argv)<=2:
    print("Fib(10)")
    print("------------------- recursive Method")
    print(timeit.timeit(lambda: recursiveMethod(10), number=1))
    print("------------------- cached Method")
    print(timeit.timeit(lambda: cachedMethod(10), number=1))
    print("------------------- manual Method")
    print(timeit.timeit(lambda: manualMethod(10), number=1))

try:
    fib = int(sys.argv[1])
    num = int(sys.argv[2])
except:
    raise Exception("use as python fib.py [maxFib] [amountIterations], 0 for 1 run of fib(1)...fib(maxFib)")
if num > 0:
    print("Fib({}), with {} iterations".format(fib,num))
    print("------------------- cached Method")
    cached = timeit.timeit(lambda: cachedMethod(fib), number=num)
    print(cached)
    print("------------------- lru Method")
    lru = timeit.timeit(lambda: lrucachedMethod(fib), number=num)
    print(lru)
    print("------------------- manual Method")
    manual = timeit.timeit(lambda: manualMethod(fib), number=num)
    print(manual)
    print("------------------- iterative Method")
    iterative = timeit.timeit(lambda: iterativeMethod(fib), number=num)
    print(iterative)

    outputs = {manual:"manual",cached:"cached",iterative:"iterative",lru:"lru"}
    print(outputs[min(manual,cached,lru,iterative)],"wins the race")

def fibrange():
    outputs = {}
    methods = [manualMethod,cachedMethod,lrucachedMethod,iterativeMethod]
    method_strings = ["manualMethod","cachedMethod","lrucachedMethod","iterativeMethod"] 
    for i in range(0,len(methods)):
        time = timeit.timeit(lambda: computeRange(methods[i],fib),number=1)
        outputs[time]=[method_strings[i], time]
    print([outputs[m] for m in sorted(outputs.keys())])

def computeRange(method,fib):
    for i in range(0,fib):
        method(fib)

if num == 0:
    fibrange()

