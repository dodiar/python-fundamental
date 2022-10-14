print('\nPerintah Del')
daftar_buku = ['1 Rahasia Magnet Rezeki', '2 Quantum Ikhlas', '3 Psycology Money', '4 Think and Grow Rich']
del daftar_buku[0]
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list compprehension')
daftar_buku = ['Rahasia Magnet Rezeki', 'Quantum Ikhlas', 'Psycology Money', 'Think and Grow Rich']
del daftar_buku[:]
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list compprehension start')
daftar_buku = ['Rahasia Magnet Rezeki', 'Quantum Ikhlas', 'Psycology Money', 'Think and Grow Rich']
del daftar_buku[0:-1] #START:END
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list compprehension start step')
daftar_buku = ['Rahasia Magnet Rezeki', 'Quantum Ikhlas', 'Psycology Money', 'Think and Grow Rich']
del daftar_buku[0::2] #START:END:STEP
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
daftar_buku = ['1 Rahasia Magnet Rezeki', '2 Quantum Ikhlas', '3 Psycology Money', '4 Think and Grow Rich']
daftar_buku_baru = daftar_buku[:]
for i in range(0,len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0,len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : ganjil')
daftar_buku = ['1 Rahasia Magnet Rezeki', '2 Quantum Ikhlas', '3 Psycology Money', '4 Think and Grow Rich']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0,len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : genap')
daftar_buku = ['1 Rahasia Magnet Rezeki', '2 Quantum Ikhlas', '3 Psycology Money', '4 Think and Grow Rich']
daftar_buku_baru = daftar_buku[1::2] #Start Stop end
for i in range(0,len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension : buang diujung')
daftar_buku = ['1 Rahasia Magnet Rezeki', '2 Quantum Ikhlas', '3 Psycology Money', '4 Think and Grow Rich']
daftar_buku_baru = daftar_buku[0:-1]
for i in range(0,len(daftar_buku_baru)):
    print(daftar_buku_baru[i])


