import urllib.request
import urllib.error

hedef = "http://127.0.0.1:8000/"
yollar = ["admin", "login", "backup", "gizli.txt", "test"]

for yol in yollar:
    url = hedef + yol
    try:
        cevap = urllib.request.urlopen(url)
        print("[+] BULUNDU", cevap.status, url)
    except urllib.error.HTTPError as hata:
        print("[-]", hata.code, url)
    except urllib.error.URLError as hata:
        print("[!] Sunucuya ulaşılamadı:", hata.reason)
        break