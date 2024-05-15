
# ********************************************************************************8
# MASTER STR
# ********************************************************************************8

from io import TextIOWrapper


teks: str = "Ayibobo Ayiti"
# 1. karaktè yo an miniskil
teks_miniskil: str = teks.lower()

#  2. koupe chenn nan tout kote ki gen espas
teks_koupe: list = teks.split(" ")
print(teks_koupe)

#  3. premye lèt chak mo an majiskil
teks_premye_let_majiskil: str = teks_miniskil.title()

#  4. rekipere premye lèt chak mo. Epi afiche yon nouvo chenn ak tout inisyal sa yo
teks = "Verite a gaye isit nan"
nouvo_mo: str = ""
for mo in teks.split(): nouvo_mo += mo[0]

print("Nouvo mo: ", nouvo_mo)

#  5. karaktè "a" ki nan yon chenn pa "@"
teks_san_a = teks.replace('a', '@')

#  6. devan dèyè, answit mete l an majiskil
devan_deye = nouvo_mo[::-1].upper()

#  7.  endeks premye karaktè "a" 
teks = "Ayiti kapab avanse"
edks_premye_a = teks.index('a')
print("Endeks premye a: ", edks_premye_a)

#  8. Afiche total tout endeks karaktè "a"
total_endeks: int = 0
for edks, let in enumerate(teks):
    if let in "aA":
        total_endeks += edks
    
print("Total endeks tout a: ", total_endeks)


#  9. endeks tout karaktè "a"
lis_endeks = [edks for edks, let in enumerate(teks) if let in "a"]
print("Lis endeks tout a: ", lis_endeks)

#  10. Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen
teks_san_espas = "".join(teks.split(" "))
teks_san_espas += str(len(teks_san_espas))
print("Teks san espas: ", teks_san_espas)

    
    
    
# ********************************************************************************8   
# MASTER LIST (Union & Intersection & Lis comprehension)
# ********************************************************************************8
# 1. Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
n = 20
lis_antye = [el for el in range(0, n+1)]
print("Lis antye: ", lis_antye)

# 2. Ou gen yon lis antye, konvèti l an yon lis chenn.
konveti_lis = list(map(str, lis_antye))
print("Lis koveti an chenn: ", konveti_lis)

# 3. Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil
lis_chenn_miniskil: list = list("qwertyui")
konveti_an_majiskil: list = [el.upper() for el in lis_chenn_miniskil]
print("Konvesyon lis miniskil an majiskil: ", konveti_an_majiskil)

# 4. Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman
lis_eleman_div3: list = [el for edks, el in enumerate(konveti_an_majiskil) if edks % 3 == 0]
print("Lis eleman endeks divizib pa 3: ", lis_eleman_div3)

# 5. Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tip
lis = [1,2,3,4,5,6,7,8,9, 10, 11]
N = 3
longe = len(lis)
n, res = divmod(longe, N)
gwoup_3_eleman = [tuple(lis[i*N: (i+1) * N]) for i in range(n)]
if res > 0:
    i = n * N
    gwoup_3_eleman.append(tuple(lis[i:]))
    
print("Longe: ", n, "Res: ", res)
print("Gwoup eleman: ", gwoup_3_eleman)

# 6. Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon
lis_ak_doublon: list = list("q2wertyuiopq2wertywetryQAWESDRTFGYHUIJOKLQWER]")
lis_san_doublon: list = list(set(lis_ak_doublon))
print("Lis san doublon: ", lis_san_doublon)

# 7. Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo.
lis_a = list("6712345")
lis_b = list("1098765345")

lis_an_komen = [el for el in lis_a if el in lis_b]
print("Eleman an komen: ", lis_an_komen)
# 8. Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo
lis_disteng_eleman = [el for el in lis_a + lis_b if (lis_a + lis_b).count(el) == 1]
print("Eleman disteng: ", lis_disteng_eleman)

# 9. Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman
diks = {"name": "James", "username": "bogosla", "age": 1024}
kle_yo = diks.keys()
vale_yo = diks.values()
# 10. Reyini 3 lis ansanm, san okenn doublon
lis_c = ["3", "5", "12", "55"]

lis_san_doublon_2 = [el for el in lis_a + lis_b + lis_c if (lis_a + lis_b + lis_c).count(el) == 1]
print("Reyni 3 lis san doublon: ", lis_san_doublon_2)

# ********************************************************************************8   
# Master class
# ********************************************************************************8

class FichyePam(object):
    def __init__(self, _chemen: str) -> None:
        self.chemen: str = _chemen
        self._fichye = None
        
    def ouvri(self):
        """Metod pou ouvri fichye, dwe rele avan w itilize 'li', 'ajoute'...
        """
        self._fichye = open(self.chemen, "a+")
        return
        
    def li(self, kantite: int=None):
        if not self._fichye: raise FileExistsError("Paka li done de fichye sa oubyen li pa ouvri!")
        self._fichye.seek(0)
        done = self._fichye.read() if not kantite else self._fichye.read(kantite)
        return done
    
    
    def ajoute(self, done):
        if not self._fichye: raise FileExistsError("Paka li done de fichye sa oubyen li pa ouvri!")
        self._fichye.write(done)
        return
    
    def femen(self):
        if not self._fichye:
            self._fichye.close()
    
tes = FichyePam("tes.txt")
tes.ouvri()

# print("\n\nFichye done: ", tes.li())
tes.ajoute("1LOT DONE ANKO324567890!!!\n")
tes.ajoute("1LOT DONE ANKOertyu!!!\n")
tes.ajoute("22221LOT DONE ANKO54678uiop!!!\n")
# print("\n\nFichye done: ", tes.li(), "\n\n")
tes.femen()



#  2. Kreye yon klas Vivan, ki gen pwopriyete moun (pye, men, non, laj).
class Vivan(object):
    def __init__(self, pnon, plaj, pmen, ppye) -> None:
        self.non = pnon 
        self.laj = plaj 
        self.men = pmen
        self.pye = ppye
        
james = Vivan("James DESTINE", 1024, 2, 2)
papam = Vivan("J.J Dsalin", 2048, 2, 2)


# Aprè kreye yon klas Poul, ki erite klas s
class Poul(Vivan):
    def __init__(self,pnon, ppye) -> None:
        super().__init__(pnon, 0, 0, ppye)
        

jeudy = Poul("Kouwoukoukou", 3)



# ********************************************************************************8   
# MASTER EXCEPTIONS
# ********************************************************************************8   

#  1. Mande itilizatè a tape yon chif, epi ajoute +5. Kapte eksepsyon ki ka rive si itilizatè a pa tape yon diji


def tape_chif(msj):
    """Tape yon chif"""
    while True:
        try:
            return int(input(msj)) 
        except ValueError:
            pass
        except KeyboardInterrupt:
            return None
        except Exception:
            return None
        
# chif_tape = tape_chif("Tape yon chif: ")
# if chif_tape:
#     print(chif_tape + 5)
        
        
    
        
        






        