import tkinter as tk
from tkinter import messagebox
import random
import math
#from numpy import Infinity
import time 


#Klase kas atbilst virsotnei
class Virsotne:

    def __init__(self,child, id, skaitlis, p1, p2,bank, limenis, heir_funkcija):
        self.child = child # virsotnes bērni
        self.id = id # virsotnes id, lai meklētu vecāku
        self.skaitlis = skaitlis # šobrid skaitlis
        self.p1 = p1 # datora punkti
        self.p2 = p2 # otra cilvēka punkti
        self.bank = bank # kas šobrīd atrodas bankā
        self.limenis = limenis # līmenis, uz kura atrodas virsotne
        self.heir_funkcija = heir_funkcija # Heiristiskā funkcija

#Klase, kas atbilst spēles kokam        
class Speles_koks:

    # Inicializējam, ka koks būs List datustruktūra
    def __init__(self):
        self.virsotnu_kopa=[]
    #Klases Speles_koks metode,
    #kas pievieno spēles kokam jaunu virsotni, 
    #kuru saņem kā argumentu
    def pievienot_virsotni(self, Virsotne):
        self.virsotnu_kopa.append(Virsotne)

#Funkcija, kas skaita, cik dalītāju ir virsotnei 
#Ir skaitītie cik ir dalītāju - 2, 3, 5
def count_2_3_5(skaitlis):
  c2 = 0 # cik daudz dalītāju = 2
  c3 = 0 # cik daudz dalītāju = 3
  c5 = 0 # cik daudz dalītāju = 5
  while True:
    if skaitlis%5 == 0:
      c5 = c5 + 1
    if skaitlis%2 == 0:
      c2 = c2 + 1
      skaitlis = skaitlis/2
    elif skaitlis%3 == 0:
      c3 = c3 + 1
      skaitlis = skaitlis/3
    else:
      return c2, c3, c5

#Funkcija, kas aprēķina Heiristisko vērtību
def heir_funkcija(tek_virsotne):
  heir_vert = 0
  heir_vert = heir_vert + (tek_virsotne.p1-tek_virsotne.p2) # punktu skaita starpība
  list = count_2_3_5(tek_virsotne.skaitlis)#satur informāciju par dalītājiem
  #Pārbauda vai spēlē tiek izmantots banks
  if tek_virsotne.bank != 0: 
    skaitlis = tek_virsotne.skaitlis/((2**list[0])*(3**list[1]))
    # Galīgs skaitlis nav 2 vai 3
    if (skaitlis > 3):
      # para limenis  + para skaitlis  & nepara limenis + nepara skaitlis  = datoram
      # nepara limenis  + para skaitlis  & para limenis + nepara skaitlis  = cilvēkam

      #tek_virsotne.limenis + list[0]+list[1] = cik daudz līmeņu vēl būs
      #tek_virsotne.bank + list[2] = cik daudz banks biegās
      if (( (tek_virsotne.limenis + list[0]+list[1]) % 2 == 0 and skaitlis%2 != 0) or ( ( tek_virsotne.limenis + list[0]+list[1]) % 2 != 0 and skaitlis%2 == 0)):
        heir_vert = heir_vert + tek_virsotne.bank + list[2]
      else:
        heir_vert = heir_vert - tek_virsotne.bank - list[2]+1
    # Galīgs skaitlis ir 2 vai 3
    else :
      if ((tek_virsotne.limenis +list[0]+list[1])%2 != 0):
        heir_vert = heir_vert + tek_virsotne.bank + list[2]
      else:
        heir_vert = heir_vert - tek_virsotne.bank - list[2]+1
  return heir_vert

#Funkcija, kas mēkle labāko gajienu
def make_best_move(state):
  #Vertības inicializācija
  bestScore = -math.inf
  bestMove = None
  #Virsotnes bērnu salīdzīnašāna
  for child_id in state.child:
    child = sp.virsotnu_kopa[child_id]
    score = sp.virsotnu_kopa[child_id].heir_funkcija
    if (score > bestScore):
      bestScore = score
      bestMove = child_id
  #Atgriež labāko gajienu
  return bestMove

