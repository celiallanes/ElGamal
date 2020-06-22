import math


def cifrar(p, a, l, k, msg):
    b = pow(a, l) % p
    c1 = pow(a, k) % p
    c2 = (pow(b, k) * msg) % p
    print("C1: " + str(c1))
    print("C2: " + str(c2))
    return c1, c2


def descifrar(c1, c2, p, l):
    msg = (pow(c1, p-1-l)*c2)%p
    print("M descifrado: " + str(msg))
    return msg


p = 15485863
a = 7
l = 28236
k = 480
msg = 128688
print("M: " + str(msg))
c1, c2 = cifrar(p, a, l, k, msg)
msg_des = descifrar(c1, c2, p, l)