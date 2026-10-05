# Tugas 3 - Tabel Perkalian dan Statistik

print("Tabel Perkalian dan Statistik")

# Meminta input n
n = int(input("n: "))

# Validasi agar n harus positif
while n <= 0:
    print("n harus bilangan positif.")
    n = int(input("n: "))

# Akumulator total seluruh hasil perkalian
total_semua = 0

# Counter untuk menghitung hasil yang genap
count_genap = 0

# Loop luar untuk membuat baris
for i in range(1, n + 1):

    # Menyimpan daftar atau informasi pasangan pada baris ini
    daftar_pasangan = []

    # Loop dalam untuk membuat kolom
    for j in range(1, n + 1):

        # Menghitung hasil perkalian
        hasil = i * j

        # Menampilkan hasil secara teratur
        print(hasil, end="\t")

        # Menyimpan pasangan (i, j)
        daftar_pasangan.append(f"({i},{j})")

        # Menambahkan hasil ke total keseluruhan
        total_semua += hasil

        # Mengecek apakah hasil genap
        if hasil % 2 == 0:
            count_genap += 1

    # Pindah ke baris berikutnya dan tampilkan informasi pasangan
    print(f"| Pasangan baris {i}: {', '.join(daftar_pasangan)}")

# Menampilkan hasil statistik
print(f"Total keseluruhan = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")
