import sys
word=sys.argv[1]
letter=sys.argv[2].split(",")
listKelime = []
ınModundaKullanılanlar = []
outModundaKullanılanlar = []
sayacDahaOnceInModundaKullanılanlar=False
sayacDahaOnceOutModundaKullanılanlar=False
sayacInModundaMı=True
listWord = list(word)
sayac2=0
""""
sayacInModundaMı False olursa Out modunda olmuş olur
"""
birdenFazlaKelime = []
listDogruKelime = []
kalanTahmin = 5
listDogruKelime.extend(list(word))
kelimeninUzunlugu = word.__len__()
print('You have ', kalanTahmin, ' guesses left')
for i in range(kelimeninUzunlugu):
    listKelime.append("-")
print(listKelime)
print('---------------------------------------')
for x in letter:
    sayac2 += 1
    if(ınModundaKullanılanlar.count(x)>0):
        sayacDahaOnceInModundaKullanılanlar=True
    if (outModundaKullanılanlar.count(x) > 0):
        sayacDahaOnceOutModundaKullanılanlar = True
    if (word.count(x) > 0):
        if (word.count(x) == 1 and sayacDahaOnceInModundaKullanılanlar==False and sayacInModundaMı==True):
            sayac = word.index(x)
            listKelime.pop(sayac)
            listKelime.insert(sayac, x)
            ınModundaKullanılanlar.append(x)
            sayacInModundaMı=True
            print('Guessed word:', x, 'You are in IN mode')
            print('You have ', kalanTahmin, 'guesses left')
            print(listKelime)
            print('---------------------------------------')
        elif(word.count(x) == 1 and sayacDahaOnceOutModundaKullanılanlar==False and sayacInModundaMı==False):
            kalanTahmin=kalanTahmin-1
            outModundaKullanılanlar.append(x)
            print('Guessed word: ' ,x , 'You are in OUT mode')
            print('You have ', kalanTahmin, 'guesses left')
            print(listKelime)
            print('---------------------------------------')
        elif (word.count(x)== 1 and sayacDahaOnceOutModundaKullanılanlar == True and sayacInModundaMı == False):
            outModundaKullanılanlar.append(x)
            kalanTahmin = kalanTahmin - 1
            outModundaKullanılanlar.append(x)
            print('Guessed word: ', x, 'You are in OUT mode')
            print('You have ', kalanTahmin, 'guesses left')
            print(listKelime)
            print('---------------------------------------')
        elif (word.count(x)== 1 and sayacDahaOnceInModundaKullanılanlar == True and sayacInModundaMı == True):
            sayacInModundaMı=False
            kalanTahmin=kalanTahmin-1
            ınModundaKullanılanlar.append(x)
            print('Guessed word: ', x, 'is used in IN mode. The game turned into OUT mode')
            print('You have ', kalanTahmin, 'guesses left')
            print(listKelime)
            print('---------------------------------------')
        elif(word.count(x) > 1 and sayacDahaOnceInModundaKullanılanlar==False and sayacInModundaMı==True):
            for i in range(kelimeninUzunlugu):
                if (word[i] == x):
                    listKelime.pop(i)
                    listKelime.insert(i, x)
            print('Guessed word:', x, 'You are in IN mode')
            print('You have ', kalanTahmin, 'guesses left')
            print(listKelime)
            print('---------------------------------------')
            ınModundaKullanılanlar.append(x)
        elif (word.count(x) > 1 and sayacDahaOnceOutModundaKullanılanlar == True and sayacInModundaMı == False):
            kalanTahmin=kalanTahmin-1
            outModundaKullanılanlar.append(x)
            print('Guessed word: ', x, 'You are in OUT mode')
            print('You have ', kalanTahmin, 'guesses left')
            print(listKelime)
            print('---------------------------------------')

        elif (word.count(x) > 1 and sayacDahaOnceInModundaKullanılanlar == True and sayacInModundaMı == True):
            sayacInModundaMı=False
            kalanTahmin = kalanTahmin - 1
            for i in range(kelimeninUzunlugu):
                if (word[i] == x):
                    listKelime.pop(i)
                    listKelime.insert(i, x)
            ınModundaKullanılanlar.append(x)
            print('Guessed word: ', x, 'is used in IN mode. The game turned into OUT mode')
            print('You have ', kalanTahmin, 'guesses left')
            print(listKelime)
            print('---------------------------------------')
        elif (word.count(x) > 1 and sayacDahaOnceOutModundaKullanılanlar == False and sayacInModundaMı == False):
            for i in range(kelimeninUzunlugu):
                if (word[i] == x):
                    listKelime.pop(i)
                    listKelime.insert(i, x)
            outModundaKullanılanlar.append(x)
    elif(word.count(x)==0):
        if(sayacInModundaMı==True):
            sayacInModundaMı=False
            kalanTahmin=kalanTahmin-1
            print('Guessed word:', x, 'The game turned into OUT mode')
            print('You have ', kalanTahmin, 'guesses left')
            print(listKelime)
            print('---------------------------------------')
        elif(sayacInModundaMı==False):
            sayacInModundaMı=True
            print('Guessed word:', x, 'The game turned into IN mode')
            print('You have ', kalanTahmin, 'guesses left')
            print(listKelime)
            print('---------------------------------------')
    if (kalanTahmin > 0 and listKelime == listWord):
        print("You won the game")
        break
    elif(kalanTahmin>0 and sayac2==letter.__len__()):
        print("You finished all letters")
        print("You lost the game")
        break
    elif(kalanTahmin==0 and listKelime.__len__()!=kelimeninUzunlugu):
        print("You lost the game")
        break



