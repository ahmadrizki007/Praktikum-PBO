class Smartphone:
    def __init__(self, merk, warna, tipe, harga):
        self.__merk = merk     # atribut private
        self._warna = warna    # atribut protected
        self.tipe = tipe       # atribut public
        self.harga = harga     # atribut public
        
        
    def info(self):
        print(f"Smartphone {self.__merk}, warna {self._warna}, tipe {self.tipe}, harga {self.harga}")
        
    def merk(self):
        return self.__merk

Smartphone = Smartphone("Iphone14", "Deep Purple","Promax" , 21000000)
Smartphone.info() # Smartphone Iphone14, warna Deep Purple, Tipe Promax, harga 21000000

print(Smartphone._warna) # Hitam
print(Smartphone.tipe)  # Promax
print(Smartphone.harga)  # 21000000

# print(Smartphone1.__merk)  # AttributeError: 'Smartphone' object
