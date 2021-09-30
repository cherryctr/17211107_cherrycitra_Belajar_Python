from datetime import datetime




print("=========================================")
print("======= TOKO MAINAN ANAK  =======")
print("=========================================")


x = datetime.now()
namaPembeli = str(input("Masukan Nama Pembeli : "))

#Kode barang di input otomatis berdasarkan Hari,Bulan,Tanggal,tahun,detik 
kodeBarangx = x.strftime("%a") + " " + "-" + " "  + x.strftime("%x") + x.strftime("%S")
kodeBarang = kodeBarangx.replace("/","")
hargaBarang = int(input("Masukan Harga Barang : "))
qtyBarang = int(input("Masukan Total Barang : "))
totalBayar = hargaBarang * qtyBarang



print("Nama Pembeli :" + " " +namaPembeli)
print("kode Barang  :" + " " +kodeBarang.upper())
print("Harga Barang :" ,hargaBarang)
print("Jumlah Beli  :" ,qtyBarang)
print(f"TOTAL        :",totalBayar )