# Input nama dan NIM
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")

# Konkatenasi nama dan NIM
data = nama + nim

def encrypt_ecb(plaintext_hex, key_bin):
    # Step 3: Rubah plainteks hexadecimal ke biner
    plaintext_bin = bin(int(plaintext_hex, 16))[2:]
    
    # Step 4: Pisah per blok 4 bit sesuai panjang blok
    block_size = 4
    plaintext_blocks = [plaintext_bin[i:i+block_size] for i in range(0, len(plaintext_bin), block_size)]

    # Step 5: XOR-kan biner plainteks per blok dengan kunci
    encrypted_blocks = []
    for block in plaintext_blocks:
        xor_result = bin(int(block, 2) ^ int(key_bin, 2))[2:].zfill(block_size)

        # Step 6: Geser tiap blok 1 bit ke kiri
        shifted_result = xor_result[1:] + xor_result[0]

        # Step 7: Hasil XOR konversi ke hexadecimal
        encrypted_blocks.append(hex(int(shifted_result, 2))[2:].upper())

    return encrypted_blocks

# Input plainteks dan kunci
plaintext_hex = input("Masukkan plainteks: ").upper()
key_bin = input("Masukkan kunci: ")

# Enkripsi ECB
result = encrypt_ecb(plaintext_hex, key_bin)

# Output hasil enkripsi
print("Hasil enkripsi ECB:", result)
