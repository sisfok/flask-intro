## Tutorial Dasar Flask

Repo ini untuk belajar bersama Flask, pelajaran ini termasuk CRUD sederhana.
Menggunakan **SQLite3**, jadi install terlebih dahulu.

### Cara menggunakan

```bash
pip install virtualenv
virtualenv env
source env/bin/activate

pip install -r requirements.txt
python app.py
```

Kemudian untuk membuat database (jika `main.db` masih kosong):

```bash
python
```

yang akan membuka interpreter Python.

Kemudian masukkan:

```pyhton
from app import db
db.create_all()
```

Perintah ini akan membuat database pada `main.db`.

Selamat belajar