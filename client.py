import hashlib
import socket
import pickle
from block import Block, Miner
import os

# Fungsi untuk memulai penambangan
def start_mining(server_address, server_port):
    # Membuat objek Miner
    miner = Miner()
    # Membuat objek socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Menghubungkan client ke server dengan alamat dan port yang ditentukan
    client.connect((server_address, server_port))

    # Mengirim permintaan blok ke server
    client.send(b"request_block")
    received_data = client.recv(4096)
    if received_data:
        # Menerima blok dari server dan mulai mining
        rblock = pickle.loads(received_data)
        mined_block = miner.mine_block(rblock)
        # Mengirim blok yang telah di-mine ke server
        client.send(pickle.dumps(mined_block))
        client.close()
        temp = input("Press enter to continue...")

# Fungsi untuk meminta blockchain dari server
def request_blockchain(server_address, server_port):
    # Membuat objek socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Menghubungkan ke server
    client.connect((server_address, server_port))

    # Mengirim permintaan blockchain ke server
    client.send(b"request_blockchain")
    received_data = client.recv(4096)
    if received_data:
        # Menerima blockchain dari server
        blockchain = pickle.loads(received_data)
        # Menutup koneksi dengan server
        client.close()
        # Mencetak setiap blok dalam blockchain
        for block in blockchain.chain:
            print(f"Data Blok: {block.data} | Nonce: {block.nonce} | Hash: {block.hash}") #block.hash, block.nonce, block.previous_hash, block.data
        _ = input("Press enter to continue...")

# Fungsi untuk menampilkan menu
def display_menu():
    print("1. Start Mining")  # Menampilkan pilihan untuk mulai menambang
    print("2. Request Blockchain")  # Menampilkan pilihan untuk meminta blockchain
    print("3. Keluar")  # Menampilkan pilihan untuk keluar

# Fungsi untuk menangani pilihan pengguna
def handle_choice(choice, server_address, server_port):
    if choice == '1':  # Jika pengguna memilih 1
        start_mining(server_address, server_port)  # Mulai menambang
    elif choice == '2':  # Jika pengguna memilih 2
        request_blockchain(server_address, server_port)  # Meminta blockchain
    elif choice == '3':  # Jika pengguna memilih 3
        exit()  # Keluar dari program
    else:  # Jika pengguna memilih selain 1, 2, atau 3
        print("Pilihan tidak valid. Silakan pilih opsi yang valid.")  # Menampilkan pesan kesalahan

# Jika script ini dijalankan sebagai program utama
if __name__ == "__main__":
    server_address = 'localhost'  # Menentukan alamat server
    server_port = 25565  # Menentukan port server

    while True:  # Loop selamanya
        os.system('cls' if os.name == 'nt' else 'clear')  # Membersihkan layar
        display_menu()  # Menampilkan menu
        choice = input("Masukkan pilihan Anda: ")  # Meminta pengguna untuk memasukkan pilihan
        handle_choice(choice, server_address, server_port)  # Menangani pilihan pengguna