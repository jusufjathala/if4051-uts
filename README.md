# IF4051 Pengembangan Sistem IoT  
Dibuat oleh 13519174 - Jusuf Junior Athala   
Program perangkat aplikasi IoT yang dapat menyalakan / mematikan lampu LED melalui broker online di HiveMQ serta menunjukkan keadaan lampu LED.
# Program menggunakan Python dan Flask dan membutuhkan library paho-mqtt 

Cara menggunakan program:  
Pada directory folder tugas, gunakan perintah command console berikut :  
1. pip install virtualenv
2. py -m venv env
3. .\env\Scripts\activate
4. pip install Flask
5. pip install paho-mqtt
6. flask run
7. masukkan file boot.py dan main.py yang ada di folder esp32 kedalam perangkat esp32
8. ubah pengaturan koneksi Wi-Fi pada boot.py
9. jalankan ESP32
  
Kemudian buka internet browser dan buka link: localhost:5000  
