import streamlit as st

def main():
    # Menu di sidebar
    menu = st.sidebar.radio("INDEFINITE INTEGRAL", ["Review Turunan", "Definisi", "Rumus Dasar Integral", "Integral Trigonometri", "Sifat Kelinieran Integral", "Teknik Integrasi"])

    if menu == "Definisi":
        st.title('BISMILLAH')
        st.header('MARI BELAJAR INTEGRAL TAK TENTU (INDEFINITE INTEGRAL)')

        # URL raw dari gambar di repositori GitHub
        github_image_url = 'https://raw.githubusercontent.com/igunlina/streamlit-example/master/Indefinite.jpg'
        st.image(github_image_url, caption='Semoga ilmunya bermanfaat', use_column_width=True)

        # Menambahkan audio dari path lokal (pastikan mengonversi backslashes menjadi double backslashes atau gunakan forward slashes)
        audio_file_path = 'children-logo-116101.mp3'  # Ganti dengan path file audio Anda
        st.audio(audio_file_path, format='audio/mp3', start_time=0)

        st.subheader("Selamat datang di halaman Beranda!")
        st.write("Halaman ini berisi informasi umum tentang pembelajaran Indefinite Integral.")
        st.write("Silakan jelajahi konten-konten yang tersedia.")
    elif menu == "Rumus Dasar Integral":
        st.subheader("Tentang Kami")
        st.write("Kami adalah tim yang berkomitmen untuk memberikan informasi seputar integral.")
        st.write("Kami berharap informasi yang kami sajikan dapat membantu Anda memahami konsep ini dengan lebih baik.")
    elif menu == "Kontak":
        st.subheader("Hubungi Kami")
        st.write("Jika Anda memiliki pertanyaan atau masukan, silakan hubungi kami melalui:")
        st.write("- Email: example@email.com")
        st.write("- Telepon: 123-456-789")
        st.write("- Alamat: Jalan Contoh No. 123")

if __name__ == '__main__':
    main()
