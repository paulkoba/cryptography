import primes

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

# Choose two large distinct prime numbers p and q, such that p mod 4 = 3 and q mod 4 = 3, return [p * q, p, q]
def generateKey(len):
    while True:
        p = primes.generatePrime(len / 2)
        q = primes.generatePrime(len / 2)

        if p % 4 == 3 and q % 4 == 3:
            return [ p * q, p, q ]

# c = m^2 mod n
def encrypt(m, n):
    return(m ** 2) % n

# Extended euclidian algorithm
def extendedEuclidianAlgorithm(a, b):
    s = 0
    o_s = 1
    t = 1
    o_t = 0
    r = b
    o_r = a
    
    while r != 0:
        q = o_r // r
        tr = r
        r = o_r - q * r
        o_r = tr

        ts = s
        s = o_s - q * s
        o_s = ts

        tt = t
        t = o_t - q * t
        o_t = tt

    return [o_r, o_s, o_t]

# return four strings that could potentially have been encrypted
def decrypt(c, p, q):
    n = p * q
    
    # Compute the square root of c modulo p and q
    mp = modularPower(c, (p + 1) // 4, p)
    mq = modularPower(c, (q + 1) // 4, q)

    # Find yp and yq such that yp * p + yq * q = 1
    ext = extendedEuclidianAlgorithm(p, q)
    yp = ext[1]
    yq = ext[2]
    
    # find four square roots of c modulo n using Chinese remainder theorem
    d1 = (yp * p * mq + yq * q * mp) % n
    d2 = n - d1
    d3 = (yp * p * mq - yq * q * mp) % n
    d4 = n - d3

    return [d1, d2, d3, d4]

def decodePotentialAnswer(ans):
    return ans.to_bytes(100, "little").rstrip(b'\x00')

s = input("Enter a string to encrypt: ").encode()
key = generateKey(512)
encrypted = encrypt(int.from_bytes(s, "little"), key[0])

print("Initial string:", s)
print("Encrypted: ", encrypted)

decrypted = decrypt(encrypted, key[1], key[2])
answers = [decodePotentialAnswer(e) for e in decrypted]

for ans in answers:
    print("Potential answer: ", ans)
