#operator dalam bentuk mehod
# merubah case dari string
# merubah semua ke upper case /  lower
salam = "aKoE KetChe ABiEz"
print("normal = " + salam)
salam = salam.upper()
print("normal = " + salam)
salam = salam.lower()
print("normal = " + salam)

# pengecekan dengan menggunakan isX method
# contoh untuk pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha () <--- untuk mengecek semuanya huruf atau tidak
# isanum () huruf dan angka
# isdecimal () untuk cek jika semua komponennya angka
# isspace () untuk cek spasi tab \n
# istitle () untuk cek semua kata apakah dengan huruf besar

judul = "It Is Is Okay Not To Be Okay"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswitch() endwith()
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = ",str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = ",str(cek_end))

## penggabungan komponen join () split ()
pisah = ['aku','sayang','kamu']
gabung = ",".join(pisah)
print(pisah)
print(gabung)

gabungan = "akuehemsayangehemkamu"
print(gabungan.split('ehem'))

#alokasi karakter 
# rjust() ljust() center() untuk allignment
kanan = "surotong".rjust(10)
print("'"+ kanan +"'")
center = "surotong".center(10)
print("'"+ center +"'")
center = "surotong".center(20,"-")
print("'"+ center +"'")

# kebalikan dengan strip
center = center.strip("-")
print("'" + center + "'")