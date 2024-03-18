import tkinter as tk
from tkinter import messagebox
import random

class SpelesGUI:
    def __init__(self, master):
        self.master = master
        master.configure(bg='beige')
        master.title("Dalīšanas Duelis: Skaitļu Cīņa")
        self.generet_sakuma_skaitlus()
        self.gajiens = 0  # Gājienu skaitītājs, lai noteiktu, kurš spēlētājs veic gājienu

    def generet_sakuma_skaitlus(self):
        self.skaitli = [random.randint(10000, 20000) for _ in range(100)]
        self.skaitli = [sk for sk in self.skaitli if sk % 6 == 0][:5]
        self.uzstadi_sakuma_skaitlu_izveles_saskarni()

    def uzstadi_sakuma_skaitlu_izveles_saskarni(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Izvēlies sākuma skaitli:", bg='beige').pack()

        for skaitlis in self.skaitli:
            poga = tk.Button(self.master, text=str(skaitlis),
                             command=lambda sk=skaitlis: self.uzstadi_speles_vidi(sk),
                             bg='tan', fg='white')
            poga.pack()

    def uzstadi_speles_vidi(self, sakuma_skaitlis):
        for widget in self.master.winfo_children():
            widget.destroy()

        self.skaitlis = sakuma_skaitlis
        self.p1_punkti = 0
        self.p2_punkti = 0
        self.bankas_punkti = 0

        self.atjaunot_ekranu()

    def dalit(self, dalitajs):
        self.gajiens += 1
        if self.skaitlis % dalitajs == 0:
            self.skaitlis //= dalitajs

            if self.skaitlis % 5 == 0:
                self.bankas_punkti += 1
            elif dalitajs == 2 or dalitajs == 3:
                if self.gajiens % 2 == 0:
                    self.p2_punkti += 1
                else:
                    self.p1_punkti += 1

            if self.skaitlis == 1:
                self.paradit_galarezultatu()
            else:
                self.atjaunot_ekranu()
        else:
            # Ja skaitlis vairs nedalās, tad tiek noteikts uzvarētājs
            if self.skaitlis % 2 == 0:  # Pāra skaitļa gadījumā
                if self.gajiens % 2 == 0:
                    self.p2_punkti += self.bankas_punkti
                else:
                    self.p1_punkti += self.bankas_punkti
            else:  # Nepāra skaitļa gadījumā
                if self.gajiens % 2 == 0:
                    self.p1_punkti += self.bankas_punkti
                else:
                    self.p2_punkti += self.bankas_punkti
            self.paradit_galarezultatu()

    def atjaunot_ekranu(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text=f"Pašreizējais skaitlis: {self.skaitlis}", bg='beige').pack()
        tk.Label(self.master, text=f"Spēlētāja 1 punkti: {self.p1_punkti}", bg='beige').pack()
        tk.Label(self.master, text=f"Spēlētāja 2 punkti: {self.p2_punkti}", bg='beige').pack()
        tk.Label(self.master, text=f"Bankā: {self.bankas_punkti}", bg='beige').pack()

        button_frame = tk.Frame(self.master, bg='beige')
        button_frame.pack()

        tk.Button(button_frame, text="Dalīt ar 2", command=lambda: self.dalit(2), bg='olive', fg='white').pack(side=tk.LEFT)
        tk.Button(button_frame, text="Dalīt ar 3", command=lambda: self.dalit(3), bg='olive', fg='white').pack(side=tk.LEFT)

    def paradit_galarezultatu(self):
        messagebox.showinfo("Spēle beigusies!", f"Spēle beigusies!\n1. Spēlētāja punkti: {self.p1_punkti}\n2. Spēlētāja punkti: {self.p2_punkti}\nBankā: {self.bankas_punkti}\nUzvarētājs: {'1. Spēlētājs' if self.p1_punkti > self.p2_punkti else '2. Spēlētājs'}")
        self.generet_sakuma_skaitlus()

root = tk.Tk()
app = SpelesGUI(root)
root.mainloop()
