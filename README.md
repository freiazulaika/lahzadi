# LAHZADI

Proyek Django untuk tugas mata kuliah Pemrograman Berbasis Platform Ganjil 2024/2025. Dibuat oleh Freia Arianti Zulaika - 2306152254.

Link menuju PWS deployment terdapat dalam [link ini](http://freia-arianti-lahzadi.pbp.cs.ui.ac.id/).

<details>
<Summary><b>Tugas 2: Implementasi Model-View-Template (MVT) pada Django</b></Summary>

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

</details>

<details>
<Summary><b>Tugas 3: Implementasi Form dan Data Delivery pada Django</b></Summary>
    
### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Dalam proses pengimplementasian platform, data delivery menjadi penting karena memudahkan komunikasi antara klien, server, dan sistem lainnya. Proses ini memastikan bahwa informasi dapat dikirim dengan cepat, aman, dan efisien. Tanpa data delivery yang baik, platform akan terasa lambat dan tidak efisien, sehingga dapat mengurangi minat pengguna.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih baik dan lebih populer daripada XML karena JSON memiliki struktur dan tampilan yang sederhana, sehingga lebih mudah dibaca oleh manusia. Selain itu, pemrosesan JSON juga cenderung lebih cepat dan lebih efisien untuk pertukaran data karena memiliki kompleksitas yang lebih rendah dibandingkan dengan XML.

###  Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django digunakan untuk mengetahui validitas/kebenaran data yang dimasukkan. Jika data yang dimasukkan sesuai dengan persyaratan yang ada di form (misal tipe data, panjang data), maka is_valid() akan bernilai True dan sebaliknya. Method ini dibutuhkan karena dapat mengetahui dan memastikan data yang mau dimasukkan ke database sudah benar. Selain itu, method ini juga mempermudah pengelolaan jika ada error ketika data yang dimasukkan tidak sesuai.

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token penting untuk melindungi aplikasi web dari serangan _Cross-Site Request Forgery (CSRF)_, di mana penyerang dapat membuat pengguna yang telah terautentikasi mengirimkan permintaan berbahaya ke server tanpa sepengetahuan mereka. Tanpa csrf_token, server tidak dapat membedakan antara request asli dan request berbahaya, sehingga penyerang dapat menyalahgunakan sesi pengguna untuk melakukan tindakan yang tidak diinginkan. Sehingga, csrf_token berperan untuk memastikan bahwa setiap request berasal dari sumber yang sah dan aman.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat direktori bernama _templates_ di dalam _main directory_
2. Membuat berkas base.html di dalam direktori tersebut
3. Menambahkan kode berikut di dalam file base.html:
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% block meta %} {% endblock meta %}
    <title>LAHZADI</title>
</head>

<body>
    {% block content %} {% endblock content %}
</body>

</html>
```
4. Pada berkas settings.py di direktori proyek lahzadi, menambahkan kode berikut di dalam variabel TEMPLATES
```
'DIRS': [BASE_DIR / 'templates']
```
5. Mengubah kode di berkas main.html yang berada di path main/templates/ dengan kode berikut:
```
{% extends 'base.html' %}
{% block content %}

<h1>LAHZADI</h1>

<h5>Name: </h5>
<p>{{ name }}
<p>
<h5>Class: </h5>
<p>{{ kelas }}
<p>

{% endblock content %}
```
6. Menambahkan kode berikut di bagian atas dari berkas models.py di subdirektori main/:
```
import uuid
```
7. Melakukan migrasi
8. Membuat berkas di direktori main dengan nama forms.py dan mengisi dengan kode berikut:
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock", "size"]
```
9. Menambahkan kode berikut di dalam berkas views.py yang ada di direktori main:
```
from django.shortcuts import render, redirect
```
10. Di dalam views.py, menambahkan fungsi berikut:
```
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
11. Mengubah fungsi show_main di dalam berkas yang sama menjadi:
```
def show_main(request):
    product_entries = Product.objects.all()
    context = {
        'name': 'Freia Arianti Zulaika',
        'kelas' : 'PBP C',
        'product_entries' : product_entries,
    }

    return render(request, "main.html", context)
