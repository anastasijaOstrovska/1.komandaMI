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
#Tiek izsaukts spēles koka konstruktors, lai izveidotu tukšu koku        
sp=Speles_koks()

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
