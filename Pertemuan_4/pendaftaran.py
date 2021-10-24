# STUDY KASUS PENDAFTARAN MAHASISWA BARU
print('================================================')
print('Aplikasi Pendaftaran Online Calon Mahasiswa Baru')
print('================================================')


inputNamaMahasiswa = input('Masukan nama lengkap : ')
inputNis = input('Masukan Nis : ')
inputJurusan = input('Masukan Nama Jurusan  : ')
print('Daftar Biaya Kuliah')
print('1. SI = Rp.2.400.000,00')
print('2. SIA = Rp.2.000.000,00')
inputNamaProdi = int(input('Pilih Prodi Yang Diinginkan (1/2) : '))


print('================================================')
print('Berikut adalah data diri anda ')
print('================================================')

print('Nama                           : ',inputNamaMahasiswa)
print('Nis                            : ',inputNis)
print('Jurusan                        : ',inputJurusan)
if inputNamaProdi == 1:
   
    print('Kode Jurusan                   : SI')
    print('Nama Prodi yang kamu ambil     : Sistem Informasi')
    print('Harga                          : Rp.2.400.000')
elif inputNamaProdi == 2:
    print('Kode Jurusan                   : SIA')
    print('Nama Prodi yang kamu ambil     : Sistem Informasi Akuntansi')
    print('Nama Prodi yang kamu ambil SIA : 2.000.000')