```
12. Membuat berkas create_product_entry.html pada direktori main/templates dan mengisi dengan kode berikut:
```
{% extends 'base.html' %}
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product Entry" />
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
13. Menambahkan kode berikut ke dalam {% block content %} di berkas main.html dalam path main/templates:
```
{% extends 'base.html' %}
{% block content %}

<h1>LAHZADI</h1>

<h5>Name: </h5>
<p>{{ name }}
<p>
<h5>Class: </h5>
<p>{{ kelas }}
<p>

    {% if not product_entries %}
<p>Belum ada data produk pada Lahzadi.</p>
{% else %}
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Stock</th>
        <th>Size</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini
    {% endcomment %}
    {% for product_entry in product_entries %}
    <tr>
        <td>{{product_entry.name}}</td>
        <td>{{product_entry.price}}</td>
        <td>{{product_entry.description}}</td>
        <td>{{product_entry.stock}}</td>
        <td>{{product_entry.size}}</td>
    </tr>
    {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product_entry' %}">
    <button>Add New Product Entry</button>
</a>
{% endblock content %}
```
14. Membuat show_xml, show_json, show_xml_by_id, dan show_json_by_id di views.py untuk mengembalikan hasil response:
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
15. Melakukan routing di urls.py di direktori main:
```
from django.urls import path
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

### Mengakses Menggunakan Postman
## XML
![XML](https://github.com/user-attachments/assets/68c722b5-03e7-488e-b2e0-b4eb19f41507)
## JSON
![JSON](https://github.com/user-attachments/assets/544f1ce5-fd06-4242-930d-830621e52e8b)
## XML by id
![XML by id](https://github.com/user-attachments/assets/fd8d2f2c-235d-41f2-a84e-903e5765890a)
## JSON by id
![JSON by id](https://github.com/user-attachments/assets/5a3601e5-7ac9-472f-9dd0-02bda01388ab)

</details>

<details>
<Summary><b>Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django</b></Summary>

### Apa perbedaan antara HttpResponseRedirect() dan redirect()?
Secara umum, HttpResponseRedirect() dan redirect() memiliki fungsi dalam mengalihkan ke URL tertentu. Perbedaan di antara keduanya adalah:
* HttpResponseRedirect(): memerlukan URL yang jelas dan lengkap (full URL atau relative path).
* redirect(): menerima URL, nama view, atau objek model, sehingga lebih fleksibel dan lebih mudah digunakan.

### Jelaskan cara kerja penghubungan model Product dengan User!
Model Product dihubungkan dengan User menggunakan <b>ForeignKey</b>, yang dapat menghubungkan setiap objek Product dengan satu pengguna. 
```
from django.db import models
import uuid
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    size = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
Pada ForeignKey, on_delete=models.CASCADE memastikan bahwa jika pengguna dihapus, semua produk yang dimiliki pengguna tersebut juga akan dihapus. Satu User bisa memiliki lebih dari satu produk, sementara setiap Product hanya dapat dimiliki oleh satu User.

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
* Authentication merupakan proses untuk mengenali atau memverifikasi identitas pengguna.
* Authorization merupakan proses untuk menentukan aksesabilitas pengguna berdasarkan peran yang dimiliki. 

