# ------0+++++++5-------8++++++11--------
# ++++++0-------5+++++++8------11++++++++
import time
from typing import DefaultDict
start_time = time.time()

print("PR untuk Rentang")
print("Nomor 1")
print("masukan angka dengan aturan\nlebih dari 0 dan kurang dari 5\nlebih dari 8 dan kurang dari 11")
inputUser = float(input("Masukan Angka Tebakan Anda :"))
print("\n",5*"=","\n")
a = (inputUser > 0)
b = (inputUser < 5)
c = (inputUser > 8)
d = (inputUser < 11)

x = a and b
y = c and d

z = x or y
print("JAWABAN ANDA :", z)
print("\n",5*"=","\n")
print("PR untuk Rentang")
print("Nomor 2")
print("masukan angka dengan aturan\nkurang dari 0\nlebih dari dari 5 dan kurang dari 8\nlebih dari 11")
inputUser = float(input("Masukan Angka Tebakan Anda :"))
print("\n",5*"=","\n")
a = (inputUser < 0)
b = (inputUser > 5)
c = (inputUser < 8)
d = (inputUser > 11)

x = b and c

z = a or x or d
print("JAWABAN ANDA :", z)
print("\n",5*"=","\n")
print (time.time() - start_time)