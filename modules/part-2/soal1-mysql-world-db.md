# Membuat beberapa query pada database *world* menggunakan MySQL

- Mengaktifkan sql.
```bash
C:\Users\>mysql.exe --user=root
```

- Melakukan *setting up* database *world*
```bash
mysql> SOURCE C:/temp/world.sql;
```

📌 Panduan *setting up* database *world* bisa dilihat melalui [MySQL: Setting Up the World Database](https://dev.mysql.com/doc/world-setup/en/)

- Menggunakan database *world*
```bash
mysql> USE world;
```

1. Menampilkan daftar **10 kota terpadat di Indonesia**.
```bash
mysql> SELECT * FROM city
    -> WHERE CountryCode = "IDN"
    -> ORDER BY Population
    -> DESC LIMIT 10;
```

2. Menampilkan daftar **10 kota terpadat di dunia beserta asal negaranya**.
```bash
mysql> SELECT city.ID AS id, city.Name AS nama_kota, city.District AS district, country.Name AS negara, city.Population AS population
    -> FROM city JOIN country
    -> ON city.CountryCode = country.Code
    -> ORDER BY city.Population DESC
    -> LIMIT 10;
```

3. Menampilkan daftar **10 negara yang tercatat merdeka paling awal**.
```bash
mysql> SELECT Code AS code, Name AS name, Continent AS continent, Region as region, IndepYear as tahun_merdeka
    -> FROM country
    -> WHERE IndepYear IS NOT NULL
    -> ORDER BY IndepYear
    -> LIMIT 10;
```

4. Menampilkan daftar **benua yang memiliki lebih dari 10 negara di dalamnya**.
```bash
mysql> SELECT Continent AS benua, COUNT(Continent) AS Jumlah_Negara, SUM(Population) AS Populasi, AVG(LifeExpectancy) AS Rata_AngkaHrpnHdp
    -> FROM country
    -> GROUP BY Continent
    -> HAVING COUNT(Continent) > 10
    -> ORDER BY Populasi DESC;
```

5. Tampilkan daftar **negara-negara Asia yang memiliki angka harapan hidup lebih dari rata-rata angka harapan hidup negara-negara Eropa**.
```bash
mysql> SELECT Name AS Nama, Continent AS Benua, LifeExpectancy AS AngkaHrpnHdp, GNP
    -> FROM country
    -> WHERE Continent = "Asia" AND LifeExpectancy>(SELECT AVG(LifeExpectancy)
    -> FROM country
    -> WHERE Continent = "Europe")
    -> ORDER BY AngkaHrpnHdp DESC;
```
