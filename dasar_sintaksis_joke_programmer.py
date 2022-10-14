# Sekuensial
print('Ibu Berkata,"Pergi Ke toko"')
print('Budi menjawab, "Apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, bila ada telor beli 6"')
print('Maka Budi berangkat ke toko')
print('Dan mulai berbelanja')

# Percabangan
jumlah_botol_susu = 125
jumlah_telur = 200
print(f"Jumlah Botol Susu {jumlah_botol_susu} botol ")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("menyampaikan hasil ke ibu")