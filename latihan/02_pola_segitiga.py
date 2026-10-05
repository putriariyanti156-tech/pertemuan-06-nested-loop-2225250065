# Latihan 2 - Pola Segitiga

# Meminta input jumlah baris
n = int(input("n: "))

# Loop luar menentukan jumlah baris
for i in range(1, n + 1):
    # Loop dalam mencetak bintang sesuai nomor baris
    for j in range(i):
        print("*", end=" ")

    # Pindah ke baris berikutnya
    print()
