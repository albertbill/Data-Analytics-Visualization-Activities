# Membuat database *sekolahku* menggunakan MySQL

Mengaktifkan sql.
```bash
C:\Users\>mysql.exe --user=root
```

Membuat database sekolahku.
```bash
mysql> CREATE database sekolahku;
```

Menggunakan database sekolahku.
```bash
mysql> USE sekolahku;
```

1. Membuat tabel _users_
```bash
mysql> CREATE TABLE users (
    -> id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    -> username VARCHAR(50) NOT NULL,
    -> email VARCHAR(50) NOT NULL,
    -> password VARCHAR(50) NOT NULL,
    -> created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -> updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
```

   Memasukan data ke dalam tabel _users_
```bash
mysql> INSERT INTO users VALUE
    -> (1, "Andi", "andi@andi.com", "12345", NULL, NULL);
    -> (2, "Budi", "budi@budi.com", "67890", NULL, NULL),
    -> (3, "Caca", "caca@caca.com", "abcde", NULL, NULL),
    -> (4, "Deni", "deni@deni.com", "fghij", NULL, NULL),
    -> (5, "Euis", "euis@euis.com", "klmno", NULL, NULL),
    -> (6, "Fafa", "fafa@fafa.com", "pqrst", NULL, NULL);
```

2. Membuat tabel _courses_
```bash
mysql> CREATE TABLE courses (
    -> id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    -> course VARCHAR(50) NOT NULL,
    -> mentor VARCHAR(50) NOT NULL,
    -> title VARCHAR(50) NOT NULL);
```

  Memasukkan data ke tabel _courses_
```bash
mysql> INSERT INTO courses VALUE
    -> (1, "C++", "Ari", "Dr."),
    -> (2, "C#", "Ari", "Dr."),
    -> (3, "C#", "Ari", "Dr."),
    -> (4, "CSS", "Cania", "S.Kom"),
    -> (5, "HTML", "Cania", "S.Kom"),
    -> (6, "Javascript", "Cania", "S.Kom"),
    -> (7, "Python", "Barry", "S.T."),
    -> (8, "Micropython", "Barry", "S.T."),
    -> (9, "Java", "Darren", "M.T."),
    -> (10, "Ruby", "Darren", "M.T.");
```

3. Membuat tabel _userCourse_
```bash
mysql> CREATE TABLE userCourse (
    -> id_user INT(11),
    -> id_course INT(11));
```

   Memasukkan data ke tabel _userCourse_
```bash
mysql> INSERT INTO userCourse VALUES
    -> (1,1),
    -> (1,2),
    -> (1,3),
    -> (2,4),
    -> (2,5),
    -> (2,6),
    -> (3,7),
    -> (3,8),
    -> (3,9),
    -> (4,1),
    -> (4,3),
    -> (4,5),
    -> (5,2),
    -> (5,4),
    -> (5,6),
    -> (6,7),
    -> (6,8),
    -> (6,9);
```

4. Menggunakan __INNER JOIN__ untuk menggabungkan peserta didik dengan kelas yang diambil beserta nama mentornya.
```bash
mysql> SELECT users.id, users.username, courses.course, courses.mentor, courses.title
    -> FROM users JOIN userCourse
    -> ON users.id = userCourse.id_user
    -> JOIN courses
    -> ON userCourse.id_course = courses.id;
```

5. Menampilkan daftar peserta didik beserta mata kuliah yang diikutinya, yang mentornya bergelar sarjana.
```bash
mysql> SELECT users.id, users.username, courses.course, courses.mentor, courses.title
    -> FROM users JOIN userCourse
    -> ON users.id = userCourse.id_user
    -> JOIN courses
    -> ON userCourse.id_course = courses.id
    -> WHERE courses.title LIKE "S%";
```

6. Menampilkan daftar peserta didik beserta mata kuliah yang diikutinya, yang mentornya bergelar selain sarjana.
```bash
mysql> SELECT users.id, users.username, courses.course, courses.mentor, courses.title
    -> FROM users JOIN userCourse
    -> ON users.id = userCourse.id_user
    -> JOIN courses
    -> ON userCourse.id_course = courses.id
    -> WHERE courses.title NOT LIKE "S%";
```

7. Menampilkan jumlah peserta didik untuk setiap mata kuliah.
```bash
mysql> SELECT courses.course, courses.mentor, courses.title, COUNT(users.username) AS jumlah_peserta
    -> FROM users JOIN userCourse
    -> ON users.id = userCourse.id_user
    -> JOIN courses
    -> ON userCourse.id_course = courses.id
    -> GROUP BY courses.course;
```

8. Menampilkan total fee untuk setiap mentor dengan besaran fee per peserta Rp. 2.000.000,-
```bash
mysql> SELECT courses.course, courses.mentor, courses.title, COUNT(users.username) AS jumlah_peserta
    -> FROM users JOIN userCourse
    -> ON users.id = userCourse.id_user
    -> JOIN courses
    -> ON userCourse.id_course = courses.id
    -> GROUP BY course;
```
