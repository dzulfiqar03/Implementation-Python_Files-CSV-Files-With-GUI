from tkinter import *

# GUI REGISTRATION DASHBOARD
def register() :
    global register_page
    register_page = Toplevel(login_page)
    register_page.geometry("500x400",) # set the configuration of GUI window 
    register_page.title("Account Register") # set the title of GUI window]
    register_page.configure(bg ="pink")
    
    Label(register_page,text="", bg="pink", height=2).pack()
    Label(register_page,text="WELCOME TO\nREGISTRATION DASHBOARD",bg="pink",font=("Roboto 15 bold"), foreground="brown").pack()
    Label(register_page,text="", bg="pink").pack()
    
    global fullNameReg_validation
    global emailReg_validation
    global passReg_validation
    global countryReg_validation

    fullNameReg_validation = StringVar()
    emailReg_validation = StringVar()
    passReg_validation = StringVar()
    countryReg_validation = StringVar()    
    
    global fullname_register_entry
    global email_register_entry
    global password_register_entry
    global country_register_entry
    
    Label(register_page, text="",bg="pink").pack()
    fullname_register = Label(register_page, text="Full Name * ", bg="pink",foreground="white")
    fullname_register.place(x=154, y= 110) 
    fullname_register_entry = Entry(register_page, width=30,textvariable=fullNameReg_validation,)
    fullname_register_entry.pack()

    Label(register_page, text="",bg="pink", height=2).pack()
    email_register = Label(register_page, text="Email * ", bg="pink",foreground="white")
    email_register.place(x=154, y= 165) 
    email_register_entry = Entry(register_page, width=30,textvariable=emailReg_validation,)
    email_register_entry.pack()
    
    Label(register_page, text="",bg="pink", height=2).pack()
    password_register = Label(register_page, text="Password * ", bg="pink", foreground="white")   
    password_register.place(x=154, y= 220) 
    password_register_entry = Entry(register_page, width=30,textvariable=passReg_validation, show= '*')
    password_register_entry.pack()
    
    Label(register_page, text="",bg="pink", height=2).pack()
    country_register = Label(register_page, text="Country * ", bg="pink", foreground="white")   
    country_register.place(x=154, y= 275) 
    country_register_entry = Entry(register_page, width=30,textvariable=countryReg_validation)
    country_register_entry.pack()

    
    Label(register_page, text="",bg="pink",).pack()
    Button(register_page, text="Register", width=10, height=1, bg="brown",foreground="white", command=register_validation).pack()
    Label(register_page, text="",bg="pink").pack()
    
    # FOR VALIDATION REGISTER 
def register_validation():
    global fullNameReg, emailReg, passReg, countryReg
    
    fullNameReg = fullNameReg_validation.get()
    emailReg = emailReg_validation.get()
    passReg = passReg_validation.get()
    countryReg = countryReg_validation.get()
    
    if len(fullNameReg) > 0 and len(emailReg) > 0 and len(passReg) > 0 and len(countryReg) > 0 :
        register_page.destroy()
        alertReg()
    else :
        wrong_Register()

      # MEMASUKKAN NAMA CUTOMER KE DALAM FILE "nama_Customer.csv"
    namaKasir = []
    import csv

    with open('./files/nama_kasir.csv', mode='a') as csv_file:
            # membuat objek writer
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # menulis baris ke file CSV
        indeks = 1
        writer.writerow([indeks, fullNameReg,])
        indeks+=1
            
    print("Data Berhasil Disimpan")
    namaKasir.append(fullNameReg)



        # IF VALIDATION REGISTER WRONG
