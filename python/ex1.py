id = 0
tugas = [""] * (6)
des = [""] * (6)
status = [""] * (6)
mood = [""] * (6)
cat = [""] * (6)
waktu = [""] * (6)
hari = [""] * (6)
tahun = [""] * (6)
wded = [""] * (6)
hded = [""] * (6)
tded = [""] * (6)

count = 0
a = "y"
while True:    #This simulates a Do Loop
    print("1. menambah tugas")
    print("2. menyelesaikan tugas")
    print("3. riwayat tugas")
    print("4. mencari tugas")
    print("5. keluar")
    pil = int(input())
    if pil == 1:
        print("=====================")
        print("id anda:")
        print(id)
        print("masukkan waktu pengerjaan:")
        w = input()
        print("masukkan hari pengerjaan:")
        h = input()
        print("masukkan tanggal")
        thn = input()
        print("=====================")
        print("masukkan judul tugas:")
        it = input()
        print("masukkan deskripsi tugas:")
        ides = input()
        print("=====================")
        print("masukkan jam deadline:")
        wed = input()
        print("masukkan hari deadline:")
        hed = input()
        print("masukkan tanggal daedline:")
        ted = input()
        print("=====================")
        waktu[id] = w
        hari[id] = h
        tahun[id] = thn
        tugas[id] = it
        des[id] = ides
        wded[id] = wed
        hded[id] = hed
        tded[id] = ted
        status[id] = "belum"
        id = id + 1
        if it == "" and ides == "":
            print("anda belum memasukkan tugas apapun")
        else:
            print("tugas berhasil di tambahkan")
    else:

        # to_do_list[id] ← inputTugas
        # deskripsi_list[id] ← inputDeskripsi
        # status_list[id] ← "Belum"
        # id ← id + 1
        if pil == 2:
            if id == 0:
                print("anda belum memasukkan tugas apapun")
            else:
                print("daftar tugas")
                i = 0
                for i in range(0, id - 1 + 1, 1):
                    print("id")
                    print(id - 1)
                    print("1. waktu pengerjaan:")
                    print(waktu[i])
                    print("2. hari pengerjaan:")
                    print(hari[i])
                    print("3. tanggal pengerjaan:")
                    print(tahun[i])
                    print("4. judul tugas: ")
                    print(tugas[i])
                    print("5. deskripsi tugas:")
                    print(des[i])
                    print("6.  waktu deadline:")
                    print(wded[i])
                    print("7. deadline hari:")
                    print(hded[i])
                    print(" 8. tanggal deadline: ")
                    print(tded[i])
                    print("9. status tugas:")
                    print(status[i])
                print("cariid")
                cariid = int(input())
                if cariid >= 0 and cariid < id:
                    status[cariid] = "selesai"
                    print("masukkan mood:")
                    print("1. 😊 2. 😏 3. 😖 4. 😮‍💨 5. 🥴 6. 😵")
                    im = input()
                    if im == "1":
                        print(" 😊 ")
                    else:
                        if im == "2":
                            print("😏 ")
                        else:
                            if im == "3":
                                print("😖 ")
                            else:
                                if im == "4":
                                    print(" 😮‍💨 ")
                                else:
                                    if im == "5":
                                        print(" 🥴 ")
                                    else:
                                        if im == "6":
                                            print(" 😵")
                                        else:
                                            print("tidak ada mood yang anda pilih")
                    mood[cariid] = im
                    print("masukkan catatan")
                    icat = input()
                    cat[cariid] = icat
                    if im == "" and icat == "":
                        print("anda belum mengisi mood dan catatan")
                    else:
                        print("mood")
                        print(mood[cariid])
                        print("catatan")
                        print(cat[cariid])
                else:
                    print("id tidak ditemukan")
        else:
            if pil == 3:
                if id == 0:
                    print("anda belum")
                else:
                    sel = False
                    for i in range(0, id - 1 + 1, 1):
                        sel = True
                        print("tugas berhasil diselesaikan")
                        print("id")
                        print(id - 1)
                        print("1. waktu pengerjaan:")
                        print(waktu[i])
                        print("2. hari pengerjaan:")
                        print(hari[i])
                        print("3. tanggal pengerjaan:")
                        print(tahun[i])
                        print("4. judul tugas: ")
                        print(tugas[i])
                        print("5. deskripsi tugas:")
                        print(des[i])
                        print("6.  waktu deadline:")
                        print(wded[i])
                        print("7. deadline hari:")
                        print(hded[i])
                        print(" 8. tanggal deadline: ")
                        print(tded[i])
                        print("9. status tugas:")
                        print(status[i])
            else:
                if pil == 4:
                    if id == 0:
                        print("tidak ada tugas apapun")
                    else:
                        print("masukkan id yang di cari")
                        cariid = int(input())
                        if 0 <= cariid and cariid < id:
                            print("id")
                            print(cariid)
                            print("tugas berhasil diselesaikan")
                            print("id")
                            print(id - 1)
                            print("1. waktu pengerjaan:")
                            print(waktu[cariid])
                            print("2. hari pengerjaan:")
                            print(hari[cariid])
                            print("3. tanggal pengerjaan:")
                            print(tahun[cariid])
                            print("tugas")
                            print(tugas[cariid])
                            print("deskripsi tugas:")
                            print(des[cariid])
                            print("6.  waktu deadline:")
                            print(wded[cariid])
                            print("7. deadline hari:")
                            print(hded[cariid])
                            print(" 8. tanggal deadline: ")
                            print(tded[cariid])
                            print("status tugas")
                            print(status[cariid])
                            if status[cariid] == "selesai":
                                if mood[cariid] == "" and cat[cariid] == "":
                                    print("anda belum mengisi mood dan catatan")
                                else:
                                    print("mood")
                                    print(mood[cariid])
                                    print("catatan")
                                    print(cat[cariid])
                            else:
                                print("tugas belum selesai, mood dan catatan belum tersedia")
                        else:
                            print("id tidak ditemukan")
                else:
                    if pil == 5:
                        print("terimaksih telah menggunkan apk ini ")
                    print("anda telah keluar")
    if a != "y": break

