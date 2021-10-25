# NAMA : CHERRY CITRA CAHYANING
# NIM : 17211107

# Untuk menjalankan harus install pretytable dulu
# Dengan Cara pip install prettytable

from prettytable import PrettyTable

banyakLooping = int(input('Masukan Banyak Looping :  '))

listNim= []
listNama= []
listUts = []
listUas = []
# listTotal= []



x = 0
while x < banyakLooping:
    print("DATA KE  - ", x+1)
    listNim.append(input("Masukan NIM : "))
    listNama.append(input("Masukan Nama : "))
    listUts.append(int(input("Masukan Nilai UTS Anda : ")))
    listUas.append(int(input("Masukan NIlai UAS Anda : "))) 
    x= x + 1


tabelHasil = PrettyTable(["No","Nim","Nama", "Nilai UTS" , "Nilai UAS","Hasil Akhir"])
a = 0
while a < banyakLooping:
    numbers = listUas + listUts
    average = sum(numbers) / len (numbers)
   
    tabelHasil.add_row([ str(a+1),listNim[a],listNama[a],listUts[a], listUas[a],average])
    a = a + 1
    
print(tabelHasil.get_string(title="Hasil Nilai Mahasiswa"))





