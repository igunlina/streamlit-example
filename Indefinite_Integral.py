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

        st.write("<font color='blue'>CONTOH 1.</font>", unsafe_allow_html=True)
        st.markdown('<font color="red">**Fungsi** $f(x)=2x$ **memiliki primitive** $F(x)=x^2$ pada   $ \mathbb{R}$  **sehingga** $(x^2)\'=2x$ </font>', unsafe_allow_html=True)

        st.write("<font color='blue'>CONTOH 2.</font>", unsafe_allow_html=True)
        st.markdown('<font color="red">**Fungsi** $f(x)=x^3$ **memiliki primitive** $F(x)=\\frac{x^4}{4}$ pada   $ \mathbb{R}$  **sehingga** $(\\frac{x^4}{4})\'=x^3$ </font>', unsafe_allow_html=True)
        
        st.write("<font color='blue'>CONTOH 3.</font>", unsafe_allow_html=True)
        st.markdown('<font color="red">**Fungsi** $f(x)=0$ **memiliki primitive** $F(x)=C \in \mathbb{R}$   **sehingga** $(C)\'=0$ </font>', unsafe_allow_html=True)

        # Tombol Kuis
        if st.button("Kuis Definisi Integral"):
            run_quiz()

    # ... (Kode yang lain)

def run_quiz():
    # Pertanyaan 1
    answer_1 = st.radio("Apa yang dimaksud dengan integral tak tentu?", ["Integral definit", "Integral tak tentu", "Integral ganda"])
    
    # Pertanyaan 2
    answer_2 = st.radio("Apa yang menyatakan fungsi yang terdifferensialkan?", ["Fungsi primitif", "Fungsi turunan", "Fungsi integral"])
    
    # Tombol Submit
    if st.button("Submit"):
        check_answers(answer_1, answer_2)

def check_answers(answer_1, answer_2):
    # Logika pengecekan jawaban dan memberikan umpan balik
    correct_answers = {"Integral tak tentu": "Benar", "Fungsi primitif": "Benar"}

    if answer_1 in correct_answers and answer_2 in correct_answers:
        st.success("Jawaban Anda benar!")
    else:
        st.error("Salah satu atau lebih jawaban Anda tidak benar. Coba lagi!")

# ... (Kode yang lain)
    
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
