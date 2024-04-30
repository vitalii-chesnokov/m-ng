import tkinter as tk
import random

def vali_sõna():
    with open("words.txt", "r", encoding="utf-8") as fail:
        sõnad = [rida.strip().lower() for rida in fail.readlines() if rida.strip()]
    return random.choice(sõnad)

def kontrolli_arvamist():
    arvamus = "".join([väli.get().strip().lower() 
    for väli in väljade_loend])
    õiged_positsioonid = sum(1 for i in range(len(valitud_sõna)) if arvamus[i] == valitud_sõna[i])
    õiged_tähed = sum(1 for täht in arvamus if täht in valitud_sõna) - õiged_positsioonid
    
    for väli in väljade_loend:
        väli.config(bg="#008080")

    for i in range(len(valitud_sõna)):
        täht = arvamus[i]
        if täht == valitud_sõna[i]:
            väljade_loend[i].config(fg="green")
        elif täht in valitud_sõna:
            väljade_loend[i].config(fg="yellow")
        else:
            väljade_loend[i].config(fg="black")

def vali_täht(täht):
    for väli in väljade_loend:
        if väli.get().strip() == "":
            väli.delete(0, tk.END)
            väli.insert(0, täht)
            break

aken = tk.Tk()
aken.title("Sõnade mäng")

valitud_sõna = vali_sõna()
sõna_pikkus = len(valitud_sõna)

sõna_vihje = f"Vihje: Sõna koosneb {sõna_pikkus} tähest."
juhend = tk.Label(aken,
                 text=sõna_vihje,
                 font="Helvetica 12")
väljade_loend = []
for i in range(sõna_pikkus):
    väli = tk.Entry(aken,
                   width=2,
                   font="Helvetica 24",
                   justify="center")
    väli.pack(side=tk.LEFT, padx=5)
    väljade_loend.append(väli)

nupp_kontrolli = tk.Button(aken,
                          text="Kontrolli",
                          font="Helvetica 16",
                          command=kontrolli_arvamist)

aruanne = tk.Label(aken,
                  text="",
                  font="Helvetica 16")
klaviatuur_raam = tk.Frame(aken)
tähed = "abcdefghijklmnopqrstuvwxyz"
for täht in tähed:
    nupp = tk.Button(klaviatuur_raam,
                    text=täht.upper(),
                    width=4,
                    height=2,
                    font="Helvetica 12",
                    command=lambda t=täht: vali_täht(t))
    nupp.grid(row=(ord(täht) - ord('a')) // 6, column=(ord(täht) - ord('a')) % 6)
nupp_kontrolli.pack(pady=20)
juhend.pack(pady=20)
klaviatuur_raam.pack(pady=20)
aruanne.pack(pady=20)
aken.mainloop()
