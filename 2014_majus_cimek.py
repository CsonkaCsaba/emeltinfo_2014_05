# 1. feladat
ip_cimek=[]
forras = open('ip.txt', 'r')
ip_cimek = forras.readlines()

# 2. feladat
print("2. feladat")
print(f"Az állományban {len(ip_cimek)} db cím van.")

# 3. feladat
print("3. feladat")
ip_cimek.sort()
print(f"A legalacsonyabb tárolt IP cím:")
print(*ip_cimek[0])

# 4. feladat
print("4. feladat")
dokumnetacios_cimek= 0
globalis_cimek= 0
helyi_cimek= 0

for ip_address in ip_cimek:
    if ip_address.startswith('2001:0db8'):
        dokumnetacios_cimek+= 1
    elif ip_address.startswith('2001:0e'):
        globalis_cimek+= 1
    elif ip_address.startswith('fc') or ip_address.startswith('fd'):
        helyi_cimek+= 1
        
print(f" A dokumentációs címek összesen: {dokumnetacios_cimek} darab")

print(f" A globális egyedi címek összesen: {globalis_cimek} darab")
print(f" A helyi egyedi címek összesen: {helyi_cimek} darab")

forras.close()
