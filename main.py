import json
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Barang:
    def __init__(self, id_barang, nama, stok, harga):
        self.id_barang = id_barang
        self.nama = nama
        self.stok = stok
        self.harga = harga

class inventory():
    def __init__(self):
        self.list_barang = []
        self.load_data()
    def Tambah_barang(self):
        
        try:
            while True:
                clear()
                #membuat id barang secra otomatis
                id_barang = f"BRG{len(self.list_barang) + 1:03d}"
                print(f"ID Barang: {id_barang}")
                nama = (input(f"Nama Barang: ")).lower()
                stok = int(input(f"stok: "))
                harga = int(input(f"Harga: "))
                barang_baru = Barang(id_barang, nama, stok, harga)#objek dibuat seperti ini jika ingin input di oop
                self.list_barang.append(barang_baru)#lalau di simpan(maybe)//
                print(f"Barang {barang_baru.nama} berhasil ditambahkan ke inventori.")
                self.simpan_data()
                print("silahkan pilih opsi di bawah ini:")
                break
        except ValueError:
                print("Input tidak valid. Silakan masukkan angka untuk stok dan harga.")
        
        except ZeroDivisionError:
            print("Angka tidak boleh nol yaa!")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

        while True:
            clear()        
            print("1. Tambah barang")
            print("2. HomePage")
            print("3. keluar")
            
            try:
                inul = int(input("masukkan pilihan anda:"))
                if inul == 1:
                    self.Tambah_barang()
                elif inul == 2:
                    self.mulai()
                elif inul == 3:
                    print("Terima kasih telah menggunakan aplikasi pencatat belanja")
                    return
                else:
                    print("Pilihan tidak valid")
                break
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka untuk pilihan.")

            except ZeroDivisionError:
                print("Angka tidak boleh nol yaa!")

            except Exception as e:
                print(f"Terjadi kesalahan: {e}")


    def Hapus_barang(self):
        clear()
        shut = input("masukkan ID barang: ")
        found = False
        print ("apa anda yakin ingin menghapus barang ini?")
        end = input("y/n: ")
        if end == "y":
            clear()
            for barang in self.list_barang:
                if shut == barang.id_barang:
                    self.list_barang.remove(barang)
                    self.simpan_data()
                    print("barang berhasil dihapus")
                    found = True
                    while True:
                        clear()
                        print ("silahkan pilih opsi di bawah ini:")
                        print("1. Hapus barang")
                        print("2. HomePage")
                        try:
                            inul = int(input("masukkan pilihan anda:"))
                            if inul == 1:
                                self.Hapus_barang()
                            elif inul == 2:
                                self.mulai()
                            else:
                                print("Pilihan tidak valid")
                                break
                        except ValueError:
                            print("Input tidak valid. Silakan masukkan angka untuk pilihan.")

                        except ZeroDivisionError:
                            print("Angka tidak boleh nol yaa!")

                        except Exception as e:
                            print(f"Terjadi kesalahan: {e}")
            if not found:
                print("barang tidak ditemukan")
        elif end == "n":
            clear()
            print("silahkan pilih opsi di bawah ini:")
            print("barang tidak dihapus")
            print("1. menghapus barang")
            print("2. HomePage")
            print("3. keluar")
            inul = int(input("masukkan pilihan anda:"))
            try:
                if inul == 1:
                    self.Hapus_barang()
                elif inul == 2:
                    self.mulai()
                elif inul == 3:
                    print("Terima kasih telah menggunakan aplikasi pencatat belanja")
                    exit()
                else:
                    print("Pilihan tidak valid")
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka untuk pilihan.")

            except ZeroDivisionError:
                print("Angka tidak boleh nol yaa!")

            except Exception as e:
                print(f"Terjadi kesalahan: {e}")
            
        else:
            print("barang tidak dihapus")


    def Tampil_barang(self,):          
            if len(self.list_barang) == 0:
                 while True:
                    clear()
                    print("inventori masih kosong")
                    print("1. HomePage")
                    print("2. tambah barang")
                    print("3. keluar")
                    try:
                        inol = int(input("masukkan pilihan anda:"))
                        if inol == 1:
                            self.mulai()
                        elif inol == 2:
                            self.Tambah_barang()
                        elif inol == 3:
                            print("Terima kasih telah menggunakan aplikasi pencatat belanja")
                            return
                        else:
                            print("Pilihan tidak valid")
                    except ValueError:
                        print("Input tidak valid. Silakan masukkan angka untuk pilihan.")

                    except ZeroDivisionError:
                        print("Angka tidak boleh nol yaa!")

                    except Exception as e:
                        print(f"Terjadi kesalahan: {e}")
            else:
                clear()
                for barang in self.list_barang:
                    print("===================")
                    print(f"ID Barang: {barang.id_barang}")
                    print(f"Nama Barang: {barang.nama}")
                    print(f"Stok: {barang.stok}")
                    print(f"Harga: {barang.harga}")
                
    def Cari_barang(self):
        clear()
        shut = input("masukkan ID barang: ")  
        shit = False 
        for i in self.list_barang:
            if shut == i.id_barang:
                print(f"ID Barang: {i.id_barang}\nNama Barang: {i.nama}\nStok: {i.stok}\nHarga: {i.harga}")
                shit = True
                break
        if not shit:
            print("barang tidak di temukan")
        
        while True:
            print("1. HomePage")
            print("2. cari barang")
            print("3. keluar")
            try:
                inl = int(input("masukkan pilihan anda:"))
                if inl == 1:
                    self.mulai()
                elif inl == 2:
                    self.Cari_barang()
                elif inl == 3:
                    print("Terima kasih telah menggunakan aplikasi pencatat belanja")
                    return
                else:
                    print("Pilihan tidak valid")

            except ValueError:
                print("Input tidak valid. Silakan masukkan angka untuk pilihan.")

            except ZeroDivisionError:
                print("Angka tidak boleh nol yaa!")

            except Exception as e:
                print(f"Terjadi kesalahan: {e}")
    def edit_barang(self):
        clear()
        shut = input("masukkan ID barang: ").lower()
        barang_ditemukan = None
        for i in self.list_barang:
            if shut.strip().lower() == i.id_barang.strip().lower():
                barang_ditemukan = i
                break
        if barang_ditemukan:
                print("barang ditemukan")
                print(f"ID Barang: {barang_ditemukan.id_barang}\nNama Barang: {barang_ditemukan.nama}\nStok: {barang_ditemukan.stok}\nHarga: {barang_ditemukan.harga}")

                while True:
                        clear()
                        print("silahkan pilih opsi di bawah ini:")
                        print("1. edit nama barang")
                        print("2. edit stok barang")
                        print("3. edit harga barang")
                        print("4. keluar")
                        try:
                            inl = int(input("masukkan pilihan anda:"))
                            if inl == 1:
                                barang_ditemukan.nama = input("masukkan nama barang baru:").lower()
                                print("barang berhasil di edit")
                            elif inl == 2:  
                                barang_ditemukan.stok = int(input("masukkan stok barang baru:"))
                                print("barang berhasil di edit")
                            elif inl == 3:
                                barang_ditemukan.harga = float(input("masukkan harga barang baru:"))
                                print("barang berhasil di edit")
                            elif inl == 4:
                                print("Terima kasih telah menggunakan aplikasi pencatat belanja")
                                return
                            else:
                                print("Pilihan tidak valid")

                        except ValueError:
                            print("Input tidak valid. Silakan masukkan angka untuk pilihan.")

                        except ZeroDivisionError:
                            print("Angka tidak boleh nol yaa!")

                        except Exception as e:
                            print(f"Terjadi kesalahan: {e}")
                        
                        self.simpan_data()
                        break

        else:
                print("barang tidak di temukan")
               
        while True:
            print("1. HomePage")
            print("2. edit barang")
            print("3. keluar")
            try:
                inl = int(input("masukkan pilihan anda:"))
                if inl == 1:
                    self.mulai()
                elif inl == 2:
                    self.edit_barang()
                elif inl == 3:
                    print("Terima kasih telah menggunakan aplikasi pencatat belanja")
                    return
                else:
                    print("Pilihan tidak valid")

            except ValueError:
                print("Input tidak valid. Silakan masukkan angka untuk pilihan.")

            except ZeroDivisionError:
                print("Angka tidak boleh nol yaa!")

            except Exception as e:
                print(f"Terjadi kesalahan: {e}")

    def simpan_data(self):
        clear()
        try:
            with open('data_barang.json', 'w') as file:
                json.dump([barang.__dict__ for barang in self.list_barang], file, indent=4)
            print("data berhasil disimpan")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
    def dua(self):
        while True:
            print("silahkan pilih opsi di bawah ini:")
            print("1. HomePage")
            print("2. keluar")
            try:
                inl = int(input("masukkan pilihan anda:"))
                if inl == 1:
                    self.mulai()
                elif inl == 2:
                    print("Terima kasih telah menggunakan aplikasi pencatat belanja")
                    exit()
                else:
                    print("Pilihan tidak valid")
                    
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka untuk pilihan.")


            except Exception as e:
                print(f"Terjadi kesalahan: {e}")

    def load_data(self):
        clear()
        try:
            with open("data_barang.json","r") as file:
                data = json.load(file)
                for item in data:
                    barang = Barang(item["id_barang"],item["nama"],item["stok"],item["harga"])
                    self.list_barang.append(barang)
            print("data berhasil dimuat")
        except FileNotFoundError:
            print("data tidak ditemukan")
        except json.JSONDecodeError:
            print("data tidak valid")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

