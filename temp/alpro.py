pembelian = int (input("Masukkan jumlah pembelian: "))
if pembelian >= 2000000:
    diskon = 0.2
elif pembelian >= 1000000:
    diskon = 0.15
elif pembelian >= 500000:
    diskon = 0.1
else:
    diskon = 0

print("Diskon yang didapat: ", diskon * 100, "%")
total = pembelian - (pembelian * diskon)
print("Total yang harus dibayar: ", total)