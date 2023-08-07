import sys

def exibirEstado():
    if (len(sys.argv) != 2):
        return

    capital = sys.argv[1]

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
    
    inv_states = dict(map(reversed, states.items())) 

    inv_capital_cities = dict(map(reversed, capital_cities.items())) 

    if inv_capital_cities.get(capital):
        sigla = inv_capital_cities[capital]
        if inv_states.get(sigla):
            print(inv_states[sigla])
    else:
        print("Unknown capital city")
    
if __name__ == '__main__':
    exibirEstado()