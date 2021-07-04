import numpy as np

import random


def mod_exp(a, exp, mod):
    fx = 1
    while exp > 0:
        if (exp & 1) == 1:
            fx = fx * a % mod
        a = (a * a) % mod
        exp = exp >> 1
    return fx


def ext_gcd(a, b):
    """扩展欧几里得算法
    求a关于b的逆元

    Args:
        a (int): 数a
        b (int): 数b

    """
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = ext_gcd(b, a % b)  # 递归直至余数等于0
        x, y = y, (x - (a // b) * y)  # 辗转相除法反向推导每层a、b的因子使得gcd(a,b)=ax by成立
        return x, y, gcd


def h(A, x, p):
    ret = A[0]
    for idx, a in enumerate(A[1:]):
        t1 = pow(x, idx + 1, p)
        t2 = (a * t1) % p
        ret = (ret + t2) % p
        # ret = (ret + (a * pow(x, idx + 1, p)) % p) % p
        # print(f"t1={t1}, t2={t2}, ret={ret}")
    return ret


def prime(x):
    if x == 0:
        return False
    if x == 1:
        return False
    if x % 2 == 0:
        return False
    i = 3
    while i < x ** 0.5 + 1:
        if x % i == 0:
            return False
        # should NOT be if x % 2 == 0: return False
        # should NOT be if i % 2 == 0: return False
        # should be if x % i == 0: return False
        i += 2
    return True


def get_primes(kmin, kmax):
    prime_list = []
    for i in range(kmin, kmax):
        if prime(i):
            prime_list.append(i)
    return prime_list


def generate_a(k, t=4):
    # 1. create p
    primes_list = get_primes(k + 5, k + 1000)
    p = primes_list[random.randint(0, len(primes_list))]

    # 2. generate  t-1 a
    A = random.sample(range(0, p), t - 1)
    A.insert(0, k)
    return p, A


# 1 * 1**3 + 2 * 2**2 + 3 * 3 + 12
# print(1 * 1**3 + 2 * 2**2 + 3 * 3 + 12)
def encode(k, t, n):
    p, A = generate_a(k, t)
    # p = 2219
    # p = 3623
    # A = [2018, 2021, 1339, 72, 1563, 35, 2189, 1622, 710, 788]
    print('A', A)
    # x_list = random.sample(range(0, int(k + n+10)), n)
    x_list = list(range(1, n + 1))
    print('X', x_list)
    y_list = []
    for x in x_list:
        y_list.append(h(A, x, p))
    return p, x_list, y_list


def decode(p, xx, yy, t):
    global tmp
    hx = 0
    random_ts = random.sample(range(0, len(xx)), t)
    print("select:")
    for s in (random_ts):
        tmp = yy[s]
        print(s, tmp)

        down = 1
        for j in random_ts:
            if j == s:
                continue
            # tmp = tmp * (-xx[j]) % p
            tmp = tmp * (-xx[j]) % p
            down *= xx[s] - xx[j]
        # tmp = tmp * ext_gcd(down, p)[0] % p
        inv = ext_gcd(down, p)[0]
        tmp = (tmp % p * inv % p) % p
        # tmp = tmp / down
        hx = (hx + tmp) % p
    # return hx % p
    return hx


if __name__ == '__main__':
    k = int(input("Input K "))
    t = int(input("Input t "))
    n = int(input("Input n "))
    dt = int(input("Input new t to decode "))
    # k = 2018
    # t, n = 10, 15
    p, xx, yy = encode(k, t=t, n=n)
    # p = 2281
    # xx = list(range(0, n))
    # yy = [49, 31, 60, 635, 761, 528, 1604, 392, 1328, 1585, 703, 2146, 1867, 1277, 1704]
    comp_cases = []
    for i, (x, y) in enumerate(zip(xx, yy)):
        print(f'P_{i + 1} ({x},{y})')
        comp_cases.append((x, y))
    ans = decode(p, xx, yy, t=dt)
    print("prime", p)
    print('decode k', ans)
