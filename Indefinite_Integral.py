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
        
        # Menambahkan audio dari path lokal (pastikan mengonversi backslashes menjadi double backslashes atau gunakan forward slashes)
        audio_file_path = 'children-logo-116101.mp3'  # Ganti dengan path file audio Anda

        # Memasukkan tag audio menggunakan st.audio tanpa perlu menambahkan tag HTML manual
        st.audio(audio_file_path, format='audio/mp3', start_time=0)
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
        
        # Menambahkan audio dari path lokal (pastikan mengonversi backslashes menjadi double backslashes atau gunakan forward slashes)
        audio_file_path = 'children-logo-116101.mp3'  # Ganti dengan path file audio Anda

        # Memasukkan tag audio menggunakan st.audio tanpa perlu menambahkan tag HTML manual
        st.audio(audio_file_path, format='audio/mp3', start_time=0)
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
            &= \frac{1}{(-2)t^2}+C_1 - 2 \cdot \frac{2}{3} t^{3/2} +C_2 + 4 \cdot \frac{1}{4} t^4 - t + C_3 \\
            &= -\frac{1}{2t^2} - \frac{4}{3} t\sqrt{t} + t^4 - t + C
            \end{align*}
        ''')
        st.write("<font color='blue'>CONTOH 3.</font>", unsafe_allow_html=True)
        st.latex(r'''
            \begin{align*}
            \int (3y-4x)^2 \,dx &= \int (9y^2 - 2 \cdot 3y \cdot 4x + 16x^2) \,dx \\
            &= 9y^2 \int 1 \,dx - 24y \int x \,dx + 16 \int x^2 \,dx \\
            &= 9y^2x + C_1 - 12yx^2 + C_2 + \frac{16}{3}x^3 + C_3 \\
            &= 9y^2x - 12yx^2 + \frac{16}{3}x^3 + C
            \end{align*}
         ''')
        st.write("<font color='blue'>CONTOH 4.</font>", unsafe_allow_html=True)
        st.latex(r'''
            \begin{align*}
            \int (5a+1)(2-3a) \,da &= \int (10a - 15a^2 + 2 - 3a) \,da \\
            &= \int (-15a^2 + 7a + 2) \,da \\
            &= -15\int a^2 \,da + 7\int a \,da + 2\int 1 \,da \\
            &= -15 \cdot \frac{1}{3}a^3 +C_1 + 7 \cdot \frac{1}{2}a^2 +C_2 + 2a + C_3 \\
            &= -5a^3 + \frac{7}{2}a^2 + 2a + C
            \end{align*}

         ''')
    
        # Tombol Kuis
        if st.button("Kuis Sifat Kelinieran Integral"):
            run_sifat_kelinieran_quiz()

    elif menu == "Teknik Integrasi":
        
        # URL raw dari gambar di repositori GitHub
        github_image_url = 'https://raw.githubusercontent.com/igunlina/streamlit-example/master/SUBSTITUSI.jpg'
        st.image(github_image_url, caption='Semoga ilmunya bermanfaat', use_column_width=True)   
        
        # Menambahkan audio dari path lokal (pastikan mengonversi backslashes menjadi double backslashes atau gunakan forward slashes)
        audio_file_path = 'children-logo-116101.mp3'  # Ganti dengan path file audio Anda

        # Memasukkan tag audio menggunakan st.audio tanpa perlu menambahkan tag HTML manual
        st.audio(audio_file_path, format='audio/mp3', start_time=0)
        
        st.write("<font color='blue'>CONTOH 1.</font>", unsafe_allow_html=True)
        st.write("Hitunglah!")
        st.latex(r'''
            \int (2x^3-4x)^{24} (3x^2-2) \,dx
        ''')
        st.write("<font color='red'>Jawab.</font>", unsafe_allow_html=True)
        st.write("Misalkan $u=2x^3-4x$ maka $du=(6x^2-4)dx$ atau $\\frac{du}{2}=(3x^2-2)dx$, sehingga,")
        st.latex(r'''
        \begin{align*}
        \int (2x^3-4x)^{24} (3x^2-2) \,dx &= \int [u]^{24} \frac{du}{2} \\
        &= \frac{1}{2 \cdot 25} [u]^{25} + C \\
        &= \frac{1}{50} (2x^3-4x)^{25} + C
        \end{align*}
        ''')
        
        st.write("<font color='blue'>CONTOH 2.</font>", unsafe_allow_html=True)
        st.write("Hitunglah!")
        st.latex(r'''
            \int -3 cos^6(x) sin(x) \ dx
        ''')
        st.write("<font color='red'>Jawab.</font>", unsafe_allow_html=True)
        st.write("Misalkan $g(x)=cosx$ maka $g' (x)=-sinx$, sehingga")
        st.latex(r'''
            \begin{align*}
            \int -3cos^6(x) \ sin(x) \,dx &= 3 \int \cos^6(x)(-\sin(x)) \,dx \\
            &= 3\int [g(x)]^6g'(x) \,dx \\
            &= 3 \cdot \frac{1}{7}[g(x)]^7 + C \\
            &= \frac{3}{7}\cos^7(x) + C
            \end{align*}
            ''')
        
        st.write("<font color='blue'>CONTOH 3.</font>", unsafe_allow_html=True)
        st.write("Hitunglah!")
        st.latex(r'''
            \int \frac{x+3}{\sqrt{x^2+6x}} \,dx
         ''')

        st.write("Misalkan $u=x^2+6x $ maka $du=(2x+6)dx$, atau  $ \\frac{du}{2}=(x+3)dx$, sehingga")
        st.latex(r'''
            \begin{align*}
            \int \frac{x+3}{\sqrt{x^2+6x}} \,dx &= \int \frac{1}{\sqrt{u}} \frac{du}{2} \\
            &= \int [u]^{-1/2} \frac{du}{2} \\
            &= \frac{1}{2} \cdot 2 \cdot [u]^{1/2} + C \\
            &= \sqrt{x^2+6x} + C
            \end{align*}
            ''')
       
        # URL raw dari gambar di repositori GitHub
        github_image_url = 'https://raw.githubusercontent.com/igunlina/streamlit-example/master/parsial.jpg'
        st.image(github_image_url, caption='Semoga ilmunya bermanfaat', use_column_width=True)

        st.write("<font color='blue'>CONTOH 4.</font>", unsafe_allow_html=True)
        st.write("Hitunglah!")
        st.latex(r'''
           \int 2x(3x+2)^3 \,dx
        ''')
        st.write("<font color='red'>Jawab.</font>", unsafe_allow_html=True)
        st.write("Misalkan $u=2x$ maka $du=2dx$ dan $dv=(3x+2)^3 dx$   ,sehingga $v = \\frac{1}{3 \cdot 4} (3x+2)^4 = \\frac{1}{12} (3x+2)^4$. Akibatnya")
        st.latex(r'''
        \begin{align*}
        \int 2x(3x+2)^3 \,dx &= 2x \cdot \frac{1}{12} (3x+2)^4 - \int \frac{1}{12} (3x+2)^4 \cdot 2 \,dx \\
        &= \frac{x}{6} (3x+2)^4 - \frac{1}{6} \cdot \frac{1}{3} \cdot \frac{1}{5} (3x+2)^4 + C \\
        &= \frac{x}{6} (3x+2)^4 - \frac{1}{90} (3x+2)^4 + C
        \end{align*}
        ''')
                
        # Tombol Kuis
        if st.button("Teknik Integrasi"):
            run_teknik_integrasi_quiz()

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

def run_sifat_kelinieran_quiz():
    # Pertanyaan 10
    answer_4 = st.radio(" $\int_{}^{}{5} da = $", ["$5a +C$", "$5x+C$", "$5ax+C$"])

    # Pertanyaan 11
    answer_5 = st.radio(" $\int_{}^{}{m^3}dm=$", ["$\\frac{1}{4} m^4 +C $", "$\\frac{1}{3} m^3 +C $", "$\\frac{1}{4} x^4 +C$"])

    # Pertanyaan 12
    answer_6 = st.radio(" $\int_{}^{}{ \\frac{1}{x^2} dx=}$", ["$- \\frac{1}{x} +C$", "$- \\frac{2}{x} +C$", "$- \\frac{1}{x^2} +C$"])

    # Tombol Submit
    submitted = st.button("Submit")

    if submitted:
        check_rumus_dasar_answers(answer_10, answer_11, answer_12)

def run_teknik_integrasi_quiz():
    # Pertanyaan 13
    answer_13 = st.radio(" $\int_{}^{}{5} da = $", ["$5a +C$", "$5x+C$", "$5ax+C$"])

    # Pertanyaan 14
    answer_14 = st.radio(" $\int_{}^{}{m^3}dm=$", ["$\\frac{1}{4} m^4 +C $", "$\\frac{1}{3} m^3 +C $", "$\\frac{1}{4} x^4 +C$"])

    # Pertanyaan 15
    answer_15 = st.radio(" $\int_{}^{}{ \\frac{1}{x^2} dx=}$", ["$- \\frac{1}{x} +C$", "$- \\frac{2}{x} +C$", "$- \\frac{1}{x^2} +C$"])

    # Tombol Submit
    submitted = st.button("Submit")

    if submitted:
        check_rumus_dasar_answers(answer_13, answer_14, answer_15)


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
        
def check_sifat_kelinieran_answers(answer_10, answer_11, answer_12):
    # Logika pengecekan jawaban dan memberikan umpan balik
    correct_answers = {"$sin \phi + C$": "Benar", "$- sec t + C$": "Benar", "$ysinx+C$": "Benar"}

    if answer_10 in correct_answers and answer_11 in correct_answers and answer_12 in correct_answers:
        st.success("Selamat! Jawaban Anda benar.")
    else:
        st.error("Mohon maaf, jawaban Anda salah. Silahkan diulangi kembali.")

def check_teknik_integrasi_answers(answer_13, answer_14, answer_15):
    # Logika pengecekan jawaban dan memberikan umpan balik
    correct_answers = {"$sin \phi + C$": "Benar", "$- sec t + C$": "Benar", "$ysinx+C$": "Benar"}

    if answer_13 in correct_answers and answer_14 in correct_answers and answer_15 in correct_answers:
        st.success("Selamat! Jawaban Anda benar.")
    else:
        st.error("Mohon maaf, jawaban Anda salah. Silahkan diulangi kembali.")
 

if __name__ == '__main__':
    main()
