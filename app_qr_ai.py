import streamlit as st
import requests

# Mengatur tampilan halaman web
st.set_page_config(page_title="Advanced AI QR Generator", layout="centered")

st.title("Pembuat QR Code AI (Advanced)")
st.write("Ubah tautan (URL) menjadi QR Code artistik berkualitas tinggi dengan parameter AI lengkap.")

# ---------------------------------------------------------
# 1. BAGIAN INPUT DATA (UI)
# ---------------------------------------------------------
st.subheader("1. Masukkan Target URL")
target_url = st.text_input(
    "URL/Tautan Tujuan", 
    placeholder="Contoh: https://qrcode-ai.com"
)

st.subheader("2. Pengaturan Visual AI")
# Input Prompt Utama
prompt_text = st.text_area(
    "Prompt (Deskripsi Visual)", 
    value="futuristic city with neon lights, cyberpunk aesthetic, highly detailed"
)

# Input Negative Prompt
negative_prompt = st.text_input(
    "Negative Prompt (Hal yang ingin dihindari AI)", 
    value="blurry, low quality, distorted, ugly, deformed"
)

# Pengaturan tambahan menggunakan layout kolom
col1, col2 = st.columns(2)
with col1:
    style_name = st.text_input("Style Name", value="style_2")
with col2:
    seed_number = st.number_input("Seed (Angka Konsistensi)", value=42, step=1)

# ---------------------------------------------------------
# 3. PROSES EKSEKUSI (BACKEND)
# ---------------------------------------------------------
st.subheader("3. Proses Generate")
if st.button("Generate QR Code"):
    if target_url and prompt_text:
        st.info("Mengirim instruksi ke server AI... (Tunggu sebentar)")
        
        API_URL = 'https://odin.qrcode-ai.com/api/qrcode'
        headers = {
            'x-api-key': 'qrc_xYWerAz0o3kxyEnuMeSC1784983849516',
            'Content-Type': 'application/json'
        }
        
        # MENGGUNAKAN FORMAT JSON LENGKAP
        payload = {
            "to": target_url,
            "type": "url",
            "config": {
                "prompt": prompt_text,
                "style_name": style_name,
                "negative_prompt": negative_prompt,
                "seed": seed_number
            }
        }
        
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                
                # Mengambil URL gambar dari struktur respons API
                hasil_qr_url = data['qrcode']['url']
                width = data['qrcode']['width']
                height = data['qrcode']['height']
                
                # Menampilkan hasil gambar dan informasi resolusi
                st.image(hasil_qr_url, caption=f"Hasil QR Code (Resolusi: {width}x{height} px)")
                st.success("Berhasil! QR Code artistik siap di-scan.")
            else:
                st.error(f"Gagal memproses. Kode Error: {response.status_code}. Pesan: {response.text}")
                
        except Exception as e:
            st.error(f"Terjadi kesalahan koneksi ke server: {e}")
            
    else:
        st.warning("Mohon isi URL Tujuan dan Prompt terlebih dahulu!")
