import streamlit as st

def main():
    st.title('Halaman Depan dengan Gambar dari GitHub')
    st.header('Selamat datang di Halaman Depan!')

    # URL raw dari gambar di repositori GitHub
    github_image_url = 'https://raw.githubusercontent.com/NamaPenggunaAnda/RepoNamaAnda/NamaBranchAnda/path/ke/gambar.jpg'

    # Menampilkan gambar dari URL
    st.image(github_image_url, caption='Deskripsi Gambar', use_column_width=True)

if __name__ == '__main__':
    main()
