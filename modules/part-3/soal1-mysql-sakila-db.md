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

3. Menampilkan daftar lengkap **rating film beserta keterangan arti rating & jumlah film tiap rating**.
    1. Membuat tabel *rating_film*
    ```bash
    mysql> CREATE TABLE rating_film (
        -> rating VARCHAR(50),
        -> keterangan VARCHAR(50)
        -> );
    ```
    2. Memasukkan data ke tabel *rating_film*
    ```bash
    mysql> INSERT INTO rating_film VALUE
        -> ("G", "General Audiences"),
        -> ("PG", "Parental Guidance Suggested"),
        -> ("PG-13", "Parental Guidances for Children Under 13"),
        -> ("R", "Restricted"),
        -> ("NC-17", "No Children Under 17 Admitted");
    ```
    3. Menampilkan rating film, keterangan rating film & total film tiap rating
    ```bash
    mysql> SELECT film.rating AS rating, rating_film.keterangan AS keterangan, COUNT(film.rating) AS jumlahMovie
        -> FROM film
        -> JOIN rating_film
        -> ON film.rating = rating_film.rating
        -> GROUP BY film.rating
        -> ORDER BY rating;
    ```
4. Menampilkan daftar **10 aktor/aktris yang paling banyak membintangi film**.
```bash
mysql> SELECT actor.actor_id, actor.first_name, actor.last_name, COUNT(film.film_id) AS jumlah_movie
    -> FROM film
    -> JOIN film_actor
    -> ON film.film_id = film_actor.film_id
    -> JOIN actor
    -> ON actor.actor_id = film_actor.actor_id
    -> GROUP BY actor.actor_id
    -> ORDER BY jumlah_movie DESC
    -> LIMIT 10;
```

5. Menampilkan daftar **kategori film beserta jumlah film yang pernah dibintangi oleh Gina Degeneres**.
```bash
mysql> SELECT category.name, COUNT(film.title) AS jumlah_movie
    -> FROM category
    -> JOIN film_category
    -> ON category.category_id = film_category.category_id
    -> JOIN film
    -> ON film_category.film_id = film.film_id
    -> JOIN film_actor
    -> ON film.film_id = film_actor.film_id
    -> JOIN actor
    -> ON film_actor.actor_id = actor.actor_id
    -> WHERE actor.actor_id = 107
    -> GROUP BY category.name;
```
