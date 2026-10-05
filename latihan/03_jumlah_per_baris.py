# Latihan 3 - Jumlah Per Baris

# Loop luar untuk baris 1 sampai 4
for i in range(1, 5):

    # Akumulator untuk jumlah setiap baris
    total_baris = 0

    # Loop dalam untuk kolom 1 sampai 3
    for j in range(1, 4):

        # Menambahkan hasil perkalian ke total baris
        total_baris += i * j

    # Menampilkan jumlah setiap baris
    print(f"Jumlah baris {i} = {total_baris}")
