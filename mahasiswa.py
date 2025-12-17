from penyimpanan import load_data, append_data

def tambah_data(mahasiswa):
    append_data(mahasiswa)
    print("Data mahasiswa berhasil ditambahkan.")

def tampilkan_data():
    data_mahasiswa = load_data()
    if not data_mahasiswa:
        print("Data mahasiswa kosong.")
        return
    print("\nDaftar Mahasiswa:")
    print("{:<20} {:<10} {:<10} {:<10}".format("Nama", "Tugas", "UTS", "UAS"))
    for mhs in data_mahasiswa:
        print("{:<20} {:<10} {:<10} {:<10}".format(mhs['nama'], mhs['tugas'], mhs['uts'], mhs['uas']))

def rata_rata_nilai():
    data_mahasiswa = load_data()
    if not data_mahasiswa:
        print("Data mahasiswa kosong.")
        return

    total_tugas = sum(mhs['tugas'] for mhs in data_mahasiswa)
    total_uts = sum(mhs['uts'] for mhs in data_mahasiswa)
    total_uas = sum(mhs['uas'] for mhs in data_mahasiswa)
    jumlah_mahasiswa = len(data_mahasiswa)

    rata_tugas = total_tugas / jumlah_mahasiswa
    rata_uts = total_uts / jumlah_mahasiswa
    rata_uas = total_uas / jumlah_mahasiswa

    print(f"Rata-rata Nilai Tugas: {rata_tugas:.2f}")
    print(f"Rata-rata Nilai UTS: {rata_uts:.2f}")
    print(f"Rata-rata Nilai UAS: {rata_uas:.2f}")

def cari_mahasiswa(nama):
    data_mahasiswa = load_data()
    for mhs in data_mahasiswa:
        if mhs['nama'].lower() == nama.lower():
            return mhs
    return None

