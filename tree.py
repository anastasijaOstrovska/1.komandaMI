#Klase kas atbilst virsotnei 
class Virsotne:
    
    def __init__(self,child, id, skaitlis, p1, p2,bank, limenis):
        self.child = child # virsotnes bērni 
        self.id = id # virsotnes id, lai meklētu vecāku
        self.skaitlis = skaitlis # šobrid skaitlis
        self.p1 = p1 # pirma cilvēka punkti
        self.p2 = p2 # otra cilvēka punkti
        self.bank = bank # kas šobrīd atrodas bankā
        self.limenis = limenis # līmenis, uz kura atrodas virsotne
               
#Klase, kas atbilst spēles kokam        
class Speles_koks:

    # Inicializējam, ka koks būs List datustruktūra
    def __init__(self):
        self.virsotnu_kopa=[]
    
    #Klases Speles_koks metode, kas pievieno spēles kokam jaunu virsotni, kuru saņem kā argumentu
    def pievienot_virsotni(self, Virsotne):
        self.virsotnu_kopa.append(Virsotne)


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

           # Punktu piešķiršana
           if skaitlis % 5 == 0:
               bank = bank + 1
           elif skaitlis % 2 == 0:
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
           jauna_virsotne=Virsotne([], id, skaitlis, p1, p2, bank, limenis)
           sp.virsotnu_kopa[pasreizeja_virsotne.id].child.append(id)
           sp.virsotnu_kopa.append(jauna_virsotne)
    
#tiek izsaukts spēles koka konstruktors, lai izveidotu tukšu koku        
sp=Speles_koks()
#tiek izveidota sākumvirsotne spēles kokā
sp.pievienot_virsotni(Virsotne([], 0, 1296, 0, 0, 0, 0))

#kamēr nav apskatītas visas saģenerētas virsotnes viena pēc otras
i = 0
while i < len(sp.virsotnu_kopa):
    pasreizeja_virsotne=sp.virsotnu_kopa[i]
    gajiena_parbaude('2',pasreizeja_virsotne)
    gajiena_parbaude('3',pasreizeja_virsotne)
    i = i + 1

#ciklam beidzoties, tiek izvadīta spēles koka virsotņu kopa
for x in sp.virsotnu_kopa:
    #print(x.child,x.id,x.skaitlis, x.p1, x.p2, x.bank, x.limenis)
    print(x.id,x.skaitlis, x.p1, x.p2, x.bank, x.limenis)
  #rangrange (1,2,6!)
    # sample frpom random package 
        
