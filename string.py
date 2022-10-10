# pengenalan string
from time import process_time


data = "ini adalah string"
#string adalah kumpulan dari karakter
print(data)
print(type(data))

# 1 cara membuat string
'''
1. dengan menggunakan single quote '...'
2. dengan menggunakan double quote "..."
'''

data = 'menggunakan single quote'
print(data)
data = "menggunakan double quote"
print(data)

print('"halo, apa kabar?"') #menggunakan tanda petik berlaku kebalikan

# 2. menggunakan tanda \
# membuat tanda ' menjadi string
print('mari solat jum\'at')
print('g\'day, isn\'t it?')

# backslash
print("C:\\user\\Ucup")

#tab
print("ucup\t\totong, jauhan")

#backspace
print("ucup \botong, jadi deketan" )

#newline
print("baris pertama.\nbaris kedua") # LF line feed --> unix
print("baris pertama.\rbaris kedua.") # CR carriage return --> comodore, acorn, lisp
print("baris pertama \r\n baris kedua") # CRLF Line feed Carriage Return --> windows

# 3. string literal atau raw 
# hati -hati
print('C:\\new folder') #path nya akan salah
# menggunakan raw string menggunakan r didepan
print(r'C:\new folder\b\b\\')

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

#multiline literal string & raw
print(r"""
Website : www.ucup.com/newID
C\\\
""")