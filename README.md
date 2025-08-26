# Instagram Unfollower Bot - Modal Version

Automated Instagram unfollower bot yang menggunakan Selenium WebDriver untuk melakukan unfollow secara batch dari modal following list.

## ⚠️ Disclaimer

**PENTING**: Bot ini dibuat untuk tujuan edukasi dan pembelajaran. Penggunaan bot untuk automasi Instagram dapat melanggar Terms of Service Instagram dan berisiko menyebabkan akun Anda dibatasi atau di-suspend. 

**🚨 WAJIB GUNAKAN AKUN TUMBAL/TEST - JANGAN AKUN UTAMA! 🚨**

- ✅ **SELALU gunakan akun dummy/tumbal untuk testing**
- ❌ **JANGAN PERNAH gunakan akun utama atau akun bisnis penting**
- ⚠️ **Risiko account ban/suspend sangat tinggi**
- 📋 **Buat akun Instagram khusus untuk testing automation**

**KAMI TIDAK BERTANGGUNG JAWAB** atas segala kerusakan, kehilangan akses, atau konsekuensi negatif lainnya yang timbul dari penggunaan script ini. Segala risiko dan tanggung jawab sepenuhnya berada di tangan pengguna.

## ✨ Fitur

- ✅ Login otomatis dengan error handling yang robust
- ✅ Membuka modal following list langsung dari profil
- ✅ Unfollow langsung dari modal (lebih cepat dan efisien)
- ✅ Anti-detection dengan user agent dan stealth mode
- ✅ Jeda random untuk menghindari rate limiting
- ✅ Handling popup dan dialog Instagram
- ✅ Error recovery dan retry mechanism
- ✅ Logging yang informatif

## 📋 Prerequisites

### 1. Python 3.7+
Pastikan Python versi 3.7 atau lebih baru terinstall di sistem Anda.

### 2. Google Chrome Browser
Bot ini memerlukan Google Chrome browser yang terinstall di sistem.

### 3. Dependencies Python
Install semua package yang diperlukan:

```bash
pip install selenium webdriver-manager
```

## 📦 Instalasi

