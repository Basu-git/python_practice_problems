dicto={
    "beng":"food",
    "mysuru":"mysurupak",
    "gadag":"Badnikayibaji",
    "belgm":"Kunda",
    "Dharwad":"peda"
}
print(dicto)
dicto["Mangaluru"]="seafood"
print(dicto)
dicto["beng"]="Biriyani"
print(dicto)
del dicto["beng"]
print(dicto)
print(dicto.keys())
print(dicto.values())