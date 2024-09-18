from time import strftime

def öppna_konto_fil():
    konton = {}
    ett_konto = None
    with open("kontonummer.txt" ,"r") as file:
        for line in file:
            line = line.strip()
            if line == "<<<<<<":
                ett_konto = None
            elif line.startswith("konto"):
                ett_konto = line
                konton[ett_konto] = {"saldo" : 0, "transaktioner" : []}
            elif line.startswith("saldo"):
                saldo = int(line.replace("saldo", "").strip())
                konton[ett_konto]["saldo"] = saldo
            elif ett_konto:
                konton[ett_konto]["transaktioner"].append(line)
    return konton


    

def finns_konto(konto):
    with open("kontonummer.txt", "r") as file:
        for line in file:
            if line.startswith(konto):
                return True
        return False

def Ny_transaktion(konto, plus_eller_minus, summa):
    #decimaltal?
    if summa.isdigit():
        summa = int(summa)
        if summa < 0:
            print("ogiltigt lågt nummer, försök igen")
        else:
            if konto["saldo"] < summa and plus_eller_minus == "-":
                print("Du kan inte dra ut mer än vad du har på ditt konto")
            else:
                tid_vid_köp = strftime("(" + "%Y-%m-%d" + "(" + "%H:%M"+ "))")
                konto["transaktioner"].extend([f"{plus_eller_minus}{summa}{tid_vid_köp}"])
                if plus_eller_minus == "+":
                    konto["saldo"] += summa
                else:
                    konto["saldo"] -= summa
                
    else: 
        print("Du måste skriva ett posetivt heltal")
        
def ny_konto():
    nytt_konto = input("Skriv in ett kontonummer XXXX: ")
    kontonummer = "konto" + nytt_konto
    if finns_konto(kontonummer):
        print("Detta konto finns redan, försök igen")
    else:
        with open("kontonummer.txt", "a") as file:
            #file.write(f"\n{kontonummer}")
            #file.write(f"\nsaldo0")
            #file.write(f"\n<<<<<<")
            print("Ditt konto har nu skapats ")



def skriv_ut_konto(konto, saldo_eller_transaktion):
    if saldo_eller_transaktion == "saldo":
        print(f"Saldo:{konto["saldo"]}")
    elif saldo_eller_transaktion == "transaktion":
        print("Transaktioner:")
        for transaktioner in konto["transaktioner"]:
            print(f"{transaktioner}") 


   
def administrera_konto(konto_akriv, kontonummer):
    while True:
        print("----KONTOMENY----")
        print("1. Ta ut pengar")
        print("2. Sätt in pengar")
        print("3. Visa saldo")
        print("4. Visa transaktioner")
        print("5. Avsluta")
        user_input = input(": ")
        if user_input == "1":
            summa = input("Hur mycket pengar vill du ta ut?")
            Ny_transaktion(konto_akriv[kontonummer], "-", summa)
        elif user_input == "2":
            summa = input("Hur mycket pengar vill sätt in?")
            Ny_transaktion(konto_akriv[kontonummer], "+", summa)
        elif user_input == "3":
            skriv_ut_konto(konto_akriv[kontonummer], "saldo")
        elif user_input == "4":
            skriv_ut_konto(konto_akriv[kontonummer], "transaktion")

        elif user_input == "5":
            break
        else:
            print("Ogiltigt svar")

                
def main():
    konto_arkiv = öppna_konto_fil()
    #skriv_ut_konto(konto_arkiv["konto0000"])
    while True:
        print("----Huvudmeny----")
        print("1. Skapa Konto")
        print("2. Administrera konto")
        print("3. Avsluta")
        user_input = input(": ")
        if user_input == "1":
            ny_konto()
        elif user_input == "2":
            user_konto = input("Ange kontonummer: ")
            kontonummer = "konto" + user_konto
            if finns_konto(kontonummer):
                administrera_konto(konto_arkiv, kontonummer)
            else:
                print("kontot finns inte")
        elif user_input == "3":
            break
        else:
            print("Ogiltigt val!!")


if __name__ == "__main__":
    main()


####Att Göra
#txt fil ska läsas up vid programstart
#fixa så funktionen finns konto tittar i en dict om kontot finns och inte i filen
#fixa så att funktionen ny konto fixar en key med kontonummer som man skrivit in och sendan en dict i den med saldo och transaktioner



#Fixa felmedelanden när man skriver in fel saker
#om filen inte finns skapa filen 
#bankonto har bara 4 siffror checker 


#öppnar txt fil i slutet och sen skriver ner alla konton och alla des transaktioner i numerisk ordning på slutet