Dalam konteks login, kedua proses tersebut diperlukan karena saling melengkapi dan memiliki fungsinya masing-masing. Di Django, proses authentication dilakukan dengan memanfaatkan sistem autentikasi bawaan (django.contrib.auth) yang menyediakan fungsi seperti authenticate(), login(), dan logout(). Sedangkan, authorization dilakukan dengan sistem Permissions dan Groups, menggunakan dekorator seperti @permission_required dan mendefinisikan izin pada model.

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login menggunakan session. Setelah pengguna berhasil login, session ID akan disimpan di cookie di dalam browser pengguna. Dalam cookie, Django hanya menyimpan session ID dan tidak menyimpan informasi seperti password. Data session disimpan di server. Fungsi lain dari cookie yaitu untuk menyimpan preferensi pengguna dan melacak perilaku pengguna. Dari semua kelebihan yang ada, cookie memiliki kekurangan yang perlu diperhatikan. Jika tidak dikelola dengan baik, cookie menjadi rentan terhadap serangan seperti XSS atau CSRF. Untuk meningkatkan keamanan, sangat perlu untuk memanfaatkan fitur seperti HttpOnly untuk mencegah akses JavaScript ke cookie, Secure untuk memastikan cookie dikirim melalui HTTPS, dan SameSite untuk membatasi pengiriman cookie antarsitus.

### Implementasi _checklist_
#### Implementasi fungsi registrasi, login, dan logout.

1. Pertama, saya mengimpor modul yang diperlukan dalam pembuatan fungsi dan form registrasi di dalam berkas `views.py` di direktori `main`. Dua modul yang saya impor yaitu `messages`untuk menampilkan pesan sukses dan `UserCreationForm` sebagai form dalam registrasi akun. 

```
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

2. Selanjutnya, saya membuat berkas `register.html` di dalam direktori `main/templates/` dengan isi kode berikut:
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
    <h1>Register</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input type="submit" name="submit" value="Daftar" /></td>
            </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
</div>

{% endblock content %}
```

Kode ini digunakan untuk menampilkan halaman registrasi menggunakan form yang dirender menggunakan `form.as_table`.

3. Setelah membuat fungsi registrasi, saya membuat fungsi login. Di dalam berkas `views.py`, saya melakukan impor modul-modul yang diperlukan di dalam fungsi login yaitu `AuthenticationForm`, `authenticate`, dan `login`. Kemudian, saya menambahkan fungsi berikut (fungsi `login_user`) di dalam berkas yang sama:
```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

4. Saya membuat fungsi login, saya membuat halaman untuk menampilkan fungsi login tersebut dengan membuat berkas `login.html` di dalam direktori `main/templates/` berisi kode berikut:
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login" /></td>
            </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %} Don't have an account yet?
    <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```

