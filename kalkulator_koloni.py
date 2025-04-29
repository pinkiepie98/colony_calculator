import streamlit as st
st.title("🧫 Welcome to Colony Calculator")
st.markdown("Selamat datang di aplikasi Kalkulator Koloni Bakteri.")

menu = st.sidebar.selectbox("Pilih Menu", ["Beranda", "Informasi Koloni Bakteri", "Tentang Kami"])

if menu == "Beranda":
    st.header("💡 Kalkulator Koloni")
    st.markdown("""
        Aplikasi ini digunakan untuk menghitung jumlah koloni bakteri berdasarkan data jumlah koloni, 
        volume inokulasi, dan faktor pengenceran. Masukkan nilai-nilai pada form yang tersedia untuk memulai perhitungan.
    """)

elif menu == "Informasi Koloni Bakteri":
    st.header("🔬 Informasi Koloni Bakteri")
    st.markdown("""
        Koloni bakteri adalah kelompok sel bakteri yang berkembang biak dari satu sel bakteri induk di atas media padat. 
        Koloni digunakan untuk memperkirakan jumlah mikroorganisme dalam sampel. 
        Ini penting dalam kontrol kualitas makanan, air, dan produk lainnya.
    """)


elif menu == "Tentang Kami":
    st.header("📘 Tentang Kami")
    st.markdown("""
        Aplikasi ini dikembangkan sebagai alat bantu pembelajaran dan praktikum dalam mikrobiologi, 
        khususnya untuk analisis jumlah koloni bakteri. Dirancang dengan antarmuka yang sederhana dan mudah digunakan.
    """)
````


st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        color: #4CAF50;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🧫 Kalkulator Koloni Bakteri</h1>', unsafe_allow_html=True)

st.write("Aplikasi sederhana untuk menghitung jumlah koloni bakteri per mL sampel berdasarkan jumlah koloni, faktor pengenceran, dan volume inokulasi.")

Input user
jumlah_koloni = st.number_input("Masukkan jumlah koloni:", min_value=0, step=1)
faktor_pengenceran = st.number_input("Masukkan faktor pengenceran:", min_value=1, step=1)
volume_inokulasi = st.number_input("Masukkan volume inokulasi (dalam mL):", min_value=0.01, step=0.01)

Tombol Hitung
if st.button("Hitung Koloni"):
    if volume_inokulasi > 0:
        hasil = jumlah_koloni / (faktor_pengenceran * volume_inokulasi)
        st.success(f"Hasil perhitungan: {hasil:.2f} CFU/mL")
    else:st.error("Volume inokulasi tidak boleh nol!")

st.markdown('</div>', unsafe_allow_html=True)

