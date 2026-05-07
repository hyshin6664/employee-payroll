"""급여대장 PNG 아이콘 (192/256/512). 보라색 + '급여' 큰글씨 + '대장' 서브."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\malgunbd.ttf",
    r"C:\Windows\Fonts\malgun.ttf",
]

def find_font():
    for f in FONT_CANDIDATES:
        if os.path.exists(f):
            return f
    raise RuntimeError("한글 폰트 못 찾음")

def make(size, fname):
    img = Image.new("RGBA",(size,size),(0,0,0,0))
    d = ImageDraw.Draw(img)
    radius = int(size*0.18)
    d.rounded_rectangle([(0,0),(size,size)], radius=radius, fill=(124,58,237,255))  # 보라
    pad = int(size*0.16)
    d.rounded_rectangle([(pad,pad),(size-pad,size-pad)], radius=int(size*0.07), fill=(255,255,255,255))
    # 상단 줄(장부 느낌)
    bar_h = int(size*0.20)
    bar_pad = int(size*0.04)
    d.rounded_rectangle([(pad+bar_pad,pad+bar_pad),(size-pad-bar_pad,pad+bar_pad+bar_h)],
                        radius=int(size*0.025), fill=(15,23,42,255))
    fp = find_font()
    # ₩ 표시
    won_font = ImageFont.truetype(fp, int(bar_h*0.7))
    bb = d.textbbox((0,0),"₩",font=won_font); ww=bb[2]-bb[0]; wh=bb[3]-bb[1]
    d.text((size-pad-bar_pad-ww-int(size*0.025), pad+bar_pad+(bar_h-wh)//2-int(size*0.01)),
           "₩",font=won_font, fill=(167,139,250,255))

    body_top = pad+bar_pad+bar_h+int(size*0.03)
    body_bot = size-pad-bar_pad
    body_h = body_bot - body_top
    cx = size//2

    txt = "급여"
    font = ImageFont.truetype(fp, int(body_h*0.55))
    bb = d.textbbox((0,0),txt,font=font); tw=bb[2]-bb[0]; th=bb[3]-bb[1]
    ty = body_top + int(body_h*0.05)
    d.text((cx - tw//2 - bb[0], ty - bb[1]), txt, font=font, fill=(124,58,237,255))

    sub = "대장"
    sf = ImageFont.truetype(fp, int(body_h*0.22))
    sb = d.textbbox((0,0),sub,font=sf); sw=sb[2]-sb[0]; sh=sb[3]-sb[1]
    sy = body_bot - sh - int(body_h*0.05)
    d.text((cx - sw//2 - sb[0], sy - sb[1]), sub, font=sf, fill=(100,116,139,255))

    out = os.path.join(OUT_DIR, fname)
    img.save(out,"PNG")
    print(f"saved {out}")

make(192,"icon-192.png")
make(256,"icon-256.png")
make(512,"icon-512.png")
