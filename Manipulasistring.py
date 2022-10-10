#operasi dan manipulasi string

# 1. menyambung string (concanate)
nama_pertama = "ucup"
nama_tengah = " D"
nama_akhir = " fame"

nama_lengkap = nama_pertama + nama_tengah + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang dari string
panjang = len(nama_lengkap)
print ("panjang dari "+ nama_lengkap +" = "+ str(panjang))

# 3. operator untuk string 
# mengecek apakah ada komponen karakter atau string di string
d = "d"
status = d in nama_lengkap
print('string "' + d + '" ada di ' + nama_lengkap + " = " + str(status))
D = "D"
status = D in nama_lengkap
print('string "' + D + '" ada di ' + nama_lengkap + " = " + str(status))
d = "d"
status = d not in nama_lengkap
print('string "' + d + '" tidak ada di ' + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing mengambil data diantara string
print("index ke-0 : " + nama_lengkap[0])
print("index ke-0 : " + nama_lengkap[7])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-1) : " + nama_lengkap[-2])
print("index ke-[0:3]:" + nama_lengkap[0:4])# harus dilebihin satu di karakter terakhir
print("index ke-[0:3]:" + nama_lengkap[3:8])
print("index ke-[0,2,4,6,8,10]:" + nama_lengkap[0:11:2])

# item paling kecil 
print("item paling kecil :" + min(nama_lengkap))
# item paling besar 
print("item paling kecil :" + max(nama_lengkap))

#mau mengambil ascii code
ascii_code = ord ("'")
print("ascii code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# operasi dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada "+ data + " = " + str(jumlah))