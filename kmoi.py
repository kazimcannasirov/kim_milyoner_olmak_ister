import tkinter as tk
from tkinter import messagebox
import random
import winsound

# ---------------- SESLER ----------------
def dogru_ses(): winsound.MessageBeep(winsound.MB_ICONASTERISK)
def yanlis_ses(): winsound.MessageBeep(winsound.MB_ICONHAND)
def joker_ses(): winsound.MessageBeep(winsound.MB_ICONQUESTION)

# ---------------- 20 GERÇEK SORU ----------------
sorular = [
    {"soru": "Türkiye'nin başkenti neresidir?", "secenekler": ["İstanbul", "Ankara", "İzmir", "Bursa"], "cevap": 1},
    {"soru": "Atatürk kaç yılında doğmuştur?", "secenekler": ["1879", "1880", "1881", "1882"], "cevap": 2},
    {"soru": "Dünyanın en büyük okyanusu hangisidir?", "secenekler": ["Atlas", "Hint", "Arktik", "Pasifik"], "cevap": 3},
    {"soru": "En hızlı kara hayvanı hangisidir?", "secenekler": ["Aslan", "Kaplan", "Çita", "Leopar"], "cevap": 2},
    {"soru": "Su kaç derecede kaynar?", "secenekler": ["90", "95", "100", "110"], "cevap": 2},

    {"soru": "Türkiye kaç coğrafi bölgeden oluşur?", "secenekler": ["5", "6", "7", "8"], "cevap": 2},
    {"soru": "Ay'a ilk ayak basan insan kimdir?", "secenekler": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Armstrong Jr."], "cevap": 1},
    {"soru": "HTML ne için kullanılır?", "secenekler": ["Oyun", "Web", "Veritabanı", "İşletim"], "cevap": 1},
    {"soru": "En büyük gezegen hangisidir?", "secenekler": ["Mars", "Venüs", "Jüpiter", "Satürn"], "cevap": 2},
    {"soru": "Python hangi tür bir dildir?", "secenekler": ["Donanım", "Programlama", "Tasarım", "Oyun"], "cevap": 1},

    {"soru": "İstiklal Marşı'nın yazarı kimdir?", "secenekler": ["Nazım Hikmet", "Mehmet Akif Ersoy", "Tevfik Fikret", "Yahya Kemal"], "cevap": 1},
    {"soru": "Dünyanın en uzun nehri hangisidir?", "secenekler": ["Amazon", "Nil", "Fırat", "Mississippi"], "cevap": 1},
    {"soru": "Türkiye'nin para birimi nedir?", "secenekler": ["Dolar", "Euro", "TL", "Sterlin"], "cevap": 2},
    {"soru": "İnsan vücudunda kaç kemik vardır?", "secenekler": ["200", "206", "210", "215"], "cevap": 1},
    {"soru": "En büyük kıta hangisidir?", "secenekler": ["Afrika", "Avrupa", "Asya", "Amerika"], "cevap": 2},

    {"soru": "Einstein hangi alanla ilgilidir?", "secenekler": ["Kimya", "Biyoloji", "Fizik", "Matematik"], "cevap": 2},
    {"soru": "Hangi gezegen Güneş'e en yakındır?", "secenekler": ["Venüs", "Dünya", "Merkür", "Mars"], "cevap": 2},
    {"soru": "Osmanlı Devleti'nin kurucusu kimdir?", "secenekler": ["Osman Bey", "Orhan Bey", "Fatih Sultan Mehmet", "Yavuz Sultan Selim"], "cevap": 0},
    {"soru": "DNA'nın açılımı nedir?", "secenekler": ["Deoksiribo Nükleik Asit", "Dinamik Nükleer Asit", "Doğal Asit", "Nükleer Asit"], "cevap": 0},
    {"soru": "Türkiye hangi kıtalar arasında yer alır?", "secenekler": ["Asya-Afrika", "Avrupa-Afrika", "Asya-Avrupa", "Amerika-Asya"], "cevap": 2}
]

# ---------------- DEĞİŞKENLER ----------------
index = 0
para = 0
baraj = 0

joker_5050 = joker_seyirci = joker_telefon = True

para_listesi = [
    0, 1000, 2000, 3000, 5000,
    10000, 20000, 30000, 50000, 75000,
    150000, 250000, 500000, 750000, 1000000,
    1500000, 2000000, 2500000, 3000000, 5000000
]

# ---------------- FONKSİYONLAR ----------------
def soruyu_goster():
    soru_label.config(text=sorular[index]["soru"])
    for i in range(4):
        secenekler[i].config(
            text=f"{chr(65+i)}: {sorular[index]['secenekler'][i]}",
            state="normal",
            bg="#1e3a8a"
        )
    durum_label.config(
        text=f"Soru {index+1}/20 | Para: {para} TL | Baraj: {baraj} TL"
    )

def cevapla(secim):
    global index, para, baraj
    if secim == sorular[index]["cevap"]:
        dogru_ses()
        secenekler[secim].config(bg="green")
        pencere.after(600, dogru_devam)
    else:
        yanlis_ses()
        messagebox.showerror("Yanlış", f"Oyun bitti!\nKazancın: {baraj} TL")
        pencere.destroy()

def dogru_devam():
    global index, para, baraj
    para = para_listesi[index+1]
    if index+1 in (5, 10):
        baraj = para
    index += 1
    if index == 20:
        messagebox.showinfo("Tebrikler", f"🏆 Büyük Ödül!\n{para} TL")
        pencere.destroy()
    else:
        soruyu_goster()

# ---------------- JOKERLER ----------------
def joker_5050_f():
    global joker_5050
    if not joker_5050: return
    joker_ses()
    joker_5050 = False
    dogru = sorular[index]["cevap"]
    sil = [i for i in range(4) if i != dogru]
    random.shuffle(sil)
    for i in sil[:2]:
        secenekler[i].config(state="disabled")

def joker_seyirci_f():
    global joker_seyirci
    if not joker_seyirci: return
    joker_ses()
    joker_seyirci = False
    dogru = sorular[index]["cevap"]
    oran = [random.randint(5, 20) for _ in range(4)]
    oran[dogru] += 40
    mesaj = "\n".join(f"{chr(65+i)}: %{oran[i]}" for i in range(4))
    messagebox.showinfo("Seyirci", mesaj)

def joker_telefon_f():
    global joker_telefon
    if not joker_telefon: return
    joker_ses()
    joker_telefon = False
    dogru = sorular[index]["cevap"]
    messagebox.showinfo("Telefon", f"📞 Bence cevap {chr(65+dogru)}")

# ---------------- TKINTER TASARIM ----------------
pencere = tk.Tk()
pencere.title("Kim Milyoner Olmak İster?")
pencere.geometry("900x600")
pencere.config(bg="#020617")

tk.Label(
    pencere,
    text="KİM MİLYONER OLMAK İSTER?",
    font=("Arial Black", 22),
    fg="gold",
    bg="#020617"
).pack(pady=15)

soru_label = tk.Label(
    pencere,
    text="",
    font=("Arial", 16),
    fg="white",
    bg="#020617",
    wraplength=800
)
soru_label.pack(pady=20)

secenekler = []
for i in range(4):
    b = tk.Button(
        pencere,
        font=("Arial", 13, "bold"),
        fg="white",
        bg="#1e3a8a",
        width=45,
        height=2,
        command=lambda i=i: cevapla(i)
    )
    b.pack(pady=6)
    secenekler.append(b)

durum_label = tk.Label(
    pencere,
    font=("Arial", 12),
    fg="#facc15",
    bg="#020617"
)
durum_label.pack(pady=10)

joker_frame = tk.Frame(pencere, bg="#020617")
joker_frame.pack()

tk.Button(joker_frame, text="50:50", width=10, command=joker_5050_f).pack(side="left", padx=5)
tk.Button(joker_frame, text="Seyirci", width=10, command=joker_seyirci_f).pack(side="left", padx=5)
tk.Button(joker_frame, text="Telefon", width=10, command=joker_telefon_f).pack(side="left", padx=5)

soruyu_goster()
pencere.mainloop()
