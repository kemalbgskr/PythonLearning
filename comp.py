# operasi komparasi
# setiap hasil dari operasi komparasi adalah boolean
# >,<,>=,<=,==,!=,is,is not
import time
start_time = time.time()

a = 4
b = 2
print('LEBIH BESAR DARI (>)')
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

print('KURANG DARI (<)')
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

print('LEBIH DARI SAMA DENGAN (>=)')
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

print('KURANG DARI SAMA DENGAN (<=)')
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

print("Sama dengan (=)")
hasil = a == 3
print(a,'==',3,'=',hasil)
hasil = b == 4
print(b,'==',3,'=',hasil)

print("tidak Sama dengan (!=)")
hasil = a != 3
print(a,'!=',3,'=',hasil)
hasil = b != 4
print(b,'!=',3,'=',hasil)

# is sebagai komparasi objek
x = 5 #adalah assignment object
y = 6
print('nilai x=', x, 'id =', hex(id(x)))
print('nilai y=', y, 'id =', hex(id(y)))
hasil = x is y 
print('x is y =', hasil)
# is sebagai komparasi objek
x = 5 #adalah assignment object
y = 6 
print('nilai x=', x, 'id =', hex(id(x)))
print('nilai y=', y, 'id =', hex(id(y)))
hasil = x is not y 
print('x is not y =', hasil)

print("")
print(time.time() - start_time)

