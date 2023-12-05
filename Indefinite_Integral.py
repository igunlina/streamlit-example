import streamlit as st

def main():
    st.title('INTEGRAL')
    st.header('MARI BELAJAR INDEFINITE INTEGRAL')

    # URL raw dari gambar di repositori GitHub
    github_image_url = 'https://raw.githubusercontent.com/igunlina/streamlit-example/master/Indefinite.jpg'

    # Menampilkan gambar dari URL
    st.image(github_image_url, caption='Semoga ilmunya bermanfaat', use_column_width=True)

    # Menu di sidebar
    menu = st.sidebar.radio("Menu", ["Beranda", "Tentang", "Kontak"])

    if menu == "Beranda":
        st.write("Anda berada di Beranda. Ini adalah konten untuk halaman Beranda.")
        st.subheader("Selamat datang di halaman Beranda!")
        st.write("Halaman ini berisi informasi umum tentang pembelajaran Indefinite Integral.")
        st.write("Silakan jelajahi konten-konten yang tersedia.")
    elif menu == "Tentang":
        st.write("Anda berada di Halaman Tentang. Ini adalah konten untuk halaman Tentang.")
        st.subheader("Tentang Kami")
        st.write("Kami adalah tim yang berkomitmen untuk memberikan informasi seputar integral.")
        st.write("Kami berharap informasi yang kami sajikan dapat membantu Anda memahami konsep ini dengan lebih baik.")
    elif menu == "Kontak":
        st.write("Anda berada di Halaman Kontak. Ini adalah konten untuk halaman Kontak.")
        st.subheader("Hubungi Kami")
        st.write("Jika Anda memiliki pertanyaan atau masukan, silakan hubungi kami melalui:")
        st.write("- Email: example@email.com")
        st.write("- Telepon: 123-456-789")
        st.write("- Alamat: Jalan Contoh No. 123")

if __name__ == '__main__':
    main()
