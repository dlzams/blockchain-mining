import hashlib
import threading
import time
class Block:
    def __init__(self, data, previous_hash): 
        #inisialisasi atribut block
        self.data = data 
        self.previous_hash = previous_hash 
        self.nonce = 0
        self.difficulty = 6
        self.timestamp = time.time()
        self.hash = self.calculate_hash() 
        
  
    def calculate_hash(self): 
        #Menghitung hash dari data blok
        sha = hashlib.sha256() 
        sha.update(str(self.data).encode('utf-8') + 
                   str(self.previous_hash).encode('utf-8') +
                   str(self.difficulty).encode('utf-8') + 
                   str(self.timestamp).encode('utf-8') +
                   str(self.nonce).encode('utf-8')) 
        return sha.hexdigest() 

class Blockchain: 
    def __init__(self): 
        #inisialisasi blockchain dengan membuat block genesis
        self.chain = [self.create_genesis_block()]
  
    def create_genesis_block(self): 
        #Membuat blok genesis (blok pertama)
        return Block("Genesis Block", "0") 

class Miner:
    def mine_block(self, block):
        # Mendefinisikan fungsi print_nonce
        def print_nonce():
            # Melakukan loop selama blok belum ditambang
            while not self.mined:
                # Mencetak nilai nonce saat ini
                print("\rNonce:", block.nonce, end="")
                # Menunggu 0.2 detik sebelum mencetak lagi
                time.sleep(0.2)

        # Mencetak pesan bahwa proses penambangan blok dimulai
        print("Mining block...")
        # Mengatur status mined menjadi False
        self.mined = False
        # Memulai thread baru untuk menjalankan fungsi print_nonce
        threading.Thread(target=print_nonce).start()

        # Melakukan loop selama hash blok tidak sama dengan string "0" sebanyak difficulty
        while block.hash[:block.difficulty] != "0" * block.difficulty:
            # Meningkatkan nilai nonce
            block.nonce += 1
            # Menghitung hash baru untuk blok
            block.hash = block.calculate_hash()

        # Mengatur status mined menjadi True setelah blok berhasil ditambang
        self.mined = True
        # Mencetak nilai nonce akhir
        print("\rNonce:", block.nonce)
        # Mencetak pesan bahwa blok berhasil ditambang, beserta nilai nonce dan hash-nya
        print("Block mined:", "Nonce:", block.nonce, "Hash:", block.hash)
        # Mengembalikan blok yang telah ditambang
        return block
