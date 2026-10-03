# Nama : M. Heri Setiawan
# NIM  : 242502040087


def normalize_key(key):
    key = ''.join(char.lower() for char in key if char.isalpha())
    if not key:
        raise ValueError('Key harus berisi minimal satu huruf alfabet.')
    return key


def encrypt(text, key):
    key = normalize_key(key)
    result = []
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            plain_pos = ord(char.lower()) - ord('a')
            key_pos = ord(key[key_index % len(key)]) - ord('a')
            cipher_pos = (plain_pos + key_pos) % 26
            result.append(chr(base + cipher_pos))
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)


def decrypt(text, key):
    key = normalize_key(key)
    result = []
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            cipher_pos = ord(char.lower()) - ord('a')
            key_pos = ord(key[key_index % len(key)]) - ord('a')
            plain_pos = (cipher_pos - key_pos) % 26
            result.append(chr(base + plain_pos))
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)


print('=== VIGENERE CIPHER ===')
print('1. Encrypt')
print('2. Decrypt')

pilihan = input('Pilih: ')
text = input('Masukkan teks: ')
key = input('Masukkan key: ')

try:
    if pilihan == '1':
        hasil = encrypt(text, key)
        print('\nHasil Encryption:')
        print(hasil)
    elif pilihan == '2':
        hasil = decrypt(text, key)
        print('\nHasil Decryption:')
        print(hasil)
    else:
        print('Pilihan tidak valid.')
except ValueError as error:
    print(f'Error: {error}')