from prettytable import PrettyTable
print('===== GEROBAK FRIED CHICKEN =====')
tabelDagangan = PrettyTable(["Kode", "Jenis Potong", "Harga"])

# Tambahkan data baris
tabelDagangan.add_row(["D", "DADA", "2500"])
tabelDagangan.add_row(["P", "PAHA", "2000"])
tabelDagangan.add_row(["S", "SAYAP", "1500"])

print(tabelDagangan)

banyakJenisPemesanan = int(input('Masukan Banyak Jenis Pemesanan:'))

kodePotong= []
banyakPotong = []
jenisPotong = []
hargaSatuan = []
jumlahTotal = []

x = 0
while x < banyakJenisPemesanan:
    print("Jenis Ke - ", x+1)
    kodePotong.append(input("Masukan Kode Potong [D/P/S] : "))
    banyakPotong.append(int(input("Masukan Banyak Potong : ")))

    if  kodePotong[x] == "D" or kodePotong[x] == "d" :
        jenisPotong.append("Dada")
        hargaSatuan.append("2500")
        jumlahTotal.append(banyakPotong[x]*int("2500"))
    elif kodePotong[x] == "P" or kodePotong[x] == "p" :
        jenisPotong.append("Paha")
        hargaSatuan.append("2000")
        jumlahTotal.append(banyakPotong[x]*int("2000"))
    elif kodePotong[x] == "S" or kodePotong[x] == "s" :
        jenisPotong.append("Sayap")
        hargaSatuan.append("1500")
        jumlahTotal.append(banyakPotong[x]*int("1500"))
    else :
        jenisPotong.append("Kode Yang Anda Masukan Salah")
        hargaSatuan.append("0")
        jumlahTotal.append(banyakPotong[x]*int("0"))     
    x= x + 1


tabelHasil = PrettyTable(["No","Jenis Potong", "Harga Satuan" , "Banyak Beli", "Jumlah Harga" ])
a = 0
while a < banyakJenisPemesanan:
    tabelHasil.add_row([ str(a+1),jenisPotong[a],hargaSatuan[a], banyakPotong[a], jumlahTotal[a]])
    # tabelHasil.add_row(['------------','-------------------','-----------','-----------','-----------'])
    # tabelHasil.add_row([ "", "" ,"", 'TOTAL : ',sum])
    
    a = a + 1
    # list_of_table_lines = tabelHasil.get_string().split('\n')
    # cell.add_row.cells[0].merge(tabelHasil.add_row.cells[-1])
# print(list_of_table_lines)
print(tabelHasil.get_string(title=" STRUK PEMBELANJAAN DI GEROBAK FRIED CHICKEN"))

jumlah_bayar = sum(jumlahTotal)
pajak = jumlah_bayar * 0.1
jumlahAkhir = jumlah_bayar + pajak 

t = PrettyTable(['TOTAL BAYAR + PPN 10% = ',round(jumlahAkhir)])



# NOTE: t is the prettytable table object
# Get string to be printed and create list of elements separated by \n
list_of_table_lines = t.get_string().split('\n')

# Use the first line (+---+-- ...) as horizontal rule to insert later
horizontal_line = list_of_table_lines[0]

# Print the table
# Treat the last n lines as "result lines" that are seperated from the
# rest of the table by the horizontal line
result_lines = 1

print("\n".join(list_of_table_lines[:-(result_lines + 1)]))
print(horizontal_line)




