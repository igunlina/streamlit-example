import streamlit as st

def main():
    # Menu di sidebar
    menu = st.sidebar.radio("INTEGRAL", ["Indefinite Integral", "Review Turunan", "Definisi", "Rumus Dasar Integral", "Integral Trigonometri", "Sifat Kelinieran Integral", "Teknik Integrasi"])

    if menu == "Indefinite Integral":
        st.title('BISMILLAH')
        st.header('MARI BELAJAR INTEGRAL TAK TENTU (INDEFINITE INTEGRAL/PRIMITIVE\ANTIDERIVATIVE)')

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

        st.write("<font color='blue'>CONTOH 1.</font>", unsafe_allow_html=True)
        st.markdown('<font color="red">**Fungsi** $f(x)=2x$ **memiliki primitive** $F(x)=x^2$ pada   $ \mathbb{R}$  **sehingga** $(x^2)\'=2x$ </font>', unsafe_allow_html=True)

        st.write("<font color='blue'>CONTOH 2.</font>", unsafe_allow_html=True)
        st.markdown('<font color="red">**Fungsi** $f(x)=x^3$ **memiliki primitive** $F(x)=\\frac{x^4}{4}$ pada   $ \mathbb{R}$  **sehingga** $(\\frac{x^4}{4})\'=x^3$ </font>', unsafe_allow_html=True)
        
        st.write("<font color='blue'>CONTOH 3.</font>", unsafe_allow_html=True)
        st.markdown('<font color="red">**Fungsi** $f(x)=0$ **memiliki primitive** $F(x)=C \in \mathbb{R}$   **sehingga** $(C)\'=0$ </font>', unsafe_allow_html=True)

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

        
        st.write("<font color='blue'>CONTOH 1.</font>", unsafe_allow_html=True)
        st.markdown('<font color="red"> $\int x dx = \\frac{1}{1+1}x^{1+1}+C=\\frac{1}{2}x^2+C$ </font>', unsafe_allow_html=True)

        st.write("<font color='blue'>CONTOH 2.</font>", unsafe_allow_html=True)
        st.markdown('<font color="red"> $\int x^2 dx = \\frac{1}{2+1}x^{2+1}+C=\\frac{1}{3}x^3+$ </font>', unsafe_allow_html=True)
        
        st.write("<font color='blue'>CONTOH 3.</font>", unsafe_allow_html=True)
        st.markdown('<font color="red"> $\int \sqrt{x} dx = \\frac{1}{\\frac{1}{2}+1}x^{\\frac{1}{2}+1}+C=\\frac{2}{3}x^{\\frac{3}{2}}+C$ </font>', unsafe_allow_html=True)
        
        # Tombol Kuis
        if st.button("Kuis Rumus Dasar Integral"):
            run_rumus_dasar_quiz()

    elif menu == "Integral Trigonometri":
        st.subheader("Integral Trigonometri")

        # URL raw dari gambar di repositori GitHub
        github_image_url = 'https://raw.githubusercontent.com/igunlina/streamlit-example/master/Integral%20trigonometri.jpg'
        st.image(github_image_url, caption='Semoga ilmunya bermanfaat', use_column_width=True)   

        st.write("<font color='blue'>CONTOH 1.</font>", unsafe_allow_html=True)
        st.markdown('<font color="red"> $\int cos a \ da = sin a+C$ </font>', unsafe_allow_html=True)

        st.write("<font color='blue'>CONTOH 2.</font>", unsafe_allow_html=True)
        st.markdown('<font color="red"> $\int -sin p \ dy = -ysin p+C$ </font>', unsafe_allow_html=True)
        
        st.write("<font color='blue'>CONTOH 3.</font>", unsafe_allow_html=True)
        st.markdown('<font color="red"> $\int -sec^2h \ dh = -tanh+C$ </font>', unsafe_allow_html=True)

        # Tombol Kuis
        if st.button("Kuis Integral Trigonometri"):
            run_integral_trigonometri_quiz()
           
   
    elif menu == "Sifat Kelinieran Integral":
        

        # URL raw dari gambar di repositori GitHub
        github_image_url = 'https://raw.githubusercontent.com/igunlina/streamlit-example/master/Sifat%20kelinieran%20integral.jpg'
        st.image(github_image_url, caption='Semoga ilmunya bermanfaat', use_column_width=True)   

        st.write("<font color='blue'>CONTOH 1.</font>", unsafe_allow_html=True)
        st.latex(r'''
            \begin{align*}
            \int (6x^5 - 2x) \,dx &= \int 6x^5 \,dx - \int 2x \,dx \\
            &= 6\int x^5 \,dx - 2\int x \,dx \\
            &= 6\left(\frac{1}{6} x^6 + C_1\right) - 2\left(\frac{1}{2} x^2 + C_2\right) \\
            &= x^6 + 6C_1 - x^2 - 2C_2 \\
            &= x^6 - x^2 + C
            \end{align*}
        ''')
        
        st.write("<font color='blue'>CONTOH 2.</font>", unsafe_allow_html=True)
        st.latex(r'''
            \begin{align*}
            \int \left(\frac{1}{t^3} - 2\sqrt{t} + 4t^3 - 1\right) \,dt 
            &= \int \frac{1}{t^3} \,dt - 2\int t^{1/2} \,dt + 4\int t^3 \,dt - \int 1 \,dt \\
            &= \frac{1}{(-2)t^2} - 2 \cdot \frac{2}{3} t^{3/2} + 4 \cdot \frac{1}{4} t^4 - t + C \\
            &= -\frac{1}{2t^2} - \frac{4}{3} t\sqrt{t} + t^4 - t + C
            \end{align*}
        ''')
        st.write("<font color='blue'>CONTOH 3.</font>", unsafe_allow_html=True)
        st.markdown('<font color="red"> $\int -sec^2h \ dh = -tanh+C$ </font>', unsafe_allow_html=True)

        # Tombol Kuis
        if st.button("Kuis Integral Trigonometri"):
            run_integral_trigonometri_quiz()

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
    # Pertanyaan 4
    answer_4 = st.radio(" $\int_{}^{}{5} da = $", ["$5a +C$", "$5x+C$", "$5ax+C$"])

    # Pertanyaan 5
    answer_5 = st.radio(" $\int_{}^{}{m^3}dm=$", ["$\\frac{1}{4} m^4 +C $", "$\\frac{1}{3} m^3 +C $", "$\\frac{1}{4} x^4 +C$"])

    # Pertanyaan 6
    answer_6 = st.radio(" $\int_{}^{}{ \\frac{1}{x^2} dx=}$", ["$- \\frac{1}{x} +C$", "$- \\frac{2}{x} +C$", "$- \\frac{1}{x^2} +C$"])

    # Tombol Submit
    submitted = st.button("Submit")

    if submitted:
        check_rumus_dasar_answers(answer_4, answer_5, answer_6)
        
