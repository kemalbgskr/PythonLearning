# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah assignment

a = 5 #adalah assingment
print("nilai a=", a)
a += 1 #artinya a = a + 1
print("nilai a += 1, nilai a menjadi", a)
a -= 2 #artinya a = a - 1
print("nilai a -= 2, nilai a menjadi", a)
a *= 5 #artinya a = a * 5
print("nilai a *= 5, nilai a menjadi", a)
a /= 2 #artinya a = a * 2
print("nilai a *= 2, nilai a menjadi", a)

# modulus floor division
b = 10
print("\nnilai B =", b)
b %= 3
print("nilai b %= 3, nilai b menjadi",b)

b = 10
print("\nnilai B =", b)
b //= 3
print("nilai b //= 3, nilai b menjadi",b)

# exponen
a = 5 
print("nilai a=", a)
a **= 3
print("nilai a **= 3, nilai a menjadi",a)

#operasi bitwise , jika memiliki boolean akan menjadi operator logika bias
c = True
print("\nnilai c =",c)
c |= False
print("nilai c |= False, nilai c menjadi",c)
c = False
print("\nnilai c =",c)
c |= False
print("nilai c |= False, nilai c menjadi",c)

#and & 
c = True
print("\nnilai c =",c)
c &= True
print("nilai c &= False, nilai c menjadi",c)
#XOR ^ 
c = True
print("\nnilai c =",c)
c ^= True
print("nilai c ^= False, nilai c menjadi",c)#
# geser gese
d = 0b0100
print("\nnilai d=",format(d,'04b'))
d >>= 2
print("nilai d >>=","maka nilai d menjadi",format(d,'04b'))
d <<= 1
print("nilai d <<=","maka nilai d menjadi",format(d,'04b'))

