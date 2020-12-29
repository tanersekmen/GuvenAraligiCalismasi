class Guven:



    # güven aralığını (alfa değerini) belirlediğimiz girdi alıyoruz.
    def guvenBelirleme(self):
        #alfa değerini belirliyoruz
        self.guven = input("Alfa değerini girin:")
        return self.guven


    #Örneklem ortalaması değerini aldığımız fonksiyon.
    def orneklemOrt(self):
        self.orneklemort = input("Örneklem ortalamasını girin:")
        return self.orneklemort


    # Varyans bilinmiyorken sigma(standart sapma) bilinmez bu nedenle örneklem sapması vardır.
    # Örneklem sapma 's' ile gösterilir. Bu fonksiyonu, varyans bilinmiyor n >= 30 ise
    # hesap kısmında entegre edilir.
    def orneklemSapma(self):
        self.orneklemsapma = input("Örneklem Sapma değerini girin: ")
        return self.orneklemsapma


    # standart sapma değerini girdiğimiz fonksiyon
    def standarSapma(self):
        self.standart_sapma = input("Standart sapma değerinizi girin:")
        return self.standart_sapma


    #populasyon (n) değerini gireceğimiz fonksiyon
    def populasyon(self):
        self.kitle = input("Kitle değerinizi giriniz: ")
        return self.kitle


    # Oran için güven aralığı kurulacağı zaman işlevselleşecek fonksiyon.
    def oran_degeri(self):
        self.oran = input("P değerini giriniz (0.50,0.40 şeklinde): ")
        return self.oran