def wrong_Register() :
    global wrongReg
    wrongReg = Toplevel(register_page)
    wrongReg.geometry("200x25",) # set the configuration of GUI window 
    wrongReg.title("Validate Register") # set the title of GUI window]
    wrongReg.configure(bg ="pink")
    
    if len(fullNameReg) == 0 :
        Label(wrongReg, text="Full Name Must Be Required",bg="pink",).pack()
    elif len(emailReg) == 0  :
        Label(wrongReg, text="Email Must Be Required",bg="pink",).pack()
    elif len(passReg) == 0 :
        Label(wrongReg, text="Password Must Be Required",bg="pink",).pack()       
    elif len(countryReg) == 0 :
        Label(wrongReg, text="Country Must Be Required",bg="pink",).pack()
    else :
        alertReg()

def alertReg() :
    global alertRegister
    alertRegister = Toplevel(login_page)
    alertRegister.geometry("200x25",) # set the configuration of GUI window 
    alertRegister.title("Alert Register") # set the title of GUI window]
    alertRegister.configure(bg ="pink")
    
    Label(alertRegister, text="Registration Success",bg="pink",).pack()
    
    
# GUI LOGIN DASHBOARD
def login() :
    
    global login_page
    login_page = Toplevel(main_screen)
    login_page.geometry("500x400",) # set the configuration of GUI window 
    login_page.title("Account Login") # set the title of GUI window]
    login_page.configure(bg ="pink")
    
    Label(login_page,text="", bg="pink", height=4).pack()
    Label(login_page,text="WELCOME TO\nLOGIN DASHBOARD",bg="pink",font=("Roboto 15 bold"), foreground="brown").pack()
    Label(login_page,text="", bg="pink").pack()
    
    global emailLgn_validation
    global passLgn_validation

    emailLgn_validation = StringVar()
    passLgn_validation = StringVar()

    global email_login_entry
    global password_login_entry
    
    Label(login_page, text="",bg="pink").pack()
    email_login = Label(login_page, text="Email * ", bg="pink",foreground="white")
    email_login.place(x=154, y= 140) 
    email_login_entry = Entry(login_page, width=30,textvariable=emailLgn_validation,)
    email_login_entry.pack()
    
    Label(login_page, text="",bg="pink", height=2).pack()
    password_login = Label(login_page, text="Password * ", bg="pink", foreground="white")   
    password_login.place(x=154, y= 195) 
    password_login_entry = Entry(login_page, width=30,textvariable=passLgn_validation, show= '*')
    password_login_entry.pack()
    
    Label(login_page, text="",bg="pink",).pack()
    Button(login_page, text="Login", width=10, height=1, bg="brown",foreground="white", command=login_validation).pack()
    Label(login_page, text="",bg="pink").pack()
    
    txtBtnLgn1 = Button(login_page, text="Don't Have Any Account ?", relief=FLAT,font=("Roboto 7 "),height=1, bg="pink",foreground="white")
    txtBtnLgn1.place(x=154, y= 295)
    txtBtnLgn2 = Button(login_page, text="Create Account", relief=FLAT,font=("Roboto 7 "),height=1, bg="pink",foreground="brown", command= register)
        
    txtBtnLgn2.place(x=271, y= 295)
    
# GUI VALIDATION LOGIN
def login_validation() :
    global emailLgn, passLgn
    
    emailLgn = emailLgn_validation.get()
    passLgn = passLgn_validation.get()
    
    if len(emailLgn) > 0 and len(passLgn) > 0:
        if emailLgn == emailReg and passLgn == passReg :
            login_page.destroy()
            alertLgn()
        else:
            wrong_Login()
    else :
        wrong_Login()
        
 
        # GUI IF VALIDATION LOGIN NOT SUCCESS
def wrong_Login() :
    global wrongLgn
    wrongLgn = Toplevel(login_page)
    wrongLgn.geometry("200x50",) # set the configuration of GUI window 
    wrongLgn.title("Validate Login") # set the title of GUI window]
    wrongLgn.configure(bg ="pink")
    
    if len(emailLgn) == 0  :
        Label(wrongLgn, text="Email Must Be Required",bg="pink",).pack()
    elif len(passLgn) == 0 :
        Label(wrongLgn, text="Password Must Be Required",bg="pink",).pack()
    
    else: 
        if emailLgn != emailReg  :
            Label(wrongLgn, text="Email Not Found",bg="pink",).pack()
        elif passLgn != passReg :
            Label(wrongLgn, text="Password Not Found",bg="pink",).pack()       
        else :
            login()
   
        