#Algoritma Minimax realizācija
def minimax(isMaxTurn, state):
  #global count_virsotnes #skaita apmeklētas vīrsotnes
  #count_virsotnes = count_virsotnes + 1
  #isMaxTurn mainīgais - satur true/false vērtību,
  #kas norāda, vai ir maksimezētājā gājiens.
  #state - pašreizējā virsotne
  if len(state.child) == 0:
    #piešķir heiristisko vertējumu strupceļam
    state.heir_funkcija = heir_funkcija(state)
    return state.heir_funkcija

  scores = []
  for child_id in state.child:
    child = sp.virsotnu_kopa[child_id]
    scores.append(minimax(not isMaxTurn, child))
  #Balstoties uz isMaxTurn mainīgo, izvēlas,
  #ka izveleties heiristisko vertību, kuru pacelt
  if isMaxTurn:
    max_score = max(scores)
    state.heir_funkcija = max_score
    return max_score
  else:
    min_score = min(scores)
    state.heir_funkcija = min_score
    return min_score

#Algoritms Alfa Beta realizācija
def alpha_beta(isMaxTurn, state, alpha, beta):
  #global count_virsotnes
  #isMaxTurn mainīgais - satur true/false vērtību,
  #kas norāda, vai ir maksimezētājā gājiens.
  #state - pašreizējā virsotne
  #count_virsotnes = count_virsotnes + 1 #skaita apmeklētas vīrsotnes
  if len(state.child) == 0:
      #piešķir heiristisko vertējumu strupceļam
      state.heir_funkcija = heir_funkcija(state)
      return state.heir_funkcija
  #Balstoties uz isMaxTurn mainīgo, izvēlas,
  #ka izveleties heiristisko vertību, kuru pacelt
  if isMaxTurn:
      max_score = float("-inf")
      for child_id in state.child:
          child = sp.virsotnu_kopa[child_id]
          score = alpha_beta(not isMaxTurn, child, alpha, beta)
          max_score = max(max_score, score)
          alpha = max(alpha, max_score)
          #nogrieziena realizācija
          if beta <= alpha:
              break
      state.heir_funkcija = max_score
      return max_score
  else:
      min_score = float("inf")
      for child_id in state.child:
          child = sp.virsotnu_kopa[child_id]
          score = alpha_beta(not isMaxTurn, child, alpha, beta)
          min_score = min(min_score, score)
          beta = min(beta, min_score)
          #nogrieziena realizācija
          if beta <= alpha:
              break
      state.heir_funkcija = min_score
      return min_score

#Algoritms gajiena uztaisīšanai
def gajiena_parbaude (gajiena_tips, pasreizeja_virsotne):
    # Pārbaude vai skaitlis dalas ar 2, ja nē tad iziet no funkcijas
    skaitlis = 0 #skaitļa vērtības inicializācija
    if gajiena_tips == '2':
        if pasreizeja_virsotne.skaitlis % 2 == 0:
           skaitlis = int(pasreizeja_virsotne.skaitlis/2)
        else:
           return
    # Pārbaude vai skaitlis dalas ar 3, ja nē tad iziet no funkcijas
    if gajiena_tips == '3':
        if pasreizeja_virsotne.skaitlis % 3 == 0:
           skaitlis = int(pasreizeja_virsotne.skaitlis/3)
        else:
           return    
    # Pārbaude vai galīgs skaitlis, ja nē tad taisa jauno virsotni  
    if  pasreizeja_virsotne.skaitlis != 2 and pasreizeja_virsotne.skaitlis != 3:

        limenis = pasreizeja_virsotne.limenis + 1
        id = len(sp.virsotnu_kopa)

        bank = pasreizeja_virsotne.bank
        p1 = pasreizeja_virsotne.p1
        p2 = pasreizeja_virsotne.p2
        heir_funkcija = 0

        # Punktu piešķiršana
        if skaitlis % 5 == 0:
            bank = bank + 1
        if skaitlis % 2 == 0:
            match limenis%2:
                case 1:
                    p1 = p1+1
                case 0:
                    p2 = p2+1
        else :
            match limenis%2:
                case 1:
                    p1 = p1-1
                case 0:
                    p2 = p2-1
            # Pārbaude vai tāda virsotne jau eksistē vienā līmenī
        i = 0
        while i < len(sp.virsotnu_kopa):
           if sp.virsotnu_kopa[i].skaitlis == skaitlis and sp.virsotnu_kopa[i].p1 == p1 and sp.virsotnu_kopa[i].p2 == p2 and sp.virsotnu_kopa[i].bank == bank and sp.virsotnu_kopa[i].limenis == limenis:
               sp.virsotnu_kopa[pasreizeja_virsotne.id].child.append(sp.virsotnu_kopa[i].id)
               return
           else:
               i = i + 1
        jauna_virsotne=Virsotne([], id, skaitlis, p1, p2, bank, limenis, heir_funkcija)
        sp.virsotnu_kopa[pasreizeja_virsotne.id].child.append(id)
        sp.virsotnu_kopa.append(jauna_virsotne)
