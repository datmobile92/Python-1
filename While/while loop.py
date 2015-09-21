__author__ = 'Admin'
while True:
    n1 = int(input('nhap vao so thu nhat'))
    n2 = int(input('nhap vao so thu hai'))
    # noinspection PyRedeclaration
    a = 1
    k = 2
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            a = k
        k += 1
        print("so chia lon nhat cua n1 = %d va n2 = %d la: %d" % (n1, n2, k))
    n1 = int(input('nhap vao so thu nhat'))
