import streamlit as st

def main():
    # Menu di sidebar
    menu = st.sidebar.radio("Kalkulus", ["Indefinite Integral", "Review Turunan", "Definisi", "Rumus Dasar Integral", "Integral Trigonometri", "Sifat Kelinieran Integral", "Teknik Integrasi"])

    if menu == "Indefinite Integral":
        st.title('BISMILLAH')
        st.header('MARI BELAJAR INTEGRAL TAK TENTU (INDEFINITE INTEGRAL/PRIMITIVE)')

        # URL raw dari gambar di repositori GitHub
        github_image_url = 'https://raw.githubusercontent.com/igunlina/streamlit-example/master/Indefinite.jpg'
        st.image(github_image_url, caption='Semoga ilmunya bermanfaat', use_column_width=True)

        # Menambahkan audio dari path lokal (pastikan mengonversi backslashes menjadi double backslashes atau gunakan forward slashes)
        audio_file_path = 'children-logo-116101.mp3'  # Ganti dengan path file audio Anda

        # Memasukkan tag audio menggunakan st.audio tanpa perlu menambahkan tag HTML manual
        st.audio(audio_file_path, format='audio/mp3', start_time=0)

    elif menu == "Definisi":
        st.subheader("Definisi Integral Tak Tentu")
        st.markdown("(Indefinite Integral /Primitive)")
        st.markdown(r"**Misalkan** $I$ **sebuah interval yang memuat lebih dari satu titik, dan sebarang fungsi** $f:I \to \mathbb{R}$. **Sebuah fungsi yang terdifferensialkan** $F$ **disebut sebagai primitive dari** $f$ **pada interval** $I$, **jika** $F'(x) = f(x)$, $x \in I$.")

        st.markdown("**CONTOH 1.**")
        st.markdown("**Fungsi** $f(x)=2x$ **memiliki primitive** $F(x)=x^2$ pada $ \mathbb{R}$ **sehingga** $(x^2)'=2x$")

        st.markdown("**CONTOH 2.**")
        st.markdown("**Fungsi** $f(x)=x^3$ **memiliki primitive** $F(x)=\\frac{x^4}{4}$ pada $ \mathbb{R}$ **sehingga** $(\\frac{x^4}{4})' = x^3$")

        st.markdown("**CONTOH 3.**")
        st.markdown("**Fungsi** $f(x)=0$ **memiliki primitive** $F(x)=C \in \mathbb{R}$ **sehingga** $(C)'=0$")

        # Tombol Kuis
        if st.button("Kuis Definisi Integral"):
            run_definisi_quiz()

    elif menu == "Review Turunan":
        st.subheader("Review Turunan")

        # Menambahkan video dari YouTube
        youtube_video_url_review = 'https://www.youtube.com/watch?v=XdiA9E5HC4I'  # Ganti dengan URL video YouTube Anda
        st.video(youtube_video_url_review)

        st.write("Sebelum mempelajari integral, mari kita review materi turunan agar mempelajari integral jadi lebih mudah.")

        st.write("Silahkan simak video pembelajaran turunan di atas dengan baik")

        st.write("Selamat menyimak!")

    elif menu == "Rumus Dasar Integral":
        st.subheader("Indefinite Integral")

        # URL raw dari gambar di repositori GitHub
        github_image_url = 'https://raw.githubusercontent.com/igunlina/streamlit-example/master/rumus%20dasar%20integral.jpg'
        st.image(github_image_url, caption='Semoga ilmunya bermanfaat', use_column_width=True)

        # Menambahkan audio dari path lokal (pastikan mengonversi backslashes menjadi double backslashes atau gunakan forward slashes)
        audio_file_path = 'integral 2x.mp3'  # Ganti dengan path file audio Anda
        st.audio(audio_file_path, format='audio/mp3', start_time=0)

        # Menuliskan persamaan matematika menggunakan Latex
        st.write("Bentuk umum indefinite integral atau integral tak tentu dapat dituliskan sebagai berikut.")
        st.latex(r'''
            \int f(x) \,dx = F(x) + C
        ''')

        st.write("Di sini, $f(x)$ adalah fungsi yang diintegralkan, $F(x)$ adalah fungsi integral tak tentu, dan $C$ adalah konstanta integrasi.")

        st.markdown("**RUMUS DASAR INTEGRAL.**")
        st.write("Jika $n$ sebarang bilangan rasional kecuali -1, maka.")
        # Menambahkan contoh persamaan matematika lainnya
        st.latex(r'''
            \int x^n \,dx = \frac{1}{n+1}x^{n+1} + C
        ''')

        st.markdown("**CONTOH 1.**")
        st.markdown("$\int x dx = \\frac{1}{1+1}x^{1+1}+C=\\frac{1}{2}x^2+C$")

        st.markdown("**CONTOH 2.**")
        st.markdown("$\int x^2 dx = \\frac{1}{2+1}x^{2+1}+C=\\frac{1}{3}x^3+C$")

        st.markdown("**CONTOH 3.**")
        st.markdown("$\int \sqrt{x} dx = \\frac{1}{\\frac{1}{2}+1}x^{\\frac{1}{2}+1}+C=\\frac{2}{3}x^{\\frac{3}{2}}+C$")

        # Tombol Kuis
        if st.button("Kuis Rumus Dasar Integral"):
            run_rumus_dasar_quiz()


