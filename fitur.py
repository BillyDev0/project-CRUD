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

        import pandas as pd
        import os

        data_baru = pd.DataFrame([{
            'id': len(data_csv['id']+2),
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

