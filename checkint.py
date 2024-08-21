import requests
import time
from pyfiglet import Figlet

def check_internet_connection(url='http://www.google.com', timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        # Mengecek jika status code adalah 200
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        pass
    return False

def print_welcome_message():
    # Membuat objek Figlet untuk menampilkan teks besar
    figlet = Figlet(font='big')  # Pilih font 'big' atau font lain sesuai keinginan
    welcome_text = figlet.renderText('Danvertt')
    print(welcome_text)

def main():
    print_welcome_message()  # Tampilkan pesan selamat datang
    while True:
        if check_internet_connection():
            print("Koneksi internet tersedia.")
        else:
            print("Koneksi internet tidak tersedia.")
        # Tunggu 60 detik sebelum pengecekan berikutnya
        time.sleep(60)

if __name__ == "__main__":
    main()
