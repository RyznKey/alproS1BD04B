def conversi_rupiah (rupiah):
    kurs = 15000
    dolar = rupiah / kurs
    return print(f"Rp. {rupiah} to ${dolar:.2f} USD")

# Main Program
rupiah = int(input("Masukan Nominal : Rp. "))
conversi_rupiah(rupiah)