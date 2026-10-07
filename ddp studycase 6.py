import json

with open("data_barang.json", "r", encoding = "utf-8") as f:
    data = json.load(f)

def tambah_data (nama_barang, stok):
    data.append({
        "Nama barang": nama_barang,
        "Stok": stok
    })
    return

def simpan_data():
    with open("data_barang.json", "w", encoding = "utf-8") as f:
        json.dump(data, f, indent = 4)
        return
    
while True:
    print("\n====Sistem Manajemen Inventaris Barang====")
    print("Ketik '1' untuk melihat data barang")
    print("Ketik '2' untuk menambah data barang")
    print("Ketik '3' untuk selesai")

    pilihan = input("pilih menu (1-3): ")
    if pilihan == "1":
        print("===Melihat barang===")
        print(data)
    elif pilihan == "2":
        print("===Menambah barang===")
        nama_barang = input("Masukan nama barang: ")
        stok = input("Masukan stok barang: ")
        while not stok.isdigit():
            print("Masukan angka bulat!")
            stok = input("Masukan stok barang: ")
        tambah_data (nama_barang, stok)
        simpan_data()
        print(data)
    elif pilihan == "3":
        print("Terima kasih telah menggunakan sistem manajemen inventaris barang!")
        break
    else:
        print("Silahkan masukan '1', '2', atau '3'")