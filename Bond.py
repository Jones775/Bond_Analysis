import time
import random



zinsumfeld = 4

class Trader:
    #Dieses Dictionary sagt, um wie viele Punkte die Trading-Wahrscheinlichkeit erhöht
    #werden soll, je nachdem, wie hoch das Verhältnis der Restlaufzeit zur Gesamtlaufzeit ist
    #Je kleiner dieses Verhältnis wird, desto höher wird die Wahrscheinlichkeit
    laufzeit_probability = {1.0: 0, 
                            0.9:1, 
                            0.8:2,
                            0.7:5,
                            0.6:10,
                            0.5:25,
                            0.4:48,
                            0.3:70,
                            0.2:85,
                            0.1:95,
                            0.0:100}

    def __init__(self, bonds):
        self.bonds = bonds
        self.buying_probability = 0

    def analize_bond(self, bond):

        restlaufzeit = bond.restlaufzeit/bond.gesamtlaufzeit
        restlaufzeit = Trader.laufzeit_probability[restlaufzeit]
        self.buying_probability += restlaufzeit
        print(self.buying_probability)

    def trade(self, bond):
        self.analize_bond(bond)
        
        if self.bonds > 0:
            pass


        

class Anleihe:

    def __init__(self, nominalwert, kurswert, interest_rate, gesamtlaufzeit, restlaufzeit):
        self.nominalwert = nominalwert
        self.kurswert = kurswert
        self.interest_rate = interest_rate
        self.gesamtlaufzeit = gesamtlaufzeit
        self.restlaufzeit = restlaufzeit

    def simulation(self):
        for year in range(self.gesamtlaufzeit+1):
            #print(f"Jahr: {year}")
            #print(f"Restlaufzeit: {self.restlaufzeit}")
            #print("-----------------------------------")
            self.restlaufzeit -= 1

            #Testen mit random renditen
            rendite = random.randint(-100, 100)
            vorherige_rendite = rendite
            self.print_chart(rendite, vorherige_rendite)

        

    def print_chart(self, rendite, vorherige_rendite):
        for _ in range(100):
            print()
        
        #if rendite > 0:
        #    print("/", end="")
        #elif rendite < 0:
        #    print("\\", end="")
        #else:
        #    print("-", end = "")

        print("Hallo")
        time.sleep(5)

bond = Anleihe(100, 100, 5, 40, 40)
#bond.simulation()

trader = Trader(40)
trader.trade(bond)