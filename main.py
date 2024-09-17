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

def ny_konto():
    nytt_konto = input("Skriv in ett kontonummer XXXX: ")

def finns_konto():
    print("Hej")

def administrera_konto():
    print("hej")

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
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            break
        else:
            print("Ogiltigt val!!")


if __name__ == "__main__":
    main()