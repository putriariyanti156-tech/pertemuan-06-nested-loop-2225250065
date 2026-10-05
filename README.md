# Pertemuan 06 Nested Loop Python

Algoritma dan Pemrograman | Pertemuan 06 | 12

Nama: ...
NIM: ...
Kelas: ...

## Tujuan

Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Cara Menjalankan

Program latihan dapat dijalankan dengan perintah berikut:

python3 latihan/01_pasangan_indeks.py

python3 latihan/02_pola_segitiga.py

python3 latihan/03_jumlah_per_baris.py

python3 latihan/04_hitung_pasangan.py

Program Tugas 3 dapat dijalankan dengan perintah:

python3 tugas/tabel_perkalian_dan_statistik.py

## Algoritma Tugas 3

### Loop Luar

Loop luar menggunakan variabel i dan berfungsi untuk mengatur baris pada tabel perkalian. Loop berjalan dari 1 sampai n.

### Loop Dalam

Loop dalam menggunakan variabel j dan berfungsi untuk mengatur kolom pada tabel perkalian. Loop berjalan dari 1 sampai n untuk setiap baris.

### Akumulator

Terdapat dua akumulator dalam program:

1. total_baris digunakan untuk menjumlahkan seluruh hasil perkalian pada satu baris.
2. total_semua digunakan untuk menjumlahkan seluruh hasil perkalian dari semua baris.

### Counter

count_genap digunakan sebagai counter untuk menghitung banyaknya hasil perkalian yang merupakan bilangan genap.

Jika hasil perkalian memenuhi kondisi hasil % 2 == 0, maka count_genap bertambah 1.

## Hasil Pengujian

### Latihan 1 - Pasangan Indeks

Loop luar berjalan dari i = 1 sampai 3 dan loop dalam berjalan dari j = 1 sampai 4.

Jumlah pasangan:

3 x 4 = 12 pasangan

Hasil yang diharapkan:

Banyak pasangan = 12

Status: Berhasil

### Latihan 2 - Pola Segitiga

Test case yang digunakan:

1. n = 1
2. n = 3
3. n = 5

Untuk n = 3, keluaran yang diharapkan:

* 
* * 
* * *

Status: Berhasil

### Latihan 3 - Jumlah Per Baris

Hasil yang diharapkan:

Jumlah baris 1 = 6
Jumlah baris 2 = 12
Jumlah baris 3 = 18
Jumlah baris 4 = 24

Status: Berhasil

### Latihan 4 - Menghitung Pasangan

Test case:

n = 2

Banyak pasangan = 1

n = 3

Banyak pasangan = 3

n = 5

Banyak pasangan = 10

Status: Berhasil

### Tugas 3 - Tabel Perkalian dan Statistik

Test case wajib:

n = 1
Jumlah pasangan = 1
Total semua = 1
Banyak hasil genap = 0

n = 2
Jumlah pasangan = 4
Total semua = 9
Banyak hasil genap = 3

n = 3
Jumlah pasangan = 9
Total semua = 36
Banyak hasil genap = 5

Semua test case berhasil dijalankan.

## Analisis Efisiensi

Program menggunakan nested loop.

Loop luar berjalan sebanyak n kali.

Loop dalam berjalan sebanyak n kali untuk setiap iterasi loop luar.

Jadi, badan loop dalam berjalan sebanyak:

n x n = n² kali

Contoh:

Jika n = 1, maka:

1² = 1 kali

Jika n = 2, maka:

2² = 4 kali

Jika n = 3, maka:

3² = 9 kali

Jika n = 5, maka:

5² = 25 kali

Dengan demikian, kompleksitas waktu nested loop adalah O(n²).

## Refleksi

Salah satu kesalahan yang dapat terjadi pada nested loop adalah meletakkan total_baris = 0 di luar loop luar.

Jika total_baris tidak direset pada setiap baris, maka hasil penjumlahan dari baris sebelumnya akan terbawa ke baris berikutnya.

Cara memperbaikinya adalah dengan meletakkan total_baris = 0 di dalam loop luar dan sebelum loop dalam.

Dengan cara tersebut, setiap baris akan memiliki perhitungan jumlah yang dimulai dari 0.

## Refleksi Teknis

### 1. Mengapa total_baris direset di setiap iterasi loop luar?

Karena total_baris digunakan untuk menghitung jumlah hasil perkalian pada satu baris.

Ketika masuk ke baris baru, total_baris harus kembali menjadi 0 agar hasil dari baris sebelumnya tidak ikut dihitung.

### 2. Mengapa total_semua tidak direset di setiap baris?

Karena total_semua digunakan untuk menghitung jumlah seluruh hasil perkalian dari semua baris.

Jika total_semua direset setiap baris, maka hasil dari baris sebelumnya akan hilang.

Oleh karena itu, total_semua hanya diinisialisasi satu kali sebelum nested loop dimulai.

### 3. Untuk n, berapa kali pernyataan hasil = i * j dieksekusi?

Pernyataan:

hasil = i * j

dieksekusi sebanyak:

n x n = n² kali

Hal tersebut terjadi karena loop luar berjalan n kali dan loop dalam berjalan n kali pada setiap iterasi loop luar.

### 4. Bagaimana Anda membuktikan count_genap benar?

Setiap hasil perkalian diperiksa menggunakan kondisi:

hasil % 2 == 0

Jika hasil pembagian dengan 2 memiliki sisa 0, maka hasil tersebut merupakan bilangan genap.

Jika kondisi tersebut benar, maka count_genap bertambah 1.

Contoh untuk n = 3:

1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9

Hasil yang genap adalah:

2, 2, 4, 6, 6

Jumlah hasil genap adalah 5.

Jadi:

count_genap = 5

### 5. Apa bagian program yang akan paling banyak melakukan operasi ketika n membesar?

Bagian program yang paling banyak melakukan operasi adalah nested loop, khususnya loop dalam.

Hal ini karena loop dalam dijalankan sebanyak n kali untuk setiap iterasi loop luar.

Jumlah keseluruhan eksekusi badan loop dalam adalah n².

Jadi, semakin besar nilai n, semakin banyak operasi yang dilakukan oleh program.

## Kesimpulan

Nested loop digunakan untuk melakukan perulangan di dalam perulangan.

Loop luar digunakan untuk mengatur baris, sedangkan loop dalam digunakan untuk mengatur kolom.

Akumulator digunakan untuk menjumlahkan nilai, sedangkan counter digunakan untuk menghitung jumlah data yang memenuhi kondisi.

Pada Tugas 3, nested loop berjalan sebanyak n² kali sehingga kompleksitas waktunya adalah O(n²).

Program telah diuji menggunakan test case yang diberikan dan menghasilkan keluaran sesuai dengan hasil yang diharapkan.