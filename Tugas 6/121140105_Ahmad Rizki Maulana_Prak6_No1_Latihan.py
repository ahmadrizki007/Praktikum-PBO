from abc import ABC, abstractmethod

class AkunBank(ABC):
    
    def __init__(self, nama, tahun, saldo):
        self.nama = nama
        self.tahun_daftar = tahun
        self.saldo = saldo
        
    @abstractmethod
    def transfer_saldo(self):
        pass
    
    @abstractmethod
    def lihat_suku_bunga(self):
        pass
    
    def lihat_saldo(self):
        print('Saldo : Rp',self.saldo)
        

class AkunGold(AkunBank):
    
    def __init__(self, nama, tahun, saldo):
        super().__init__(nama, tahun, saldo)
        self.usia_akun = 2023 - tahun
        self.bunga = 0
        
        
        if self.usia_akun >= 3 and self.saldo >= 1000000000:
            temp = 0.01*self.saldo
            self.saldo -= temp
            self.bunga = 1
        elif self.usia_akun < 3 and self.saldo >= 1000000000:
            temp = 0.02*self.saldo
            self.saldo -= temp
            self.bunga = 2
        elif self.saldo < 1000000000:
            temp = 0.03*self.saldo
            self.saldo -= temp
            self.bunga = 3
            
    
    def transfer_saldo(self):
        temp = self.saldo
        
        tf = int(input('Jumlah transfer : '))
        
        if self.usia_akun >= 3 and tf > 100000:
            self.saldo -= tf
        elif self.usia_akun < 3 and tf > 100000:
            self.saldo -= (tf+2000)
        elif tf < 100000:
            self.saldo -= tf
            
        if self.saldo < 0:
            print('Saldo Tidak Cukup!')
            self.saldo = temp
            self.transfer_saldo()
            
    def lihat_suku_bunga(self):
        print("Suku Bunga :",self.bunga,"%")
    

class AkunSilver(AkunBank):
    
    def __init__(self, nama, tahun, saldo):
        super().__init__(nama, tahun, saldo)
        self.usia_akun = 2023 - tahun
        self.bunga = 0
        
        
        if self.usia_akun >= 3 and self.saldo >= 10000000:
            temp = 0.01*self.saldo
            self.saldo -= temp
            self.bunga = 1
        elif self.usia_akun < 3 and self.saldo >= 10000000:
            temp = 0.02*self.saldo
            self.saldo -= temp
            self.bunga = 2
        elif self.saldo < 10000000:
            temp = 0.03*self.saldo
            self.saldo -= temp
            self.bunga = 3
            
    
    def transfer_saldo(self):
        temp = self.saldo
        
        tf = int(input('Jumlah transfer : '))
        
        if self.usia_akun >= 3 and tf > 100000:
            self.saldo -= (tf+2000)
        elif self.usia_akun < 3 and tf > 100000:
            self.saldo -= (tf+5000)
        elif tf < 100000:
            self.saldo -= tf
            
        if self.saldo < 0:
            print('Saldo Tidak Cukup!')
            self.saldo = temp
            self.transfer_saldo()
            
    def lihat_suku_bunga(self):
        print("Suku Bunga :",self.bunga,"%")
            
            
user1 = AkunGold("Ahmad Rizki",2022,10000000000)
user2 = AkunSilver("Rizki Maulana",2019,9000000000)

user1.lihat_saldo()
user1.lihat_suku_bunga()

user1.transfer_saldo()
user1.lihat_saldo()
print(40*"=")
user2.lihat_saldo()
user2.lihat_suku_bunga()

user2.transfer_saldo()
user2.lihat_saldo()
