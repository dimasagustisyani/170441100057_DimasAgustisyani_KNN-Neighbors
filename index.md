# Pengertian dan Cara Kerja Algoritma K-Nearest Neighbors (KNN)

![](C:\mkdocs-material-master\docs\assets\images\1.png)

K-nearest neighbors atau knn adalah algoritma yang berfungsi untuk melakukan klasifikasi suatu data berdasarkan data pembelajaran (*train data sets*), yang diambil dari k tetangga terdekatnya (*nearest neighbors*). Dengan k merupakan banyaknya tetangga terdekat.

#### **A. Cara Kerja Algoritma K-Nearest Neighbors (KNN)**

K-nearest neighbors melakukan klasifikasi dengan proyeksi data pembelajaran pada ruang berdimensi banyak. Ruang ini dibagi menjadi bagian-bagian yang merepresentasikan kriteria data pembelajaran. Setiap data pembelajaran direpresentasikan menjadi titik-titik ***c*** pada ruang dimensi banyak.

##### 

##### **Klasifikasi Terdekat (Nearest Neighbor Classification)**

**Data baru** yang diklasifikasi selanjutnya diproyeksikan pada ruang dimensi banyak yang telah memuat titik-titik c data pembelajaran. Proses klasifikasi dilakukan dengan mencari titik **c** terdekat dari **c-baru** (*nearest neighbor*)*.* Teknik pencarian tetangga terdekat yang umum dilakukan dengan menggunakan formula jarak euclidean*.* Berikut beberapa formula yang digunakan dalam algoritma knn.

- ###### **Euclidean Distance**

  Jarak Euclidean adalah formula untuk mencari jarak antara 2 titik dalam ruang dua dimensi.

  ![](C:\mkdocs-material-master\docs\assets\images\2.png)

- ###### **Hamming Distance**

  Jarak Hamming adalah cara mencari jarak antar 2 titik yang dihitung dengan panjang vektor biner yang dibentuk oleh dua titik tersebut dalam block kode biner.

- ###### **Manhattan Distance**

  Manhattan Distance atau Taxicab Geometri adalah formula untuk mencari jarak **d** antar 2 vektor ***p,q*** pada ruang dimensi **n***.*

- ###### **Minkowski Distance**

  Minkowski distance adalah formula pengukuran antar 2 titik pada ruang vektor normal yang merupakan hibridisasi yang mengeneralisasi euclidean distance dan mahattan distance.

Teknik pencarian tetangga terdekat disesuaikan dengan dimensi data, proyeksi, dan kemudahan implementasi oleh pengguna.

------

##### **Banyaknya k Tetangga Terdekat**

Untuk menggunakan algoritma k nearest neighbors, perlu ditentukan banyaknya k tetangga terdekat yang digunakan untuk melakukan klasifikasi data baru. Banyaknya k, sebaiknya merupakan angka ganjil, misalnya k = 1, 2, 3, dan seterusnya. Penentuan nilai k dipertimbangkan berdasarkan banyaknya data yang ada dan ukuran dimensi yang dibentuk oleh data. Semakin banyak data yang ada, angka k yang dipilih sebaiknya semakin rendah. Namun, semakin besar ukuran dimensi data, angka k yang dipilih sebaiknya semakin tinggi.

------

##### **Algoritma K-Nearest Neighbors**

1. Tentukan k bilangan bulat positif berdasarkan ketersediaan data pembelajaran.
2. Pilih tetangga terdekat dari data baru sebanyak k.
3. Tentukan klasifikasi paling umum pada langkah (ii), dengan menggunakan frekuensi terbanyak.
4. Keluaran klasifikasi dari data sampel baru.

------

#### **B. Contoh Aplikasi K Nearest Neighbor**

Contoh berikut diambil dari buku “**Data Science Algorithms in a Week**” yang ditulis oleh  Dávid Natingga.

Pada contoh ini, dilakukan klasifikasi suhu udara berdasarkan persepsi seseorang yang bernama Marry. Adapun klasifikasi suhu udara terdiri dari 2 persepsi yaitu **Panas** dan **Dingin**. Persepsi ini dapat diukur berdasarkan 2 variabel yaitu **temperatur dalam derajat celcius** dan **kecepatan** **angin dalam km/h**. Diperoleh data berikut,

| Temperatur Udara (ºC) | Kecepatan Angin (km/jam) | Klasifikasi atau Persepsi Marry |
| --------------------- | ------------------------ | ------------------------------- |
| 10                    | 0                        | Dingin                          |
| 25                    | 0                        | Panas                           |
| 15                    | 5                        | Dingin                          |
| 20                    | 3                        | Panas                           |
| 18                    | 7                        | Dingin                          |
| 20                    | 10                       | Dingin                          |
| 22                    | 5                        | Panas                           |
| 24                    | 6                        | Panas                           |

Untuk contoh ini terbentuk ruang dimensi 2, yang berisi 2 kriteria yaitu **temperatur udara** dan **kecepatan angin**.

![](C:\mkdocs-material-master\docs\assets\images\3.png)

Pada proyeksi di atas sumbu vertikal adalah kecepatan angin, sumbu horizontal adalah temperatur suhu, warna biru adalah dingin, dan warna merah adalah panas.

Dari proyeksi diatas, dapat dilakukan klasifikasi data baru. Misalnya, Bagaimana persepsi Marry saat temperatur udara 16°C dan kecepatan angin 3km/jam.

![](C:\mkdocs-material-master\docs\assets\images\3.png)

Proses pencarian tetangga terdekat

![](C:\mkdocs-material-master\docs\assets\images\4.png)

Dapat diketahui tetangga terdekatnya adalah titik ***c dingin*** dengan temperature 15°C dan kecepatan angin 5km/jam. Jadi berdasarkan pemilihan k = 1, klasifikasinya adalah **dingin**.

Dengan melakukan proses di atas terhadap semua titik, diperoleh proyeksi klasifikasi berikut.

![](C:\mkdocs-material-master\docs\assets\images\5.png)

**Catatan: Untuk pemilihan k lainnya, hasil klasifikasi ditentukan dengan frekuensi terbanyak. Misalnya k = 3, dengan titik terdekat dingin, panas, dingin. Hasil klasifikasi data baru tersebut adalah dingin.**