import streamlit as st
import requests

# Mengatur tampilan halaman web
st.set_page_config(page_title="Artistic QR Generator", layout="centered")

st.title("Pembuat QR Code Artistik (AI)")
st.write("Ubah tautan (URL) menjadi QR Code karya seni menggunakan AI secara otomatis!")

# Mengatur layout input di web
st.subheader("1. Masukkan Data")
# Karena API langsung meminta URL tujuan, kita ganti tombol upload dengan input teks
target_url = st.text_input(
    "Masukkan URL/Tautan Tujuan", 
    placeholder="Contoh: https://google.com"
)

prompt = st.text_area(
    "Masukkan Deskripsi Visual (Prompt)", 
    placeholder="Contoh: futuristic city with neon lights"
)

# Tombol untuk memulai proses
st.subheader("2. Proses AI")
if st.button("Generate QR Code"):
    # Pengecekan apakah URL dan prompt sudah diisi
    if target_url and prompt:
        st.info("Memproses ke server AI... (Tunggu sebentar ya)")

        # ---------------------------------------------------------
        # BAGIAN INTEGRASI API AI (Menggunakan kode aslimu)
        # ---------------------------------------------------------
        
        API_URL = 'https://odin.qrcode-ai.com/api/qrcode'
        
        # Header menggunakan format dari kodemu ('x-api-key')
        headers = {
            'x-api-key': 'qrc_xYWerAz0o3kxyEnuMeSC1784983849516',
            'Content-Type': 'application/json'
        }
        
        # Payload (data json) yang dikirim ke server AI
        payload = {
            'to': target_url,
            'type': 'url',
            'config': {
                'prompt': prompt,
                'style_name': 'style_2'
            }
        }
        
        try:
            # Mengirim request menggunakan format JSON
            response = requests.post(API_URL, headers=headers, json=payload)
            
            # Jika berhasil (Kode 200)
            if response.status_code == 200:
                # Mengambil data balasan dari server dalam bentuk JSON
                data = response.json()
                
                # Mengambil URL gambar hasil sesuai kodemu
                hasil_qr_url = data['qrcode']['url']
                
                # Menampilkan gambar langsung dari URL yang diberikan API
                st.image(hasil_qr_url, caption="Hasil QR Code Artistik!")
                st.success("Yey, proses selesai!")
            else:
                st.error(f"Gagal memproses. Kode Error: {response.status_code}. Pesan: {response.text}")
                
        except Exception as e:
            st.error(f"Terjadi kesalahan koneksi ke internet atau server: {e}")
            
    else:
        st.warning("Mohon isi URL Tujuan dan Deskripsi Visual (Prompt) terlebih dahulu!")
