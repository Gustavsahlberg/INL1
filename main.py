import time

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

def Ny_transaktion():
    print("hej")       
        
def ny_konto():
    nytt_konto = input("Skriv in ett kontonummer XXXX: ")
    kontonummer = "konto" + nytt_konto
    if finns_konto(kontonummer):
        print("Detta konto finns redan, försök igen")
    else:
        with open("kontonummer.txt", "a") as file:
            file.write(f"\n{kontonummer}")
            file.write(f"\nsaldo0")
            file.write(f"\n<<<<<<")
        print("Ditt konto har nu skapats ")
    
def administrera_konto():
    print("----KONTOMENY----")
    print("1. Ta ut pengar")
    print("2. Sätt in pengar")
    print("3. Visa saldo")
    print("4. Avsluta")


def skriv_ut_konto(konto):
    print(f"{konto}")
    print(f" Saldo:{konto["saldo"]}")
    print("Transaktioner:")
    for transaktioner in konto["transaktioner"]:
        print(f"{transaktioner}")
                
def main():
    konto_arkiv = öppna_konto_fil()
    skriv_ut_konto(konto_arkiv["konto0000"])
    while True:
        print("----Huvudmeny----")
        print("1. Skapa Konto")
        print("2. Administrera konto")
        print("3. Avsluta")
        user_input = input(": ")
        if user_input == "1":
            ny_konto()
        elif user_input == "2":
            pass
        elif user_input == "3":
            break
        else:
            print("Ogiltigt val!!")


if __name__ == "__main__":
    main()