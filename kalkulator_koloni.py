
import streamlit as st

# Sidebar menu
menu = st.sidebar.radio("Pilih Menu", ["Home", "Kalkulator Total Plate Count", "Tentang Kami"])

# Tambahkan background image & style
st.markdown(f"""
    <style>
    body {{
        background-image: url("https://i.pinimg.com/736x/9d/4a/8e/9d4a8e3c2a9f2560f5febd654b189910.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        height: 100vh;
        margin: 0;
    }}
    .main {{
        background-color: rgba(255, 255, 255, 0.8);  /* Transparansi latar belakang agar teks lebih terbaca */
        padding: 20px;
        border-radius: 10px;
        margin-top: 10%;
    }}
    .title {{
        color: #4CAF50;
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

# Halaman: Home
if menu == "Home":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">🧫 Selamat Datang di Aplikasi TPC</h1>', unsafe_allow_html=True)
    st.write("Aplikasi ini membantu menghitung **Total Plate Count (TPC)** atau jumlah koloni bakteri per mL sampel cair. Gunakan menu di sebelah kiri untuk mulai.")
    st.markdown('</div>', unsafe_allow_html=True)

# Halaman: Kalkulator Total Plate Count
elif menu == "Kalkulator Total Plate Count":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">🔢 Kalkulator Total Plate Count</h1>', unsafe_allow_html=True)

    st.write("Masukkan data pengamatan laboratorium:")

    koloni_1 = st.number_input("Jumlah koloni pada cawan 1:", min_value=0, step=1)
    koloni_2 = st.number_input("Jumlah koloni pada cawan 2:", min_value=0, step=1)

    faktor_pengenceran = st.number_input("Faktor pengenceran (misal 10⁻³ → isi 1000):", min_value=1, step=1)
    jumlah_pengenceran = st.number_input("Jumlah pengenceran yang dihitung:", min_value=1, step=1)

    if st.button("Hitung TPC"):
        rata_rata = (koloni_1 + koloni_2) / 2
        tpc = rata_rata / (faktor_pengenceran * jumlah_pengenceran)
        st.success(f"Total Plate Count (TPC): **{tpc:.4f} CFU/mL**")

    st.markdown('</div>', unsafe_allow_html=True)

# Halaman: Tentang Kami
elif menu == "Tentang Kami":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">👨‍🔬 Tentang Kami</h1>', unsafe_allow_html=True)
    st.write("""
        Aplikasi ini dibuat untuk menghitung Total Plate Count (TPC) secara cepat dan akurat.
        \n💻 Dibuat menggunakan Python & Streamlit.
        \n📧 Kontak: lab@example.com
    """)
    st.markdown('</div>', unsafe_allow_html=True)
