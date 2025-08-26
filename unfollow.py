#!/usr/bin/env python3
"""
Instagram Unfollower Bot - Modal Version (Fixed)
- Login dengan error handling yang lebih baik
- Buka profil & klik link Following
- Unfollow langsung dari modal list (lebih cepat & efisien)
"""

import time, random, getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class InstagramUnfollower:
    def __init__(self, username, headless=False):
        self.driver = None
        self.wait = None
        self.headless = headless
        self.username = username

    def setup_driver(self):
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        self.wait = WebDriverWait(self.driver, 20)
        print("✅ Chrome driver initialized")

    def login(self, password):
        try:
            print("🌐 Membuka Instagram...")
            self.driver.get("https://www.instagram.com/")
            time.sleep(5)

            # Cek dan dismiss cookie notice jika ada
            try:
                cookie_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Accept') or contains(text(), 'Allow')]")
                cookie_btn.click()
                time.sleep(2)
            except NoSuchElementException:
                pass

            print("📧 Mengisi username dan password...")
            
            # Tunggu form login muncul
            user_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            pass_input = self.driver.find_element(By.NAME, "password")

            # Clear dan isi form
            user_input.clear()
            pass_input.clear()
            
            user_input.send_keys(self.username)
            time.sleep(1)
            pass_input.send_keys(password)
            time.sleep(1)
            
            # Klik tombol login
            login_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            login_btn.click()
            
            print("⏳ Menunggu login...")
            time.sleep(8)

            # Cek apakah ada challenge atau error
            current_url = self.driver.current_url
            print(f"Current URL: {current_url}")
            
            if "challenge" in current_url:
                print("⚠️ Login challenge detected! Harus verifikasi manual.")
                input("Selesaikan verifikasi manual, lalu tekan Enter...")
                return True
                
            # Cek apakah login berhasil (ada elemen yang menandakan login berhasil)
            try:
                # Tunggu hingga halaman home muncul atau ada elemen yang menandakan login berhasil
                self.wait.until(EC.any_of(
                    EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/direct')]")),
                    EC.presence_of_element_located((By.XPATH, "//svg[@aria-label='Home']")),
                    EC.presence_of_element_located((By.XPATH, "//span[text()='Home']"))
                ))
                print("✅ Login berhasil!")
                
                # Handle popup "Save login info" jika muncul
                try:
                    not_now_btn = self.driver.find_element(By.XPATH, "//button[text()='Not Now' or text()='Tidak Sekarang']")
                    not_now_btn.click()
                    time.sleep(2)
                except NoSuchElementException:
                    pass
                    
                # Handle popup notifikasi jika muncul
                try:
                    not_now_btn = self.driver.find_element(By.XPATH, "//button[text()='Not Now' or text()='Tidak Sekarang']")
                    not_now_btn.click()
                    time.sleep(2)
                except NoSuchElementException:
                    pass
                
                return True
                
            except TimeoutException:
                # Cek apakah ada error message
                try:
                    error_msg = self.driver.find_element(By.XPATH, "//div[contains(text(), 'incorrect') or contains(text(), 'salah')]")
                    print(f"❌ Login gagal: {error_msg.text}")
                    return False
                except NoSuchElementException:
                    print("❌ Login gagal - timeout waiting for homepage")
                    return False

        except Exception as e:
            print(f"❌ Error saat login: {e}")
            return False

    def open_following_modal(self):
        try:
            print("📋 Membuka halaman profil...")

            # Buka halaman profil
            profile_url = f"https://www.instagram.com/{self.username}/"
            self.driver.get(profile_url)
            time.sleep(5)

            # Tunggu halaman profil load
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//header")))
            print("✅ Halaman profil terbuka")

            # Cari dan klik link "Following"
            print("🔍 Mencari link Following...")
            following_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/following')]"))
            )
            
            print("👆 Mengklik link Following...")
            self.driver.execute_script("arguments[0].click();", following_link)
            time.sleep(3)

            # Tunggu modal muncul
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
            print("✅ Modal Following terbuka")
            time.sleep(2)
            return True

        except Exception as e:
            print(f"❌ Error membuka following modal: {e}")
            return False

    def unfollow_user_from_modal(self, btn):
        try:
            # Scroll ke button untuk memastikan terlihat
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
            time.sleep(1)
            
            # Klik tombol Following / Mengikuti
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(2)

            # Tunggu dan klik konfirmasi Unfollow
            confirm_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[text()='Unfollow' or text()='Berhenti mengikuti']")
                )
            )
            self.driver.execute_script("arguments[0].click();", confirm_btn)
            time.sleep(1)
            return True

        except Exception as e:
            print(f"⚠️ Gagal unfollow: {e}")
            return False

    def safe_unfollow_batch(self, max_unfollows=10):
        count = 0
        consecutive_failures = 0
        
        print(f"🚀 Memulai unfollow batch (max: {max_unfollows})")
        
        while count < max_unfollows and consecutive_failures < 5:
            try:
                # Tunggu sebentar untuk load
                time.sleep(2)
                
                # Cari semua tombol Following/Mengikuti di modal
                buttons = self.driver.find_elements(
                    By.XPATH, "//button[contains(., 'Following') or contains(., 'Mengikuti')]"
                )

                if not buttons:
                    print("⚠️ Tidak ada tombol Following lagi atau modal tertutup.")
                    break

                # Ambil user teratas yang masih ada
                btn = buttons[0]
                
                # Coba ambil nama user untuk log
                try:
                    user_container = btn.find_element(By.XPATH, "./../../..")
                    username = user_container.find_element(By.XPATH, ".//a").text
                    print(f"🎯 Mencoba unfollow: {username}")
                except:
                    print(f"🎯 Mencoba unfollow user ke-{count + 1}")
                
                success = self.unfollow_user_from_modal(btn)

                if success:
                    count += 1
                    consecutive_failures = 0
                    print(f"✅ Berhasil unfollow {count}/{max_unfollows}")
                    
                    # Jeda random untuk keamanan
                    delay = random.uniform(4, 8)
                    print(f"⏳ Jeda {delay:.1f} detik...")
                    time.sleep(delay)
                else:
                    consecutive_failures += 1
                    print(f"⚠️ Gagal unfollow (percobaan {consecutive_failures}/5)")
                    time.sleep(3)

                # Scroll modal untuk load user baru
                modal = self.driver.find_element(By.XPATH, "//div[@role='dialog']")
                self.driver.execute_script("arguments[0].scrollTop += 300;", modal)
                time.sleep(2)

            except Exception as e:
                consecutive_failures += 1
                print(f"⚠️ Error dalam loop: {e}")
                print(f"Percobaan gagal berturut-turut: {consecutive_failures}/5")
                time.sleep(3)

        if consecutive_failures >= 5:
            print("❌ Terlalu banyak error berturut-turut, menghentikan proses")
        
        print(f"🎉 Selesai! Total unfollow: {count}")

    def close(self):
        if self.driver:
            print("🔒 Menutup browser...")
            self.driver.quit()


