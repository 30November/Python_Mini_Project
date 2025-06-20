from random import randint
no_of_pt=int(input("Enter total points of the match:"))
sym = ['Rock',"Scisor","Paper"]
comp = p = 0 #comp , person
 
while (max(comp,p) != no_of_pt):
    for i,e in enumerate(sym):
        print(f"{i+1}.{e}")
    choose = int(input("Enter the choice (1-3):"))-1
    if choose not in range(3):
        print("ENTER THE VALID CHOICE")
        continue
    
    comp_ch = randint(0,2)
    print("YOU CHOOSE->",sym[choose])
    print("COMPUTER CHOOSE->",sym[comp_ch])
    
    if comp_ch == choose:
        print("LOL!")
    else:
        if (comp_ch+1)%3==choose:
            print("1 POINT TO COMPUTER")
            comp += 1
        else:
            print("1 POINT TO YOU")
            p += 1
    print(f"POINT\tCOMPUTER:{comp} and YOU:{p}\n")

print("Winner is","COMPUTER" if comp > p else "YOU")

        
    

