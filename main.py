"""Entri satu kata untuk bounty "The Internet in One Word".

Kenapa "brainrot"? Karena itulah gambaran internet hari ini dalam
satu kata yang jujur dan kocak: semua orang scroll tanpa henti, otak
pelan-pelan meleleh kena meme absurd, tren aneh, dan video pendek
yang tidak ada habisnya — lalu mereka tetap balik lagi besok, dengan
senang hati. Satu kata, tapi langsung kena: internet modern itu
bukan lagi soal informasi, melainkan soal hiburan yang bikin
ketagihan sampai isi kepala terasa digoreng. Brainrot merangkum itu
semua — kekonyolan, kecanduan scroll, dan budaya meme — tanpa perlu
kalimat panjang. Dan yang paling lucu: kata ini sendiri lahir dari
internet, jadi internet sedang menggambarkan dirinya sendiri.
"""

import os
import re

ANSWER = "brainrot"

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def _check(word: str) -> str:
    """Pastikan yang ditulis tepat satu kata huruf saja.

    Menolak string kosong, kata yang mengandung angka atau spasi,
    dan apa pun yang bukan satu kata utuh — supaya output tidak
    pernah melanggar aturan bounty.
    """
    cleaned = word.strip()
    if not cleaned:
        raise ValueError("entri tidak boleh kosong")
    if not re.fullmatch(r"[A-Za-z]+", cleaned):
        raise ValueError("entri harus tepat satu kata huruf saja")
    if cleaned != cleaned.lower():
        raise ValueError("entri harus huruf kecil semua")
    return cleaned


def main() -> None:
    word = _check(ANSWER)
    os.makedirs(OUT_DIR, exist_ok=True)
    target = os.path.join(OUT_DIR, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(word + "\n")


if __name__ == "__main__":
    main()
