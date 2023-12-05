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
        # Tambahkan konten khusus untuk halaman Beranda di sini
        st.subheader("Selamat datang di halaman Beranda!")
        st.write("Silakan jelajahi informasi yang tersedia.")
    elif menu == "Tentang":
        st.write("Anda berada di Halaman Tentang. Ini adalah konten untuk halaman Tentang.")
        # Tambahkan konten khusus untuk halaman Tentang di sini
        st.subheader("Tentang Kami")
        st.write("Kami adalah tim yang berkomitmen untuk memberikan informasi seputar integral.")
    elif menu == "Kontak":
        st.write("Anda berada di Halaman Kontak. Ini adalah konten untuk halaman Kontak.")
        # Tambahkan konten khusus untuk halaman Kontak di sini
        st.subheader("Hubungi Kami")
        st.write("Jika Anda memiliki pertanyaan, silakan hubungi kami di example@email.com.")

if __name__ == '__main__':
    main()
