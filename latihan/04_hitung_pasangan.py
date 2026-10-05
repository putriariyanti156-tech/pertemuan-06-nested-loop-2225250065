# Latihan 4 - Menghitung Pasangan

# Meminta input n
n = int(input("n: "))

# Counter untuk menghitung pasangan yang memenuhi kondisi
count = 0

# Loop luar untuk nilai i
for i in range(1, n + 1):

    # Loop dalam untuk nilai j
    for j in range(1, n + 1):

        # Mengecek apakah i + j <= n
        if i + j <= n:
            count += 1

# Menampilkan jumlah pasangan
print(f"Banyak pasangan = {count}")
