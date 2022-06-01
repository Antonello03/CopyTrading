from math import floor

#importi iniziali da osservare
partenza = [350,500,1000]

#profitti da osservare
profitti = [1.1, 1.125, 1.15]

#anni di osservazione
N_anni = 2

#intervallo mesi di osservazione
jmp = 3

for prof in profitti:
    print("Con un profitto del",round((prof-1),3)*100,"%")
    for anno in range (1,N_anni + 1):
        print("Anno " , anno)
        for mese in range (1,13,jmp):
        #if mese == 1 or mese == 12:
            print ("Mese", mese ,": ", end='')
            for x in range(0,(len(partenza))):
                print(floor(partenza[x] * (pow(prof , mese + ((anno - 1) * 12)) )) , " " , end='')
            print()
        print()
    print()