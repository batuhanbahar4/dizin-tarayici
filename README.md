# Dizin Tarayıcı (Directory Scanner)

Python ve `urllib` ile yazılmış basit bir web dizin tarayıcısı. dirb/gobuster gibi araçların temel mantığını anlamak için geliştirildi.

## Ne yapar?
- Bir kelime listesindeki yolları hedef adrese tek tek istek atarak dener
- Bulunan yolları `[+]`, bulunamayanları `[-]` ile raporlar
- Sunucuya ulaşılamazsa taramayı güvenli şekilde durdurur

## Örnek çıktı
```
[+] BULUNDU 200 http://127.0.0.1:8000/admin
[-] 404 http://127.0.0.1:8000/login
[-] 404 http://127.0.0.1:8000/backup
[+] BULUNDU 200 http://127.0.0.1:8000/gizli.txt
[-] 404 http://127.0.0.1:8000/test
```

## Öğrendiklerim
- `try/except` ile hata yakalama
- `HTTPError` (sunucu cevap verdi: 404, 403...) ile `URLError` (sunucuya ulaşılamadı) farkı
- Liste + `for` döngüsü ile otomasyon

## Kullanım
```bash
python3 -m http.server 8000      # test sunucusu
python3 dizin_tarayici.py
```

⚠️ Sadece kendi sistemlerinizde veya izinli ortamlarda kullanın.
