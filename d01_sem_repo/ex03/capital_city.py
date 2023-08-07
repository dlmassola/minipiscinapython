import sys

def exibirCapital():
    if (len(sys.argv) != 2):
        return

    estado = sys.argv[1]

    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }
    
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
        }
    
    if states.get(estado):
        sigla = states[estado]
        if capital_cities.get(sigla):
            print(capital_cities[sigla])
    else:
        print("Unknown state")


if __name__ == '__main__':
    exibirCapital()