#L07-02 Aatu

def paaohjelma():
    class VARASTO:
        automerkki = ""
        lukumaara = ""
    varasto = VARASTO()
    aliohjelma_kysymys(varasto)
    aliohjelma_tulostus(varasto)

def aliohjelma_kysymys(varasto):
    varasto.automerkki = str(input("Anna automerkki: "))
    varasto.lukumaara = int(input("Anna automerkin lukumäärä varastossa: "))
    return varasto

def aliohjelma_tulostus(varasto):
    print("Varastossa on nyt",varasto.automerkki+"-merkkisiä autoja",varasto.lukumaara,"kpl.")

paaohjelma()