# GUI ALERT WHEN LOGIN IS SUCCESS
def alertLgn() :
    if login_validation :
        global alertLogin
        alertLogin = Toplevel(main_screen)
        alertLogin.geometry("400x70",) # Menyusun Configurasi GUI window 
        alertLogin.title("Alert Login") # Menyusun judul GUI window]
        alertLogin.configure(bg ="pink")
            
        Label(alertLogin, text="Login Success",bg="pink",).pack()
        Label(alertLogin, text="KLIK OK UNTUK BERPINDAH KE HALAMAN COMMAND PROMPT",bg="pink",).pack()

        Button(alertLogin, text="OK", width=10, height=1, bg="brown",foreground="white", command=outFromDashboard,justify=RIGHT).pack()

            
            
# GUI MAIN DASHBOARD BEFORE GO TO COMMAND PROMPT
def outFromDashboard():
    main_screen.destroy()
    
    # BERPINDAH KE HALAMAN COMMAND PROMPT
    import csv
    import os
    namaCustomer = []
        # MENGCONFIGURASIKAN FILE CSV (menu_kopi.csv dan menu_makanan.csv)
    menu_pilih = []
    namaPesananSnack = []
    hargaPesananSnack = []
    namaPesananKopi = []
    hargaPesananKopi = []
            
    arrTotalHargaPerSnack = []
    arrTotalHargaPerKopi = []
    

            #HALAMAN DASHBOARD
    os.system('cls')
        # MEMASUKI HALAMAN UTAMA DASHBOARD ABAH COFFEE (MELIPUTI PEMESANAN PRODUK PELANGGAN DAN PEMBAYARAN)
    print("-"*20,"Pagi, " +  fullNameReg)
    print("="*50)
    print("SELAMAT DATANG DI DASHBOARD UTAMA ABAH COFFEE")
    print("="*50)
    print()
            
        # PIHAK KASIR MEMILIH JIKA MENEKAN 1 MAKA BERPINDAH KE HALAMAN PEMESANA, JIKA NO 2 MAKA KASIR INGIN MELIHAT MENU YANG DIJUAL SESUAI HARGA
    pilihKasir = int(input("Pilih Salah Satu :\n1. Melakukan Pemesanan Customer\n2. Melihat Menu Berdasarkan Harga\nMasukkan Pilihan Anda : "))
    if pilihKasir == 1 :
        os.system('cls')
        print("="*50)
        print("SELAMAT DATANG DI HALAMAN PEMESANAN ABAH COFFEE")
        print("="*50)
        print()

        nama = input("Nama Customer: ")
                
            # MEMASUKKAN NAMA CUTOMER KE DALAM FILE "nama_Customer.csv"
        import csv

        with open('./files/nama_Customer.csv', mode='a') as csv_file:
                # membuat objek writer
            writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                # menulis baris ke file CSV
            indeks = 1
            writer.writerow([indeks, nama,])
            indeks+=1
            
        print("Data Berhasil Disimpan")
        namaCustomer.append(nama)
        
        # MENAMPILKAN FILE CSV SESUI INPUTAN KASIR
        menu = input("Pilih menu (snack/kopi) : ")
        if menu == 'snack':

            file_path="./files/menu_makanan.csv"
        elif menu == 'kopi':
            file_path = "./files/menu_kopi.csv"

        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                menu_pilih.append(row)
        labels = menu_pilih.pop(0)
        print()
        print("="*50)
        print("DAFTAR MENU ABAH COFFEE SHOP")
        print("="*50)        
        print(f'{labels[0]:<5} {labels[1]:<25} {labels[2]:<7}')
        print("-"*50)



        for data in menu_pilih:
            print(f'{data[0]:<5} {data[1]:<25} {data[2]:<7}')
        print(f'{0:<5}  ',"Halaman Pembayaran")
        print("-"*50)

                    
        pesan_menu = "1"
        totalHarga = 0
        while pesan_menu != "0":
            pesan_menu = str(input("Masukkan pilihan menu (kode menu) : "))
                    
                            
            status_menu= 0
                    
            dataSnack = { "1" : {"nama" : "frenchfries", "harga" : 8000},
                            "2" : {"nama" : "churros", "harga" : 9000},
                        "3" : {"nama" : "rokupang  susu", "harga" : 2000},
                            "4" : {"nama" : "flat cookies", "harga" : 8000},
                            "5" : {"nama" : "dimsum", "harga" : 10000},
                            "6" : {"nama" : "pangseat", "harga" : 10000},
                            "7" : {"nama" : "tahu crispy", "harga" : 10000},
                            "8" : {"nama" : "jamur crispy", "harga" : 10000},
                            "9" : {"nama" : "mie goreng telur", "harga" : 12000},
                            "10" : {"nama" : "ubi  balls", "harga" : 12000},}
            for i in dataSnack :
                if pesan_menu == i :
                    status_menu = 1
                    namaPesananSnack.append(dataSnack[i]["nama"])
                    hargaPesananSnack.append(dataSnack[i]["harga"])
                    print("Tersimpan")
                    if status_menu == 0:
                        print("Menu tidak ditemukan")
                    
            dataKopi = { "11" : {"nama" : "matchandu", "harga" : 15000},
                            "12" : {"nama" : "banana coffee milk", "harga" : 12000},
                        "13" : {"nama" : "japanese coffee", "harga" : 13000},
                            "14" : {"nama" : "tubrukers coffee", "harga" : 12000},
                            "15" : {"nama" : "coffee milk butter", "harga" : 14000},
                            "16" : {"nama" : "coffee latte", "harga" : 15000},
                            "17" : {"nama" : "americano", "harga" : 15000},
                            "18" : {"nama" : "v60 manual brew", "harga" : 18000},
                            "19" : {"nama" : "caramel macchiato", "harga" : 13000},
                            "20" : {"nama" : "creame brulee", "harga" : 18000},}
            for i in dataKopi :
                    if pesan_menu == i :
                        status_menu = 1
                        namaPesananKopi.append(dataKopi[i]["nama"])
                        hargaPesananKopi.append(dataKopi[i]["harga"])
                        print("Tersimpan")
                        if status_menu == 0:
                            print("Menu tidak ditemukan")
        
        #HALAMAN PEMBAYARAN UTAMA
        os.system('cls')
        print("="*50)
        print("SELAMAT DATANG DI HALAMAN PEMBAYARAN") 
        print("="*50) 
                
        print("Atas Nama \t : ",nama)  
        
        if menu == "snack" :
            indeksPesananSnack = 1
            print("Dengan rincian Menu Yang Dipesan :")
            for i in namaPesananSnack :
                print(indeksPesananSnack,"."," ",i)
                indeksPesananSnack+=1

            indeksHargaSnack = 1
            print("Dengan rincian harga tiap Item :")
            for hargaSnack in hargaPesananSnack :
                print(indeksHargaSnack,"."," ",hargaSnack)
                arrTotalHargaPerSnack.append(hargaSnack)                
                indeksHargaSnack+=1

                            
        elif menu == "kopi" :            
            indeksPesananKopi = 1
            print("Dengan rincian Menu Yang Dipesan :")
            for i in namaPesananKopi :
                print(indeksPesananKopi,"."," ",i)
                indeksPesananKopi+=1

            indeksHargaKopi = 1
            print("Dengan rincian harga tiap Item :")
            for hargaKopi in hargaPesananKopi :
                print(indeksHargaKopi,"."," ",hargaKopi)
                arrTotalHargaPerKopi.append(hargaKopi)                
                indeksHargaKopi+=1
        
        for k in arrTotalHargaPerSnack:
            totalHarga += k

                                
        for k in arrTotalHargaPerKopi:
            totalHarga += k

        # MENAMPILKAN TOTAL HARGA MENU  YANG DIPESAN CUSTOMER
        print("-"*50)
        print("Total Harga :",totalHarga)
        print("-"*50)
        
        # MENAMPILKAN JUMLAH UANG KEMBALIAN CUSTOMER
        uangTerima = int(input("Jumlah Uang Yang Diterima : Rp"))
        uangKembali = uangTerima - totalHarga
        print("-"*50)
        print("Uang Kembalian Sebesar"," ","Rp",uangKembali)      
        
        # PIHAK KASIR MEMILIH MELANJUTKAN PEMESANAN ATAU TOKO TUTUP/KELUAR
        pilihanKasir = input("Pilih:\n1. Kembali Ke Halaman Dashboard Utama\n2. SignOut dan Keluar\nMasukkan Pilihan Anda: ")
        while pilihanKasir != "2":
            menu_pilih.clear()
            namaPesananSnack.clear()
            hargaPesananSnack.clear()
            namaPesananKopi.clear()
            hargaPesananKopi.clear()
            arrTotalHargaPerSnack.clear()
            arrTotalHargaPerKopi.clear()
                                    #HALAMAN DASHBOARD
            os.system('cls')
                # MEMASUKI HALAMAN UTAMA DASHBOARD ABAH COFFEE (MELIPUTI PEMESANAN PRODUK PELANGGAN DAN PEMBAYARAN)
            print("-"*20,"Pagi, " +  fullNameReg)
            print("="*50)
            print("SELAMAT DATANG DI DASHBOARD UTAMA ABAH COFFEE")
            print("="*50)
            print()
                    
                # PIHAK KASIR MEMILIH JIKA MENEKAN 1 MAKA BERPINDAH KE HALAMAN PEMESANAN, JIKA NO 2 MAKA KASIR INGIN MELIHAT MENU YANG DIJUAL SESUAI HARGA
            pilihKasir = int(input("Pilih Salah Satu :\n1. Melakukan Pemesanan Customer\n2. Melihat Menu Berdasarkan Harga\nMasukkan Pilihan Anda : "))
            
            # JIKA KEMBALI UNTUK MELAKUKAN PEMESANAN
            if pilihKasir == 1 :
                os.system('cls')
                print("="*50)
                print("SELAMAT DATANG DI HALAMAN PEMESANAN ABAH COFFEE")
                print("="*50)
                print()

                nama = input("Nama Customer: ")
                        
                    # MEMASUKKAN NAMA CUTOMER KE DALAM FILE "nama_Customer.csv"
                import csv

                with open('./files/nama_Customer.csv', mode='a') as csv_file:
                        # membuat objek writer
                    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        # menulis baris ke file CSV
                    indeks = 1
                    writer.writerow([indeks, nama,])
                    indeks+=1
                    
                print("Data Berhasil Disimpan")
                namaCustomer.append(nama)
                        
                menuUlang = input("Pilih menu (snack/kopi) : ")
                if menuUlang == 'snack':

                    fileUlang_path="./files/menu_makanan.csv"
                elif menuUlang == 'kopi':
                    fileUlang_path = "./files/menu_kopi.csv"

                with open(fileUlang_path) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=",")
                    for row in csv_reader:
                        menu_pilih.append(row)
                labels = menu_pilih.pop(0)
                print()
                print("="*50)
                print("DAFTAR MENU ABAH COFFEE SHOP")
                print("="*50)        
                print(f'{labels[0]:<5} {labels[1]:<25} {labels[2]:<7}')
                print("-"*50)



                for data in menu_pilih:
                    print(f'{data[0]:<5} {data[1]:<25} {data[2]:<7}')
                print(f'{0:<5}  ',"Halaman Pembayaran")
                print("-"*50)

                            
                pesan_menu = "1"
                totalHarga = 0
                while pesan_menu != "0":
                    pesan_menu = str(input("Masukkan pilihan menu (kode menu) : "))
                            
                                    
                    status_menu= 0
                            
                    dataSnack = { "1" : {"nama" : "frenchfries", "harga" : 8000},
                                    "2" : {"nama" : "churros", "harga" : 9000},
                                "3" : {"nama" : "rokupang  susu", "harga" : 2000},
                                    "4" : {"nama" : "flat cookies", "harga" : 8000},
                                    "5" : {"nama" : "dimsum", "harga" : 10000},
                                    "6" : {"nama" : "pangseat", "harga" : 10000},
                                    "7" : {"nama" : "tahu crispy", "harga" : 10000},
                                    "8" : {"nama" : "jamur crispy", "harga" : 10000},
                                    "9" : {"nama" : "mie goreng telur", "harga" : 12000},
                                    "10" : {"nama" : "ubi  balls", "harga" : 12000},}
                    for i in dataSnack :
                        if pesan_menu == i :
                            status_menu = 1
                            namaPesananSnack.append(dataSnack[i]["nama"])
                            hargaPesananSnack.append(dataSnack[i]["harga"])
                            print("Tersimpan")
                            if status_menu == 0:
                                print("Menu tidak ditemukan")
                            
                    dataKopi = { "11" : {"nama" : "matchandu", "harga" : 15000},
                                    "12" : {"nama" : "banana coffee milk", "harga" : 12000},
                                "13" : {"nama" : "japanese coffee", "harga" : 13000},
                                    "14" : {"nama" : "tubrukers coffee", "harga" : 12000},
                                    "15" : {"nama" : "coffee milk butter", "harga" : 14000},
                                    "16" : {"nama" : "coffee latte", "harga" : 15000},
                                    "17" : {"nama" : "americano", "harga" : 15000},
                                    "18" : {"nama" : "v60 manual brew", "harga" : 18000},
                                    "19" : {"nama" : "caramel macchiato", "harga" : 13000},
                                    "20" : {"nama" : "creame brulee", "harga" : 18000},}
                    for i in dataKopi :
                            if pesan_menu == i :
                                status_menu = 1
                                namaPesananKopi.append(dataKopi[i]["nama"])
                                hargaPesananKopi.append(dataKopi[i]["harga"])
                                print("Tersimpan")
                                if status_menu == 0:
                                    print("Menu tidak ditemukan")
                
                #HALAMAN PEMBAYARAN KETIKA KASIR MELAKUKAN PEMESANAN UNTUK CUSTOMER SELANJUTNYA    
                os.system('cls')
                print("="*50)
                print("SELAMAT DATANG DI HALAMAN PEMBAYARAN") 
                print("="*50) 
                        
                print("Atas Nama \t : ",nama) 
                if menuUlang == "snack" :
                    indeksPesananSnack = 1
                    print("Dengan rincian Menu Yang Dipesan :")
                    for i in namaPesananSnack :
                        print(indeksPesananSnack,"."," ",i)
                        indeksPesananSnack+=1

                    indeksHargaSnack = 1
                    print("Dengan rincian harga tiap Item :")
                    for hargaSnack in hargaPesananSnack :
                        print(indeksHargaSnack,"."," ",hargaSnack)
                        arrTotalHargaPerSnack.append(hargaSnack)                
                        indeksHargaSnack+=1

                                
                elif menuUlang == "kopi" :            
                    indeksPesananKopi = 1
                    print("Dengan rincian Menu Yang Dipesan :")
                    for i in namaPesananKopi :
                        print(indeksPesananKopi,"."," ",i)
                        indeksPesananKopi+=1

                    indeksHargaKopi = 1
                    print("Dengan rincian harga tiap Item :")
                    for hargaKopi in hargaPesananKopi :
                        print(indeksHargaKopi,"."," ",hargaKopi)
                        arrTotalHargaPerKopi.append(hargaKopi)                
                        indeksHargaKopi+=1
                
                for k in arrTotalHargaPerSnack:
                    totalHarga += k

                                        
                for k in arrTotalHargaPerKopi:
                    totalHarga += k

                # MENAMPILKAN TOTAL HARGA PEMESANAN CUSTOMER SELANJUTNYA
                print("-"*50)
                print("Total Harga :",totalHarga)
                print("-"*50)
                
                # MENAMPILKAN JUMLAH UANG KEMBALIAN
                uangTerima = int(input("Jumlah Uang Yang Diterima : Rp"))
                uangKembali = uangTerima - totalHarga
                print("-"*50)
                print("Uang Kembalian Sebesar"," ","Rp",uangKembali)
                pilihanKasir = input("Pilih:\n1. Kembali Ke Halaman Dashboard Utama\n2. SignOut dan Keluar\nMasukkan Pilihan Anda: ")

            elif pilihKasir == 2:
                    # MENCARI RANGE HARGA PRODUK DENGAN "BINARY SEARCH"
                dataRangeHarga = [0,5000,10000,15000,20000]
                first = dataRangeHarga[0]
                last = len(dataRangeHarga)-1
                count = 0
                found = False
                search = int(input("Masukkan Range Harga (Rp5000, Rp10000, Rp15000, Rp20000) : Rp"))
                while first <= last and not found :
                    mid = (first + last) // 2
                    count+=1
                    if dataRangeHarga[mid] < search:
                        first = mid+1
                    elif dataRangeHarga[mid] > search:
                        last = mid-1
                    else : 
                        found = True

                if found :
                    print("ditentukan Harga", search, "pada indeks : ", mid)
                    print("Sebanyak", count, "kali")
                    if search <= 5000:
                        print("Berikut Menu dengan range harga dibawah Rp5000")
                        print("=> Snack :\n1. Rokupang susu\n\n=> Kopi :\nTidak Ada")
                        pilihanKasir = input("Pilih:\n1. Kembali Ke Halaman Dashboard Utama\n2. SignOut dan Keluar\nMasukkan Pilihan Anda: ")

                    elif search > 5000 and search <= 10000 :
                        print("Berikut Menu dengan range harga Rp5000-Rp10000")
                        print("=> Snack :\n1. French Fries\n2. Churros\n3. Flat Cookies\n4. Dimsum\n5. Pangseat\n6. Tahu Crispy\n7. Jamur Crispi\n\n=> Kopi :\nTidak Ada")
                        pilihanKasir = input("Pilih:\n1. Kembali Ke Halaman Dashboard Utama\n2. SignOut dan Keluar\nMasukkan Pilihan Anda: ")
                    elif search > 10000 and search <= 15000 :
                        print("Berikut Menu dengan range harga Rp10000-Rp15000")
                        print("=> Snack :\n1. Mie Goreng Telur\n2. Ubi Balls\n\n=> Kopi :\n1. Matchandu\n2. Banana Coffee\n3. Japanase Coffee\n4. Tubrukers Coffee\n5. Coffee Milk Butter\n6. Coffee Latte\n7. Americano\n8. Caramel Macchiato")
                        pilihanKasir = input("Pilih:\n1. Kembali Ke Halaman Dashboard Utama\n2. SignOut dan Keluar\nMasukkan Pilihan Anda: ")
                    else :
                        print("Berikut Menu dengan range harga diatas Rp15000")
                        print("=> Snack :\nTidak Ada\n\n=> Kopi :\n1. V60 Manual Brew\n2. Creme Brulee")                        
                        pilihanKasir = input("Pilih:\n1. Kembali Ke Halaman Dashboard Utama\n2. SignOut dan Keluar\nMasukkan Pilihan Anda: ")

                else :
                    print('Harga', search, "tidak ditemukan dalam Menu")
                    print("count", count)
                    pilihanKasir = input("Pilih:\n1. Kembali Ke Halaman Dashboard Utama\n2. SignOut dan Keluar\nMasukkan Pilihan Anda: ")
                    
        # JIKA PIHAK KASIR MEMILIH NO 2. SIGNOUT DAN KELUAR
        print("-"*50)
        print("SignOut Success")
        print("-"*50) 
        print()           
        print("Terima Kasih")
                    
                  
                    
        
    else :
                # MENCARI RANGE HARGA PRODUK DENGAN "BINARY SEARCH"
        dataRangeHarga = [0,5000,10000,15000,20000]
        first = dataRangeHarga[0]
        last = len(dataRangeHarga)-1
        count = 0
        found = False
        search = int(input("Masukkan Range Harga (Rp5000, Rp10000, Rp15000, Rp20000) : Rp"))
        while first <= last and not found :
            mid = (first + last) // 2
            count+=1
            if dataRangeHarga[mid] < search:
                first = mid+1
            elif dataRangeHarga[mid] > search:
                last = mid-1
            else : 
                found = True

        if found :
            print("ditentukan Harga", search, "pada indeks : ", mid)
            print("Sebanyak", count, "kali")
            if search <= 5000:
                print("Berikut Menu dengan range harga dibawah Rp5000")
                print("=> Snack :\n1. Rokupang susu\n\n=> Kopi :\nTidak Ada")
            elif search > 5000 and search <= 10000 :
                print("Berikut Menu dengan range harga Rp5000-Rp10000")
                print("=> Snack :\n1. French Fries\n2. Churros\n3. Flat Cookies\n4. Dimsum\n5. Pangseat\n6. Tahu Crispy\n7. Jamur Crispi\n\n=> Kopi :\nTidak Ada")
            elif search > 10000 and search <= 15000 :
                print("Berikut Menu dengan range harga Rp10000-Rp15000")
                print("=> Snack :\n1. Mie Goreng Telur\n2. Ubi Balls\n\n=> Kopi :\n1. Matchandu\n2. Banana Coffee\n3. Japanase Coffee\n4. Tubrukers Coffee\n5. Coffee Milk Butter\n6. Coffee Latte\n7. Americano\n8. Caramel Macchiato")
            else :
                print("Berikut Menu dengan range harga diatas Rp15000")
                print("=> Snack :\nTidak Ada\n\n=> Kopi :\n1. V60 Manual Brew\n2. Creme Brulee")                        

        else :
            print('Harga', search, "tidak ditemukan dalam Menu")
            print("count", count)


