

# MASTER STR
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

    