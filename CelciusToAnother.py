# Latihan konversi satuan temperature
import time
start_time = time.time()
# Program konversi celcius ke satuan lain 
print("\nPROGRAM PENGHITUNG TEMPERATURE\n")
# Celcius
celci = float(input('Masukan Suhu Dalam Celcius :'))
print("Suhu Dalam Celcius", celci," Derajat Celcius")
# Reamur
ream = (4/5) * celci
print("Suhu Dalam Reamur Adalah ",ream, "Derajat Reamur")
# Farenheit
Fahren = ((9/5) * celci) + 32
print("Suhu Dalam Fahrenheit Adalah ",Fahren, "Derajat Fahrenheit")

# Kelvin
Kel = celci + 273
print("Suhu Dalam Kelvin Adalah ",Kel, "Derajat Kelvin")
print()
print (time.time() - start_time)
