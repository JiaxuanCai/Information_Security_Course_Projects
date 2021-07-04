p = 1231
A = [545, 159, 1198, 978, 3652, 3354, 1027, 466, 689]
k = 10
acc = p
for j in range(1, k):
    t1 = pow(1, j, p)
    t2 = A[j-1]*t1 % p
    acc = (acc+t2) % p  # 还好
    print(f't1= {t1}, t2={t2} acc={acc}')
print(acc)
