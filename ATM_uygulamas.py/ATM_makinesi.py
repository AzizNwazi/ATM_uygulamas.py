print("\n")

print(
    """
*************************************
Hos geldiniz islem seciniz ....
1.Bakiye sorgulama
2.Para Yatirma
3.Para cekme

Programdan cikmek icin "q" ya basin. """
)

bakiye = 1000  # Başlangıçta hesapta bulunan bakiye miktarı

while True:
    islem = input("Islem seciniz: ")  # Kullanıcıdan işlem seçimini al

    if islem == "q":
        print("Cikis yapiliyor...")
        break  # "q" tuşuna basılınca programdan çıkılır
    elif islem == "1":
        print("Bakiyeniz:", bakiye)  # Bakiye sorgulama işlemi
    elif islem == "2":
        miktar = int(
            input("Yatirmak istediginiz miktari giriniz: ")
        )  # Para yatırma işlemi
        bakiye += miktar
    elif islem == "3":
        miktar = int(input("Cekmek istediginiz miktari girin: "))  # Para çekme işlemi
        if bakiye - miktar < 0:
            print("Hesabinizda o kadar miktar bulunmamaktadir.")
            continue  # Yeterli bakiye olmadığında kullanıcıya tekrar işlem seçtirilir
        bakiye -= miktar
    else:
        print(
            "Gecersiz secim..."
        )  # Geçersiz bir işlem seçildiğinde kullanıcıya uyarı verilir