def main():
    print("=== Instagram Unfollower Modal (Fixed Version) ===")
    
    try:
        username = input("📧 Username Instagram: ").strip()
        password = getpass.getpass("🔑 Password Instagram (tidak akan terlihat): ").strip()
        
        if not username or not password:
            print("❌ Username dan password harus diisi!")
            return
            
        max_unfollow = int(input("📊 Berapa maksimal unfollow (misal 10-50): "))
        
        if max_unfollow <= 0:
            print("❌ Jumlah unfollow harus lebih dari 0!")
            return

        bot = InstagramUnfollower(username, headless=False)
        bot.setup_driver()

        # Login
        if not bot.login(password):
            print("❌ Login gagal, script dihentikan")
            bot.close()
            return

        # Buka following modal
        if not bot.open_following_modal():
            print("❌ Gagal membuka following modal")
            bot.close()
            return

        # Mulai unfollow
        bot.safe_unfollow_batch(max_unfollow)
        
        print("✅ Script selesai!")
        input("Tekan Enter untuk menutup browser...")
        bot.close()

    except KeyboardInterrupt:
        print("\n⚠️ Script dihentikan oleh user")
        if 'bot' in locals():
            bot.close()
    except Exception as e:
        print(f"❌ Error tak terduga: {e}")
        if 'bot' in locals():
            bot.close()


if __name__ == "__main__":
    main()