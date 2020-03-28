# Membuat beberapa query pada database *world* menggunakan MySQL

- Mengaktifkan sql
```bash
C:\Users\>mysql.exe --user=root
```

- Melakukan *setting up* database *world*
```bash
mysql> SOURCE C:/temp/world.sql;
```

📌 Panduan *setting up* database *world* bisa dilihat melalui [MySQL: Setting Up the world Database](https://dev.mysql.com/doc/world-setup/en/)

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

5. Menampilkan daftar **negara-negara Asia yang memiliki angka harapan hidup lebih dari rata-rata angka harapan hidup negara-negara Eropa**.
```bash
mysql> SELECT Name AS Nama, Continent AS Benua, LifeExpectancy AS AngkaHrpnHdp, GNP
    -> FROM country
    -> WHERE Continent = "Asia" AND LifeExpectancy>(SELECT AVG(LifeExpectancy)
    -> FROM country
    -> WHERE Continent = "Europe")
    -> ORDER BY AngkaHrpnHdp DESC;
```

6. Menampilkan **daftar 10 negara yang bahasa resminya (official language) adalah bahasa Inggris, dan memiliki persentase pengguna bahasa Inggris tertinggi di dunia**.
```bash
mysql> SELECT countrylanguage.CountryCode AS countrycode, country.Name AS name, countrylanguage.Language AS language, countrylanguage.IsOfficial as isOfficial, countrylanguage.Percentage as percentage
    -> FROM countrylanguage
    -> JOIN country
    -> ON countrylanguage.CountryCode = country.Code
    -> WHERE countrylanguage.language = "English" AND countrylanguage.isOfficial = "T"
    -> ORDER BY percentage DESC
    -> LIMIT 10;
```

7. Menampilkan **daftar negara ASEAN beserta populasi negaranya, Pendapatan Nasional Bruto/GNP (Gross National Product), ibukota & populasi ibukota**.
```bash
mysql> SELECT country.Name AS Negara_ASEAN, country.Population AS Populasi_Negara, country.GNP AS GNP, city.Name AS Ibukota_Negara, city.Population AS Populasi_Ibukota
    -> FROM country
    -> JOIN city
    -> ON country.Code = city.CountryCode
    -> WHERE city.ID = 939
    -> OR city.ID = 538
    -> OR city.ID = 1800
    -> OR city.ID = 1522
    -> OR city.ID = 2432
    -> OR city.ID = 2464
    -> OR city.ID = 2710
    -> OR city.ID = 766
    -> OR city.ID = 3208
    -> OR city.ID = 3320
    -> OR city.ID = 3770
    -> ORDER BY Negara_ASEAN;
```
