import streamlit as st
from PIL import Image
import requests

# Mengatur tampilan halaman web
st.set_page_config(page_title="Artistic QR Generator", layout="centered")

st.title("Pembuat QR Code Artistik (ControlNet)")
st.write("Ubah QR code dasar menjadi karya seni menggunakan Stable Diffusion!")

# Mengatur layout input di web
st.subheader("1. Masukkan Bahan Dasar")
uploaded_file = st.file_uploader("Unggah QR Code Dasar (Format: JPG/PNG)", type=["png", "jpg", "jpeg"])

prompt = st.text_area(
    "Masukkan Deskripsi Visual (Prompt)", 
    placeholder="Contoh: A lush tropical forest with waterfalls, parrots, and subtle hidden patterns..."
)

# Tombol untuk memulai proses
st.subheader("2. Proses AI")
if st.button("Generate QR Code"):
    # Pengecekan apakah data sudah lengkap
    if uploaded_file is not None and prompt:
        st.info("Memproses gambar... (Ini akan memanggil API AI)")
        
        # Menampilkan gambar QR code asli yang diunggah
        image = Image.open(uploaded_file)
        st.image(image, caption="QR Code Asli", width=250)

        # ---------------------------------------------------------
        # BAGIAN INTEGRASI API AI (BACKEND)
        # Di sinilah kamu mengirim gambar dan prompt ke mesin AI.
        # Jika menggunakan API seperti Replicate, kodenya diletakkan di sini.
        #
        # Contoh simulasi logika (pseudocode):
        # file_data = uploaded_file.getvalue()
        # response = requests.post(
        #     "URL_API_STABLE_DIFFUSION_KAMU", 
        #     data={"prompt": prompt, "image": file_data}
        # )
        # final_image = Image.open(BytesIO(response.content))
        # st.image(final_image, caption="Hasil QR Code Artistik")
        # ---------------------------------------------------------
        
        st.success("Proses selesai! (Nantinya hasil gambar AI akan muncul di sini)")
    else:
        st.warning("Mohon unggah QR Code dan masukkan prompt terlebih dahulu sebelum menekan tombol!")
