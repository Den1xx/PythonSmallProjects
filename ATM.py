#Bankamatik uygulaması

denizHesap = {
    'ad': 'Deniz KK',
    'hesapNo': '12345678',
    'bakiye': 6000,
    'ekHesap': 3000,
}

aliHesap = {
    'ad': 'Ali Turan',
    'hesapNo': '12345678',
    'bakiye': 2000,
    'ekHesap': 1000,
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanımı = input('ek hesap kullanılsın mı? (e/h) ')

            if ekHesapKullanımı == 'e':
                ekHesapkullanılacakmiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapkullanılacakmiktar
                print('paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)    
            else:
                print(f"kullanıcı hesabında {hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('bakiyeniz yetersiz.')
            bakiyeSorgula(hesap)      


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} numaralı hesabınızın bakiyesi: {hesap['bakiye']} TL ve ek hesabınızda ise {hesap['ekHesap']} TL bulunmaktadır.")



print('***********************')


def paraYatir(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    if miktar >= 10000:
        aktarma = input(f'yatırma limitinizi aştınız: {miktar} fazlalığı ek hesaba aktarmak istermisiniz ? (e/h)')
        if aktarma == 'e':
            limitAsimi = miktar - 10000
            bakiyeNet = miktar - limitAsimi
            hesap['ekHesap'] += limitAsimi
            hesap['bakiye'] += bakiyeNet
            bakiyeSorgula(hesap)
        else:
            limitAsimi = miktar - 10000
            bakiyeNet = miktar - limitAsimi
            hesap['bakiye'] += bakiyeNet
            print(f'lütfen para üstünüzü alınız: {limitAsimi}')
            bakiyeSorgula(hesap)

    else:
        hesap['bakiye'] += miktar
        bakiyeSorgula(hesap)
        




paraYatir(denizHesap, 14000)
paraCek(denizHesap, 19000)
            

