import math, sys

E, L, R = [int(x) for x in sys.stdin.readlines()]

def isPrime(n:int) -> bool:
    cap:int = int(math.sqrt(n))
    for k in range(2, cap+1):
        if (n % k == 0):
            return False
    return True

rolling_product:int = 1

for i in range(L, R + 1):
    if isPrime(i):
        rolling_product = (rolling_product * i) % 1000000007
base = rolling_product
for i in range(2, E + 1):
    rolling_product = (rolling_product * base  % 1000000007)
print(rolling_product % 1000000007)