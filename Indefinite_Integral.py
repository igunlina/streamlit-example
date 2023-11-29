import streamlit as st

def main():
    st.title('Halaman Depan dengan Gambar dari GitHub')
    st.header('Selamat datang di Halaman Depan!')

    # URL raw dari gambar di repositori GitHub
    github_image_url = 'https://raw.githubusercontent.com/igunlina/streamlit-example/master/Indefinite.jpg'

    # Menampilkan gambar dari URL
    st.image(github_image_url, caption='Deskripsi Gambar', use_column_width=True)

 # Menu di sidebar
    menu = st.sidebar.radio("Menu", ["Beranda", "Tentang", "Kontak"])

    if menu == "Beranda":
        st.write("Anda berada di Beranda.")
        # Tambahkan konten Beranda di sini
    elif menu == "Tentang":
        st.write("Anda berada di Halaman Tentang.")
        # Tambahkan konten Tentang di sini
    elif menu == "Kontak":
        st.write("Anda berada di Halaman Kontak.")
        # Tambahkan konten Kontak di sini
if __name__ == '__main__':
    main()
