# SipQ
Project sistem informasi partai dan quickcount.

Cara setup enviroment untuk memulai development.

jalankan command - command berikut:
```Shell
mkdir sipq
cd sipq
python -m venv venv
git clone git@github.com:bokunodev/sipq .
source venv/bin/activate
pip install -r requirements.txt
```

Untuk menjalankan development server:
```Shell
hypercorn app:app -w 1 -k trio -b 127.0.0.1:8000 --reload
```
informasi lebih lanjut bisa dilihat menggunakan `hypercon --help`

Semua pulll request **HARUS** di format menggunakan [yapf](https://github.com/google/yapf)
