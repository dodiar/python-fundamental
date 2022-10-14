daftar_buku = ['Rahasia Magnet Rezeki', 'Quantum Ikhlas', 'Psycology Money', 'Think and Grow Rich']
print('Tampilkan vaiabel daftar_buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'ESQ Power', -211, 3.14]
print('\nTampilkan dengan for in range, dimana tiap data elemen berbeda-beda')
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Rahasia Magnet Rezeki', 'Quantum Ikhlas', 'Psycology Money', 'Think and Grow Rich']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Tematik 1')
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear List')
daftar_buku.clear()
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Rahasia Magnet Rezeki', 'Quantum Ikhlas', 'Psycology Money', 'Think and Grow Rich']
daftar_buku[0] = 'Magnet Rezeki'
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke 2')
buku = daftar_buku.pop(1)
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang tadi diambi')
print(buku)

print('\nPop')
daftar_buku.pop()
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -1')
daftar_buku = ['Rahasia Magnet Rezeki', 'Quantum Ikhlas', 'Psycology Money', 'Think and Grow Rich']
daftar_buku.pop(-1)
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

