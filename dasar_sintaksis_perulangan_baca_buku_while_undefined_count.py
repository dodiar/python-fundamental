"""
Program perulangan baca buku dengan while sampai paham
"""
jumlah_buku = 10
print('Ibu berkata,"Baca semua bukumu!"')
total_jumlah_baca = 0

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f'Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1} belum paham')
    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f'Buku ke{jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami')

print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')
if jumlah_buku_yang_sudah_dibaca_dan_dipahami == jumlah_buku:
    print('"Bu, Semua buku sudah dibaca dan dipahami"')
else:
    print(f'"Bu, tidak semua buku bisa di baca dan dipahami. budi hanya bisa memahami '
          f'{jumlah_buku_yang_sudah_dibaca_dan_dipahami} buku')