# GUI EVENT BUTTON "KELUAR"
def btn_keluar() :
    main_screen.destroy()
    print("Terima Kasih")    
    
# GUI MAIN SCREEN OF ABAH COFFEE
def main_Screen() :
    global main_screen
             
    main_screen = Tk()   # create a GUI window 
    main_screen.geometry("500x400",) # set the configuration of GUI window 
    main_screen.title("Launch Screen") # set the title of GUI window]
    main_screen.configure(bg ="pink")
    
    Label(text="", bg="black", height=8).pack()
    Label(main_screen,text="WELCOME",bg="brown",foreground="white",width=34,font=("Roboto 15 bold"),justify=CENTER,pady=4).pack()
    Label(main_screen,text="ABAH COFFEE SHOP",bg="white",font=("Roboto 29 bold"),justify=CENTER, padx=4,foreground="brown").pack()
    Label(text="", bg="pink").pack()
    btn_login = Button(text="Login", font=("Roboto 10 bold"), padx=50, pady=2, bg="brown", foreground="white", command=login)
    btn_login.place(x=75, y= 250) 
    btn_keluars = Button(text="Keluar", font=("Roboto 10 bold"), padx=50, pady=2, bg="brown", foreground="white", command=btn_keluar)
    btn_keluars.place(x=275, y= 250)
    main_screen.mainloop() # start the GUI

main_Screen()