import socket
import datetime   # Libraria per daten dhe kohen.
import random   # Libraria per gjetjen e rastesishme te elementeve.
import math   # Libraria math, e kam perdorur tek gjetja e pjestuesit me te madh te perbashket.
from collections import Counter   # Libraria Counter, e kam perdorur tek operacioni MOSTFREQUENT.

localIP = 'localhost'
localPort = 13000
bufferSize = 128

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)   # Krijojme nje datagram socket.
UDPServerSocket.bind((localIP, localPort))

print("Serveri ka startuar.")
print("Serveri eshte duke pritur per ndonje kerkese.")


while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    operacioni = str(message.decode("utf-8"))   # Operacioni nuk vjen si string andaj e dekodojme ne utf-8.


    if operacioni=="IPADDRESS":   # Metoda IPADDRESS
        hostname = socket.gethostname()   # Ketu e marrim emrin e hostit, pastaj prej saj IP adresen.
        IPAdresa = socket.gethostbyname(hostname)

        print('Kerkesa nga klienti: Cila eshte IP Adresa ime. ')
        print('Kalkulimi nga serveri: IP Adresa jote eshte ' + IPAdresa +'.')  

        text =  IPAdresa

        textEncoded = text.encode(encoding='UTF-8')   # Kete text nuk mund ta dergojme si string ne anen e klientit
        UDPServerSocket.sendto(textEncoded, address) 
        print('Perfundoi komunikimi.')

        

    elif operacioni=="PORT":   # Metoda PORT
        print('Kerkesa nga klienti: Cili eshte porti. ')
        print('Kalkulimi nga serveri: Porti eshte: ' + str(address[1]) +'.')   # Portin e nxjerrim nga vektori Adress, elementin e dyte te tije.

        text = str(address[1]) + '.'

        textEncoded = text.encode(encoding='UTF-8')

        UDPServerSocket.sendto(textEncoded, address)
        print('Perfundoi komunikimi.')



    elif operacioni=="COUNT":   # Metoda COUNT
        KerkesaEKlientit = UDPServerSocket.recvfrom(bufferSize)
        message = KerkesaEKlientit[0]
        short = str(message.decode("utf-8")) 
        
        zanore=0
        bashketingellore=0
        for i in short:
            if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='y' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='Y'):
                zanore=zanore+1
            elif (i=='b' or i=='c' or i=='d' or i=='f' or i=='g' or i=='h' or i=='j' or i=='k' or i=='l' or i=='m' or i=='n' or i=='p' or i=='q' or i=='r' or i=='s' or i=='t' or i=='v' or i=='x' or i=='w' or i=='z' 
                 or i=='B' or i=='C' or i=='D' or i=='F' or i=='G' or i=='H' or i=='J' or i=='K' or i=='L' or i=='M' or i=='N' or i=='P' or i=='Q' or i=='R' or i=='S' or i=='T' or i=='V' or i=='X' or i=='W' or i=='Z'):
                bashketingellore=bashketingellore+1

        a = str(zanore) + ' zanore dhe ' + str(bashketingellore) + ' bashtingllore.'
        ae = a.encode(encoding='utf-8')

        print('Kerkesa nga klienti: Sa zanore dhe bashtingllore ka teksti: '+ short +'.')
        print('Kalkulimi nga serveri: Teksti ka ' + a)
        
        UDPServerSocket.sendto(ae, address)
        print('Perfundoi komunikimi.')



    elif operacioni=="REVERSE":   # Metoda REVERSE
        KerkesaEKlientit = UDPServerSocket.recvfrom(bufferSize)
        message = KerkesaEKlientit[0]
        str1 = str(message.decode("utf-8")) 

        reversedText=[]   # Funksioni per kthimin e tekstit nga prape.
        index = len(str1)
        while index > 0: 
            reversedText += str1[ index - 1 ] 
            index = index - 1
        listToStr = ''.join(reversedText)   # Kthimi nga vargu ne string.

        listToStrWithoutSpaces=listToStr.strip(" ")   # Funksioni .strip(" ") largon hapesirat para dhe pas tekstit.

        print('Kerkesa nga klienti: Me kthe mbrashte tekstin qe do e shkruaj. ')
        print('Kalkulimi nga serveri: ' + listToStrWithoutSpaces + '.')

        textEncoded = listToStrWithoutSpaces.encode(encoding='UTF-8')
        UDPServerSocket.sendto(textEncoded, address)

        print('Perfundoi komunikimi.')



    elif operacioni=="PALINDROME":   # Metoda PALINDROME
        KerkesaEKlientit = UDPServerSocket.recvfrom(bufferSize)
        message = KerkesaEKlientit[0]
        str1 = str(message.decode("utf-8")) 

        print('Kerkesa nga klienti: A eshte ky tekst polindrom apo jo: ' + str1 +'.')

        rev = ''.join(reversed(str1))   # Kam perdorur nje funksion te predefinuar ne python
                                                                 # ''.join(reversed(s)) qe e kthen mbrashte textin.

        if (str1 == rev):   # Nese teksti i kthyer mbrashte eshte i barabarte me textin fillestar
            text1 = 'eshte'   # atehere ai tekst eshte polindrom.
        else:
            text1 = 'nuk eshte'
        
        print('Kalkulimi nga serveri: Teksti i dhene',text1,'polindrom.')

        text = 'Teksti i dhene ' + text1 + ' polindrom.'

        textEncoded = text.encode(encoding='UTF-8')
        UDPServerSocket.sendto(textEncoded, address)

        print('Perfundoi komunikimi.')        



    elif operacioni=="TIME":   # Metoda TIME           
        print('Kerkesa nga klienti: Cila eshte data dhe sa ora ne kete moment. ')

        now = datetime.datetime.now()   # Ketu nxjerrim daten dhe oren e tanishme.

        print('Kalkulimi nga serveri: Data dhe ora e tanishme:  '+ now.strftime("%d-%m-%Y %H:%M:%S")+'.')  
        text = now.strftime("%d-%m-%Y %H:%M:%S")

        textEncoded = text.encode(encoding='UTF-8')

        UDPServerSocket.sendto(textEncoded, address)
        print('Perfundoi komunikimi.')



    elif operacioni=="GAME":   # Metoda GAME
        print('Kerkesa nga klienti: Me kthe 5 numra te rastesishem nga rangu [0-35].')

        randomlist = random.sample(range(0, 30), 5)   # Funksioni qe gjen 5 numra te rastesishem nga rangu [0-35].
        randomlist.sort()   # Ketu e kam bere sortimin ashtu si eshte kerkuar ne projekt.
        text=str(randomlist)   # E kthejme ne string, per ta derguar me lehte te klienti.

        print('Kalkulimi nga serveri: 5 numra te rastesishem nga rangu [0-35]: ' + text + '.')

        textEncoded = text.encode(encoding='UTF-8')

        UDPServerSocket.sendto(textEncoded, address)
        print('Perfundoi komunikimi.')



    elif operacioni=="GCF":   # Metoda GCF
        KerkesaEKlientit = UDPServerSocket.recvfrom(bufferSize)
        message = KerkesaEKlientit[0]
        str1 = str(message.decode("utf-8")) 

        print('Kerkesa nga klienti:' + str1)

        def Convert(string):   # Ketu nga klienti e marrim si p.sh. gcf 10 20, kete tekst(string), e kthejme ne varg.
            li = string.split(" ")
            return li 

        list = Convert(str1)   # Listen e mbushim ketu.

        x=int(list[1])   # Elementin e dyte, qe i bie te jete numri i pare qe eshte ne string e kthejme ne int.
        y=int(list[2])   # Elementin e trete, qe i bie te jete numri i dyte qe eshte ne string e kthejme ne int.

        print('Kalkulimi nga serveri: Pjestuesi me i madh i perbashket (GCF) ne mes te ' + str(x) + ' dhe te ' + str(y) + ' eshte ' + str(math.gcd(x,y))+'.')

        text = str(math.gcd(x,y))
        
        textEncoded = text.encode(encoding='UTF-8')

        UDPServerSocket.sendto(textEncoded, address)
        print('Perfundoi komunikimi.')


  
    elif operacioni=="CONVERT":   # Metoda CONVERT
        KerkesaEKlientit = UDPServerSocket.recvfrom(bufferSize)
        message = KerkesaEKlientit[0]
        str1 = str(message.decode("utf-8")) 

        print('Kerkesa nga klienti:' + str1)

        def Convert(string):   # Funksioni per konvertimin e stringut ne list, elementet ndahen me " " - hapesire.
            li = string.split(" ")
            return li 

        list = Convert(str1)   # Listen e mbushim ketu.

        # Sqarim: Kam mundur te bej kete detyre ne menyre me te thjeshte, por keshtu eshte kerkuar.

        if (list[1] == 'CmToFeet') or (list[1] == 'cmtofeet') or (list[1] == 'CMTOFEET'):
            cm = float(list[2])
            feet = cm / 30.48
            text = feet
        elif (list[1] == 'FeetToCm') or (list[1] == 'feettocm') or (list[1] == 'FEETTOCM'):
            feet = float(list[2])
            cm = feet * 30.48
            text = cm
        elif (list[1] == 'KmToMiles') or (list[1] == 'kmtomiles') or (list[1] == 'KMTOMILES'):
            km = float(list[2])
            miles = km*1.609
            text = miles
        elif (list[1] == 'MilesToKm') or (list[1] == 'milestokm') or (list[1] == 'MILESTOKM'):
            miles = float(list[2])
            km = miles / 1,609
            text = km
        else:
            text = 'Keni shtypur ndonje gje gabim!\nMbani mend, CONVERT {Hapsire} Opcioni {Hapsire} Numer.\nDuhet ta shkruani saktesisht operacionin:\nPer shendrrimin nga cm ne feet shkruane: CmToFeet.\nPer shendrrimin nga feet ne cm shkruane: FeetToCm.\nPer shendrrimin nga km ne miles shkruane: KmToMiles.\nPer shendrrimin nga miles ne km shkruane: MilesToKm.'
        
        print('Kalkulimi nga serveri: ' + str(text)+'.')        

        textfloatencode = str(text)
        textEncoded = textfloatencode.encode(encoding='UTF-8')

        UDPServerSocket.sendto(textEncoded, address)
        print('Perfundoi komunikimi.')



    elif operacioni=="MYHEALTH":   # Metoda My Health
        KerkesaEKlientit = UDPServerSocket.recvfrom(bufferSize)
        message = KerkesaEKlientit[0]
        str1 = str(message.decode("utf-8")) 

        print('Kerkesa nga klienti: A jam i infektuar me virusin COVID-19.')

        def Convert(string):   # Me kete funskion bejme konvertimin nga string ne nje list, qe ti qasemi nje nga nje elementeve.
            li = string.split(", ")
            return li 
        
        virusi = Convert(str1)

        mundesia = 0   # Mundesia qe te jemi te infektuar ne fillim eshte zero, por pastaj varesisht prej pergjigjieve shkon duke u rritur.
        if float(virusi[1]) > 38.0:
            mundesia=mundesia+15

        if (virusi[2] == 'po') or (virusi[2] == 'Po') or (virusi[2] == 'pO') or (virusi[2] == 'PO'):
            mundesia=mundesia+15
        elif (virusi[2] == 'jo') or (virusi[2] == 'Jo') or (virusi[2] == 'jO') or (virusi[2] == 'JO'):
            mundesia=mundesia+0

        if (virusi[3] == 'po') or (virusi[3] == 'Po') or (virusi[3] == 'pO') or (virusi[3] == 'PO'):
            mundesia=mundesia+15
        elif (virusi[3] == 'jo') or (virusi[3] == 'Jo') or (virusi[3] == 'jO') or (virusi[3] == 'JO'):
            mundesia=mundesia+0

        if (virusi[4] == 'po') or (virusi[4] == 'Po') or (virusi[4] == 'pO') or (virusi[4] == 'PO'):
            mundesia=mundesia+20
        elif (virusi[4] == 'jo') or (virusi[4] == 'Jo') or (virusi[4] == 'jO') or (virusi[4] == 'JO'):
            mundesia=mundesia+0

        if (virusi[5] == 'po') or (virusi[5] == 'Po') or (virusi[5] == 'pO') or (virusi[5] == 'PO'):
            mundesia=mundesia+10
        elif (virusi[5] == 'jo') or (virusi[5] == 'Jo') or (virusi[5] == 'jO') or (virusi[5] == 'JO'):
            mundesia=mundesia+0

        if (virusi[6] == 'po') or (virusi[6] == 'Po') or (virusi[6] == 'pO') or (virusi[6] == 'PO'):
            mundesia=mundesia+25
        elif (virusi[6] == 'jo') or (virusi[6] == 'Jo') or (virusi[6] == 'jO') or (virusi[6] == 'JO'):
            mundesia=mundesia+0


        print('Kalkulimi nga serveri: Ju keni ' + str(mundesia)+' % mundesi qe ju te jeni te infektuar me COVID-19.')

        text = str(mundesia)+' % mundesi qe ju te jeni te infektuar me COVID-19.'

        textEncoded = text.encode(encoding='UTF-8')

        UDPServerSocket.sendto(textEncoded, address)
        print('Perfundoi komunikimi.')



    elif operacioni=="MOSTFREQUENT":   # Metoda Most frequent
        KerkesaEKlientit = UDPServerSocket.recvfrom(bufferSize)
        message = KerkesaEKlientit[0]
        str1 = str(message.decode("utf-8")) 

        list = str1.split()

        print('Kerkesa nga klienti: Cilet fjale jane perdorur me se shpeshti. ')
        print('Kalkulimi nga serveri: Fjalet qe jane perdorur me se shpeshti jane: ')  

        Counter0 = Counter(list) 
        FP = Counter0.most_common(3)   # FP - Fjala me e perdorur, (3) e kam zgjedhur sepse dua ti di vetem top 3 fjalet me te perdorura.
        
        text = ('1. Fjala ' + str(FP[0][0]) + ' eshte perdorur ' + str(FP[0][1]) + ' here.\n' + '2. Fjala ' + str(FP[1][0]) + ' eshte perdorur ' + str(FP[1][1]) + ' here.\n' + '3. Fjala ' + str(FP[2][0]) + ' eshte perdorur ' + str(FP[2][1]) + ' here.')
        print(text)

        bytesToSend = text.encode(encoding='UTF-8')

        UDPServerSocket.sendto(bytesToSend, address)
        print('Perfundoi komunikimi.')



    else:
        print('Ky operacion nuk egziston.')