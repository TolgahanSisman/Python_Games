queue = ["Ayşe","Ali","Özgür","Cem","Melis","Suna","Derya","Aykut","Duygu","Şeref"]
liste=[]
print("\nSiranin ilk durumu --> ",queue)

def oyun():
    for i in range(9):
        for i in range(3):
            cevap = int(input("\nBir sayı giriniz: "))
            if cevap < 10 and cevap > 0:
                sıra=queue.index(queue[cevap])
                liste = queue[0:sıra]
                del queue[0:sıra]
                queue.extend(liste)
                print("Güncel sıra -->        ",queue)
                print("______________________________________________________")
            else:
                print("1-10 arası bir sayı giriniz.")
        print("______________________________________________________")
        print("\nSıra başındaki oyuncu elendi --> ",queue.pop(0))
        print("______________________________________________________")
        print("\nSırada kalan oyuncular --> ",queue)
    print("\nKazanan oyuncu ","----->",queue[0], "<-----")
oyun()