5. Untuk membuat fungsi `logout`, saya melakukan impor modul-modul yang diperlukan di dalam fungsi `logout` yaitu `logout` di berkas `views.py`. Di dalam berkas yang sama, saya membuat fungsi `logout` seperti di kode berikut:
```
from django.contrib.auth import logout
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

6. Saya menambahkan button `logout` di berkas `main.html` di direktori `main/templates/`

```
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```

7. Terakhir, saya melakukan routing url untuk fungsi `registrasi`, `login`, dan `logout` dengan menambahkan kode berikut di dalam berkas `urls.py` di direktori `main`:
```
urlpatterns = [
    ...
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```

#### Implementasi pembuatan dua akun dan masing-masing tiga _dummy_ data
1. Pertama, saya menjalankan perintah `python manage.py runserver` di terminal.
2. Saya membuka `http://localhost:8000/` di browser
3. Saya melakukan registrasi untuk dua akun.
4. Di tiap akun-nya, saya memasukan tiga data

#### Implementasi menghubungkan model `Product` dengan `User`
1. Saya mengimpor modul `User` di berkas `models.py` yang ada di direktori `main` dengan menambahkan kode berikut:
```
from django.contrib.auth.models import User
```

2. Di dalam berkas yang sama, saya menambahkan ForeignKey di class `Product` dengan menambahkan kode berikut:
```
class Product(models.Model):
    ...
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

3. Di berkas `views.py` di direktori `main`, saya mengubah fungsi `create_product_entry` menjadi sebagai berikut:
```
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
Pada kode ini, objek yang sudah dibuat melalui form tidak langsung disimpan di database. Sehingga, kita dapat mengubah/memodifikasi objek tersebut sebelum disimpan di database.

4. Masih di berkas yang sama, saya mengubah nilai dari `product_entries` dan `context` yang ada di fungsi `show_main` menjadi:
```
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        ...
    }

    return render(request, "main.html", context)
```

5. Selanjutnya, saya melakukan migrasi
```
python manage.py makemigrations
python manage.py migrate
```

6. Terakhir, di berkas `settings.py` di subdirektori `lahzadi`, saya mengubah variabel `DEBUG` dan melakukan impor seperti berikut:
```
import os
...
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
...
```

#### Implementasi tampilan detail informasi pengguna yang sedang logged in dan cookies
1. Di berkas `views.py` yang ada di direktori `main`, saya melakukan impor dan menambahkan kode di fungsi `login_user` pada blok `form.is_valid()` sehingga menjadi seperti berikut:
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
...
def login_user(request):
   ...
      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   ...
...
```

2. Kemudian, di fungsi `show_main`, saya menambahkan kode berikut di dalam `context` :
```
context = {
...
        ...
        'last_login': request.COOKIES['last_login'],
    }
...
```

3. Di fungsi `logout_user`, saya memodifikasi kode menjadi seperti kode berikut:
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

4. Selanjutnya, di akhir berkas `main.html`, saya menambahkan kode berikut untuk menampilkan data login terakhir:
```
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
```
</details>

<details>
<Summary><b>Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS</b></Summary>

### Urutan prioritas _CSS Selector_ pada HTML
Secara garis besar, CSS Selector terbagi atas 4 bagian. Jika diurutkan dari prioritas tertinggi, maka:

1. Inline Styles
Inline style terdapat pada elemen HTML dengan tanda style=“…”. Contohnya `<p style=“color:red;”>Contoh</p>`

2. ID Selector (#)
ID Selector ditandai dengan adanya tanda #. ID selector ini memiliki prioritas yang lebih tinggi dari class atau elemen. Contoh:
```
#option{
    color: red;
}
```

3. Class Selector (.)
Class selector ditandai dengan adanya tanda (.). ID selector ini memiliki prioritas yang lebih tinggi dari tag HTML. Contoh:
```
.option{
    color: red;
}
```

4. Tag Selector
ID Selector ini memiliki urutan terrendah. Ditandai dengan penggunaan elemen tag HTML. Contoh:
```
p, h2{
    color: red;
}
```

5. Important Rule
Ditandai dengan adanya tanda `!important`. Dapat mendahulukan urutan prioritas suatu properti tanpa memperhatikan urutan ID Selector di atas.

### _Responsive Design_ dalam pengembangan web
_Responsive design_ sangat penting untuk diperhatikan karena pengaksesan suatu website oleh pengguna tidak hanya melalui _desktop_, namun juga dapat melalui device-device lain seperti _smartphone_, tablet, dan lain sebagainya. Dengan adanya _responsive design_, pengguna dapat menggunakan _website_ dengan tampilan yang konsisten dan dapat mendapatkan pengalaman yang baik dalam menjalankan _website_ tersebut. 

Contoh aplikasi yang sudah menerapkan responsive design adalah <b>Pinterest</b> dan aplikasi yang belum menerapkan responsive design adalah <b>SIAKNG</b>.

### Perbedaan antara margin, border, dan padding, serta pengaplikasiannya
* Margin adalah ruang kosong di luar elemen yang berfungsi sebagai pemisah antarelemen.
* Border adalah garis pembatas yang mengelilingi elemen, terletak di antara margin dan padding.
* Padding adalah ruang kosong di dalam elemen, terletak di antara elemen dan border.
```
.box{
    border: 10px;
    padding: 15px;
    margin: 20px;
}
```
![margin-padding-border](https://github.com/user-attachments/assets/f797dd18-788b-44d5-97e1-7b45520386fc)
sumber: https://www.pluralsight.com/blog/creative-professional/whats-difference-margin-padding

### Konsep flex box dan grid layout di CSS

* Flex box (flexible box) adalah salah satu model layout yang dimiliki CSS. Model layout ini mengatur letak elemen dalam satu dimensi (secara horizontal/kolom atau vertikal/baris). Kegunaan dari flex box adalah elemen-elemen dapat menyesuaikan ukurannya sesuai dengan batas ruang yang diberikan.

```
.container{
    display: flex;
    justify-content: space-around;
}
```

* CSS grid adalah model layout CSS yang mengatur letak elemen dalam dua dimensi (horizontal/kolom atau vertikal/baris). Kegunaan dari CSS grid yaitu dapat membuat tata letak yang responsif dan kompleks dengan mudah.
```
.grid-container {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    grid-template-rows: auto;
    }
