print("---------------------------------------------------------------")
print("---------------------------------------------------------------")
print("--            Nama : Nabil Daffa Athalasyah                  --")
print("--            NIM  : 2409116090                              --") 
print("--            Kelas: Sistem Informasi C 2024                 --")
print("--        Tugas Mini Project 2 Dasar Pemrograman             --")
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")

from prettytable import PrettyTable

# Variabel global untuk menyimpan tiket yang dipilih, user info, dan saldo e-wallet
tiket_terpilih = None
Username = None
Code = None
e_wallet_balance = 100000  # Saldo awal E-Wallet customer

# Fungsi untuk Admin Only
def admin_only():
    tiket_list = [
        {"kategori": "VVIP Grandstand", "harga": "7.500.000"},
        {"kategori": "VIP Grandstand", "harga": "5.000.000"},
        {"kategori": "Premium Grandstand", "harga": "3.500.000"},
        {"kategori": "Festival & Regular Grandstand", "harga": "2.500.000"}
    ]

    def top_up_ewallet_admin():
        global e_wallet_balance
        print("\n=== Top-up E-Wallet Customer ===")
        try:
            nominal = float(input("Masukkan jumlah top-up untuk customer: Rp "))
            e_wallet_balance += nominal
            print(f"Top-up berhasil! Saldo e-wallet customer sekarang: Rp {e_wallet_balance:.2f}")
        except ValueError:
            print("Input tidak valid! Nominal harus berupa angka.")
        input("Tekan Enter untuk kembali...")

    def update_harga_tiket():
        # Menampilkan tiket yang ada
        print("\n=== Ubah Harga Tiket ===")
        for i, tiket in enumerate(tiket_list, start=1):
            print(f"[{i}] {tiket['kategori']} - Harga saat ini: Rp {tiket['harga']}")

        try:
            pilihan_tiket = int(input("Pilih tiket yang ingin diubah harganya (1/2/3/4): "))
            if 1 <= pilihan_tiket <= len(tiket_list):
                tiket_baru = tiket_list[pilihan_tiket - 1]
                print(f"Anda memilih untuk mengubah harga {tiket_baru['kategori']}.")
                harga_baru = input("Masukkan harga baru: ")
                tiket_baru['harga'] = harga_baru
                print("Harga tiket berhasil diubah!")
            else:
                print("Pilihan tiket tidak valid!")
        except ValueError:
            print("Input harus berupa angka!")
        input("Tekan Enter untuk kembali...")

    while True:
        print("\n=== Admin Only ===")
        print("[1] Lihat Daftar Tiket")
        print("[2] Tambah Tiket Baru")
        print("[3] Ubah Harga Tiket")
        print("[4] Top-up E-Wallet Customer")
        print("[5] Kembali ke Menu Utama")
        
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            # Menampilkan daftar tiket menggunakan PrettyTable
            tabel = PrettyTable()
            tabel.title = "Daftar Tiket MyPertamina GrandPrix"
            tabel.field_names = ["Kategori Tiket", "Harga"]

            for tiket in tiket_list:
                tabel.add_row([tiket["kategori"], tiket["harga"]])

            print(tabel)
            input("\nTekan Enter untuk kembali...")
        elif pilihan == "2":
            kategori = input("Masukkan kategori tiket baru: ")
            harga = input("Masukkan harga tiket: ")
            tiket_list.append({"kategori": kategori, "harga": harga})
            print("Tiket baru berhasil ditambahkan!")
            input("Tekan Enter untuk kembali...")
        elif pilihan == "3":
            update_harga_tiket()  # Memperbaiki fungsi yang belum ada
        elif pilihan == "4":
            top_up_ewallet_admin()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk kembali...")

