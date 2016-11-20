relative_atomic_mass = 0
character_count = -1
subscript_num = 1
raw_compound = input('Insert one mole of your compound. If subscript is needed, use <n\n')
length = len(raw_compound)
sub_compound = raw_compound.replace('<0','₀').replace('<1','₁').replace('<2','₂').replace('<3','₃').replace('<4','₄').replace('<5','₅').replace('<6','₆').replace('<7','₇').replace('<8','₈').replace('<9','₉')
periodic_table = {'H':1,
                  'He':4,
                  'Li':7,
                  'Be':9,
                  'B':11,
                  'C':12,
                  'N':14,
                  'O':16,
                  'F':19,
                  'Ne':20,
                  'Na':23,
                  'Mg':24,
                  'Al':27,
                  'Si':28,
                  'P':31,
                  'S':32,
                  'Cl': 35.5,
                  'Ar':40,
                  'K':39,
                  'Ca':40,
                  'Sc':45,
                  'Ti':48,
                  'V':51,
                  'Cr':52,
                  'Mn':55,
                  'Fe':56,
                  'Co':59,
                  'Ni':59,
                  'Cu':63.5,
                  'Zn':65,
                  'Ga':70,
                  'Ge':73,
                  'As':75,
                  'Se':79,
                  'Br':80,
                  'Kr':84,
                  'Rb':85,
                  'Sr':88,
                  'Y':89,
                  'Zr':91,
                  'Nb':93,
                  'Mo':96,
                  'Tc':98,
                  'Ru':101,
                  'Rh':103,
                  'Pd':106,
                  'Ag':108,
                  'Cd':112,}

compound = []
for character in raw_compound:
   character_count = character_count +1
   if character.isupper() and character_count+1 == length:
      compound.append(raw_compound[character_count])
   elif character.isupper() and  raw_compound[character_count+1].islower() and character_count+2 == length:
      compound.append(raw_compound[character_count:character_count+2])
   elif character.isupper() and  raw_compound[character_count+1].islower() and raw_compound[character_count + 2] == '<':
      while subscript_num <= int(raw_compound[character_count+3]):    
         subscript_num = subscript_num + 1 
         compound.append(raw_compound[character_count:character_count+2])
   elif character.isupper()  and raw_compound[character_count + 1] == '<':
      while subscript_num <= int(raw_compound[character_count+2]):    
         subscript_num = subscript_num + 1 
         compound.append(raw_compound[character_count])
   elif character.isupper() and  raw_compound[character_count+1].islower() and raw_compound[character_count + 2] != '<':
      compound.append(raw_compound[character_count:character_count+2])
   elif character.isupper():
      compound.append(raw_compound[character_count])
#print(compound)



for element in compound:
    relative_atomic_mass = relative_atomic_mass + float(periodic_table[element])

print(relative_atomic_mass)








#₀₁₂₃₄₅₆₇₈₉
