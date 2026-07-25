import streamlit as st
import requests

# Mengatur tampilan halaman web
st.set_page_config(page_title="Advanced AI QR Generator", layout="centered")

st.title("Pembuat QR Code AI (Advanced)")
st.write("Ubah tautan (URL) menjadi QR Code artistik berkualitas tinggi dengan parameter AI lengkap.")

# DAFTAR API KEY BARU
API_KEYS = [
    "qrc_POnzZzb_nwRiYp-OnEmB1784986994929",
    "qrc_-U_JNSOJ7lwQvyfbwLRd1784987079238",
    "qrc_Jb-bXByGEcZMyd1ZHKOs1784987303682",
]

# Inisialisasi Session State
if 'selected_preset' not in st.session_state:
    st.session_state.selected_preset = "Mata Futuristik (Cybernetic Eye)"
if 'prompt_text' not in st.session_state:
    st.session_state.prompt_text = "futuristic cybernetic eye with glowing neon lights, intricate mechanical details, highly detailed, sharp contrast"
if 'negative_prompt' not in st.session_state:
    st.session_state.negative_prompt = "blurry, low quality, distorted, ugly, deformed"

def update_preset():
    preset = st.session_state.pilihan_preset
    if preset == "Mata Futuristik (Cybernetic Eye)":
        st.session_state.prompt_text = "futuristic cybernetic eye with glowing neon lights, intricate mechanical details, highly detailed, sharp contrast"
        st.session_state.negative_prompt = "blurry, low quality, distorted, ugly, deformed"
    elif preset == "Pemandangan Gunung Salju (Mountain Snow)":
        st.session_state.prompt_text = "snowy mountain peaks, dramatic clouds, blue and white landscape, artistic QR code integration, highly detailed, sharp contrast"
        st.session_state.negative_prompt = "blurry, low quality, deformed, text, watermark"
    elif preset == "Kotak 3D Gaya Minecraft (Minecraft Blocks)":
        st.session_state.prompt_text = "3d voxel blocks, minecraft style landscape, green and brown nature, floating islands, detailed pixel structure, artistic QR code"
        st.session_state.negative_prompt = "blurry, low quality, flat 2d, distorted, ugly"
    elif preset == "Lukisan Jepang / Geisha (Japanese Geisha)":
        st.session_state.prompt_text = "traditional Japanese geisha painting, Mount Fuji background, cherry blossoms, red and blue floral pattern, ukiyo-e art style, detailed QR code"
        st.session_state.negative_prompt = "blurry, low resolution, monochrome, deformed face, low quality"
    elif preset == "Burung Berwarna-warni (Colorful Bird)":
        st.session_state.prompt_text = "vibrant colorful tropical bird perched on a branch, rainbow feathers, detailed plumage, glowing neon background, sharp artistic QR code"
        st.session_state.negative_prompt = "blurry, dull colors, low quality, monochrome, distorted"

# ---------------------------------------------------------
# 1. BAGIAN INPUT DATA (UI) & PRESET GAYA
# ---------------------------------------------------------
st.subheader("1. Pilih Preset Gaya / Tema AI")

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
        ),
        key="pilihan_preset",
        on_change=update_preset
    )

with col_preview:
    current_preset = st.session_state.pilihan_preset
    if current_preset == "Mata Futuristik (Cybernetic Eye)":
        st.image("https://raw.githubusercontent.com/ardiansyah-23/Artistic-QR-Generator/main/Mata-Futuristik-Cybernetic-Eye.png", width=200, caption="Preview: Mata Futuristik")
    elif current_preset == "Pemandangan Gunung Salju (Mountain Snow)":
        st.image("https://raw.githubusercontent.com/ardiansyah-23/Artistic-QR-Generator/main/mountain-snow-peaks-blue-black-background-black-square-artistic-qr-code.webp", width=200, caption="Preview: Mountain Snow")
    elif current_preset == "Kotak 3D Gaya Minecraft (Minecraft Blocks)":
        st.image("https://raw.githubusercontent.com/ardiansyah-23/Artistic-QR-Generator/main/minecraft-green-brown-black-square-3d-qr-code-art.webp", width=200, caption="Preview: Minecraft Blocks")
    elif current_preset == "Lukisan Jepang / Geisha (Japanese Geisha)":
        st.image("https://raw.githubusercontent.com/ardiansyah-23/Artistic-QR-Generator/main/geisha-japanese-painting-red-blue-background-black-square-artistic-qr-code.webp", width=200, caption="Preview: Japanese Geisha")
    elif current_preset == "Burung Berwarna-warni (Colorful Bird)":
        st.image("https://raw.githubusercontent.com/ardiansyah-23/Artistic-QR-Generator/main/colorful-bird-orange-blue-background-black-square-artistic-qr-code.webp", width=200, caption="Preview: Colorful Bird")
    else:
        st.info("Mode Kustom: Bebas tulis prompt kustommu sendiri di bawah.")

st.subheader("2. Masukkan Target URL & Parameter")
target_url = st.text_input(
    "URL/Tautan Tujuan", 
    value="https://qrcode-ai.com",
    placeholder="Contoh: https://qrcode-ai.com"
)

prompt_text = st.text_area("Prompt (Deskripsi Visual)", key="prompt_text")
negative_prompt = st.text_input("Negative Prompt (Hal yang ingin dihindari AI)", key="negative_prompt")

seed_number = st.number_input("Seed (Angka Konsistensi)", value=42, step=1)
style_name = "style_2"

# ---------------------------------------------------------
# 3. PROSES EKSEKUSI (BACKEND DENGAN ROTASI MULTI API KEY)
# ---------------------------------------------------------
st.subheader("3. Proses Generate")
if st.button("Generate QR Code"):
    if target_url and prompt_text:
        API_URL = 'https://odin.qrcode-ai.com/api/qrcode'
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
        
        berhasil = False
        response = None
        
        for index, key in enumerate(API_KEYS):
            st.info(f"Mencoba mengirim dengan API Key ke-{index + 1}...")
            headers = {
                'x-api-key': key,
                'Content-Type': 'application/json'
            }
            
            try:
                response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
                
                if response.status_code == 200:
                    berhasil = True
                    break
                elif response.status_code == 421:
                    continue
                else:
                    break
            except Exception as e:
                continue
        
        if berhasil and response:
            data = response.json()
            hasil_qr_url = data['qrcode']['url']
            width = data['qrcode']['width']
            height = data['qrcode']['height']
            
            st.image(hasil_qr_url, caption=f"Hasil QR Code (Resolusi: {width}x{height} px)")
            st.success("Berhasil! QR Code artistik siap di-scan.")
        else:
            if response and response.status_code == 421:
                st.error("Semua API Key yang terdaftar telah habis kuotanya (Limit 421).")
            else:
                error_msg = response.text if response else "Koneksi gagal"
                st.error(f"Gagal memproses. Pesan: {error_msg}")
    else:
        st.warning("Mohon isi URL Tujuan dan Prompt terlebih dahulu!")
