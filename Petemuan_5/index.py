from prettytable import PrettyTable

print('===== GEROBAK FRIED CHICKEN =====')

kode = ['D','P','S']
jenisPotong = ['dada','Paha','Sayap']
hargaSatuan = ['2500','2000','1500']
# Tentukan nama kolom apa saja ketika inisialisasi tabel

tabelDagangan = PrettyTable(["Kode", "Jenis Potong", "Harga"])

# Tambahkan data baris
tabelDagangan.add_row(["D", "DADA", "2500"])
tabelDagangan.add_row(["P", "PAHA", "2000"])
tabelDagangan.add_row(["S", "SAYAP", "1500"])


# Cetak Tabel Siswa
print(tabelDagangan)

banyakJenisPemesanan = int(input('Masukan Banyak Jenis Pemesanan:'))
# kodePotong = input('Masukan kodePotong (D/P/S):')
# banyakPotong = int(input('Banyak Potong :'))

for i  in range(banyakJenisPemesanan):
    print("Pesanan ke -  " + str(i+1))
    print('Daftar Menu : ')
    print('Dada')
    print('Paha')
    print('Sayap')
    kodePotong = input('Masukan kode Potong (D/S/P)) :')
    banyakPotong = int(input('Banyak Potong :'))



tabelHasil = PrettyTable(["No","Jenis Potong", "Harga Satuan" , "Banyak Beli", "Jumlah Harga" ])

if kodePotong == "D":
 hargaSatuans =  hargaSatuan[0]
 jenisPotongs = jenisPotong[0]
 jumlahHarga = hargaSatuan[0] * banyakPotong
elif kodePotong == "P":
 hargaSatuans =  hargaSatuan[1]
 jenisPotongs = jenisPotong[1]
 jumlahHarga = hargaSatuan[1] * banyakPotong
elif kodePotong == "S":
 hargaSatuans =  hargaSatuan[2]
 jenisPotongs = jenisPotong[2]
 jumlahHarga = hargaSatuan[2] * banyakPotong


for i in range(banyakJenisPemesanan):
    tabelHasil.add_row([ str(i+1),jenisPotongs,hargaSatuans, banyakPotong, jumlahHarga])

# Cetak Tabel Siswa
print(tabelHasil)


