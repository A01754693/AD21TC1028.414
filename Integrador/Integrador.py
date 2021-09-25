fact = "/Users/cosettediaz/Documents/GitHub/integrador-a01754693/covidmx_reducido.csv.py"

def lectura_archivo(a):
    Lista = open("covidmx_reducido.csv.py", "r")
    a = []
    for i in Lista:
        x = i.split(",")
        a.append(x)
    return a

def main(fact):
    fin = lectura_archivo(fact)
    print(fin)