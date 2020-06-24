import Crypto
from Crypto import Hash
from Crypto import Random
from Crypto import Util
from Crypto import Cipher
from Crypto import Signature
from Crypto import Math
from numpy.ma import zeros


de

def pot(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif a == 0:
        return 0
    else:
        return a * pot(a, b - 1)


def potencia(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif a == 0:
        return 0
    else:
        result = 1
        z = zeros(b)
        for i in z:
            result *= a
        return result


x = potencia(2, 333333)
print(str(x))
