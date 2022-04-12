evet = 1
hayır = 0

# User Registration
                                                                                  #coded by Salihvr 
kAdi = input("Choose Username : ")
kSifre = input("Choose Password : ")
print("Başarıyla Kayıt Oldunuz. Giriş İçin Yönlendiriliyorsunuz...")

# Member Login

girishakki = 3

while girishakki > 0:
    girishakki -= 1
    gkAdi = input("Member Name : ")
    gSifre = input("Password : ")

    if gkAdi ==  kAdi and gSifre == kSifre:
        print(f"{kAdi} Hoş Geldin. Anasayfaya Yönlendiriliyorsun...")
        break
    else:
        print(f"Kullanıcı Adı ya da Şifre Yanlış! Kalan Giriş Hakkınız {girishakki}")
        continue


# Reset PSW

while girishakki == 0:

    try:
        print("Şifrenizi Sıfırlamak İstiyor Musunuz? 1-Evet, 0-Hayır")
        cevap = int(input("Lütfen Birini Seçiniz : "))

        if cevap == evet:
            yenisifre = input("choose new password : ")
            yenisifre = kSifre.replace(kSifre, yenisifre)

            if yenisifre == kSifre:
                print("The new password cannot be the same as the old one")
            else:
                print("Your Password Has Been Changed Successfully! You Are Redirected To The Main Menu...")
                break

        elif cevap == hayır:
            print("Hesap ile Bağlantınız Kesilmiştir! Çıkış Yapılıyor...")
            break
        else:
            print("Geçersiz Giriş. Lütfen Kontrol Edin!")
    except:
        print("Geçersiz Tuşlama. Lütfen Kontrol Ediniz.")
        continue