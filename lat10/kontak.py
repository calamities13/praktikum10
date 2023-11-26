from prettytable import PrettyTable

#Buat dictionary daftar kontak
daftar_kontak = {
    'Ari': '081234567',
    'Dina': '087654321',
}

#Tampilkan kontaknya Ari
print(f"Kontak Ari: {daftar_kontak.get('Ari', 'Kontak tidak ditemukan')}")

#Tambah kontak baru dengan nama Riko, nomor 087654544
daftar_kontak['Riko'] = '087654544'
print("Kontak Riko ditambahkan.")

#Ubah kontak Dina dengan nomor baru 088999776
if 'Dina' in daftar_kontak:
    daftar_kontak['Dina'] = '088999776'
    print("Nomor kontak Dina diubah.")
else:
    print("Kontak Dina tidak ditemukan.")

#Tampilkan semua Nama
print("Semua Nama:")
for nama in daftar_kontak.keys():
    print(nama)

#Tampilkan semua Nomor
print("\nSemua Nomor:")
for nomor in daftar_kontak.values():
    print(nomor)

#Tampilkan daftar Nama dan nomornya menggunakan pretty table
tabel_kontak = PrettyTable()
tabel_kontak.field_names = ["Nama", "Nomor"]
for nama, nomor in daftar_kontak.items():
    tabel_kontak.add_row([nama, nomor])

print("\nDaftar Nama dan Nomor:")
print(tabel_kontak)

#Hapus kontak Dina
if 'Dina' in daftar_kontak:
    del daftar_kontak['Dina']
    print("\nKontak Dina dihapus.")
else:
    print("\nKontak Dina tidak ditemukan.")