1. **Clone atau download file script**
   ```bash
   # Jika menggunakan git
   git clone <repository-url>
   
   # Atau download file instagram_unfollower.py
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Atau install manual:
   ```bash
   pip install selenium webdriver-manager
   ```

3. **Pastikan Chrome browser terinstall**
   - Download dari: https://www.google.com/chrome/

## 🚀 Cara Penggunaan

### Menjalankan Script

```bash
python3 instagram_unfollower.py
```

### Input yang Diperlukan

1. **Username Instagram**: Username akun Instagram **TUMBAL/DUMMY** (JANGAN akun utama!)
2. **Password Instagram**: Password akun tumbal (input tersembunyi untuk keamanan)
3. **Jumlah Unfollow**: Maksimal jumlah akun yang ingin di-unfollow (disarankan 10-50 untuk keamanan)

### Contoh Penggunaan

```
=== Instagram Unfollower Modal (Fixed Version) ===
📧 Username Instagram: dummy_account_123  # GUNAKAN AKUN TUMBAL!
🔑 Password Instagram (tidak akan terlihat): 
📊 Berapa maksimal unfollow (misal 10-50): 25
```

### ⚠️ PERINGATAN SEBELUM MENGGUNAKAN

**WAJIB BACA dan PAHAMI:**

1. **🚫 JANGAN gunakan akun utama/bisnis/penting**
2. **✅ BUAT akun Instagram dummy khusus untuk testing**
3. **📋 SIAPKAN akun tumbal dengan beberapa following**
4. **⚠️ PAHAMI risiko: akun bisa di-ban permanen**
5. **🛡️ TIDAK ADA GARANSI keamanan akun**

## ⚙️ Konfigurasi

### Mode Headless
Untuk menjalankan browser dalam mode headless (tidak terlihat):

```python
bot = InstagramUnfollower(username, headless=True)
```

### Mengubah Delay
Anda dapat mengubah jeda waktu dalam method `safe_unfollow_batch()`:

```python
# Ubah delay random (default: 4-8 detik)
delay = random.uniform(2, 5)  # Jeda lebih cepat (risiko lebih tinggi)
delay = random.uniform(6, 12) # Jeda lebih lambat (lebih aman)
```

## 🛡️ Keamanan dan Best Practices

### ⚠️ PERINGATAN UTAMA

**🚨 GUNAKAN HANYA AKUN TUMBAL - JANGAN AKUN UTAMA! 🚨**

**Cara Membuat Akun Tumbal:**
1. Buat akun Instagram baru dengan email dummy
2. Isi profil secukupnya (foto, bio singkat)
3. Follow beberapa akun (20-100 akun)
4. Biarkan akun "aging" selama beberapa hari
5. Baru gunakan untuk testing bot

### Rekomendasi Penggunaan Aman

1. **Batasi Jumlah Unfollow**: 
   - Maksimal 20-50 per session
   - Jangan gunakan setiap hari

2. **Gunakan Jeda yang Cukup**:
   - Minimal 3-5 detik antar unfollow
   - Jeda random lebih baik dari jeda tetap

3. **Hindari Penggunaan Berlebihan**:
   - Maksimal 1-2 kali per minggu
   - Monitor aktivitas akun Anda

4. **Backup Data Penting**:
   - Screenshot following list sebelum menggunakan
   - Catat akun penting yang tidak ingin di-unfollow

### Tanda-tanda Account Limiting

Hentikan penggunaan jika mengalami:
- Captcha berulang saat login
- Pesan "Action Blocked" dari Instagram
- Akun sementara di-suspend
- Fitur Instagram dibatasi

## 🔧 Troubleshooting

### Error "ChromeDriver not found"
```bash
# Install ulang webdriver-manager
pip uninstall webdriver-manager
pip install webdriver-manager
```

### Error "Element not found"
- Instagram mungkin mengubah layout
- Coba update script atau buka issue

### Login Challenge/2FA
- Script akan pause untuk verifikasi manual
- Selesaikan verifikasi di browser, lalu tekan Enter

### Rate Limiting
- Kurangi jumlah unfollow per session
- Tambah jeda antar unfollow
- Tunggu beberapa jam sebelum menggunakan lagi

## 🔄 Update dan Maintenance

Instagram sering mengubah struktur HTML dan anti-bot detection. Jika script tidak berfungsi:

1. **Update dependencies**:
   ```bash
   pip install --upgrade selenium webdriver-manager
   ```

2. **Check for updates**: Periksa repository untuk versi terbaru

3. **Report issues**: Laporkan bug atau error yang ditemukan

## ⚖️ Legal dan Ethical Use

**⚠️ TANGGUNG JAWAB PENGGUNA:**
- **SEMUA RISIKO ditanggung pengguna sepenuhnya**
- **TIDAK ADA GARANSI** script akan bekerja tanpa masalah
- **TIDAK ADA DUKUNGAN** jika akun Anda bermasalah
- **GUNAKAN DENGAN BIJAK** dan siap menanggung konsekuensi

**Aturan Penggunaan:**
- ✅ Gunakan hanya pada akun tumbal/dummy Anda sendiri
- ✅ Patuhi Terms of Service Instagram
- ✅ Gunakan untuk pembelajaran dan automasi personal
- ✅ **SELALU test dengan akun yang tidak penting**
- ❌ Jangan gunakan untuk spam atau harassment
- ❌ Jangan jual atau distribusikan untuk tujuan komersial
- ❌ Jangan gunakan pada akun orang lain tanpa izin
- ❌ **Jangan pakai akun utama/bisnis/penting**

**🚨 SEKALI LAGI: AKUN BISA DI-BAN PERMANEN! 🚨**

## 📞 Support

Jika mengalami masalah:

1. **Baca troubleshooting section** di atas
2. **Check Instagram Terms of Service** terbaru
3. **Update script** ke versi terbaru
4. **Gunakan dengan bijak** dan bertanggung jawab

## 📝 Changelog

### Version 1.0 (Current)
- ✅ Initial release dengan modal-based unfollowing
- ✅ Improved error handling dan retry mechanism
- ✅ Anti-detection features
- ✅ Comprehensive logging

---

**⚠️ DISCLAIMER AKHIR**: 
- **GUNAKAN AKUN TUMBAL - BUKAN AKUN UTAMA!**
- **KAMI TIDAK BERTANGGUNG JAWAB** atas kerusakan akun atau konsekuensi negatif apapun
- **SEGALA RISIKO** sepenuhnya ditanggung pengguna
- **PAHAMI RISIKONYA** sebelum menggunakan script ini
- **Instagram automation = risiko tinggi account ban**
