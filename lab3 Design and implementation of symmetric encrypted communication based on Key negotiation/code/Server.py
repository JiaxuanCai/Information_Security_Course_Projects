import DH
import DES
import socket

def server_main():
    print('===================欢迎使用DH/DES加密通信系统！===================')
    # 建立socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8090))
    # 开始监听，这里接收对方传来的A
    print('正在监听中......')
    server.listen()
    conn, addr = server.accept()
    A = int(conn.recv(1024))
    print('已接收到', addr, '传来的A：', A)
    # 输入密钥
    while True:
        b = int(input('请选择一个正整数b：'))
        if b < 0:
            print('您输入的数据不符合要求，请重新输入！')
        else:
            break
    # 用b计算B发给接收方
    # 获取n和g
    # n, g = DH.params_select(64)
    g = 5
    n = 0xffffffffffffff61
    B = DH.cal_send_val(g,n,b)
    conn.send(bytes(str(B), encoding='utf-8'))
    print('B已安全地发送给了接收方！')
    key = DES.bin2str(DH.cal_pub_key(A, b, n))
    print('计算得到密钥为：', key)
    # 输入明文，加密发送
    while True:
        # 监听
        print('------正在监听中......')
        ciphertext_rcv = str(conn.recv(1024), encoding='utf8')
        print('已接收到', addr, '传来的密文：', ciphertext_rcv)
        # 解密
        plaintext_send = DES.des_deptypt_all(ciphertext_rcv, key)
        print('解密得到明文：', plaintext_send)
        # 发送信息
        message = input('请输入需要发送的信息：')
        # DES加密
        ciphertext = DES.des_enptypt_all(message, key)
        # 发送密文
        conn.send(bytes(ciphertext, encoding='utf-8'))
        print('信息已发送，等待对方回复！')
        # 推出条件
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
    server.close()
    print('已断开连接')

server_main()


