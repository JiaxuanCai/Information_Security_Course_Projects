# IP置换表
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# 逆IP置换表
IP_REV= [40, 8, 48, 16, 56, 24, 64, 32,
         39, 7, 47, 15, 55, 23, 63, 31,
         38, 6, 46, 14, 54, 22, 62, 30,
         37, 5, 45, 13, 53, 21, 61, 29,
         36, 4, 44, 12, 52, 20, 60, 28,
         35, 3, 43, 11, 51, 19, 59, 27,
         34, 2, 42, 10, 50, 18, 58, 26,
         33, 1, 41, 9, 49, 17, 57, 25]

# S盒中的S1盒
S1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
      0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
      4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
      15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
# S盒中的S2盒
S2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
      3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
      0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
      13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
# S盒中的S3盒
S3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
      13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
      13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
      1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
# S盒中的S4盒
S4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
      13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
      10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
      3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
# S盒中的S5盒
S5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
      14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
      4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
      11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
# S盒中的S6盒
S6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
      10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
      9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
      4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
# S盒中的S7盒
S7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
      13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
      1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
      6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
# S盒中的S8盒
S8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
      1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
      7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
      2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
# S盒
S = [S1, S2, S3, S4, S5, S6, S7, S8]

SHIFT = [1, 1, 2, 2, 2, 2, 2, 2,
         1, 2, 2, 2, 2, 2, 2, 1]

# P盒
P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]

# 压缩置换表1，不考虑每字节的第8位，将64位密钥减至56位。然后进行一次密钥置换。
PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# 压缩置换表2，用于将循环左移和右移后的56bit密钥压缩为48bit
PC_2 = [14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32]

# 用于对数据进行扩展置换，将32bit数据扩展为48bit
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

def str2bin(stri):
    '''
    将字符串转化为二进制
    :param stri: 待转化的字符串
    :return: 一个二进制比特流的字符串
    '''
    bitstream = ""
    # 对每一位分别进行转换，每个字符占八位
    for ch in stri:
        temp = bin(ord(ch))[2:] # 要去掉前面的'0b'
        # 不足八位的补齐
        temp = '0' * (8 - len(temp)) + temp
        bitstream += temp
    return bitstream

def bin2str(bin_str):
    '''
    将二进制字符串以8位为一个字符转化为字符串
    :param bin: 二进制字符串
    :return: 转换得到的字符串
    '''
    stri = ''
    # 对每八个二进制数进行转换
    for i in range(0, len(bin_str), 8):
        temp = chr(int(bin_str[i:i+8], 2))
        stri += temp
    return stri


def replace(bitstream, table):
    '''
    IP置换，将输入比特流通过IP置换为新的比特流
    :param bitstream: 待置换的64位比特流
    :return: 置换后的64位比特流
    '''
    res = ""
    for index in table:
        res += bitstream[index - 1]
    return res

def shift(bitstream, shift_num):
    '''
    对bitstream，左移shift_num位
    :param bitstream: 待左移的比特流
    :param shift_num: 左移位数
    :return:
    '''
    return bitstream[-shift_num:] + bitstream[:-shift_num]


def gen_subkey(key):
    '''
    子密钥的生成
    :param key: 密钥，一个56位的二进制字符串
    :return: 一个子密钥列表，包含16个48位的子密钥
    '''
    subkeys = []
    # 首先将密钥进行PC_1置换
    after_PC_1 = replace(key, PC_1)
    # 将密钥分为C0和D0两部分
    C0 = after_PC_1[:28]
    D0 = after_PC_1[28:]
    # 循环变换16次生成子密钥
    for num in SHIFT:
        # 先进行左移
        C0 = shift(C0, num)
        D0 = shift(D0, num)
        # 进行PC_2置换
        subkey = replace(C0 + D0, PC_2)
        # 子密钥加入子密钥列表中
        subkeys.append(subkey)
    return subkeys

def s_box(bitstream):
    '''
    将48位的二进制字符串经过S盒压缩置换得到56位的二进制字符串
    :param bitstream: 48位的二进制字符串
    :return: 56位的二进制字符串
    '''
    res = ""
    box_num = 0
    # 6位为一组进行循环
    for i in range(0, len(bitstream), 6):
        # 二进制字符串转化为十进制数字
        row = int(bitstream[i] + bitstream[i+5], 2)
        col = int(bitstream[i+1:i+5], 2)
        # 读取S盒对应位置的数并转化为二进制字符串
        temp = bin(S[box_num][row*16 + col])[2:]
        box_num += 1
        # 前面补0
        temp = (4-len(temp)) * '0' + temp
        res += temp
    return res

