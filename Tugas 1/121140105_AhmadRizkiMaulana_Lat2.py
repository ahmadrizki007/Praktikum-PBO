#Latihan 2#
##Ahmad Rizki Maulana_121140105##

username = "informatika"
password = "12345678"

for i in range(3):
    username = str(input("Username anda : "))
    password = str(input("Password anda : "))
    if username == username and password == password:
        print("Berhasil login!")
        exit()
    elif i == 2 and (username != username or password != password):
        print("Akun anda diblokir!")
    else:
        print("Username atau password salah, coba lagi!")
    print()
