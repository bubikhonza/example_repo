

def print_status(funkce):
    def wrapper(*args, **kwargs):
        print("Spouštím funkci...")
        vysledek = funkce(*args, **kwargs)
        print("Hotovo.")
        return vysledek
    return wrapper

@print_status
def sum(a, b):
    print("Funkce bezi")
    return a + b

res = sum(1,2)
print(res)