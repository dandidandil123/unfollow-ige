# Instagram Unfollower Bot - Modal Version

Automated Instagram unfollower bot yang menggunakan Selenium WebDriver untuk melakukan unfollow secara batch dari modal following list.

## ⚠️ Disclaimer

**PENTING**: Bot ini dibuat untuk tujuan edukasi dan pembelajaran. Penggunaan bot untuk automasi Instagram dapat melanggar Terms of Service Instagram dan berisiko menyebabkan akun Anda dibatasi atau di-suspend.

**🚨 GUNAKAN AKUN TUMBAL - JANGAN AKUN UTAMA! 🚨**

Buat akun Instagram dummy khusus untuk testing. Risiko account ban/suspend sangat tinggi.

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

1. **Clone repository**
   ```bash
   git clone https://github.com/dandidandil123/unfollow-ige.git
   cd unfollow-ige
   ```

2. **Install dependencies manual**
   ```bash
   pip install selenium webdriver-manager
   ```

## 🚀 Cara Penggunaan

### Menjalankan Script

```bash
python unfollowe.py
```

### Input yang Diperlukan

1. **Username Instagram**: Username akun Instagram (gunakan akun dummy untuk safety)
2. **Password Instagram**: Password akun (input tersembunyi untuk keamanan)
3. **Jumlah Unfollow**: Maksimal jumlah akun yang ingin di-unfollow (disarankan 10-50 untuk keamanan)

### Contoh Penggunaan

```
=== Instagram Unfollower Modal (Fixed Version) ===
📧 Username Instagram: your_username
🔑 Password Instagram (tidak akan terlihat): 
📊 Berapa maksimal unfollow (misal 10-50): 25
```

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

**Aturan Penggunaan:**
- ✅ Gunakan hanya pada akun Anda sendiri
- ✅ Patuhi Terms of Service Instagram
- ✅ Gunakan untuk pembelajaran dan automasi personal
- ❌ Jangan gunakan untuk spam atau harassment
- ❌ Jangan jual atau distribusikan untuk tujuan komersial
- ❌ Jangan gunakan pada akun orang lain tanpa izin

**Catatan**: Penggunaan automation tools Instagram memiliki risiko tinggi. Pastikan Anda memahami konsekuensinya.

## 📞 Support

Jika mengalami masalah:

1. **Baca troubleshooting section** di atas
2. **Check Instagram Terms of Service** terbaru
3. **Update script** ke versi terbaru
4. **Buka issue** di [GitHub repository](https://github.com/dandidandil123/unfollow-ige/issues)
5. **Gunakan dengan bijak** dan bertanggung jawab

## 📝 Changelog

### Version 1.0 (Current)
- ✅ Initial release dengan modal-based unfollowing
- ✅ Improved error handling dan retry mechanism
- ✅ Anti-detection features
- ✅ Comprehensive logging

---

**⚠️ Reminder**: Selalu gunakan automation tools dengan bijak dan bertanggung jawab. Instagram memiliki sistem deteksi bot yang canggih, jadi selalu prioritaskan keamanan akun Anda.
