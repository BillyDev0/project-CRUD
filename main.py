from fitur import create,read
import pandas as pd

def main():
    data_csv=pd.read_csv('data.csv')
    while True:
        print('''
=== MENU ===
1. Tambah Data
2. Lihat Data
3. Hapus Data
4. Keluar
''')
        pilih= input('Pilih: ')
        if pilih=='1':
            create(data_csv)

        elif pilih=='2':
            read(data_csv)
main()