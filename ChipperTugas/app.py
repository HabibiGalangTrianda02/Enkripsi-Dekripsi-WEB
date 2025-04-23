# Import library dari Flask
from flask import Flask, render_template, request

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Fungsi untuk mengenkripsi teks menggunakan Caesar Cipher
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Hanya mengenkripsi huruf alfabet
            shift_base = 65 if char.isupper() else 97  # Tentukan basis ASCII (65 untuk 'A', 97 untuk 'a')
            # Geser karakter sesuai nilai shift dan pastikan tetap dalam rentang alfabet
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # Jika bukan huruf, langsung tambahkan tanpa perubahan
            result += char
    return result

# Fungsi untuk mendekripsi teks Caesar Cipher
def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Hanya mendekripsi huruf alfabet
            shift_base = 65 if char.isupper() else 97
            # Geser karakter ke kiri untuk dekripsi
            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char
    return result

# Route utama untuk menampilkan halaman dan memproses input
@app.route('/', methods=['GET', 'POST'])
def index():
    plaintext = ''     # Teks asli
    ciphertext = ''    # Teks hasil enkripsi
    mode = 'encrypt'   # Mode default: enkripsi
    shift = 3          # Nilai pergeseran default

    if request.method == 'POST':  # Jika user mengirim form (POST)
        text = request.form['text']        # Ambil teks dari input form
        mode = request.form['mode']        # Ambil mode (encrypt/decrypt) dari radio button
        shift = int(request.form.get('shift', 3))  # Ambil nilai shift dari input, default 3

        if mode == 'encrypt':
            plaintext = text
            ciphertext = encrypt(text, shift)  # Enkripsi teks
        elif mode == 'decrypt':
            ciphertext = text
            plaintext = decrypt(text, shift)  # Dekripsi teks

    # Render file HTML (index.html) dengan data yang sudah diproses
    return render_template('index.html', plaintext=plaintext, ciphertext=ciphertext, mode=mode, shift=shift)

# Menjalankan server Flask hanya jika file ini dijalankan langsung
if __name__ == '__main__':
    app.run(debug=True)  # Aktifkan debug mode agar error lebih informatif
