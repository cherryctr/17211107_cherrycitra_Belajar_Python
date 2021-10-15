# STUDY KASUS PENDAFTARAN MAHASISWA BARU
print('================================================')
print('Aplikasi Program hitung gaji karyawan')
print('================================================')

# TOTAL GAJI
gaji = 300000

# INPUT DATA 
inputNamaKaryawan= input('Masukan nama lengkap : ')

# PILIHAN DAFTAR TUNJANGAN
print('Daftar Tunjangan Golongan : ')
print('1')
print('2')
print('3')

inputGolonganJabatan = int(input('Masukan Golongan Jabatan (1/2/3): '))

# INPUT TUNJANGAN PENDIDIKAN
print('Daftar Tunjangan Pendidikan : ')
print('1. SMA/SMK')
print('2. D1')
print('3. D3')
print('4. S1')
inputPendidikan = int(input('Masukan Pendidikan (1/2/3/4) : '))
# inputJamKerja = input('Masukan Jumlah Jam Kerja : ')




print('================================================')
print('Berikut adalah data diri anda ')
print('================================================')

print('Karyawan Yang Bernama          : ',inputNamaKaryawan)
# print('Golongan Jabatan               : ',inputGolonganJabatan)
# print('Pendidikan                     : ',inputPendidikan)
print('Honor Yang diterima')

# HITUNG TUNJANGAN JABATAN BERDASARKAN GOLONGAN
if inputGolonganJabatan == 1:
   plusTungangan =  5/100
   totalTunjanganGajiJabatan = gaji * plusTungangan
   print('Tunjangan Jabatan : ', round(totalTunjanganGajiJabatan))

 
   
elif inputGolonganJabatan == 2:
   plusTungangan =  10/100
   totalTunjanganGajiJabatan = gaji * plusTungangan
   print('Tunjangan Jabatan : ', round(totalTunjanganGajiJabatan))

elif inputGolonganJabatan == 3:
    plusTungangan =  15/100
    totalTunjanganGajiJabatan = gaji * plusTungangan
    print('Tunjangan Jabatan : ', round(totalTunjanganGajiJabatan))
else:
    exit();

# HITUNG TUNJANGAN BERDASARKAN PENDIDIKAN
if inputPendidikan == 1:
   plusTunganganPendidikan =  2.5/100
   totalTunjanganGajiPendidikan = gaji * plusTunganganPendidikan
   print('Tunjangan Pendidikan : ', round(totalTunjanganGajiJabatan))

 
   
elif inputPendidikan == 2:
   plusTunganganPendidikan =  5/100
   totalTunjanganGajiPendidikan = gaji * plusTunganganPendidikan
   print('Tunjangan Pendidikan : ', round(totalTunjanganGajiPendidikan))

elif inputPendidikan == 3:
    plusTunganganPendidikan =  20/100
    totalTunjanganGajiPendidikan = gaji * plusTunganganPendidikan
    print('Tunjangan Pendidikan : ', round(totalTunjanganGajiPendidikan))

elif inputPendidikan == 4:
    plusTunganganPendidikan =  30/100
    totalTunjanganGajiPendidikan = gaji * plusTunganganPendidikan
    print('Tunjangan Pendidikan : ', round(totalTunjanganGajiPendidikan))
    
else:
    print('ok')
totalGajiSeluruh = gaji + totalTunjanganGajiJabatan + totalTunjanganGajiPendidikan
print('total gaji :',round(totalGajiSeluruh))