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

def display_menu():
    print("Pilih opsi:")
    print("1. Cek Koneksi Internet")
    print("2. Keluar")

def main():
    print_welcome_message()  # Tampilkan pesan selamat datang
    
    while True:
        display_menu()  # Tampilkan menu pilihan
        choice = input("Masukkan pilihan (1/2): ").strip()

        if choice == '1':
            if check_internet_connection():
                print("Koneksi internet tersedia.")
            else:
                print("Koneksi internet tidak tersedia.")
        elif choice == '2':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
        
        # Tunggu 1 detik sebelum menampilkan menu lagi
        time.sleep(1)

if __name__ == "__main__":
    main()
