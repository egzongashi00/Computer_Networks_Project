import socket

def main():
    serverName = 'localhost'
    serverPort = 13000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverName,serverPort))

    operacioniprim = input("Jeni lidhur me serverin. \nOperacioni (IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT, MYHEALTH, MOSTFREQUENT)? ")

    # Funksionet e perdorura.
    def Convert(string):   # Funksioni per konvertimin e stringut ne list, elementet ndahen me " " - hapesire.
        li = string.split(" ") 
        return li 

    def repeat():   # Funksioni repeat, qe ta pyesim klientin se a ka ndonje kerkese tjeter.
        pytje = input('\n\n\nA keni ndonje kerkese tjeter? (Po/Jo): ')       
        pytje0 = pytje.upper()
        if (pytje0 == "PO"):
            print('---------------------------------------')
            goto = main()            
        else:
            print('Lidhja me serverin ka perfunduar, cdo te mire.')
            s.close()

    list = Convert(operacioniprim)   # Listen e mbushim ketu.

    operacioni = list[0].upper()   # Pa marre parasysh se si e shenojme kerkesen ajo tek serveri shkon me shkronja te medha.
    s.send(str.encode(operacioni))   # Ketu ja dergojme serverit se cili operacion na nevojitet.   

    if operacioni=="IPADDRESS":
        mesazhi=''
        while True:
            data = s.recv(128)
            if len(data) <= 0:
                break
            mesazhi += data.decode("utf-8")
            print('Përgjigjja: IP Adresa e klientit është: ', mesazhi,'.')
        s.close()        
        repeat()

    elif operacioni=="PORT":
        mesazhi=''
        while True:
            data = s.recv(128)
            if len(data) <= 0:
                break
            mesazhi += data.decode("utf-8")
            print('Përgjigjja: Klienti është duke përdorur portin', mesazhi)
        s.close()
        repeat()

    elif operacioni=="COUNT":
        list[0]=''   # Ketu fjalen e pare qe eshte COUNT e fshijme ne menyre qe mos te ia llogarise zanoret dhe bashtinglloret.
        a = ' '.join(list)   # Ketu listen e kthejme ne string dhe e dergojme ne anen e serverit.
        s.sendall(str.encode(a))
        mesazhi=''
        while True:
            data = s.recv(128)
            if len(data) <= 0:
                break
            mesazhi += data.decode("utf-8")
            print('Përgjigjja: Teksti i pranuar përmban', mesazhi)
        s.close()
        repeat()

    elif operacioni=="REVERSE":
        list[0]=''   # Ketu fjalen e pare qe eshte REVERSE e fshijme ne menyre qe mos ta ktheje mbrashte edhe kete fjale.
        a = ' '.join(list)   # Ketu listen e kthejme ne string dhe e dergojme ne anen e serverit.
        s.sendall(str.encode(a))
        mesazhi=''
        while True:
            data = s.recv(128)
            if len(data) <= 0:
                break
            mesazhi += data.decode("utf-8")
            print('Përgjigjja:', mesazhi,'.')
        s.close()
        repeat()

    elif operacioni=="PALINDROME":
        list[0]=''   # Ketu fjalen e pare qe eshte PALINDROME e fshijme ne menyre qe mos te kontrollohet se a eshte polindrome apo jo.
        a = ' '.join(list)   # Ketu listen e kthejme ne string dhe e dergojme ne anen e serverit.
        ab = a + ' '   # Po i'a shtoj nje space ne fund qe space-in qe na ka mbet pershkak te elementit te pare qe e hjekem mos te na shkaktoje probleme.
        s.sendall(str.encode(ab))
        mesazhi=''
        while True:
            data = s.recv(128)
            if len(data) <= 0:
                break
            mesazhi += data.decode("utf-8")
            print('Përgjigjja:', mesazhi)
        s.close()
        repeat()

    elif operacioni=="TIME":
        mesazhi=''
        while True:
            data = s.recv(128)
            if len(data) <= 0:
                break
            mesazhi += data.decode("utf-8")
            print('Përgjigjja:', mesazhi, '.')
        s.close()
        repeat()

    elif operacioni=="GAME":
        mesazhi=''
        while True:
            data = s.recv(128)
            if len(data) <= 0:
                break
            mesazhi += data.decode("utf-8")
            print('Përgjigjja:', mesazhi,'.')
        s.close()
        repeat()

    elif operacioni=="GCF":
        a = ' '.join(list)   # Ketu listen e kthejme ne string dhe e dergojme ne anen e serverit.
        s.sendall(str.encode(a))
        mesazhi=''
        while True:
            data = s.recv(128)
            if len(data) <= 0:
                break
            mesazhi += data.decode("utf-8")
            print('Përgjigjja:', mesazhi,'.')
        s.close()
        repeat()

    elif operacioni=="CONVERT":
        a = ' '.join(list)   # Ketu listen e kthejme ne string dhe e dergojme ne anen e serverit.   
        s.sendall(str.encode(a))
        mesazhi=''
        while True:
            data = s.recv(128)
            if len(data) <= 0:
                break
            mesazhi += data.decode("utf-8")
            print('Përgjigjja:', mesazhi)
        s.close()
        repeat()

    elif operacioni=="MYHEALTH":
        print('KUJDES!!! \nTek pyetja 2 shkruane temperaturen tuaj me numer, nga pyetja 3-7 pergjigjuni me po ose jo.')
        question1=input('Shkruani emrin tend: ')
        question2=input('Sa e keni temperaturen trupore? ')
        question3=input('A keni ethe? ')
        question4=input('A keni kollitje? ')
        question5=input('A keni veshtiresi ne frymemarrje? ')
        question6=input('A ndjeheni i lodhur? ')
        question7=input('A keni pasur kontakt fizik me ndonje person te infektuar me COVID-19? ')
        print('---------------------------------------')
        list = []
        list.insert(0,question1)   # I fusim te gjitha pyetjet ne nje list.
        list.insert(1,question2)
        list.insert(2,question3)
        list.insert(3,question4)
        list.insert(4,question5)
        list.insert(5,question6)
        list.insert(6,question7)

        list2=', '
        list3 = list2.join(list)   # Elementet e listes i grupojme ne nje string te vetem.

        s.sendall(str.encode(list3))
        mesazhi = ''
        while True:
            data = s.recv(128)
            if len(data) <= 0:
                break
            mesazhi += data.decode("utf-8")
            print('Ju keni: ', mesazhi)
        s.close()
        repeat()

    elif operacioni=="MOSTFREQUENT":
        list[0]=''   # Ketu fjalen e pare qe eshte REVERSE e fshijme ne menyre qe mos ta ktheje mbrashte edhe kete fjale.
        a = ' '.join(list)   # Ketu listen e kthejme ne string dhe e dergojme ne anen e serverit.
        s.sendall(str.encode(a))
        mesazhi=''
        while True:
            data = s.recv(128)
            if len(data) <= 0:
                break
            mesazhi += data.decode("utf-8")
            print('Fjalet qe jane perdorur me se shpeshti jane: \n' + mesazhi)
        s.close()
        repeat()

    elif (operacioni=="SHKYQU") or (operacioni==''):
        print('Lidhja me serverin ka perfunduar, cdo te mire.')
        s.close()

    else:
        print('Ky operacion nuk egziston.')
        repeat()

goto1=main()