def run_definisi_quiz():
    # Pertanyaan 1
    answer_1 = st.radio("Tentukan primitive dari fungsi $f(x)=2x$", ["$F(x)=x^2$", "$F(x)=2x^2$", "$F(x)=4$"])

    # Pertanyaan 2
    answer_2 = st.radio("Tentukan primitive dari fungsi $f(x)=x^3$", ["$F(x)= \\frac{1}{3} x^3$", "$F(x)=2x$", "$F(x)=\\frac{1}{2} x^2$"])

    # Pertanyaan 3
    answer_3 = st.radio("Tentukan primitive dari fungsi $f(x)=0$", ["$F(x)=0$", "$F(x)=C \in \mathbb{R}$", "$F(x)=3x^2$"])

    # Tombol Submit
    submitted = st.button("Submit")

    if submitted:
        check_definisi_answers(answer_1, answer_2, answer_3)


def run_rumus_dasar_quiz():
    # Pertanyaan 1
    answer_1 = st.radio(" $\( \int_{}^{}{5} da = \)$", ["$F(x)=2x^2$", "$F(x)=4x^2$", "$F(x)=4$"])

    # Pertanyaan 2
    answer_2 = st.radio("Tentukan primitive dari fungsi $f(x)=x^2$", ["$F(x)= \\frac{1}{3} x^3$", "$F(x)=2x$", "$F(x)=\\frac{1}{2} x^2$"])

    # Pertanyaan 3
    answer_3 = st.radio("Tentukan primitive dari fungsi $f(x)=6$", ["$F(x)= 6x$", "$F(x)=0$", "$F(x)=3x^2$"])

    # Tombol Submit
    submitted = st.button("Submit")

    if submitted:
        check_rumus_dasar_answers(answer_1, answer_2, answer_3)


def check_definisi_answers(answer_1, answer_2, answer_3):
    # Logika pengecekan jawaban dan memberikan umpan balik
    correct_answers = {"$F(x)=x^2$": "Benar", "$F(x)= \\frac{1}{3} x^3$": "Benar", "$F(x)=0$": "Benar"}

    if answer_1 in correct_answers and answer_2 in correct_answers and answer_3 in correct_answers:
        st.success("Selamat! Jawaban Anda benar.")
    else:
        st.error("Mohon maaf, jawaban Anda salah. Silahkan diulangi kembali.")


def check_rumus_dasar_answers(answer_1, answer_2, answer_3):
    # Logika pengecekan jawaban dan memberikan umpan balik
    correct_answers = {"$F(x)=2x^2$": "Benar", "$F(x)= \\frac{1}{3} x^3$": "Benar", "$F(x)= 6x$": "Benar"}

    if answer_1 in correct_answers and answer_2 in correct_answers and answer_3 in correct_answers:
        st.success("Selamat! Jawaban Anda benar.")
    else:
        st.error("Mohon maaf, jawaban Anda salah. Silahkan diulangi kembali.")


if __name__ == '__main__':
    main()
