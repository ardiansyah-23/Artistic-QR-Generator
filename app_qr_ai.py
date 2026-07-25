import streamlit as st
import requests

# Mengatur tampilan halaman web
st.set_page_config(page_title="Advanced AI QR Generator", layout="centered")

st.title("Pembuat QR Code AI (Advanced)")
st.write("Ubah tautan (URL) menjadi QR Code artistik berkualitas tinggi dengan parameter AI lengkap.")

# ---------------------------------------------------------
# 1. BAGIAN INPUT DATA (UI) & PRESET GAYA DENGAN PREVIEW GAMBAR
# ---------------------------------------------------------
st.subheader("1. Pilih Preset Gaya / Tema AI")

# Menyiapkan kamus tautan gambar preview untuk setiap preset
preview_images = {
    "Mata Futuristik (Cybernetic Eye)": "https://cdn.qrcode-ai.com/qrcode/sample-eye.png", # Ganti dengan URL preview yang sesuai jika ada
    "Pemandangan Gunung Salju (Mountain Snow)": "https://cdn.qrcode-ai.com/qrcode/mountain-snow-peaks-blue-black-background-black-square-artistic-qr-code.webp",
    "Kotak 3D Gaya Minecraft (Minecraft Blocks)": "https://cdn.qrcode-ai.com/qrcode/minecraft-green-brown-black-square-3d-qr-code-art.webp",
    "Lukisan Jepang / Geisha (Japanese Geisha)": "https://cdn.qrcode-ai.com/qrcode/geisha-japanese-painting-red-blue-background-black-square-artistic-qr-code.webp",
    "Burung Berwarna-warni (Colorful Bird)": "https://cdn.qrcode-ai.com/qrcode/colorful-bird-orange-blue-background-black-square-artistic-qr-code.webp",
    "Kustom (Tulis Sendiri)": None
}

# Layout kolom: Kolom kiri untuk pilihan selectbox, kolom kanan untuk preview gambar
col_select, col_preview = st.columns([1, 1])

with col_select:
    pilihan_preset = st.selectbox(
        "Pilih Template Gaya:",
        (
            "Mata Futuristik (Cybernetic Eye)",
            "Pemandangan Gunung Salju (Mountain Snow)",
            "Kotak 3D Gaya Minecraft (Minecraft Blocks)",
            "Lukisan Jepang / Geisha (Japanese Geisha)",
            "Burung Berwarna-warni (Colorful Bird)",
            "Kustom (Tulis Sendiri)"
        )
    )

with col_preview:
    if pilihan_preset == "Mata Futuristik (Cybernetic Eye)":
        st.info("Preview: Tema Mata Cybernetic / Futuristik")
    elif pilihan_preset == "Pemandangan Gunung Salju (Mountain Snow)":
        st.image("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=200&auto=format&fit=crop&q=60", width=150, caption="Acuan: Mountain Snow")
    elif pilihan_preset == "Kotak 3D Gaya Minecraft (Minecraft Blocks)":
        st.info("Acuan: Tema Blok Voxel 3D")
    elif pilihan_preset == "Lukisan Jepang / Geisha (Japanese Geisha)":
        st.info("Acuan: Tema Ukiyo-e Geisha")
    elif pilihan_preset == "Burung Berwarna-warni (Colorful Bird)":
        st.info("Acuan: Tema Burung Tropis")
    else:
        st.write("Mode Kustom (Bebas atur prompt sendiri)")

# Mengatur nilai otomatis berdasarkan preset yang dipilih
if pilihan_preset == "Mata Futuristik (Cybernetic Eye)":
    default_prompt = "futuristic cybernetic eye with glowing neon lights, intricate mechanical details, highly detailed, sharp contrast"
    default_negative = "blurry, low quality, distorted, ugly, deformed"
elif pilihan_preset == "Pemandangan Gunung Salju (Mountain Snow)":
    default_prompt = "snowy mountain peaks, dramatic clouds, blue and white landscape, artistic QR code integration, highly detailed, sharp contrast"
    default_negative = "blurry, low quality, deformed, text, watermark"
elif pilihan_preset == "Kotak 3D Gaya Minecraft (Minecraft Blocks)":
    default_prompt = "3d voxel blocks, minecraft style landscape, green and brown nature, floating islands, detailed pixel structure, artistic QR code"
    default_negative = "blurry, low quality, flat 2d, distorted, ugly"
elif pilihan_preset == "Lukisan Jepang / Geisha (Japanese Geisha)":
    default_prompt = "traditional Japanese geisha painting, Mount Fuji background, cherry blossoms, red and blue floral pattern, ukiyo-e art style, detailed QR code"
    default_negative = "blurry, low resolution, monochrome, deformed face, low quality"
elif pilihan_preset == "Burung Berwarna-warni (Colorful Bird)":
    default_prompt = "vibrant colorful tropical bird perched on a branch, rainbow feathers, detailed plumage, glowing neon background, sharp artistic QR code"
    default_negative = "blurry, dull colors, low quality, monochrome, distorted"
else:
    default_prompt = "futuristic city with neon lights, cyberpunk aesthetic, highly detailed"
    default_negative = "blurry, low quality, distorted, ugly, deformed"

st.subheader("2. Masukkan Target URL & Parameter")
target_url = st.text_input(
    "URL/Tautan Tujuan", 
    value="https://qrcode-ai.com",
    placeholder="Contoh: https://qrcode-ai.com"
)

# Input Prompt Utama
prompt_text = st.text_area(
    "Prompt (Deskripsi Visual)", 
    value=default_prompt
)

# Input Negative Prompt
negative_prompt = st.text_input(
    "Negative Prompt (Hal yang ingin dihindari AI)", 
    value=default_negative
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
                hasil_qr_url = data['qrcode']['url']
                width = data['qrcode']['width']
                height = data['qrcode']['height']
                
                st.image(hasil_qr_url, caption=f"Hasil QR Code (Resolusi: {width}x{height} px)")
                st.success("Berhasil! QR Code artistik siap di-scan.")
            else:
                st.error(f"Gagal memproses. Kode Error: {response.status_code}. Pesan: {response.text}")
                
        except Exception as e:
            st.error(f"Terjadi kesalahan koneksi ke server: {e}")
            
    else:
        st.warning("Mohon isi URL Tujuan dan Prompt terlebih dahulu!")
