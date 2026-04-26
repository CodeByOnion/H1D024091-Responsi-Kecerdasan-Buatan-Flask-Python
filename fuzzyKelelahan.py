def hitungKelelahan(durasiTidur, bebanKegiatan):
    tidurKurang = max(0, min((6 - durasiTidur) / (6 - 0), 1)) if durasiTidur <= 6 else 0
    tidurCukup = max(0, min((durasiTidur - 4) / (6 - 4), (8 - durasiTidur) / (8 - 6))) if 4 <= durasiTidur <= 8 else 0
    tidurOptimal = max(0, min((durasiTidur - 7) / (10 - 7), 1)) if durasiTidur >= 7 else 0

    bebanRendah = max(0, min((5 - bebanKegiatan) / (5 - 1), 1)) if bebanKegiatan <= 5 else 0
    bebanSedang = max(0, min((bebanKegiatan - 3) / (5 - 3), (8 - bebanKegiatan) / (8 - 5))) if 3 <= bebanKegiatan <= 8 else 0
    bebanTinggi = max(0, min((bebanKegiatan - 6) / (10 - 6), 1)) if bebanKegiatan >= 6 else 0

    rules = [
        (min(tidurOptimal, bebanRendah), 15, "Saraf Prima", "Kondisi ideal untuk fokus coding atau scroll fesnuk."),
        (min(tidurOptimal, bebanSedang), 25, "Saraf Prima", "Kondisi ideal untuk fokus coding atau scroll fesnuk."),
        (min(tidurOptimal, bebanTinggi), 45, "Kelelahan Ringan", "Segera istirahat sejenak, konsumsi air putih, dan hindari ngoding."),
        (min(tidurCukup, bebanRendah), 30, "Saraf Prima", "Kondisi ideal untuk fokus coding atau scroll fesnuk."),
        (min(tidurCukup, bebanSedang), 50, "Kelelahan Ringan", "Segera istirahat sejenak, konsumsi air putih, dan hindari ngoding."),
        (min(tidurCukup, bebanTinggi), 65, "Kelelahan Ringan", "Segera istirahat sejenak, konsumsi air putih, dan hindari ngoding."),
        (min(tidurKurang, bebanRendah), 60, "Kelelahan Ringan", "Segera istirahat sejenak, konsumsi air putih, dan hindari ngoding."),
        (min(tidurKurang, bebanSedang), 85, "Kelelahan Saraf Tinggi", "Wajib tidur! Jangan memaksakan ngoding atau scroll fesnuk."),
        (min(tidurKurang, bebanTinggi), 100, "Kelelahan Saraf Tinggi", "Wajib tidur! Jangan memaksakan ngoding atau scroll fesnuk.")
    ]

    pembilang = sum(w * z for w, z, label, s in rules)
    penyebut = sum(w for w, z, label, s in rules)

    if penyebut == 0:
        return 0, "Data Tidak Valid", "Silakan masukkan input yang benar."

    skor_akhir = pembilang / penyebut

  
    status_final = max(rules, key=lambda x: x[0])[2]
    saran_final = max(rules, key=lambda x: x[0])[3]

    return round(skor_akhir, 2), status_final, saran_final