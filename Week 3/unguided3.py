def conversi (dolar):
    rupiah = 15000
    hasil = dolar * rupiah
    return print(f"{dolar} USD to Rp. {hasil}")

dolar = int(input("Masukan Nominal : "))
conversi(dolar)