# Fungsi untuk Customer Only
def customer_only():
    global tiket_terpilih  # Menggunakan variabel global
    global e_wallet_balance
    tiket_list = [
        {"kategori": "VVIP Grandstand", "harga": "7.500.000"},
        {"kategori": "VIP Grandstand", "harga": "5.000.000"},
        {"kategori": "Premium Grandstand", "harga": "3.500.000"},
        {"kategori": "Festival & Regular Grandstand", "harga": "2.500.000"}
    ]

    def proses_pembayaran(total_harga):
        global e_wallet_balance
        print("\n=== Proses Pembayaran ===")
        print("Metode Pembayaran:")
        print("[1] Kartu Kredit")
        print("[2] Transfer Bank")
        print("[3] E-Wallet (Saldo Anda: Rp {:.2f})".format(e_wallet_balance))

        metode = input("Pilih metode pembayaran: ")
        
        if metode in ["1", "2"]:
            # Pembayaran menggunakan metode selain e-wallet
            print(f"Total yang harus dibayar: Rp {total_harga}")
            pembayaran = input("Masukkan jumlah yang dibayar: Rp ")

            try:
                pembayaran = float(pembayaran)
                if pembayaran >= float(total_harga.replace('.', '')):
                    kembalian = pembayaran - float(total_harga.replace('.', ''))
                    print(f"Pembayaran berhasil! Kembalian Anda: Rp {kembalian:.2f}")
                else:
                    kekurangan = float(total_harga.replace('.', '')) - pembayaran
                    print(f"Pembayaran gagal! Anda masih kurang: Rp {kekurangan:.2f}")
            except ValueError:
                print("Jumlah yang dibayarkan tidak valid!")
        elif metode == "3":
            # Pembayaran menggunakan e-wallet
            total_harga_num = float(total_harga.replace('.', ''))
            if e_wallet_balance >= total_harga_num:
                e_wallet_balance -= total_harga_num
                print(f"Pembayaran berhasil menggunakan E-Wallet! Sisa saldo: Rp {e_wallet_balance:.2f}")
            else:
                kekurangan = total_harga_num - e_wallet_balance
                print(f"Saldo E-Wallet tidak cukup! Anda masih kurang: Rp {kekurangan:.2f}")
        else:
            print("Metode pembayaran tidak valid!")

    while True:
        print("\n=== Customer Only ===")
        print("[1] Lihat Tiket")
        print("[2] Pesan Tiket")
        print("[3] Kembali ke Menu Utama")
        
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            # Menampilkan daftar tiket menggunakan PrettyTable
            tabel = PrettyTable()
            tabel.title = "Daftar Tiket MyPertamina GrandPrix"
            tabel.field_names = ["Kategori Tiket", "Harga"]

            for tiket in tiket_list:
                tabel.add_row([tiket["kategori"], tiket["harga"]])

            print(tabel)
            input("\nTekan Enter untuk kembali...")
        elif pilihan == "2":
            # Menampilkan daftar pilihan tiket
            print("Pilih tiket yang ingin dipesan:")
            for i, tiket in enumerate(tiket_list, start=1):
                print(f"[{i}] {tiket['kategori']} - Rp {tiket['harga']}")

            try:
                pilihan_tiket = int(input("Masukkan pilihan tiket (1/2/3/4): "))
                if 1 <= pilihan_tiket <= len(tiket_list):
                    tiket_terpilih = tiket_list[pilihan_tiket - 1]  # Menyimpan tiket yang dipilih
                    print(f"Anda memilih {tiket_terpilih['kategori']}.")
                    proses_pembayaran(tiket_terpilih['harga'])
                else:
                    print("Pilihan tiket tidak valid!")
            except ValueError:
                print("Input harus berupa angka!")
            input("Tekan Enter untuk kembali...")
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk kembali...")

# Fungsi Login Admin
def login_admin():
    global Username, Code  # Menyimpan username dan code admin secara global
    while True:
        print("\n=== Login Admin ===")
        Username = input("Masukkan Username Admin: ")
        Code = input("Masukkan Code Admin: ")

        if Username == "Admin" and Code == "1234":
            print(f"Selamat Datang Admin, {Username}!")
            input("Tekan Enter untuk melanjutkan...")
            admin_only()
            break
        else:
            print("Username atau Code Admin salah! Silahkan coba lagi.")
            input("Tekan Enter untuk coba lagi...")

# Fungsi Login Customer
def login_customer():
    global Username, Code  # Menyimpan username dan code customer secara global
    while True:
        print("\n=== Login Customer ===")
        Username = input("Masukkan Username Customer: ")
        Code = input("Masukkan Code Customer: ")

        if Username == "NabDaff" and Code == "090":
            print(f"Selamat Datang kembali pengguna MyPertamina, {Username}!")
            input("Tekan Enter untuk melanjutkan...")
            customer_only()
            break
        else:
            print("Username atau Code Customer salah! Silahkan coba lagi.")
            input("Tekan Enter untuk coba lagi...")

# Menampilkan Main Menu menggunakan PrettyTable
while True:
    tabel = PrettyTable()
    tabel.title = "Selamat datang di MyPertamina App Menu"
    tabel.field_names = ["Pilihan", "Pertamina Mandalika GrandPrix of Indonesia"]

    tabel.add_row(["1.)", "Login Admin"])
    tabel.add_row(["2.)", "Login Customer"])
    tabel.add_row(["3.)", "Exit"])

    print(tabel)

    Pilihan = input("Masukkan pilihan: ")

    if Pilihan == "1":
        login_admin()
    elif Pilihan == "2":
        login_customer()
    elif Pilihan == "3":
        print("--------------------------------------------------------------------------------------")
        print("--------------             Print Out Booking Ticket                   ----------------")
        print(f"--         Username: {Username}                                                    --")
        print(f"--         Code    : {Code}                                                        --")
        if tiket_terpilih:
            print(f"--     Ticket  : {tiket_terpilih['kategori']} - Rp {tiket_terpilih['harga']}   --")
            print("--                    TICKET PAID OFF!                                          --")
        else:
            print("--                  Ticket  : Belum ada tiket yang dibeli!                      --")
        print("--------------------        SEE YOU AT MANDALIKA!!!              ---------------------")
        print("--------------------------------------------------------------------------------------")
        break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
