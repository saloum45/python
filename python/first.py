print("hello this is first python program")
print(14*60)
print('hi')

age = 15
if(age>=18): 
    print("you are not a teenager")
else:
    print("you are a teenager")
print("ji")
calcul = 5 / 8
calcul = float(calcul)
print(calcul)

# a loop while with a like compter
a=1
while(a!=6):
    print("don't repeat your self")
    a+=1
jeu_lance = True
print(" ")
while jeu_lance:
    choixMenu = input("> ")
    if choixMenu=="again":
        continue
    elif choixMenu=="quiet":
        break
    elif choixMenu=="hello":
        print("hello")
    else :
        print("repeat what you inputed is not availible")
        continue
