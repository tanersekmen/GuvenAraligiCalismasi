from ana_guven_aralik import Guven


g1 = Guven()

main_menu = True
while True:
    if main_menu:
        #seçimlere göre aksiyon veren yapının temel kısmı burada oluşuyor.
        print("""
        ---
            Güven Aralığı İçin Seçin:
        A. Varyans Bilinirken Güven Aralığı
        B. Varyans Bilinmiyor fakat n >=30 için Güven Aralığı
        C. Oran için Güven Aralığı
        D. Çıkış
        ---""")
        main_menu = False
        choice = input("Yapmak istediğiniz işlemi giriniz:")

        # varyans bilinirken güven aralığı
        if choice == 'A' or choice == 'a':
            # hangi güven düzeyinde olduğuna göre sonuç farklılaşıyor.
            # her güven derecesinin z tablosunda farklı değerleri vardır.
            print("""
        ----- Güven Düzeyleri
        A. %99
        B. %95
        C. %90
        D. Ana Menü
        """)

            secim = input("İşleminizi seçin:")

            if secim == '90':
                #%90 güvenle olan değerin Zalpha/2 değeri guven_90'a denk gelmektedir.
                guven_90 = 1.645
                orneklem = float(g1.orneklemOrt())
                sapma = float(g1.standarSapma())
                populasyon = float(g1.populasyon())


                # formüllerin her birini repodan kontrol edebilirsiniz.
                alt_sinir = orneklem - (guven_90 * sapma / (populasyon**(1/2)))
                ust_sinir = orneklem + (guven_90 * sapma / (populasyon**(1/2)))
                print("Alt sınır: ", alt_sinir)
                print("Ust sınır:", ust_sinir)
                break

            elif secim == '95':
                # %95 güvenle olan değerin Zalpha/2 değeri guven_95'e denk gelmektedir.
                guven_95 = 1.96
                orneklem = float(g1.orneklemOrt())
                sapma = float(g1.standarSapma())
                populasyon = float(g1.populasyon())



                alt_sinir = orneklem - (guven_95 * sapma / (populasyon**(1/2)))
                ust_sinir = orneklem + (guven_95 * sapma / (populasyon**(1/2)))
                print("Alt sınır: ", alt_sinir)
                print("Ust sınır:", ust_sinir)
                break

            elif secim == '99':
                # %99 güvenle olan değerin Zalpha/2 değeri guven_99'a denk gelmektedir.
                guven_99 = 2.58
                orneklem = float(g1.orneklemOrt())
                sapma = float(g1.standarSapma())
                populasyon = float(g1.populasyon())


                alt_sinir = orneklem - (guven_99 * sapma / (populasyon**(1/2)))
                ust_sinir = orneklem + (guven_99 * sapma / (populasyon**(1/2)))
                print("Alt sınır: ", alt_sinir)
                print("Ust sınır:", ust_sinir)
                break


            elif secim=='d' or secim =='D':
                # ana menüye dönmek için d seçeneğine basınca ana ekrana dönmesi için yazdığım dizin.
                main_menu = True
            else:
                print("Hatalı işlem yaptınız.")


        #-----------------------------

        elif choice == 'B' or choice == 'b':
            # Güven derecesine göre değişkenlik gösteren değerler vardır.
            print("""
            ----- Güven Düzeyleri
            A. %99
            B. %95
            C. %90
            D. Ana Menü
            """)

            secim = input("İşleminizi seçin:")

            if secim == '90':
                # %90 güvenle olan değerin Zalpha/2 değeri guven_90'a denk gelmektedir.
                guven_90 = 1.645
                orneklem = float(g1.orneklemOrt())
                orneklem_sapma = float(g1.orneklemSapma())
                populasyon = float(g1.populasyon())


                alt_sinir = orneklem - (guven_90 * orneklem_sapma / (populasyon**(1/2)))
                ust_sinir = orneklem + (guven_90 * orneklem_sapma / (populasyon**(1/2)))
                print("Alt sınır: ", alt_sinir)
                print("Ust sınır:", ust_sinir)
                break

            elif secim == '95':
                # %95 güvenle olan değerin Zalpha/2 değeri guven_95'e denk gelmektedir.
                guven_95 = 1.96
                orneklem = float(g1.orneklemOrt())
                orneklem_sapma = float(g1.orneklemSapma())
                populasyon = float(g1.populasyon())



                alt_sinir = orneklem - (guven_95 * orneklem_sapma / (populasyon**(1/2)))
                ust_sinir = orneklem + (guven_95 * orneklem_sapma / (populasyon**(1/2)))
                print("Alt sınır: ", alt_sinir)
                print("Ust sınır:", ust_sinir)
                break

            elif secim == '99':
                # %99 güvenle olan değerin Zalpha/2 değeri guven_99'a denk gelmektedir.
                guven_99 = 2.58
                orneklem = float(g1.orneklemOrt())
                orneklem_sapma = float(g1.orneklemSapma())
                populasyon = float(g1.populasyon())



                alt_sinir = orneklem - (guven_99 * orneklem_sapma / (populasyon**(1/2)))
                ust_sinir = orneklem + (guven_99 * orneklem_sapma / (populasyon**(1/2)))
                print("Alt sınır: ", alt_sinir)
                print("Ust sınır:", ust_sinir)
                break


            elif secim == 'd' or secim == 'D':
                # ana menüye dönmek için d seçeneğine basınca ana ekrana dönmesi için yazdığım dizin.
                main_menu = True
            else:
                print("90 95 99 ya da d değerlerini giriniz.")


        # -----------------------------

        elif choice=='c' or choice=='C':
            # Güven derecesine göre değişkenlik gösteren değerler vardır.
            print("""
            ----- Güven Düzeyleri
            A. %99
            B. %95
            C. %90
            D. Ana Menü
            """)
            secim = input("İşleminizi seçin:")

            if secim == '90':
                # %90 güvenle olan değerin Zalpha/2 değeri guven_90'a denk gelmektedir.
                guven_90 = 1.645
                p_orani = float(g1.oran_degeri())
                populasyon = float(g1.populasyon())

                # diğerlerine farklı olarak burada oranın aralığı olduğu için p değeri ve
                # formül içerisinde **(1/2) var. Amacım herhangi bir kütüphaneye bağlı kalmadan
                # direkt olarak karekökünü bu şekilde almak istedim.
                alt_sinir = p_orani - (guven_90 * ((p_orani*(1-p_orani) / populasyon)**(1/2)))
                ust_sinir = p_orani + (guven_90 * ((p_orani*(1-p_orani) / populasyon)**(1/2)))
                print("Alt sınır: ", alt_sinir)
                print("Ust sınır:", ust_sinir)
                break


            elif secim == '95':
                # %95 güvenle olan değerin Zalpha/2 değeri guven_95'e denk gelmektedir.
                guven_95 = 1.96
                p_orani = float(g1.oran_degeri())
                populasyon = float(g1.populasyon())


                # diğerlerine farklı olarak burada oranın aralığı olduğu için p değeri ve
                # formül içerisinde **(1/2) var. Amacım herhangi bir kütüphaneye bağlı kalmadan
                # direkt olarak karekökünü bu şekilde almak istedim.
                alt_sinir = p_orani - (guven_95 * ((p_orani*(1-p_orani) / populasyon)**(1/2)))
                ust_sinir = p_orani + (guven_95 * ((p_orani*(1-p_orani) / populasyon)**(1/2)))
                print("Alt sınır: ", alt_sinir)
                print("Ust sınır:", ust_sinir)
                break

            elif secim == '99':
                # %99 güvenle olan değerin Zalpha/2 değeri guven_99'a denk gelmektedir.
                guven_99 = 2.58
                p_orani = float(g1.oran_degeri())
                populasyon = float(g1.populasyon())

                # diğerlerine farklı olarak burada oranın aralığı olduğu için p değeri ve
                # formül içerisinde **(1/2) var. Amacım herhangi bir kütüphaneye bağlı kalmadan
                # direkt olarak karekökünü bu şekilde almak istedim.
                alt_sinir = p_orani - (guven_99 * ((p_orani*(1-p_orani) / populasyon)**(1/2)))
                ust_sinir = p_orani + (guven_99 * ((p_orani*(1-p_orani) / populasyon)**(1/2)))
                print("Alt sınır: ", alt_sinir)
                print("Ust sınır:", ust_sinir)
                break


            elif secim == 'd' or secim == 'D':
                #ana menüye dönmek için d seçeneğine basınca ana ekrana dönmesi için yazdığım dizin.
                main_menu = True
            else:
                print("90 95 99 ya da d değerlerini giriniz.")


        # -----------------------------
        elif choice == 'd' or choice == 'D':
                print("çıkış yapılıyor...")


        # -----------------------------
        else:
            print("Uygun değeri giriniz.")
            break