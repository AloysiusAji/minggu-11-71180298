# Aloysius Gonzaga Ardhian Krisna Aji
# 71180298

# Alex sedang membuat program menggunakan tuple
# sebagai temannya yang baik bantulah alex
# membuat program yang dapat menjabarkan isi keranjang buah
# berdasarkan tuple berikut

# input
# keranjang = ("apple", "banana", "cherry", "apple", "cherry","apple", "banana","melon","dragon fruit","melon","banana","orange")

# output 
# jumlah masing-masing dari buah

def buah(keranjang):
    tampung = []
    keranjang2 = sorted(keranjang)
    
    for i in keranjang2:
        if keranjang2.count(i) > 1:
            if[i,keranjang2.count(i)] not in tampung:
                tampung.append([i,keranjang2.count(i)])
        else:
            tampung.append([i,keranjang2.count(i)])
    print("==========Keranjang Buah==========")
    for j in tampung:
        print(f'{j[1]} buah {j[0]}')
        print("==============================")

keranjang = ("apple", "banana", "cherry", "apple", "cherry","apple", "banana","melon","dragon fruit","melon","banana","orange")
buah(keranjang)