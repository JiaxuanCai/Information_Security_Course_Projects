import DH
import DES
import socket


def client_main():
    print('===================欢迎使用DH/DES加密通信系统！===================')
    # 建立socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8090))
    # 输入密钥
    while True:
        a = int(input('请选择一个正整数a：'))
        if a < 0:
            print('您输入的数据不符合要求，请重新输入！')
        else:
            break
    # 计算A并发送
    # n, g = DH.params_select(64)
    g = 5
    n = 0xffffffffffffff61
    # print('g:', g)
    # print('n:', n)
    A = DH.cal_send_val(g, n, a)
    print('计算得到A:', A)
    client.send(bytes(str(A), encoding='utf-8'))
    print('已将计算得到的A发送给对方！')
    # 接收B
    B = int(client.recv(1024))
    print('已从对方接收到B：', B)
    # 计算密钥
    key = DES.bin2str(DH.cal_pub_key(B, a, n))
    print('计算得到密钥为：', key)
    # 输入明文，加密发送
    while True:
        message = input('请输入需要发送的信息：')
        # DES加密
        ciphertext = DES.des_enptypt_all(message, key)
        # 发送密文
        client.send(bytes(ciphertext, encoding='utf-8'))
        print('信息已发送，等待对方回复！')
        ciphertext_rcv = str(client.recv(1024), encoding='utf-8')
        print('已接收到密文：', ciphertext_rcv)
        # 解密
        plaintext_send = DES.des_deptypt_all(ciphertext_rcv, key)
        print('解密得到明文：', plaintext_send)
        # 退出条件
        while True:
            isnext = input('是否继续通信？(y/n)\n')
            if isnext != 'y' and isnext != 'n':
                print('请输入\'y\'或\'n\'确定是否继续通信！')
            else:
                break
        if isnext == 'y':
            continue
        else:
            break
    # 断开连接
    client.close()
    print('已断开连接')


client_main()


