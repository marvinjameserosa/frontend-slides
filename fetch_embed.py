import urllib.request
import re

url = "https://www.instagram.com/p/DYBMtXxisip/embed/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print("Embed HTML len:", len(html))
        # Look for images in embed
        imgs = re.findall(r'<img[^>]+src="([^">]+)"', html)
        print("Embed images found:", len(imgs))
        for img in imgs:
            clean = img.replace('&amp;', '&')
            print("IMG:", clean)
except Exception as e:
    print("Embed error:", e)
