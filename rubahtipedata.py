# merubah tipe data
##INTEGER
import time
from typing import DefaultDict
start_time = time.time()
print ("===INTEGER===")
data_int = 1
print ("data =", data_int, ",type =",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai int = 0
print ("data =", data_float, ",type =",type(data_float))
print ("data =", data_str, ",type =",type(data_str))
print ("data =", data_bool, ",type =",type(data_bool))

##FLOAT
print ("===FLOAT===")
han = 2
print ("data jancok =", han, ",type data =",type(han))

data_int = int(han) #akan dibulatkan kebawah
data_str = str(han)
data_bool = bool(han)
data_float = float(han) #akan false jika nilai int = 0
print ("data =", data_int, ",type =",type(data_int))
print ("data =", data_str, ",type =",type(data_str))
print ("data =", data_bool, ",type =",type(data_bool))
print ("dara =", data_float, "type =",type(data_float))

##string
print ("===string===")
data_str = "10"
print ("data =", data_str, ",type =",type(data_str))

data_int = int(data_str) 
data_bool = bool(data_str)
data_float = float(data_str)
print ("data =", data_int, ",type =",type(data_int))
print ("data =", data_bool, ",type =",type(data_bool))
print ("data =", data_float, ",type =",type(data_float))

print (time.time() - start_time)