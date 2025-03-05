import os
import time
import random
import string
from datetime import datetime, timedelta

# Fungsi untuk menampilkan pesan dengan warna
def tampilkan_pesan(warna, pesan):
    """Menampilkan pesan dengan warna yang ditentukan"""
    warna_merah = "\033[91m"
    warna_normal = "\033[0m"
    
    if warna == "merah":
        print(f"{warna_merah}{pesan}{warna_normal}")
    else:
        print(pesan)

# Fungsi untuk menghasilkan kode OTP palsu
def buat_otp():
    """Membuat kode OTP palsu 6 digit"""
    otp = ''.join(random.choices(string.digits, k=6))  # 6 digit angka acak
    return otp

# Fungsi untuk menghitung waktu kadaluarsa OTP
def hitung_kadaluarsa():
    """Menghitung waktu kadaluarsa OTP (valid selama 5 menit)"""
    waktu_sekarang = datetime.now()
    waktu_kadaluarsa = waktu_sekarang + timedelta(minutes=5)
    return waktu_kadaluarsa.strftime("%H:%M:%S")

# Fungsi untuk mengirim OTP ke nomor WhatsApp menggunakan Termux API
def kirim_otp(nomor_wa, otp):
    """Mengirim OTP ke nomor WhatsApp menggunakan Termux API"""
    pesan = f"Kode OTP Anda: {otp}"
    
    try:
        # Mengirim SMS (bisa diubah menjadi pengiriman WhatsApp Web menggunakan API jika diperlukan)
        os.system(f'termux-sms-send -n +62{nomor_wa} "{pesan}"')
        print(f"Pesan: '{pesan}' telah berhasil dikirim ke +62{nomor_wa}")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengirim OTP: {e}")

# Tampilan Awal
tampilkan_pesan("merah", "BIGBOY")
time.sleep(1)  # Jeda sedikit agar tampilan lebih menarik

# Menampilkan waktu sekarang
print("Masukkan Jam dan Tanggal Sekarang:")
print(f"Hari, Tanggal, Bulan, Tahun: {datetime.now().strftime('%A, %d %B %Y')}")
print(f"Jam: {datetime.now().strftime('%H:%M:%S')}")

# Input nomor WhatsApp
nomor_wa = input("Masukkan nomor WhatsApp (tanpa +62, hanya angka): ")
while not nomor_wa.isdigit() or len(nomor_wa) < 10:  # Validasi input nomor
    print("Nomor WhatsApp tidak valid! Harap masukkan nomor yang benar (min. 10 digit).")
    nomor_wa = input("Masukkan nomor WhatsApp (tanpa +62, hanya angka): ")

# Membuat OTP Palsu
otp = buat_otp()
print(f"OTP yang dihasilkan: {otp}")

# Menghitung waktu kadaluarsa OTP
waktu_kadaluarsa = hitung_kadaluarsa()
print(f"OTP ini akan kadaluarsa pada pukul {waktu_kadaluarsa}.")

# Mengonfirmasi sebelum mengirim
konfirmasi = input(f"Apakah Anda yakin ingin mengirim OTP {otp} ke +62{nomor_wa}? (y/n): ").lower()
if konfirmasi == 'y':
    print("Mengirim OTP ke WhatsApp...")
    kirim_otp(nomor_wa, otp)
    print("OTP berhasil dikirim!")
else:
    print("Pengiriman OTP dibatalkan.")

# Simulasi waktu kadaluarsa OTP
print("\nPerhatian: OTP ini hanya berlaku untuk 5 menit. Setelah itu, OTP akan kadaluarsa.")
time.sleep(5)  # Simulasi waktu kadaluarsa
print("Waktu OTP telah kadaluarsa.")

