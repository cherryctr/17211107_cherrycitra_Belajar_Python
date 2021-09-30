#Operator logika digunakan melakukan operasi terhadap nilai dari tipe boolean (True dan False).

#Operasi AND hanya akan meghasilkan nilai True saat kedua operand bernilai True, selain dari pada itu akan bernilai False, sementara untuk operator OR akan menghasilkan nilai True jika salah satu atau kedu operand bernilai True. Operasi OR akan menghasilkan nilai False saat kedua operand bernilai False.
print("Operasi AND")
print("True and True \t:", True and True)
print("True and False \t:", True and False)
print("False and True \t:", False and True)
print("False and False\t:", False and False)


#Operasi OR akan menghasilkan nilai False saat kedua operand bernilai False.
print("\nOperasi OR")
print("True or True \t:", True or True)
print("True or False \t:", True or False)
print("False or True \t:", False or True)
print("False or False \t:", False or False)


#Sementara untuk operasi NOT (negasi) adalah kebalikan dari nilai operand, jika nilai operand bernilai True maka dengan operasi NOT akan menghasilkan nilai False begitu juga sebaliknya jika benilai False akan di balik menjadi True.
print("\nOperasi NOT")
print("not True \t:", not True)
print("not False \t:", not False)