import datetime

# Viernes 13 del anio

def Viernes13delAnio(anio):
    viernes13 = []
    for mes in range(1, 13):
        dia = datetime.date(anio, mes, 13)
        if dia.weekday() == 4:
            viernes13.append(dia)
    return viernes13

def main():
    anio = int(input("Introduce un año: "))
    viernes13 = Viernes13delAnio(anio)
    if viernes13:
        print(f"Los viernes 13 del año {anio} son:")
        for dia in viernes13:
            print(dia.strftime("%d de %B"))
    else:
        print(f"No hay viernes 13 en el año {anio}.")

if __name__ == "__main__":
    main()

