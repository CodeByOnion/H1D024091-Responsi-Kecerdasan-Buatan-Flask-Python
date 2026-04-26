def hitungPrediksiUjian(data_jawaban):
    
    q_keys = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11']
    total_skor = 0
    
    # Menghitung poin (A = 1, B = 0)
    for key in q_keys:
        jawaban = data_jawaban.get(key)
        if jawaban == 'A':
            total_skor += 1

    # Logika Inferensi (Forward Chaining berbasis Skor)
    if total_skor >= 9:
        prediksi = "Lulus Predikat A (Sangat Aman)"
        evaluasi = "Persiapan akademik, fisik, dan eksekusi ujianmu sangat matang. Kamu menguasai ruang ujian sepenuhnya."
        badge_color = "success"
    elif total_skor >= 6:
        prediksi = "Lulus Predikat B (Aman)"
        evaluasi = "Secara umum kamu siap, namun ada beberapa celah di persiapan atau kondisi fisik yang membuatmu rentan melakukan kesalahan kecil."
        badge_color = "primary"
    elif total_skor >= 4:
        prediksi = "Predikat C (Batas Kritis)"
        evaluasi = "Performa ujianmu tertolong oleh keberuntungan atau ingatan jangka pendek. Sangat bergantung pada nilai tugas."
        badge_color = "warning"
    else:
        prediksi = "Risiko Tinggi Remedial / Mengulang"
        evaluasi = "Terjadi kegagalan sistemik. Evaluasi ulang cara belajarmu, jam terbang latihan, dan kondisi kesehatan fisik/mental."
        badge_color = "danger"

    return prediksi, evaluasi, total_skor, badge_color