```

### Implementasi _checklist_
#### Menambahkan fitur _edit product_
1. Pertama, saya menyambungkan tailwind ke aplikasi saya dengan menambahkan kode berikut di bagian head berkas `base.html` di direktori templates.
```
<script src="https://cdn.tailwindcss.com">
</script>
```

2. Di berkas `views.py`, saya menambahkan fungsi berikut:
```
def edit_product(request, id):
    mood = Product.objects.get(pk = id)
    form = ProductForm(request.POST or None, instance=mood)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```

3. Saya membuat berkas baru bernama `edit_product.html` di subdirektori `main/templates`. Kemudian, saya mengisi berkas tersebut dengan kode berikut:
```
{% extends 'base.html' %}

{% load static %}

{% block content %}

<h1>Edit Mood</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Mood"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

4. Selanjutnya, di berkas `main.html`, saya menambahkan kode berikut untuk memunculkan tombol edit:
```
    <td>
        <a href="{% url 'main:edit_product' product_entry.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
```

5. Menambahkan import reverse di `views.py`
6. Melakukan routing url di `urls.py` dan menambahkan import `edit_product`.
7. Menambahkan path berikut ke `urlpatterns`:
```
...
path('edit-product/<uuid:id>', edit_product, name='edit_product'),
```

#### Menambahkan fitur _delete product_
1. Di berkas `views.py`, saya membuat _function_ baru bernama `delete_product` yang berisi kode berikut:
```
def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```

2. Selanjutnya, saya melakukan routing url di `urls.py` dengan meng-import `delete_product` dan menambahkan path berikut di `urlspattern`:
```
...
    path('delete/<uuid:id>', delete_product, name='delete_product'),
```

3. Di berkas `main.html`, saya menambahkan kode berikut untuk memunculkan button delete di tampilan halaman:
```
    <td>
        <a href="{% url 'main:delete_product' product_entry.pk %}">
            <button>
                Delete
            </button>
        </a>
    </td>
```

#### Kustomisasi desain pada template HTML menggunakan Tailwind
#####  Kustomisasi halaman login, register, dan tambah product
1. Pertama, saya membuat direktori baru di root directory yaitu direktori `static/css` dan membuat berkas `global.css` di dalamnya.

2. Kemudian, saya menghubungakan `global.css` dan script _Tailwind_ ke `base.html` dengan mengubah isi berkas `base.html` seperti berikut:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
  </head>
  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```

Berkas login, register, dan tambah product:
* [Login](main/templates/login.html).
* [Register](main/templates/register.html).
* [Add Product](main/templates/create_product.html).

#### Membuat Navigation Bar
Saya membuat berkas bernama `navbar.html` di direktori `templates/`. Berkas dari navbar terdapat di halaman [ini](templates/navbar.html)

#### Membuat daftar produk dan card produk
Saya membuat berkas bernama `card_product.html` di direktori `main/templates/`. Berkas dari card product terdapat di halaman [ini](main/templates/create_product.html)
</details>
