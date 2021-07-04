from math import gcd

def mod_power(a, b, p):
    """
        取模幂运算
        args：底数a，指数b，对p求模
        returns：结果
    """
    a = a % p
    y = 1
    while b != 0:
        if b & 1:
            y = (y * a) % p
        b >>= 1
        a = (a * a) % p
    return y


def has_mod_sqrt(f, p):
    """
        使用欧拉判别法判断是否有对应的模平方根
        args：结果f，对p求模
        returns：是否有
    """
    ret = mod_power(f, (p - 1) // 2, p)
    if ret == 1:
        return True
    else:
        return False


def compute_mod_sqrt(f, p):
    """
        使用Tonelli–Shanks算法计算模平方根
        args：结果f，对p求模
        returns：是否有
    """
    if has_mod_sqrt(f, p):
        t = 0
        s = p - 1
        while s % 2 == 0:
            s = s // 2
            t = t + 1
        if t == 1:
            ret = mod_power(f, (s + 1) // 2, p)
            return ret, p - ret
        elif t >= 2:
            x_ = mod_power(f, p - 2, p)
            n = 1
            while has_mod_sqrt(n, p):
                n = n + 1
            b = mod_power(n, s, p)
            ret = mod_power(f, (s + 1) // 2, p)
            t_ = 0
            while t - 1 > 0:
                if mod_power(x_ * ret * ret, 2 ** (t - 2), p) == 1:
                    pass
                else:
                    ret = ret * (b ** (2 ** t_)) % p
                t = t - 1
                t_ = t_ + 1
            return ret, p - ret
        else:
            return -2, -2
    else:
        return -1, -1

def Ep(x, a, b):
    '''
    定义在有限域上的椭圆曲线方程
    :args
        :param x: 自变量
        :param a: 一次项系数
        :param b: 常数项系数
        :param p: 有限域大小，素数
    :return：
        因变量
    '''
    return x ** 3 + a * x + b


def check_valid_Ep(a, b, p):
    '''
    检查椭圆曲线相关参数是否正确
    :args:
        :param a: 一次项系数
        :param b: 常数项系数
        :param p: 有限域大小
    :return: 参数是否符合要求
    '''
    if gcd(p, 2) != 1:
        return False
    return (4*a**3+27*b**2) != 0

def check_in_Ep(P, a, b, p):
    return (P[1]**2) % p == Ep(P[0], a, b) % p

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

def negative(P, p):
    '''
    计算P的负元
    :args:
        :param P: 椭圆曲线上一点
        :param p: 有限域大小
    :return: P的负元
    '''
    return (P[0], (-P[1]) % p)

def get_rank(G, a, p):
    '''
    计算对应基点的阶数
    :args:
        :param G: 在椭圆曲线上选取的一个基点
        :param a: 椭圆曲线一次项系数
        :param p: 有限域大小
        :return:
    '''
    n = 1
    P = G
    G_neg = negative(P, p)
    while P != G_neg:
        P = ecc_plus(P, G, a, p)
        n += 1
    return n + 1

def compute_group(a, b, p):
    """
        根据给定的椭圆曲线方程计算在Abel群里的坐标点
        args： 有限域大小
        returns： 计算得到的Abel群
    """
    x = 0
    AbelGroup = []
    while x < p:
        f = (((((x * x) % p) * x % p) + a * x) % p + b) % p
        x += 1
        y1, y2 = compute_mod_sqrt(f, p)
        if y1 == y2 == -1:
            continue
        else:
            AbelGroup.append((x - 1, y1))
            AbelGroup.append((x - 1, y2))
    return AbelGroup

def ecc_plus(P, Q, a, p):
    '''
    椭圆曲线加法
    :args:
        :param P: 椭圆曲线上的一个点
        :param Q: 椭圆曲线上的另一个点
        :param a: 椭圆曲线的一次项系数
        :param p: 有限域大小，素数
    :return:
        椭圆曲线P+Q的结果，是在椭圆曲线上的另一个点
    '''
    x1, x2, y1, y2 = P[0], Q[0], P[1], Q[1]
    if P == Q:
        inv = ext_gcd(2 * y1, p)[0]
        k = ((3 * x1 ** 2 + a) * inv) % p
    else:
        inv = ext_gcd(x2 - x1, p)[0]
        k = ((y2 - y1) * inv) % p
    x3 = (k ** 2 - x1 - x2) % p
    y3 = (k * (x1 - x3) - y1) % p
    return (x3, y3)


def get_rP(r, P, a, p):
    '''
    计算椭圆曲线上的r*P
    当r=key(私钥), P=G(基点)时，计算得到的结果是公钥
    :args:
        :param r: int
        :param P: 椭圆曲线上一点，(int, int)
        :param a: 椭圆曲线的一次项系数
        :param p: 有限域大小
    :return: 结果 r*P, (int, int)
    '''
    if r == 1:
        return P
    # key能被2整除时，计算key/2 * G + key/2 *G
    # key不能被2整除时，计算(key-1)*G + G
    if r % 2 == 0:
        half = get_rP(r/2, P, a, p)
        return ecc_plus(half, half, a, p)
    else:
        return ecc_plus(get_rP(r-1, P, a, p), P, a, p)

def mapping(c, AbelGroup):
    """
        根据待传输的明文得到映射之后的坐标
        args： 待传输的明文c，以单个字节为单位
        returns： 映射完成之后得到的坐标
    """
    return AbelGroup[ord(c)]  # ASCII编码

def demapping(P, AbelGroup):
    '''
    根据椭圆曲线上的点得到原字符
    :args:
        :param P: 椭圆曲线上一点
        :param AbelGroup: 椭圆曲线在有限域上形成的Abel群
    :return: 该点对应的字符
    '''
    return chr(AbelGroup.index(P))

def print10(arr):
    '''
    辅助打印输出函数，以一行十个元素的方式打印输出
    :param arr: 需要打印输出的数组
    '''
    for i in range(len(arr)):
        print(arr[i], end="")
        if (i+1)%10 == 0:
            print("\n", end="")
    print("\n", end="")

def ecc_main():
    '''
    ECC加密过程模拟
    使用输入输出过程模拟信息的传输
    '''
    print("--------------User1进行的操作--------------")
    # 椭圆曲线的选取
    while True:
        while True:
            print("一类可以用来加密的椭圆曲线的形式为y^2 = x^3 + ax + b (mod p)")
            a = int(input("请输入一次项系数a(a为正整数): "))
            b = int(input("请输入常数项系数b(b为正整数): "))
            p = int(input("请输入有限域大小p(p大于2的素数)，为了保证生成的椭圆曲线有足够多的点用于映射字符，p应至少大于256: "))
            # 椭圆曲线参数校验
            if check_valid_Ep(a, b, p):
                break
            else:
                print("输入参数不符合要求，请重新输入！")
        # 计算得到的Abel群
        abel = compute_group(a, b, p)
        # 检查能否表示所有字符
        if len(abel) < 256:
            print("输入的椭圆曲线在有限域上的点小于256，请重新选择参数！")
        else:
            break

    # 基点的选取
    while True:
        print("请在椭圆曲线上选择一个点作为基点(该有限域椭圆曲线上的点如下所示)")
        print10(abel)
        G = (int(input("请输入基点横坐标： ")), int(input("请输入基点纵坐标： ")))
        # 检查基点是否在abel群中
        if check_in_Ep(G, a, b, p):
            break
        else:
            print("输入的点不在Abel群中，请重新输入")

    # 获取椭圆曲线的阶
    rank = get_rank(G, a, p)

    # User1 选择私钥
    while True:
        key = int(input("请输入私钥(正整数且小于阶数n，对于以上给定参数，n={}): ".format(rank)))
        # 私钥检验
        if key < rank:
            break
        else:
            print("输入的私钥不符合要求，请重新输入！")
    # 获取公钥
    KEY = get_rP(key, G, a, p)
    print("--------------User1传输给User2--------------")
    print("椭圆曲线Ep: y^2 = x^3 + %dx + %d (mod %d)" %(a,b,p))
    print("基点G: ", format(G))
    print("公钥KEY: ", format(KEY))
    print("--------------User2进行的操作--------------")
    # User2 选择随机数r
    while True:
        r = int(input("请输入一个随机数r(正整数且小于阶数n，对于以上给定参数，n={}): ".format(rank)))
        # 私钥检验
        if r < rank:
            break
        else:
            print("输入的随机数不符合要求，请重新输入！")
    # 输入明文：
    plaintext = input("请输入待发送的明文(M):")
    # 进行加密
    ciphertext_C1 = []
    ciphertext_C2 = get_rP(r, G, a, p)
    for ch in plaintext:
        ch_P = mapping(ch, abel)
        user2_C1 = ecc_plus(ch_P, get_rP(r, KEY, a, p), a, p)
        ciphertext_C1.append(user2_C1)

    print("--------------User2传输给User1--------------")
    print("密文C1和C2如下：(C1 = M + r*KEY, C2 = r*G)")
    print("C1: ")
    print10(ciphertext_C1)
    print("C2: \n", ciphertext_C2)
    print("--------------User1进行的操作--------------")
    # 逐字解密
    str = ""
    for user1_C1 in ciphertext_C1:
        ch_P = ecc_plus(user1_C1, negative(get_rP(key, ciphertext_C2, a, p), p), a, p)
        ch = demapping(ch_P, abel)
        str += ch
    print("解密方法：M = C1 - key*C2")
    print("解密得到的字符串为: ", str)

if __name__ == '__main__':
    n = 1
    while True:
        print("--------------椭圆曲线加密模拟(第", n, "次)--------------")
        n += 1
        ecc_main()
        while True:
            ans = input("是否继续模拟？(y/n)")
            if ans!='y' and ans!='n':
                print("请输入'y'或'n'表示是否继续")
            else:
                break
        if ans == 'n':
            break
