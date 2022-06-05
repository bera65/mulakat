def birinciOncelik(array, baslangic, son): #bu fonksiyon değerleri alıp parçalamak için kullanacağız
    sayi = baslangic #sayiyi ilk değeden başlatalım
    for i in range(baslangic+1, son+1): #girilen array değerine göre i yi döndereceğiz
        if array[i] <= array[baslangic]: #değer öncekiden küçük veya eşit ise
            sayi += 1
            array[i], array[sayi] = array[sayi], array[i]
    array[sayi], array[baslangic] = array[baslangic], array[sayi] #hızlı bir arama yapıyoruz değerleri sıralamak için
    return sayi

def siralma(array, baslangic=0, son=None): #ikinci fonksiyon sıralama  yapmak için kullanacağız
    if son is None:
        son = len(array) - 1
    def _sirala(array, baslangic, son):
        if baslangic >= son:
            return
        sayi = birinciOncelik(array, baslangic, son) #önceki değerleri alalım
        _sirala(array, baslangic, sayi-1)
        _sirala(array, sayi+1, son)
    return _sirala(array, baslangic, son) #aldığımız değerleri küçükten büyüğe doğru sıraladık ve geri döndürdük

telefon = [0,5,44,841,21,71]
siralma(telefon)
print(telefon)