class inventoryApp(inventory):
    def __init__(self):
        super().__init__()
    def mulai(self):
        while True:
            clear()
            print("Selamat datang di aplikasi pencatat belanja")
            print("Menu:")
            print("1. Tambah barang")
            print("2. Hapus barang")
            print("3. Tampilkan barang")
            print("4. Cari barang")
            print("5. edit data")
            print("6. Simpan data")
            print("7. Load data")
            print("8. Keluar")
            try:
                pilihan = input("Pilih menu: ")
                if pilihan == "1":
                    self.Tambah_barang()
                elif pilihan == "2":
                    self.Hapus_barang()
                elif pilihan == "3":
                    self.Tampil_barang(),self.dua()
                elif pilihan == "4":
                    self.Cari_barang()
                elif pilihan == "5":
                    self.edit_barang()
                elif pilihan == "6":
                    self.simpan_data(), self.dua()
                elif pilihan == "7":
                    self.load_data(),self.dua()
                elif pilihan == "8":
                    print("Terima kasih telah menggunakan aplikasi pencatat belanja")
                    exit()
                else:
                    print("Pilihan tidak valid")
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka untuk pilihan.")

            except ZeroDivisionError:
                print("Angka tidak boleh nol yaa!")

            except Exception as e:
                print(f"Terjadi kesalahan: {e}")
        
#memnaggil def mulai
store = inventoryApp()
store.mulai()

