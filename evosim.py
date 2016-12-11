import random
class Creature(object):
    def __init__(self):
        per = [0] * 100000
        ran1temp = random.randint(0, 99999)
        ran2temp = random.randint(0, 99999)
        ran1 = min(ran1temp, ran2temp)
        ran2 = max(ran1temp, ran2temp)
        per[ran1] = 1
        per[ran2] = 2
        strper = ran1 / 100000
        chrper = (ran2 - ran1) / 100000
        intper = (100000-ran2) / 100000
        self.strength = strper * 5
        self.charisma = chrper * 5
        self.intelligence = intper * 2.5
        
creaturelist = [Creature() for i in range(0, 1001)]
x = 1000
for i in range (0, x):
    livelist = [None] * 500
    deadlist = [None] * 500
    for n in range(0, 500):
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        while True:
            if (a in livelist or b in livelist or a in deadlist or b in deadlist) == 0:
                chall1 = creaturelist[a]
                chall2 = creaturelist[b]
                break
            else:
                a = random.randint(0, 1000)
                b = random.randint(0, 1000)
        if chall1.intelligence > chall2.intelligence:
            tempstr1 = chall1.strength + (random.random() * chall1.intelligence)
            tempstr2 = chall2.strength
        elif chall1.intelligence < chall2.intelligence:
            tempstr2 = chall2.strength + (random.random() * chall2.intelligence)
            tempstr1 = chall1.strength
        else:
            tempstr1 = chall1.strength + (random.random() * chall1.intelligence)
            tempstr2 = chall2.strength            
        if tempstr1 > tempstr2:
            livelist[n] = chall1
            deadlist[n] = chall2
        elif tempstr1 < tempstr2:
            livelist[n] = chall2
            deadlist[n] = chall1
    #charisma will kick bottom 50 creatures livelist and add top 50 creatures deadlist
    cooplive = sorted(livelist, key=lambda Creature: Creature.charisma)
    coopdead = sorted(deadlist, key=lambda Creature: Creature.charisma)
    temp = [None] * 100
    cnt1 = 0
    cnt2 = 0
    while cnt1 < (len(livelist)/10):
        temp100[cnt1] = cooplive[cnt1]
        cnt1 = cnt1 + 1
    while cnt2 < (len(deadlist)/10):
        temp100[cnt1+cnt2] = coopdead[len(coopdead)-cnt2-1]
        cnt2 = cnt2 + 1
    cooplive[:int(len(cooplive)/10)] = temp100[int(len(temp100)/2):]
    coopdead[int(len(coopdead)/10):] = temp100[:int(len(temp100)/2)]
    deadlist = coopdead
    livelist = cooplive
    sumstrl = sum(Creature.strength for Creature in livelist)
    sumstrd = sum(Creature.strength for Creature in deadlist)
    sumintl = sum(Creature.intelligence for Creature in livelist)
    sumintd = sum(Creature.intelligence for Creature in deadlist)
    sumchrl = sum(Creature.charisma for Creature in livelist)
    sumchrd = sum(Creature.charisma for Creature in deadlist)
    #need to add matplotlib script here
    print ("Generation " + str(i+1))
    print ("Average strength of living was: " + str(sumstrl / 500))
    print ("Average strength of dead was: " + str(sumstrd / 500))
    print ("Average intelligence of living was: " + str(sumintl / 500))
    print ("Average intelligence of dead was: " + str(sumintd / 500))
    print ("Average charisma of living was: " + str(sumchrl / 500))
    print ("Average charisma of dead was: " + str(sumchrd / 500))
    for k in range(len(creaturelist)):
        chk = creaturelist[k]
        if chk in deadlist:
            creaturelist[k] = [None]
    nextlist = [Creature() for i in range(0, 1001)]
    for ind in range(len(nextlist)):
        nextlist[ind].strength = 0
        nextlist[ind].intelligence = 0
        nextlist[ind].charisma = 0
    donelist = [None] * 500
    while True:
        h = random.randint(0, 249)
        k = random.randint(0, 249) + 250
        if (h in donelist or k in donelist) == False:
            break
        else:
            h = random.randint(0, 249)
            k = random.randint(0, 249) + 250
    for r in range(0, len(nextlist)-1):
        mot = livelist[h]
        dad = livelist[k]
        newstr = (mot.strength + dad.strength)/2
        newint = (mot.intelligence + dad.intelligence)/2
        newchr = (mot.charisma + dad.charisma)/2
        nextlist[r].strength = newstr
        nextlist[r].intelligence = newint
        nextlist[r].charisma = newchr
    creaturelist = livelist + nextlist
    
        
        
        
    
    
    
    
    

                


        
