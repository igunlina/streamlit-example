import streamlit as st

def main():
    st.title('Halaman Depan dengan Gambar')
    st.header('Selamat datang di Halaman Depan!')

    # Menampilkan gambar dari direktori lokal
    image = open('Indefinite.jpg', 'rb')
    st.image(image, caption='Deskripsi Gambar', use_column_width=True)

if __name__ == '__main__':
    main()
