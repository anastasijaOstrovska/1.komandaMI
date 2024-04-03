import random
import math
from numpy import Infinity



#Klase kas atbilst virsotnei
class Virsotne:

    def __init__(self,child, id, skaitlis, p1, p2,bank, limenis, heir_funkcija):
        self.child = child # virsotnes bērni
        self.id = id # virsotnes id, lai meklētu vecāku
        self.skaitlis = skaitlis # šobrid skaitlis
        self.p1 = p1 # pirma cilvēka punkti
        self.p2 = p2 # otra cilvēka punkti
        self.bank = bank # kas šobrīd atrodas bankā
        self.limenis = limenis # līmenis, uz kura atrodas virsotne
        self.heir_funkcija = heir_funkcija # Heiristiskā funkcija

#Klase, kas atbilst spēles kokam        
class Speles_koks:

    # Inicializējam, ka koks būs List datustruktūra
    def __init__(self):
        self.virsotnu_kopa=[]

    #Klases Speles_koks metode, kas pievieno spēles kokam jaunu virsotni, kuru saņem kā argumentu
    def pievienot_virsotni(self, Virsotne):
        self.virsotnu_kopa.append(Virsotne)

def count_2_3_5(skaitlis):
  c2 = 0 # cik daudz dalitaju = 2
  c3 = 0 # cik daudz dalitaju = 3
  c5 = 0 # cik daudz dalitaju = 5
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

def heir_funkcija(tek_virsotne):
  heir_vert = 0
  heir_vert = heir_vert + (tek_virsotne.p1-tek_virsotne.p2) # punktu skaits
  list = count_2_3_5(tek_virsotne.skaitlis)
  #check bank
  if tek_virsotne.bank != 0:
    # para limenis  + para skaitlis  & nepara limenis + nepara skaitlis  = mums
    # nepara limenis  + para skaitlis  & para limenis + nepara skaitlis  = citam 
    # nav 2 vai 3
    if (tek_virsotne.skaitlis/((2**list[0])*(3**list[1])) > 3):
      if (( (tek_virsotne.limenis + list[0]+list[1]) % 2 != 0 and tek_virsotne.skaitlis%2 != 0) or ( ( tek_virsotne.limenis + list[0]+list[1]) % 2 == 0 and tek_virsotne.skaitlis%2 == 0)):
        heir_vert = heir_vert + tek_virsotne.bank
      else:
        heir_vert = heir_vert - tek_virsotne.bank
    # ir 2 vai 3
    else :
      if ((tek_virsotne.limenis +list[0]+list[1])%2 == 0):
        heir_vert = heir_vert + tek_virsotne.bank
      else:
        heir_vert = heir_vert - tek_virsotne.bank   
  return heir_vert
# 0 - max
# 1 - min
# 2 - max
# 3 - min - nepara 

def make_best_move(state):
  bestScore = -math.inf
  bestMove = None
  for child_id in state.child:
    child = sp.virsotnu_kopa[child_id]
    score = minimax(False, child)
    if (score > bestScore):
      bestScore = score
      bestMove = child_id
  return bestScore, bestMove


def minimax(isMaxTurn, state):
  if len(state.child) == 0:
    state.heir_funkcija = heir_funkcija(state)
    return state.heir_funkcija

  scores = []
  for child_id in state.child:
    child = sp.virsotnu_kopa[child_id]
    scores.append(minimax(not isMaxTurn, child))
  if isMaxTurn:
    max_score = max(scores)
    state.heir_funkcija = max_score
    return max_score
  else:
    min_score = min(scores)
    state.heir_funkcija = min_score
    return min_score

def alpha_beta(isMaxTurn, state, alpha, beta):
  if len(state.child) == 0:
      state.heir_funkcija = heir_funkcija(state)
      return state.heir_funkcija

  if isMaxTurn:
      max_score = float("-inf")
      for child_id in state.child:
          child = sp.virsotnu_kopa[child_id]
          score = alpha_beta(not isMaxTurn, child, alpha, beta)
          max_score = max(max_score, score)
          alpha = max(alpha, max_score)
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
          if beta <= alpha:
              break
      state.heir_funkcija = min_score
      return min_score


def gajiena_parbaude (gajiena_tips, pasreizeja_virsotne):
    # Pārbaude vai skaitlis dalas ar 2, ja nē tad iziet no funkcijas
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

#tiek izsaukts spēles koka konstruktors, lai izveidotu tukšu koku        
sp=Speles_koks()
# Random skaitļa ģenerēšana kas dalās gan ar 2, gan ar 3
while True:
    random_skaitlis = random.randint(10000,20000)
    if random_skaitlis%2 == 0 and random_skaitlis%3 == 0:
        break
#tiek izveidota sākumvirsotne spēles kokā
sp.pievienot_virsotni(Virsotne([], 0, 11664, 0, 0, 0, 0, 0))

#kamēr nav apskatītas visas saģenerētas virsotnes viena pēc otras
i = 0
level = 3
while i < len(sp.virsotnu_kopa) and sp.virsotnu_kopa[i].limenis < level:
    pasreizeja_virsotne=sp.virsotnu_kopa[i]
    gajiena_parbaude('2',pasreizeja_virsotne)
    gajiena_parbaude('3',pasreizeja_virsotne)
    i = i + 1
i = 0 
if count_2_3_5(sp.virsotnu_kopa[0].skaitlis)[2] > 0:
  while i < len(sp.virsotnu_kopa):
    if len(sp.virsotnu_kopa[i].child) == 0 :
      if sp.virsotnu_kopa[i].skaitlis == 2 or sp.virsotnu_kopa[i].skaitlis == 3 or sp.virsotnu_kopa[i].skaitlis%2 == 0:
        match sp.virsotnu_kopa[i].limenis%2:
          case 1:
            sp.virsotnu_kopa[i].p1 = sp.virsotnu_kopa[i].p1+sp.virsotnu_kopa[i].bank
          case 0:
            sp.virsotnu_kopa[i].p2 = sp.virsotnu_kopa[i].p2+sp.virsotnu_kopa[i].bank
      else:
        match sp.virsotnu_kopa[i].limenis%2:
          case 1:
            sp.virsotnu_kopa[i].p2 = sp.virsotnu_kopa[i].p2+sp.virsotnu_kopa[i].bank
          case 0:
            sp.virsotnu_kopa[i].p1 = sp.virsotnu_kopa[i].p1+sp.virsotnu_kopa[i].bank
      sp.virsotnu_kopa[i].bank = 0
    i = i + 1



rezultats = make_best_move(sp.virsotnu_kopa[0])
print(rezultats)

for x in sp.virsotnu_kopa:
  print(x.id, x.skaitlis, x.p1, x.p2, x.bank, x.limenis, x.heir_funkcija)






