daf_nama = []
daf_no   = []

def menu():
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    print()

print("Selamat datang!")
print()

while True:
    menu()
    pilih = int(input("Pilih menu: "))
    print()
    
    if pilih == 1:
        print("Daftar kontak:")
        for x in daf_nama :
            print("Nama: ",x)
            for y in daf_no :
                if daf_nama.index(x) == daf_no.index(y):
                    print("No Telepon: ", y)
        print()

    elif pilih == 2:
        nama = input("Nama: ")
        nomor = input("No Telepon: ")
        daf_nama.append(nama)
        daf_no.append(nomor)
        print("Kontak berhasil ditambahkan")
        print()
        
    elif pilih == 3:
        print("Program selesai, sampai jumpa!")
        break

    else :
        print("Menu tidak tersedia")
        print()
    


