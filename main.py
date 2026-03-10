

def print_status(funkce):
    def wrapper(*args, **kwargs):
        print("Spouštím funkci...")
        vysledek = funkce(*args, **kwargs)
        print("Hotovo.")


