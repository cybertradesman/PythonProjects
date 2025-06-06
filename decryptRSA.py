import gmpy2

# N = 1079
# E = 43
# C = 996 894 379 631 894 82 379 852 631 677 677 194 893

e = 43
p = 13
q = 83
n = p * q

c = [996, 894, 379, 631, 894, 82, 379, 852, 631, 677, 677, 194, 893]
phi = (p-1)*(q-1)

d = gmpy2.invert(e, phi) # This is a gear that generates two numbers, one from phi and one from e through the gmpy equation
print(d)

for i in c: #go through the array and decrypt one character at a time
    m = pow(i, d, n) # each value is another equation (index in array "i", value "d" generated from gmpy, "n" which is p * q)
    print(chr(m)) #message "m" to decrypt
    
print("")
# We didn't need password crackers or anything to crack this ciphertext- just some googling, factoring prime numbers on a website online
# You will get millions of potential value pairs for p and q in reality if RSA is implemented properly, thus, RSA is VERY SECURE still today