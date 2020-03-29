# Membuat beberapa query pada database *sakila* menggunakan MySQL

- Mengaktifkan sql
```bash
C:\Users\>mysql.exe --user=root
```

- Melakukan *setting up* database *sakila*
```bash
mysql> SOURCE C:/temp/sakila-db/sakila-schema.sql;
mysql> SOURCE C:/temp/sakila-db/sakila-data.sql;
```

📌 Panduan *setting up* database *sakila* bisa dilihat melalui [MySQL: Sakila Sample Database](https://dev.mysql.com/doc/sakila/en/sakila-installation.html)

- Menggunakan database *sakila*
```bash
mysql> USE sakila;
```

1. Menampilkan daftar **10 film komedi dengan durasi tersingkat**.
```bash
mysql> SELECT title, category, length
    -> FROM film_list
    -> WHERE category="Comedy"
    -> ORDER BY length
    -> LIMIT 10;
```

2. Menampilkan daftar lengkap **kategori film beserta jumlah film tiap kategori & rata-rata harga sewa DVD film tiap kategori**.
```bash
mysql> SELECT category, COUNT(category) AS jumlahMovie, AVG(price) AS rataHargaSewa
    -> FROM film_list
    -> GROUP BY category
    -> ORDER BY jumlahMovie DESC;
```

1. A numbered list
              1. A nested numbered list
