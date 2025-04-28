sisi = 20 # sisi segitiga
count = 1 # jumlah bintang
spasi = sisi // 2 # jumlah spasi

while True:   # loop untuk mencetak segitiga
    if count <= sisi: # jika jumlah bintang kurang dari atau sama dengan sisi segitiga
        print(" " * spasi , "*" * count) # mencetak spasi dan bintang
        count += 2 # menambah jumlah bintang
        spasi -= 1 # mengurangi jumlah spasi
    else: # jika jumlah bintang lebih dari sisi segitiga
        break # keluar dari loop