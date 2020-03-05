#My implementation of the Miller-Rabin primality test
import random as r 

possible  = 0
remainder = 0
p = 0

def composite(possible, p, exponent, remainder):
    possible = pow(possible, remainder, p)
    if possible == 1 or possible == p - 1:
        return False
    for _ in range(exponent):
        possible = pow(possible, 2, p)
        if possible == p - 1:
            return False
    return True

def decompose(n):
    exponent = 0 
    while n % 2 == 0:
        n = n/2
        exponent +=1
    return exponent, n

def primeEsitimation(p, accuaracy):
    if p == 2 or p == 3:
        return True
    if p < 2:
        return False
    exponent, remainder = decompose(p-1)
    for _ in range(accuaracy):
        possible = r.randint(2, p-2)
        if composite(possible, p, exponent, remainder):
            return False
    return True

print(primeEsitimation(1000, 100))