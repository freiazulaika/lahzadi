# LAHZADI

Proyek Django untuk tugas mata kuliah Pemrograman Berbasis Platform Ganjil 2024/2025. Dibuat oleh Freia Arianti Zulaika - 2306152254.

Link menuju PWS deployment terdapat dalam [link ini](http://freia-arianti-lahzadi.pbp.cs.ui.ac.id/).

## Tugas 2: Implementasi Model-View-Template (MVT) pada Django

### Langkah Implementasi Checklist
Implementasi dari checklist pada tugas 2:
#### Membuat sebuah proyek Django baru
1. Membuat direktori bernama “lahzadi” dalam direktori lokal dan masuk ke dalam direktori tersebut
2. Membuat _virtual environment_ dalam direktori tersebut menggunakan perintah berikut:
    ```
    py -m venv env
    ```
3. Melakukan aktivasi _virtual environment_ menggunakan perintah berikut:
    ```
    env\Scripts\activate
    ```
4. Di dalam direktori tersebut, membuat file berjudul “requirements.txt” yang berisi:
   ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
5. Melakukan instalasi terhadap _dependencies_ menggunakan perintah berikut:
    ```
    pip install -r requirements.txt
    ```
6. Membuat project Django bernama 'lahzadi' menggunakan perintah berikut:
    ```
    django-admin startproject lahzadi .
    ```
7. Membuat repositori baru di GitHub dengan nama 'lahzadi'
8. Menginisiasi direktori lokal “lahzadi” sebagai repositori git menggunakan perintah berikut:
   ```
    git init
    ```
9. Menambahkan berkas .gitignore
10. Membuat _branch_ utama baru bernama 'main' dengan menggunakan perintah berikut:
    ```
    git branch -M main
    ```
11. Menghubungkan direktori lokal dengan repositori GitHub dengan menggunakan perintah berikut:
    ```
    git remote add origin https://github.com/freiazulaika/lahzadi.git
    ```
11. Melakukan _add_, _commit_, dan _push_ dari direktori lokal ke repositori GitHub
    
####  Membuat aplikasi dengan nama main pada proyek tersebut
1. Masih dalam direkotri yang sama, membuat aplikasi bernama 'main' menggunakan perintah berikut:
    ```
    python manage.py startapp main
    ```
2. Menambahkan 'main' ke INSTALLED_APPS di dalam berkas settings.py

#### Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib (name, price, description)
1. Pada berkas models.py di dalam direktori aplikasi 'main', menambahkan class 'Product' dengan atribut name, price, description, stock, note, dan size
2. Melakukan makemigrations menggunakan perintah berikut:
   ```
   python manage.py makemigrations
   ```
3. Melakukan migration menggunakan perintah berikut:
   ```
   python manage.py migrate
   ```

#### Membuat sebuah fungsi pada views.py
1. Membuat direktori bernama 'template' di dalam direktori aplikasi 'main' dan membuat berkas baru bernama 'main.html'
2. Di dalam berkas 'main.html', menambahkan nama toko, nama, dan kelas
3. Dalam berkas views.py di dalam direktori aplikasi 'main', menambahkan fungsi bernama 'show_main' yang berisi dictionary yang berisi data (nama dan kelas) yang akan dihubungkan ke tampilan. Fungsi ini akan mengembalikan untuk me-_render_ tampilan di berkas main.html

#### Melakukan routing pada proyek agar dapat menjalankan aplikasi main dan membuat sebuah routing pada urls.py aplikasi main
1. Membuat berkas 'urls.py' di direktori aplikasi 'main' dan menambahkan isi:
   ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
2. Membuka berkas 'urls.py' di direktori proyek 'lahzadi' dan menambahkan isi:
    ```
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
     ```
#### Melakukan deployment ke PWS
1. Masuk ke dalam _website_ PWS dan membuat proyek baru bernama 'lahzadi'
2. Menambahkan url _deployment_ PWS di dalam berkas settings.py di proyek 'lahzadi'
3. Melakukan _add_, _commit_, dan _push_ ke GitHub
4. Melakukan perintah pada _Project Command_ di PWS
5. Tunggu hasil proyek hingga menunjukkan status _successful_

### Bagan
![bagan](https://github.com/user-attachments/assets/1bcf8685-3f62-4cf1-a02e-1859d55bfd96)

### Fungsi git dalam pengembangan perangkat lunak
Fungsi git dalam pengembangan perangkat lunak:
* Git dapat membantu kita dalam mengelompokkan dan melacak perubahan kode yang dilakukan.
* Git memudahkan dalam berkolaborasi dengan banyak pengembang melalui kemampuannya seperti mengelola project/kode dalam branch yang berbeda, sehingga tidak mengganggu kode di branch utama.

### Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django dijadikan permulaan dalam pembelajaran pengembangan perangkat lunak karena Django menggunakan bahasa Python yang relatif sederhana dan mudah dipahami. Selain itu, Django juga sudah menyediakan banyak fitur bawaan yang memudahkan dalam pengembangan aplikasi web dengan cepat. Django memiliki struktur yang terorganisasi dan memiliki bentuk Model-View-Template (MVT) yang memudahkan pengembang dalam membangun dan mengelola aplikasi web. Django juga dapat menangani pengembangan aplikasi yang kompleks serta memiliki fitur keamanan yang baik.

### Mengapa model pada Django disebut sebagai ORM?
Model di Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai jembatan antara objek Python dan tabel dalam database. Dengan ORM, pengembang dapat mengelola database menggunakan kode Python tanpa harus menulis _query_ SQL. Django mengubah atribut dalam kelas Python menjadi kolom-kolom di tabel database, sehingga interaksi dengan database jadi lebih mudah. ORM ini otomatis menerjemahkan operasi Python menjadi perintah SQL, sehingga proses mengelola data lebih sederhana dan teratur.


