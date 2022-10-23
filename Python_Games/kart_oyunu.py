import random
                                                    # KARTLAR RASTGELE DAĞITILDI #
kartlar = list(range(1, 101))
oyuncu1 = random.sample(kartlar, 5)
# print("==========================================================")
# print("Oyuncu1'in kartlari  -->", oyuncu1)
oyuncu2 = random.sample(kartlar, 5)
# print("Oyuncu2'nin kartlari -->", oyuncu2)
oyuncu1_ters = list()
oyuncu2_ters = list()
oyuncu1_puan = 0
oyuncu2_puan = 0

def quicksort(start, end, liste):                   # SIRALAMA ALGORİTMASI #
    if start >= end:
        return
    pivot = liste[end]
    j = start
    for i in range(j, end):
        if liste[i] < pivot:
            z = liste[j]
            liste[j] = liste[i]
            liste[i] = z
            j += 1

    a = liste[end]
    liste[end] = liste[j]
    liste[j] = a

    quicksort(start, j - 1, oyuncu1)
    quicksort(j + 1, end, oyuncu1)
    quicksort(start, j - 1, oyuncu2)
    quicksort(j + 1, end, oyuncu2)

quicksort(0, len(oyuncu1)-1, oyuncu1)
quicksort(0, len(oyuncu2)-1, oyuncu2)
# print("==========================================================")
# print("Oyuncu1'in sıralanmış kartlari   -->", oyuncu1)
# print("Oyuncu2'nin sıralanmış kartlari  -->", oyuncu2)
# print("==========================================================")

def kart_kapatma():                                 # KARTLAR KÜÇÜKTEN BÜYÜĞE KAPATILDI #
    for i in oyuncu1:
        oyuncu1_ters.append(i)
        # print(oyuncu1_ters)
    oyuncu1_ters.reverse()

    # print("===========================")
    for i in oyuncu2:
        oyuncu2_ters.append(i)
        # print(oyuncu2_ters)
    oyuncu2_ters.reverse()
    # print("===========================")

kart_kapatma()

def kart_atma():                                    # KARTLAR ORTAYA ATILIYOR #
    oyuncu1_puan = 0
    oyuncu2_puan = 0
    for i in range(5):
        print("\nHamle İçin 'Enter' Tuşlayınız.")
        input()
        x = oyuncu1_ters.pop()
        y = oyuncu2_ters.pop()
        if x > y:
            oyuncu1_puan +=1
            print("Oyuncu1 : ", x)
            print("Oyuncu2 : ", y)
            print("Oyuncu1 1 puan kazandı.")
            print("===========================")
        else:
            oyuncu2_puan += 1
            print("Oyuncu1 : ", x)
            print("Oyuncu2 : ", y)
            print("Oyuncu2 1 puan kazandı.")
            print("===========================")

    print("Oyuncu1 toplam puan: ", oyuncu1_puan)
    print("Oyuncu2 toplam puan: ", oyuncu2_puan)
    print("===========================")
    if oyuncu1_puan > oyuncu2_puan:
        print("Kazanan", format(oyuncu1_puan), "puan ile Oyuncu1",)
    else:
        print("Kazanan", format(oyuncu2_puan), "puan ile Oyuncu2",)

kart_atma()

