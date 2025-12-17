import os

def load_data():
    if not os.path.exists('data_mahasiswa.csv'):
        return []
    
    with open('data_mahasiswa.csv', 'r') as file:
            lines = file.readlines()
            data = []
            for line in lines:
                nama, tugas, uts, uas = line.strip().split(',')
                mahasiswa = {
                    'nama': nama,
                    'tugas': float(tugas),
                    'uts': float(uts),
                    'uas': float(uas)
                }
                data.append(mahasiswa)
            return data

def append_data(mahasiswa):
    with open('data_mahasiswa.csv', 'a') as file:
        line = f"{mahasiswa['nama']},{mahasiswa['tugas']},{mahasiswa['uts']},{mahasiswa['uas']}\n"
        file.write(line)

