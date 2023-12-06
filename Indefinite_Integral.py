import streamlit as st

def main():
    # Menu di sidebar
    menu = st.sidebar.radio("INDEFINITE INTEGRAL", ["Review Turunan", "Definisi", "Rumus Dasar Integral", "Integral Trigonometri", "Sifat Kelinieran Integral", "Teknik Integrasi"])

    if menu == "Definisi":
        st.title('BISMILLAH')
        st.header('MARI BELAJAR INTEGRAL TAK TENTU (INDEFINITE INTEGRAL/PRIMITIVE)')

        # URL raw dari gambar di repositori GitHub
        github_image_url = 'https://raw.githubusercontent.com/igunlina/streamlit-example/master/Indefinite.jpg'
        st.image(github_image_url, caption='Semoga ilmunya bermanfaat', use_column_width=True)

        # Menambahkan audio dari path lokal (pastikan mengonversi backslashes menjadi double backslashes atau gunakan forward slashes)
        audio_file_path = 'children-logo-116101.mp3'  # Ganti dengan path file audio Anda
        st.audio(audio_file_path, format='audio/mp3', start_time=0)

        st.subheader("Definisi Integral Tak Tentu")
        st.markdown("(Indefinite Integral /Primitive)")
        st.markdown(r"**Misalkan** $I$ **sebuah interval yang memuat lebih dari satu titik, dan sebarang fungsi** $f:I \to \mathbb{R}$. **Sebuah fungsi yang terdifferensialkan** $F$ **disebut sebagai primitive dari** $f$ **pada interval** $I$, **jika** $F'(x) = f(x)$, $x \in I$.")


        st.write("CONTOH.")
        st.markdown(r"**Misalkan** $I$ **sebuah interval yang memuat lebih dari satu titik, dan sebarang fungsi** $f:I \to \mathbb{R}$. **Sebuah fungsi yang terdifferensialkan** $F$ **disebut sebagai primitive dari** $f$ **pada interval** $I$, **jika** $F'(x) = f(x)$, $x \in I$.")

    elif menu == "Review Turunan":
        st.subheader("Review Turunan")

        # Menambahkan video dari YouTube
        youtube_video_url_review = 'https://www.youtube.com/watch?v=XdiA9E5HC4I'  # Ganti dengan URL video YouTube Anda
        st.video(youtube_video_url_review)

        st.write("Sebelum mempelajari integral, mari kita review materi turunan agar mempelajari integral jadi lebih mudah.")
       
        st.write("Silahkan simak video pembelajaran turunan di atas dengan baik")
       
        st.write("Selamat menyimak!")
    elif menu == "Rumus Dasar Integral":
        st.subheader("Rumus Dasar Integral")

        # Menuliskan persamaan matematika menggunakan Latex
        st.latex(r'''
            \int f(x) \,dx = F(x) + C
        ''')

        st.write("Di sini, $f(x)$ adalah fungsi yang diintegrasikan, $F(x)$ adalah fungsi integral tak tentu, dan $C$ adalah konstanta integrasi.")
        
        st.write("Anda dapat menyesuaikan persamaan matematika tersebut sesuai dengan konteks dan rumus dasar yang ingin Anda sertakan.")
        
        # Menambahkan contoh persamaan matematika lainnya
        st.latex(r'''
            \int x^2 \,dx = \frac{1}{3}x^3 + C
        ''')

        st.write("Contoh lain, di sini $\\int x^2 \\,dx$ menghasilkan $1/3 x^3 + C$ sebagai solusi integralnya.")



    elif menu == "Kontak":
        st.subheader("Hubungi Kami")
        st.write("Jika Anda memiliki pertanyaan atau masukan, silakan hubungi kami melalui:")
        st.write("- Email: example@email.com")
        st.write("- Telepon: 123-456-789")
        st.write("- Alamat: Jalan Contoh No. 123")

if __name__ == '__main__':
    main()
