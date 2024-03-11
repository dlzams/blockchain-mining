import socket
import pickle
import threading
from block import Block, Blockchain

# Inisialisasi semaphore untuk 20 klien
client_semaphore = threading.Semaphore(20)

# Fungsi untuk menangani koneksi klien
def handle_client(conn, blockchain):
    # Menerima data dari klien
    received_data = conn.recv(4096)
    # Jika klien meminta blok
    if received_data == b"request_block":
        print("Klien meminta blok...")
        # Membuat blok baru dan mengirimkannya ke klien
        new_block = Block("Data transaksi", blockchain.chain[-1].hash)
        conn.send(pickle.dumps(new_block))
        # Menerima blok yang telah di-mine dari klien
        mined_block = pickle.loads(conn.recv(4096))
        print(f"Blok yang telah di-mine: Nonce: {mined_block.nonce} Bukti: {mined_block.hash}")
        # Menambahkan blok yang telah di-mine ke blockchain
        blockchain.chain.append(mined_block)
    # Jika klien meminta blockchain
    if received_data == b"request_blockchain":
        print("Klien meminta blockchain...")
        # Mengirimkan blockchain ke klien
        conn.send(pickle.dumps(blockchain))
    # Menutup koneksi dengan klien
    conn.close()
    # Melepaskan semaphore
    client_semaphore.release()

# Fungsi untuk memulai server blockchain
def start_blockchain_server():
    # Membuat objek blockchain
    blockchain = Blockchain()

    # Membuat socket server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Mengikat server ke ip local pada port 25565
    server.bind(('localhost', 25565))
    # Server mulai mendengarkan koneksi masuk
    server.listen(5)

    print("Server Pembuat Blok sedang berjalan...")

    # Loop utama server
    while True:
        # Mendapatkan semaphore
        client_semaphore.acquire()
        # Menerima koneksi dari klien
        conn, addr = server.accept()
        print(f"Koneksi dari {addr}")

        # Memulai thread baru untuk menangani klien
        client_thread = threading.Thread(target=handle_client, args=(conn, blockchain))
        client_thread.start()

# Bagian utama dari program
if __name__ == "__main__":
    # Memulai server blockchain
    start_blockchain_server()