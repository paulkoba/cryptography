import math
import random

def generateKey(q):
    key = random.randint(math.pow(10, 20), q)
    while math.gcd(q, key)!=1:
        key = random.randint(math.pow(10, 20), q)
    return key

# Calculate b ^ e mod m
def modularPower(b, e, m):
    r = 1
    if 1 & e:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1: r = (r * b) % m
    return r

def encrypt(msg, q, h, g):
    c2 = []
    y = generateKey(q)
    s = modularPower(h,y,q) # s = h ^ y, "shared secret"
    c1 = modularPower(g,y,q) # c1 = g ^ y
    # compute c2 = m * s
    for i in range(0, len(msg)):
        c2.append(msg[i])
    for i in range(0, len(c2)):
        c2[i] = s * ord(c2[i])
    return c1, c2

def decrypt(c1, c2, key, q):
    pt = []
    h = modularPower(c2, key, q)
    for i in range(0, len(c1)):
        pt.append(chr(int(c1[i] / h)))
    return pt

message = input("Enter message: ")
q = int(input("Enter q: "))
g = int(input("Enter g: "))

if q < g:
    print("q should be greater than g")
    exit()

key = generateKey(q)
print("Key: ", key)
p, encrypted = encrypt(message, q, modularPower(g, key, q), g)
print("Encrypted: ", encrypted)
print("Decrypting back using p, key and q")
print('Plaintext =', ''.join(decrypt(encrypted, p, key, q)))
