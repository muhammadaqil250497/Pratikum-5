data = {}
while True:
    print("")
    x = input("(L)ihat, (T)ambah, (U)bah, (H)apus,(C)ari, (K)eluar: ")
# Untuk keluar dari program
    if x.lower() == "k":
        print("Keluar dari program")
        break
# untuk melihat list
    elif x.lower() == "l":
        if data.items():
            print("================================== Daftar Nilai ======================================")
            print("======================================================================================")
            print("| No | NIM | NAMA | TUGAS | UTS | UAS | AKHIR |")
            print("======================================================================================")
            i = 0
            for x in data.items():
                i += 1
                print("| {6:4} | {0:13s} | {1:13} | {2:8d} | {3:6d} | {4:7d} | {5:12.2f} | " \
                      .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
                print("======================================================================================")
        else:
            print("===================================== Daftar Nilai ===================================")
            print("======================================================================================")
            print("| No | Nama | NIM | TUGAS | UTS | UAS | Nilai Akhir |")
            print("======================================================================================")
            print("| Tidak Ada Daftar Nilai |")
            print("======================================================================================")
# Untuk menambahkan data
    elif x.lower() == "t":
        print("Tambah Data")
        nim = int(input("NIM\t\t: "))
        nama = input("Nama\t\t: ")
        tugas = int(input("NIlai Tugas\t: "))
        uts = int(input("Nilai UTS\t: "))
        uas = int(input("Nilai UAS\t: "))
        nilaiakhir = ((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
        data[nama] = nim, tugas, uts, uas, nilaiakhir
# Untuk mengubah data
    elif x.lower() == "u":
        print("Edit Data Nilai Mahasiswa")
        nama = input("Masukan Nama\t\t:")
        if nama in data.keys():
            nim = input("NIM\t\t\t:")
            tugas = int(input("Nilai Tugas Baru\t: "))
            uts = int(input("Nilai UTS Baru\t\t: "))
            uas = int(input("Nilai UAS Baru\t\t: "))
            nilaiakhir = ((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
            data[nama] = nim, tugas, uts, uas, nilaiakhir
        else:
            print("Data nilai{0} tidak ada ".format(nama))
# Untuk menghapus data
    elif x.lower() == "h":
        print("Hapus Data Nilai Mahasiswa")
        nama = input("Masukan Nama\t:")
        if nama in data.keys():
            del data[nama]
        else:
            print("Data {0} tidak ada".format(nama))
# Untuk Mencari data
    elif x.lower() == "c":
        print("Cari Data Nilai Mahasiswa")
        nama = input("Masukan Nama\t: ")
        if nama in data.keys():
            print("============================ Daftar Nilai ========================================")
            print("==================================================================================")
            print("|No | Nama | NIM | TUGAS | UTS | UAS | Nilai Akhir |")
            print("| {6:4} | {0:13s} | {1:13} | {2:8d} | {3:6d} | {4:7d} | {5:12.2f} | " \
                      .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print("==================================================================================")
        else:
            print("Datanya {0} tidak ada ".format(nama))
    else:
        print("============================ Daftar Nilai ============================================")
        print("======================================================================================")
        print("| No | Nama | NIM | TUGAS | UTS | UAS | Nilai Akhir |")
        print("======================================================================================")
        print("| Tidak Ada Daftar Nilai |")
        print("======================================================================================")

else:
    print("Pilih Menu Yang Tersedia")