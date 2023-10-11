i. Anggota kelompok: <br>
Jeslyn Theodora - 2206082026 <br>
Puti Raissa - 2206830391 <br> 
Muhammad Rafli Mahesa - 2206828140 <br>
Mohammad Fauzan Aditya - 2206827831 <br>
Rena Martha Ulima - 2206818783 <br>

ii. Cerita aplikasi yang diajukan serta manfaatnya <br>
LiteraHub adalah sebuah website perpustakaan yang dirancang supaya pengguna dapat mencari dan meminjam buku, berdiskusi dengan anggota perpustakaan lain dalam forum, serta melakukan reservasi tempat untuk membaca. LiteraHub terdiri dari berbagai fitur, yaitu fitur Product, Forum, Daftar Buku, Pinjam Buku, dan Reservasi LiteraHub. Adapun manfaat LiteraHub, yaitu untuk memudahkan pengguna dalam mencari ketersediaan buku tanpa perlu datang ke perpustakaan secara langsung dan pengguna juga dapat berdiskusi mengenai topik bacaan sesuai dengan minatnya pada forum yang disediakan oleh LiteraHub. Pengguna yang memiliki karya tulis juga dapat mempublikasikan karyanya di LiteraHub. Selain itu, LiteraHub juga membantu pengguna untuk melihat ketersediaan tempat baca dan melakukan reservasi tempat baca di perpustakaan.  <br>

iii. Daftar modul yang akan diimplementasikan <br>
1. Modul LembarAsa <br>
Pengguna yang sudah login bisa menambahkan karyanya ke dalam web LiteraHub. Ketika ingin menambahkan karya, akan ada pop up untuk mengisi *form* yang meminta *input* judul buku, penulis, dll. Disamping itu, akan ada tampilan buku-buku yang diambil dari *dataset* dan karya pengguna (jika ditambahkan). <br>
<br>

2. Modul Forum <br>
Pengguna dapat mengisi obrolan dengan pengguna lainnya untuk saling memberi rekomendasi buku yang bagus ataupun hanya untuk sekadar berdiskusi. *Form* pada modul ini akan meminta *input* teks dan pengguna dapat menambahkan buku serta detailnya saat membuat pesan obrolan. <br>

3. Modul Daftar buku <br>
Pada modul ini, pengguna dapat mencari buku yang diinginkan sesuai judul, nama penulis, dan genrenya. Gambarannya seperti *search* di Shopee filter. Bagian ini juga menampilkan buku-buku yang tersedia dan akan ada buku yang berasal dari modul LembarAsa (karya yang ditambahkan oleh pengguna juga akan ditampilkan disini). Selain itu, pengguna bisa mengisi/melihat review dari buku yang dicari. <br>

4. Modul Peminjaman buku <br>
Modul untuk pengguna melakukan checkout/pinjam buku. Pada modul ini akan ada tampilan pop up untuk mengisi nama peminjam, lama meminjam, dll. Jika sudah di checkout, keterangan peminjaman di bukunya akan bertambah. Selain itu, detail dari peminjam buku akan disimpan untuk keperluan tampilan daftar, yakni tampilan apa saja buku yang telah/sedang dipinjam oleh pengguna. <br>

5. Modul Reservasi LiteraHub <br>
Pengguna dapat melakukan reservasi tempat untuk baca buku secara offline. Pengguna akan mengisi *form*, seperti tanggal kunjungan, nomor anggota, judul buku yang dipinjam, dll. Pada bagian sini akan ditampilkan daftar tempat yang tersedia. <br>

iv. Sumber Dataset Katalog Buku <br>
	https://www.kaggle.com/datasets/saurabhbagchi/books-dataset <br>

* *Role* atau peran pengguna beserta deskripsinya (karena bisa saja lebih dari satu jenis pengguna yang mengakses aplikasi) <br>

* Pengguna tidak *login* <br>
Pengguna yang hanya mengunjungi website LiteraHub tanpa melakukan registrasi akun. Pengguna ini memiliki akses: <br>
* Dapat mengakses daftar buku
* Dapat melihat rekomendasi buku

* Pengguna *login* <br>
Pengguna yang telah melakukan registrasi dan memiliki akun LiteraHub. Pengguna ini memiliki akses: <br>
* Dapat mengakses daftar buku
* Dapat melihat rekomendasi buku
* Dapat berdiskusi di forum
* Dapat reservasi kunjungan LiteraHub
* Dapat menambahkan karyanya ke dalam LiteraHub
* Dapat *checkout*/pinjam buku
