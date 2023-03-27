class orang:
    def __init__(self, nama, nim, kelas_siakad, jumlah_sks):
        self.nama = nama
        self.nim = nim
        self.kelas_siakad = kelas_siakad
        self.jumlah_sks = jumlah_sks
        
    def tampil(self):
        print("Nama: ", self.nama)
        print("NIM: ", self.nim)
        print("kelas siakad: ", self.kelas_siakad)
        print("Jumlah SKS:", self.jumlah_sks)
    
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
kelas_siakad = input("Masukkan kelas Siakad: ")
jumlah_sks = int(input("Masukkan jumlah SKS: "))

print("====================CETAK========================")

siswa = orang(nama, nim, kelas_siakad, jumlah_sks)
siswa.tampil()
