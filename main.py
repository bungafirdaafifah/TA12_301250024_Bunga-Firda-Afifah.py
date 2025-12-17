from mahasiswa import tambah_data, tampilkan_data, rata_rata_nilai, cari_mahasiswa

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Tampilkan Rata-Rata Nilai Mahasiswa")
        print("4. Cari Nama Mahasiswa")
        print("5. Keluar")
        
        choice = input("Pilih menu (1-5): ")
        
        print("----------------------------")
        
        if choice == '1':
            nama = input("Masukkan nama mahasiswa: ")
            tugas = float(input("Masukkan nilai Tugas: "))
            uts = float(input("Masukkan nilai UTS: "))      
            uas = float(input("Masukkan nilai UAS: "))

            mahasiswa = {
                'nama': nama,       
                'tugas': tugas,
                'uts': uts,
                'uas': uas
            }

            tambah_data(mahasiswa)
        elif choice == '2':
            tampilkan_data()
        elif choice == '3':
            rata_rata_nilai()
        elif choice == '4':
            nama_cari = input("Masukkan nama mahasiswa yang dicari: ")
            hasil = cari_mahasiswa(nama_cari)
            if hasil:
                print("Data ditemukan:")
                print(f"Nama: {hasil['nama']}, Tugas: {hasil['tugas']}, UTS: {hasil['uts']}, UAS: {hasil['uas']}")
            else:
                print("Mahasiswa tidak ditemukan.")
        elif choice == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()