def feistel(bitstream, key):
    '''
    feistel函数
    :param bitstream: 32位的二进制字符串
    :param key: 48位的子密钥
    :return:
    '''
    # 扩展置换
    after_E = replace(bitstream, E)
    # 与子密钥进行异或
    after_key = strxor(after_E, key)
    # 压缩置换
    after_S = s_box(after_key)
    # 进行P置换以获取雪崩效应
    afte_P = replace(after_S, P)
    return afte_P

def strxor(str1, str2):
    '''
    对字符串形式的比特流进行异或
    :param str1: 待进行异或操作的二进制字符串
    :param str2: 待进行异或操作的二进制字符串
    :return: 异或结果
    '''
    res = ""
    for ch1, ch2 in zip(str1, str2):
        res += str(int(ch1) ^ int(ch2))
    return res


def feistel_net(left, right, key):
    '''
    Feistel网络一次操作
    :param left: 左二进制字符串，32位
    :param right: 右二进制字符串，32位
    :param key: 子密钥，48位
    :return:
    '''
    new_left = right
    new_right = strxor(left, feistel(right, key))
    return new_left, new_right

def des_encrypt(bin_plaintext, subkeys):
    '''
    对一个64位的明文进行加密
    :param bin_plaintext: 64位的二进制字符串明文
    :param subkeys: 子密钥列表
    :return:
    '''
    # 首先对明文进行IP变换
    after_IP = replace(bin_plaintext, IP)
    left = after_IP[:32]
    right = after_IP[32:]
    # 进入Feistel网络循环15次
    for i in range(15):
        left, right = feistel_net(left, right, subkeys[i])
    # 最后一次，左右不需要交换
    right, left = feistel_net(left, right, subkeys[15])
    # 经过IP逆变换得到密文，并转化为字符串
    ciphertext = bin2str(replace(left + right, IP_REV))
    return ciphertext

def des_enptypt_all(plaintext, key):
    '''
    对明文进行加密
    :param plaintext: 明文，字符串
    :param key: 密钥，包含八个字符的字符串
    :return: 密文
    '''
    # 明文和密钥转化为二进制形式
    bin_key = str2bin(key)
    # 明文不足8个字符的部分补齐
    if len(plaintext) % 8 != 0:
        plaintext = (8 - (len(plaintext) % 8)) * '\0' + plaintext
    # 明文每8个字符分为一组
    bin_plaintext = []
    for i in range(0, len(plaintext), 8):
        bin_plaintext.append(str2bin(plaintext[i:i+8]))
    # for i in range(len(bin_plaintext)):
    #     print(bin2str(bin_plaintext[i]))
    # 生成子密钥
    subkeys = gen_subkey(bin_key)
    # 分组加密
    ciphertext = ''
    for sub_plaintext in bin_plaintext:
        ciphertext += des_encrypt(sub_plaintext, subkeys)
    return ciphertext

def des_deprypt(bin_ciphertext, subkeys):
    '''
    对一个64位密文块进行解密
    :param bin_ciphertext: 64位密文块
    :param subkeys: 子密钥列表
    :return:
    '''
    # 首先对密文进行IP变换
    after_IP = replace(bin_ciphertext, IP)
    left = after_IP[:32]
    right = after_IP[32:]
    # 进入Feistel网络循环15次，这里密钥需要倒置
    for i in range(15):
        left, right = feistel_net(left, right, subkeys[15 - i])
    # 最后一次，左右不需要交换
    right, left = feistel_net(left, right, subkeys[0])
    # 经过IP逆变换得到明文，并转化为字符串
    plaintext = bin2str(replace(left + right, IP_REV))
    return plaintext

def des_deptypt_all(ciphertext, key):
    '''
    对密文进行解密
    :param ciphertext: 密文，字符串
    :param key: 密钥，字符串
    :return: 明文
    '''
    # 密文和密钥转化为二进制形式
    bin_key = str2bin(key)
    # 密文每8个字符分为一组
    bin_ciphertext = []
    for i in range(0, len(ciphertext), 8):
        bin_ciphertext.append(str2bin(ciphertext[i:i+8]))
    # 生成子密钥
    subkeys = gen_subkey(bin_key)
    # 分组解密
    plaintext = ''
    for sub_ciphertext in bin_ciphertext:
        plaintext += des_deprypt(sub_ciphertext, subkeys)
    return plaintext.replace('\0', '')