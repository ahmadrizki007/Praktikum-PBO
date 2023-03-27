class Komputer:
    def __init__(self, merk, jenis, harga):
        self.merk = merk
        self.jenis = jenis
        self.harga = harga

    def __str__(self):
        return f"{self.jenis} produksi {self.merk}"

class Processor(Komputer):
    def __init__(self, merk, jenis, harga, core, kecepatan):
        super().__init__(merk, jenis, harga)
        self.core = core
        self.kecepatan = kecepatan

    def __str__(self):
        return f"{self.jenis} {self.core} core {self.kecepatan} GHz"

class RAM(Komputer):
    def __init__(self, merk, jenis, harga, capacity):
        super().__init__(merk, jenis, harga)
        self.capacity = capacity

    def __str__(self):
        return f"{self.jenis} {self.capacity}"

class HDD(Komputer):
    def __init__(self, merk, jenis, harga, capacity, rpm):
        super().__init__(merk, jenis, harga)
        self.capacity = capacity
        self.rpm = rpm

    def __str__(self):
        return f"{self.jenis} {self.capacity} {self.rpm} RPM"

class VGA(Komputer):
    def __init__(self, merk, jenis, harga, capacity):
        super().__init__(merk, jenis, harga)
        self.capacity = capacity

    def __str__(self):
        return f"{self.jenis} {self.capacity}"

class PSU(Komputer):
    def __init__(self, merk, jenis, harga, daya):
        super().__init__(merk, jenis, harga)
        self.daya = daya

    def __str__(self):
        return f"{self.jenis} {self.daya} W"

P1 = Processor('Intel', 'Core i7 7740X', 4350000, 4, '4.3')
P2 = Processor('AMD', 'Ryzen 5 3600', 2500000, 4, '3.6')
RAM1 = RAM('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB')
RAM2 = RAM('G.SKILL', 'DDR4 2400MHz', 328000, '4GB')
HDD1 = HDD('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)
HDD2 = HDD('Seagate', 'HDD 2.5 inch', 295000, '1TB', 7200)
VGA1 = VGA('Asus', 'VGA GTX 1050', 250000, '2GB')
VGA2 = VGA('Asus', 'VGA GTX 1060Ti', 250000, '8GB')
PSU1 = PSU('Corsair', 'Corsair V550', 250000, '550')
PSU2 = PSU('Corsair', 'Corsair V550', 250000, '550')

Rakit = [[P1, RAM1, HDD1, VGA1, PSU1], [P2, RAM2, HDD2, VGA2, PSU2]]

for i, komputer in enumerate(Rakit):
    print(f"Komputer {i+1}")
    for j in komputer:
        print(j)
    print()
