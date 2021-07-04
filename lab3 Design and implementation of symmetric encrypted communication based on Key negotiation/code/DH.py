#import sympy
import sympy


def params_select(digits):
    n = sympy.prevprime(2**digits)
    g = primitive_root(n)
    return n, g


# 用辗转相除求最大公因子
def gcd(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


# 欧拉函数-暴力循环版
def euler(a):
    count = 0
    for i in range(1, a):
        if gcd(a, i) == 1:
            count += 1
    return count


def order(a, n, b):
    #   输出b在mod(a)中的阶
    #   n是mod(a)群的阶
    p = 1
    while p <= n and (b ** p % a != 1):
        p += 1
    if p <= n:
        return p
    else:
        return -1

# 求任意数最小的原根
def primitive_root(a):
    eular_a = euler(a)
    for b in range(2, a):
        if order(a, eular_a, b) == eular_a:
            return b

def cal_send_val(g, n, pri_key):
    return (g ** pri_key) % n


def cal_pub_key(rec_val, pri_key, n):
    pub_key = (rec_val ** pri_key) % n
    bin_pub_key = str(bin(pub_key).replace('0b', ''))
    bin_pub_key = (64 - len(bin_pub_key)) * '0' + bin_pub_key
    return bin_pub_key
