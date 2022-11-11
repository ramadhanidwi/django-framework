# Aplikasi Database Warga

## Description 
Aplikasi ini dirancang dengan tujuan untuk mempermudah pendataan masyarakat sekitar agar lebih tertata dan terpantau dengan baik. Adapun beberapa hal yang perlu di install terlebih dahulu, yaitu: 
- Python 3.9.2 atau yang terbaru 
- Django 4.1.3

## Tahapan sebelum menjalankan aplikasi: 
1. Download repository ini 
2. Install library yang akan digunakan 
- Pillow 
 ```bash
 pip install pillow
 ```
- Django export-import
  ```bash
  pip install django-import-export
  ```
3. Masuk pada folder aplikasi 
4. Lakukan export database
  Database yang digunakan adalah SQLite
  ```bash
  python manage.py makemigrations
  python manage.py 
  ```
5. Jalankan server
  ```bash
  python manage.py runserver
  ```
