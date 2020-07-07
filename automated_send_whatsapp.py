# Author = Salim Suprayogi
# Diharapkan saran dan masukan untuk bisa berkembang dan lebih maju bagi author

# selenium.webdriver module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import module datetime
from datetime import datetime
# import module random
import random
# import module time
import time


def automated_wa():
    # geckodriver sebagai proxy untuk browser
    # lokasi driver di lokal
    driver = webdriver.Firefox(executable_path=r"C:/geckodriver.exe")
    # driver = webdriver.Chrome(executable_path=r"C:/chromedriver.exe") # browser chrome

    # arahkan halaman yang akan di buka
    driver.get("https://web.whatsapp.com/")
    # scan barcode whatsapp setelah muncul url tersebut
    # menunggu
    time.sleep(10)

    # mencari nama kontak whatsapp
    text_search_name = "ubah_nama_kontak_disini"
    # interaksi elemen bidang pencarian nama kontak
    search = driver.find_element_by_xpath("//div[@data-tab='3']")
    # interaksi elemen untuk action enter
    search.send_keys(text_search_name + Keys.ENTER)

    time.sleep(5)

    '''
    case : "10 kata 60 karakter 51 karakter tanpa spasi
    '''

    # mencari bidang pesan whatsapp
    search = driver.find_element_by_xpath("//div[@data-tab='1']")
    # input text di dalam bidang pesan whatsapp
    # untuk indikator pesan / input mulai
    search.send_keys(
        "A ===start=== char 50, 100, 150, 160, 180, 200, 220, 250, 300, 350 ", str(datetime.now()))
    search.send_keys(Keys.RETURN)

    time.sleep(5)

    # membaca file .txt
    try:
        # lokasi dimana file tersebut berada (ubah lokasi ini sesuai lokasi file txt)
        text_in = "C:/cerita_anak.txt"
        # open file, dengan mode read dan character set "utf-8" agar bisa memahami karakter dari berbagai bahasa
        f = open(text_in, "r", encoding="utf-8")
        # baca file .txt
        data = f.read()
        # pesan yang yang di inputkan didalam bidang pesan whatsapp
        a = 0
        i = 0
        # ubah [2] untuk menentukan berapa banyak pesan yang diinginkan
        while a < 2:
            char = [50, 100, 150, 160, 180, 200, 220, 250, 300, 350]
            # enumarete() : mengembalikan objek enumerate yaitu objek iterable yang tiap itemnya berpasangan dengan indeks
            for indeks, val in enumerate(char):
                # datetime.now() : munujukan waktu realtime
                # ubah menjadi tipe data string str()
                today = str(datetime.now())
                i = i + 1
                search.send_keys(i, ")", today, ")", data[:val])
                search.send_keys(Keys.RETURN)
            a = a + 1
    finally:
        # close file .txt
        f.close()

    # untuk indikator pesan / input sudah selesai
    search.send_keys(
        "B ===end=== char 50, 100, 150, 160, 180, 200, 220, 250, 300, 350 ", str(datetime.now()))
    search.send_keys(Keys.RETURN)

    # close browser
    driver.close()


if __name__ == "__main__":
    # menjalankan fungsi automated_wa()
    automated_wa()
