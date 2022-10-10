# episode operatior bitwise, operasi biner, binary
a = 9
b = 5

#bitwise or (|)

c = a | b
print("\n======or======")
print("nilai:",a,"binary :", format(a,'08b'))
print("nilai:",b,"binary :", format(b,'08b'))
print('------------------')
print("nilai:",c,"binary :", format(c,'08b'))

# bitwise dengan and &

print("\n======and=====") # ( & )
c = a & b
print("nilai:",c,"binary :", format(c,'08b'))
print("\n======XOR=====") # ( ^ )
c = a ^ b
print("nilai:",c,"binary :", format(c,'08b'))

# bitwise NOT ( ~ )
c = ~a
print("\n======NOT=====") # ( ~ )
print("nilai:",c,"binary :", format(c,'08b'))
print("\n======FLIP NOT=====") # ( ~ )
d = 0b0000001001
e = 0b1111111111
print("nilai:",d^e,"binary :", format(d^e,'08b'))

#shifting right (>>)
print("\n======shift rigth=====") # ( >> )
c = a >> 2
print("nilai:",c,"binary :",format(c,'08b'))

#shifting right (>>)
print("\n======shift left=====") # ( << )
c = a << 2
print("nilai:",c,"binary :",format(c,'08b'))