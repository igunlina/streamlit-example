import streamlit as st

def main():
    st.title('INTEGRAL')
    st.header('MARI BELAJAR INDEFINITE INTEGRAL')

    # URL raw dari gambar di repositori GitHub
    github_image_url = 'https://raw.githubusercontent.com/igunlina/streamlit-example/master/Indefinite.jpg'

    # Menampilkan gambar dari URL
    st.image(github_image_url, caption='Semoga ilmunya bermanfaat', use_column_width=True)

    # Menu di sidebar
    menu = st.sidebar.radio("Menu", ["Definisi", "Review antiderivative", "Rumus Integral Dasar", "Integral Trigonometri", "Sifat Kelinieran Integral", "Teknik Integrasi"])

    if menu == "Beranda":
        st.write("Anda berada di Beranda. Ini adalah konten untuk halaman Beranda.")
    elif menu == "Tentang":
        st.write("Anda berada di Halaman Tentang. Ini adalah konten untuk halaman Tentang.")
    elif menu == "Kontak":
        st.write("Anda berada di Halaman Kontak. Ini adalah konten untuk halaman Kontak.")

if __name__ == '__main__':
    main()
