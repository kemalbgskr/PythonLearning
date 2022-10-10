# Latihan Komparasi dan Logika
# membuat gabungan area rentang dari angka
# +++++++3---------10+++++++
inputUser = float(input("masukan angka yang bernilai\nkurang dari 3 \natau \nlebih dari 10 ="))
#++++++3-----------
#memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari 3 =",isKurangDari)

#-------10+++++++
#memeriksa angkat lebih dari 10 
isLebihDari = (inputUser > 10)
print("lebih dari 10 =",isLebihDari)

P = isKurangDari or isLebihDari
print("Jawaban Anda", P)
print("\n",10*"=","\n")
#Kasus irisan
# -------3++++++++10--------
inputUser = float(input("masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10 ="))
print("\n",10*"=","\n")
#------3+++++
isLebihDari = (inputUser > 3)
print("lebih dari 3 =",isLebihDari)
#++++++10-----
isKurangDari = (inputUser < 10)
print("kurang dari 10 =",isKurangDari)

AA = isKurangDari and isLebihDari
print("Jawaban Anda", AA)

