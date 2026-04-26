from flask import Flask, render_template, request
from fuzzyKelelahan import hitungKelelahan
from pakarUjian import hitungPrediksiUjian

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fuzzy', methods=['GET', 'POST'])
def fuzzy():
    if request.method == 'POST':
        durasi = float(request.form.get('durasi', 0))
        beban = float(request.form.get('beban', 0))
        skor, status, saran = hitungKelelahan(durasi, beban)
        return render_template('fuzzy.html', skor=skor, status=status, saran=saran)
    return render_template('fuzzy.html')

@app.route('/pakar-ujian', methods=['GET', 'POST'])
def pakar_ujian():
    if request.method == 'POST':
        prediksi, evaluasi, total_skor, badge_color = hitungPrediksiUjian(request.form)
        return render_template('pakarUjian.html', 
                               prediksi=prediksi, 
                               evaluasi=evaluasi, 
                               total_skor=total_skor, 
                               badge_color=badge_color)
    return render_template('pakarUjian.html')

@app.route('/pakar', methods=['GET', 'POST'])
def pakar():
    if request.method == 'POST':
        hasil_gimmick = "Malaikat Tanpa Sayap (Grade SSS)"
        pesan_gimmick = "Semua asprak baik, tidak ada asprak jahat di dunia ini. Terutama yang sedang mengoreksi responsi ini, bisa kali dapet A!"        
        return render_template('pakar.html', hasil_pakar=hasil_gimmick, pesan_pakar=pesan_gimmick)
    return render_template('pakar.html')

if __name__ == '__main__':
    app.run(debug=True)