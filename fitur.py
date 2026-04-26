import pandas as pd
import os


def create(data_csv):
    try:
        nama = input('Nama: ')
        
        try:
            umur = int(input('Umur: '))
        except ValueError:
            print(' Umur harus angka')
            return
        
        departemen = input('Departemen: ')
        
        try:
            gaji = int(input('Gaji: '))
        except ValueError:
            print(' Gaji harus angka')
            return
        
        data_baru = pd.DataFrame([{
            'id': data_csv['id'].max() + 1,
            'nama': nama,
            'umur': umur,
            'departemen': departemen,
            'gaji': gaji
        }])

        # cek file ada atau belum
        if not os.path.exists('data.csv'):
            data_baru.to_csv('data.csv', index=False)
        else:
            data_baru.to_csv('data.csv', mode='a', index=False, header=False)

        print('Sukses membuat data baru')
    
    except PermissionError:
        print('File lagi kebuka (tutup dulu CSV-nya)')
    except Exception as e:
        print(f' Terjadi error: {e}')

def read(data_csv):
    nama=input('Nama: ')
    if nama in data_csv.values:
        hasil=data_csv[data_csv['nama']==nama]
        print(hasil)
    else:
        print('Data tidak ditemukan')