def run_integral_trigonometri_quiz():
    # Pertanyaan 7
    answer_7 = st.radio(" $\int_{}^{}{cos \phi } \ d \phi = $", ["$sin \phi + C$", "$- sin \phi + C$", "$- cos \phi + C $"])

    # Pertanyaan 8
    answer_8 = st.radio(" $\int_{ }^{ }{-sec \ t \ tan  \ t} \ dt = $", ["$- sec t + C$", "$sec t + C$", "$ cosec  t + C$"])
    
    # Pertanyaan 9
    answer_9 = st.radio(" $\int_{}^{}{sinx} \ dy=$", ["$ysinx+C$", "$siny+C $", "$xsiny+C$"])

   
    # Tombol Submit
    submitted = st.button("Submit")

    if submitted:
        check_rumus_dasar_answers(answer_7, answer_8, answer_9)

def check_definisi_answers(answer_1, answer_2, answer_3):
    # Logika pengecekan jawaban dan memberikan umpan balik
    correct_answers = {"$F(x)=x^2$": "Benar", "$F(x)= \\frac{1}{3} x^3$": "Benar", "$F(x)=0$": "Benar"}

    if answer_1 in correct_answers and answer_2 in correct_answers and answer_3 in correct_answers:
        st.success("Selamat! Jawaban Anda benar.")
    else:
        st.error("Mohon maaf, jawaban Anda salah. Silahkan diulangi kembali.")


def check_rumus_dasar_answers(answer_4, answer_5, answer_6):
    # Logika pengecekan jawaban dan memberikan umpan balik
    correct_answers = {"$5a +C$": "Benar", "$\\frac{1}{4} m^4 +C$": "Benar", "$- \frac{1}{x} +C$": "Benar"}

    if answer_4 in correct_answers and answer_5 in correct_answers and answer_6 in correct_answers:
        st.success("Selamat! Jawaban Anda benar.")
    else:
        st.error("Mohon maaf, jawaban Anda salah. Silahkan diulangi kembali.")

def check_rumus_dasar_answers(answer_7, answer_8, answer_9):
    # Logika pengecekan jawaban dan memberikan umpan balik
    correct_answers = {"$sin \phi + C$": "Benar", "$- sec t + C$": "Benar", "$ysinx+C$": "Benar"}

    if answer_7 in correct_answers and answer_8 in correct_answers and answer_9 in correct_answers:
        st.success("Selamat! Jawaban Anda benar.")
    else:
        st.error("Mohon maaf, jawaban Anda salah. Silahkan diulangi kembali.")
        
if __name__ == '__main__':
    main()
