teori = input("Nilai ujian teori : ")
prak = input("Nilai ujian praktek : ")

t = float(teori)
p = float(prak)

if (t >= 70) and (p >= 70 )  :
    print("Selamat, anda lulus!")
elif (t < 70) and (p < 70 )  :
    print("Anda harus mengulang ujian teori dan praktek.")
elif (t >= 70) :
     print("Anda harus mengulang ujian praktek.")
else :
    print("Anda harus mengulang ujian teori.")