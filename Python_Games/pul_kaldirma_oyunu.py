def pul_kaldirma_oyna(toplam_pul_adedi,max_pul):
    while toplam_pul_adedi > 0:
        oyuncu1 = int(input("1. Oyuncu : "))
        while oyuncu1 > max_pul or oyuncu1 < 1:
            print("Lütfen 1'den",(max_pul),"'e kadar bir rakam giriniz.")
            print("===========================================")
            oyuncu1 = int(input("1. Oyuncu : "))
        toplam_pul_adedi = toplam_pul_adedi - oyuncu1
        if toplam_pul_adedi <= 0:
            print(" *** 1.OYUNCU OYUNU KAZANDI. TEBRİKLER.. *** ")
            print("===========================================")
            break
        print("Oyunda ",toplam_pul_adedi,"adet pul kaldı.")
        print("===========================================")
        oyuncu2 = int(input("2. Oyuncu : "))
        while oyuncu2 > max_pul or oyuncu2 < 1:
            print("Lütfen 1'den",(max_pul),"'e kadar bir rakam giriniz.")
            print("===========================================")
            oyuncu2 = int(input("2. Oyuncu : "))
        toplam_pul_adedi = toplam_pul_adedi - oyuncu2
        if toplam_pul_adedi <= 0:
            print(" *** 2.OYUNCU OYUNU KAZANDI. TEBRİKLER.. *** ")
            print("===========================================")
            break
        print("Oyunda ",toplam_pul_adedi,"adet pul kaldı.")
        print("===========================================")
pul_kaldirma_oyna(100,5)