#Virsotne, lai mainītu spēlētāju no cilvēka uz datora 
vir = Virsotne([], 0, 0, 0, 0, 0, 0, 0)
#Tiek izsaukts spēles koka konstruktors, lai izveidotu tukšu koku        
sp=Speles_koks()

#Laika skaitīšana inicializēšana
#tkop = 0
#Laika skaitīšana inicializēšana
#count_dat_gaj = 0
#Algoritms koka veidošanai uz 4 līmeņiem, skaitot sakotnējas virsotnes līmeni no 0
def koka_veid(Virsotne):
  #Tiek izveidota sākumvirsotne spēles kokā
  sp.pievienot_virsotni(Virsotne)

  #Kamēr nav apskatītas visas saģenerētas virsotnes viena pēc otras, līdz noteiktājām līmenīm
  i = 0
  while i < len(sp.virsotnu_kopa) and sp.virsotnu_kopa[i].limenis < 3:
    pasreizeja_virsotne = sp.virsotnu_kopa[i]
    gajiena_parbaude('2',pasreizeja_virsotne)
    gajiena_parbaude('3',pasreizeja_virsotne)
    i = i + 1

class SpelesGUI:
    # Inicializējam, sākuma nosacījumus
    def __init__(self, master):
        self.master = master
        master.geometry('400x300')
        master.configure(bg='cornsilk2')
        master.title("Dalīšanas Duelis: Skaitļu Cīņa")

        # Pirmais solis - algoritma izvēle
        self.choose_algorithm()
    #Funkcija, lai izvēlētos algoritmu
    def choose_algorithm(self):
        #Notīra ekrānu
        self.clear_widgets()

        self.master.configure(bg='cornsilk2')

        tk.Label(self.master, text="Izvēlies algoritmu:", bg='cornsilk2').pack()

        # Izvēlēties algoritmu - pogas
        tk.Button(self.master, text="Minimax", command=lambda: self.choose_starter("Minimax"), bg='tan', fg='white').pack()
        tk.Button(self.master, text="Alpha Beta", command=lambda: self.choose_starter("Alpha Beta"), bg='tan', fg='white').pack()

    #Funkcija, lai izvēlētos, kurš spēlēs pirmais
    def choose_starter(self, algorithm):
        self.algorithm = algorithm  # Glabā izvēlēto algoritmu
        self.clear_widgets()

        tk.Label(self.master, text="Kurš sāk spēli?", bg='cornsilk2').pack()

        # Izvēlēties spēlētāju - pogas
        tk.Button(self.master, text="Cilvēks", command=lambda: self.generet_sakuma_skaitlus("Spēlētājs"), bg='tan', fg='white').pack()
        tk.Button(self.master, text="Dators", command=lambda: self.generet_sakuma_skaitlus("Dators"), bg='tan', fg='white').pack()

    #Funkcija, lai izveidotu sākuma skaitļus
    def generet_sakuma_skaitlus(self, starter):
        self.starter = starter  # Saglabā to, kurš sāks spēli
        self.clear_widgets()

        #Randoma skaitļu ģenerēšana
        self.skaitli = [random.randint(10000, 20000) for _ in range(100)]
        self.skaitli = [sk for sk in self.skaitli if sk % 6 == 0][:5]

        self.uzstadi_sakuma_skaitlu_izveles_saskarni()

    #Funkcija, lai izvēlētos sākuma skaitļu
    def uzstadi_sakuma_skaitlu_izveles_saskarni(self):
        tk.Label(self.master, text="Izvēlies sākuma skaitli:", bg='cornsilk2').pack()

        for skaitlis in self.skaitli:
            tk.Button(self.master, text=str(skaitlis),
                      command=lambda sk=skaitlis: self.uzstadi_speles_vidi(sk),
                      bg='tan', fg='white').pack()

    #Funkcija, lai palaistu izvēlēto algoritmu
    def alg_izvele(self, Virsotne):
      sp.virsotnu_kopa = [] # inicializē jaunu virsotņu kopu
      Virsotne.id = 0 # inicializē virsotņu ID
      Virsotne.limenis = 0 # inicializē virsotņu līmeni

      koka_veid(Virsotne) # Koka veidošana
      #Algoritma izvēle
      if self.algorithm == "Minimax":
        rezultats = minimax(True, sp.virsotnu_kopa[0])
      elif self.algorithm == "Alpha Beta":
        rezultats = alpha_beta(True, sp.virsotnu_kopa[0], -math.inf, math.inf)
      else:
        print("Error: no method")
        pass
    pass 
    #Funkcija, lai izveidotu spēles vidi
    def uzstadi_speles_vidi(self, sakuma_skaitlis):
        #global tkop, count_dat_gaj, count_virsotnes
        self.clear_widgets()
        self.id = 0
        self.limenis = -1 #apzīme, ka 1.gajienu taisa cilvēks
        self.skaitlis = sakuma_skaitlis
        self.p1_punkti = 0
        self.p2_punkti = 0
        self.bankas_punkti = 0
        #tkop = 0
        #count_dat_gaj = 0
        #count_virsotnes = 0
        self.gajiens = 0  # reseto gājienu skaitīšanu
        if self.starter == "Dators":
          self.master.configure(bg='cornsilk3')
          self.alg_izvele(Virsotne([], 0, sakuma_skaitlis, 0, 0, 0, 0, 0))
          self.limenis = 0 # inicializē virsotņu līmeni
          self.atjaunot_ekranu()
          self.master.after(1500, self.dators_dala)
        self.atjaunot_ekranu()
    pass
    #Galīgas virsotnes punktiem tiek pievienots banks
    def banka_pieskirsana(self):
      if self.bankas_punkti > 0: #Pārbaudē vai bankā nav 0- skaitlis dalās ar 5
          # para limenis  + para skaitlis  & nepara limenis + nepara skaitlis  = datoram
          # nepara limenis  + para skaitlis  & para limenis + nepara skaitlis  = cilvēkam
        if self.skaitlis == 2 or self.skaitlis == 3 or self.skaitlis%2 == 0:
          match self.limenis%2:
            case 1:
              self.p1_punkti = self.p1_punkti+self.bankas_punkti
            case 0:
              self.p2_punkti = self.p2_punkti+self.bankas_punkti
        else:
          match self.limenis%2:
            case 1:
              self.p2_punkti = self.p2_punkti+self.bankas_punkti
            case 0:
              self.p1_punkti = self.p1_punkti+self.bankas_punkti
          self.bankas_punkti = 0
          self.atjaunot_ekranu()

    #Funkcija, kas realizē datora gajienu
    def dators_dala(self):
      #pārbauda vai ir datora gajiens 
      if self.limenis % 2 == 0:
        #global tkop, count_dat_gaj
        #count_dat_gaj = count_dat_gaj + 1
        #t1 = time.time()
        #jauns sakums 
        if self.id == 17:
          #pārbaude vai ir spēles beigas 
          if (count_2_3_5(self.skaitlis)[0] != 0 or  count_2_3_5(self.skaitlis)[1] != 0) and (self.skaitlis != 2 and self.skaitlis != 3):
            vir.child = []
            vir.skaitlis = self.skaitlis
            vir.p1 = self.p1_punkti
            vir.p2 = self.p2_punkti
            vir.bank = self.bankas_punkti
            self.id = 0
            self.alg_izvele(vir)
          else:
            self.banka_pieskirsana()#piešķir bankas punktus spēlētājiem
            self.paradit_galarezultatu()
            return
        elif len(sp.virsotnu_kopa[self.id].child) == 0:
          if (count_2_3_5(self.skaitlis)[0] != 0 or count_2_3_5(self.skaitlis)[1] != 0) and self.skaitlis != 2 and self.skaitlis != 3:
            Virsotne = sp.virsotnu_kopa[self.id]
            self.alg_izvele(Virsotne)
            self.id = 0
          else:
            self.banka_pieskirsana()
            self.paradit_galarezultatu()
            return
        #izvēlas labāko gajienu
        state = sp.virsotnu_kopa[self.id]
        id = make_best_move(state)
        #t2 = time.time()
        #tkop = tkop + (t2-t1)
        if id is not None:
          self.id = sp.virsotnu_kopa[id].id
          self.limenis = sp.virsotnu_kopa[id].limenis
          self.skaitlis = sp.virsotnu_kopa[id].skaitlis
          self.p1_punkti = sp.virsotnu_kopa[id].p1
          self.p2_punkti = sp.virsotnu_kopa[id].p2
          self.bankas_punkti = sp.virsotnu_kopa[id].bank
          self.atjaunot_ekranu()
      pass

    #Funkcija, kas realizē spēlētāja gajienu
    def dalit(self, dalitajs):
      #Pārbaude vai ir spēlētāja gājiens
      if self.limenis % 2 != 0 or self.limenis == -1:
        #Pārbaude vai ir spēles beidzas
        if count_2_3_5(self.skaitlis)[0] == 0 and count_2_3_5(self.skaitlis)[1] == 0 or (self.skaitlis == 2 or self.skaitlis == 3):
          self.banka_pieskirsana()
          self.paradit_galarezultatu()
          return
        #Pārbaude vai var dalīt ar izvēlēto skaitli
        if self.skaitlis % dalitajs == 0:
          #Pārbaude vai ir sasniegtas koka beigas vai spēlētājs taisa pirmo gājienu
          if self.limenis == 3 or self.limenis == -1:
            #Taisa jauno virsotni
            self.id = 17 #ID, kas noteikti neitilps koka virsotnēs
            self.limenis = 0
            self.skaitlis = int(self.skaitlis / dalitajs)
            if self.skaitlis % 5 == 0:
              self.bankas_punkti = self.bankas_punkti + 1
            if self.skaitlis % 2 == 0:
              self.p2_punkti = self.p2_punkti + 1
            else :
              self.p2_punkti = self.p2_punkti - 1
          else:
            self.skaitlis = int(self.skaitlis/dalitajs)
            child = sp.virsotnu_kopa[self.id].child
            num = 0
            #Atjauno virsotni, lai sēkotu kokam
            for i in child:
              if sp.virsotnu_kopa[child[num]].skaitlis == self.skaitlis:
                self.id = sp.virsotnu_kopa[child[num]].id
                self.limenis = sp.virsotnu_kopa[child[num]].limenis
                self.skaitlis = sp.virsotnu_kopa[child[num]].skaitlis
                self.p1_punkti = sp.virsotnu_kopa[child[num]].p1
                self.p2_punkti = sp.virsotnu_kopa[child[num]].p2
                self.bankas_punkti = sp.virsotnu_kopa[child[num]].bank
              num += 1
          self.atjaunot_ekranu()
          #Aizkave pirms datora gājiena
          self.master.after(1500, self.dators_dala)
    pass
    #Funkcija, lai paradītu, kura ir gājiens
    def get_gajiens(self):
       if self.limenis % 2 == 0:
          return 'Dators'
       else:
          return 'Cilvēks'

    #Funkcija, lai paradītu, kura ir gājiens ar krasu
    def get_krasa(self):
      if self.limenis % 2 == 0:
        return 'cornsilk3'
      else:
        return 'cornsilk2' 

    #Funkcija, lai atjuanotu ekrānu
    def atjaunot_ekranu(self):
        # Metode, kad atjaunojas spēles ekrāns - noteiktie punkti utt
      for widget in self.master.winfo_children():
        widget.destroy()
      krasa = self.get_krasa()

      self.master.configure(bg=krasa)

      tk.Label(self.master, text=f"Gājiens: {self.get_gajiens()}", bg=krasa).pack()
      tk.Label(self.master, text=f"Pašreizējais skaitlis: {self.skaitlis}", bg=krasa).pack()
      tk.Label(self.master, text=f"Datora punkti: {self.p1_punkti}", bg=krasa).pack()
      tk.Label(self.master, text=f"Cilvēka punkti: {self.p2_punkti}", bg=krasa).pack()
      tk.Label(self.master, text=f"Bankā: {self.bankas_punkti}", bg=krasa).pack()

      button_frame = tk.Frame(self.master, bg=krasa)
      button_frame.pack()

      tk.Button(button_frame, text="Dalīt ar 2", command=lambda: self.dalit(2), bg='olive', fg='white').pack(side=tk.LEFT)
      tk.Button(button_frame, text="Dalīt ar 3", command=lambda: self.dalit(3), bg='olive', fg='white').pack(side=tk.LEFT)

    #Funkcija, kura atdod rezultātu 
    def result(self):
       if self.p1_punkti > self.p2_punkti:
          return 'Dators'
       elif self.p1_punkti < self.p2_punkti:
          return 'Cilvēks'
       else:
          return 'Neizšķirts'

    #Funkcija, kas parada beigas rezultātu
    def paradit_galarezultatu(self):
      messagebox.showinfo("Spēles beigas!", f"Spēle ir beigusies!\nDatora punkti: {self.p1_punkti}\nCilvēka punkti: {self.p2_punkti}\nBankā: {self.bankas_punkti}\nUzvarētājs: {self.result()}")
      # pārbaudīt spēlēt vēlreiz pogu
      #print("vidējais laiks", tkop/count_dat_gaj) # izvada vidējo laiku
      #print("apmēklētās virsotnes", count_virsotnes) # izvada apmēklēto virsotņu skaitu

      self.choose_algorithm()
      pass

    def clear_widgets(self):
        # metode, kas palīdz notīrīt ekrānu
        for widget in self.master.winfo_children():
            widget.destroy()

root = tk.Tk()
app = SpelesGUI(root)
root.mainloop()

