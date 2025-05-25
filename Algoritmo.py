def DecimalABinario(Numero ,num_bits):
  binario = bin(Numero)[2:].zfill(num_bits)
  return binario
#

def ContarUnos(Numero):
  return Numero.count('1')
#

def MostrarTabla(Tabla):
  print("Índice   -   Binario   -   Cantidad de Unos")
  for clave in Tabla:
    print("  ",clave,"    -   ", Tabla[clave][0],"    -      ", Tabla[clave][1])
#

def ComprobarBitsDiferentes (Cadena1, Cadena2):
  Diferencia = 0
  for i in range(len(Cadena1)):
    if Cadena1[i] != Cadena2[i]:
      Diferencia += 1
  return Diferencia
#

def SustitucionBitsDiferentes(Cadena1, Cadena2):
  NuevaCadena = ""
  for i in range(len(Cadena1)):
    if Cadena1[i] != Cadena2[i]:
      NuevaCadena += "-"
    else:
      NuevaCadena += Cadena1[i]
  return NuevaCadena
#

def BinarioALetra(Cadena):
  mapping = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
    10: 'J',
    11: 'K',
    12: 'L',
    13: 'M',
    14: 'N',
    15: 'O',
    16: 'P'
}
  Resultado = ""
  Cadena = list(Cadena)
  for i in range(len(Cadena)):
    if Cadena[i] == "0":
      Resultado = Resultado + mapping[i+1] + "'"
    if Cadena[i] == "1":
      Resultado = Resultado + mapping[i+1]
  return Resultado
#

def convertir_claves_a_string(obj):
    if isinstance(obj, dict):
        return {str(k): convertir_claves_a_string(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [convertir_claves_a_string(elem) for elem in obj]
    else:
        return obj


def Algoritmo(Minterm, DontCare):

    Minterminos = Minterm

    NroBits = 0
    Minterminos = sorted(Minterminos + DontCare)

    while 2**NroBits <= max(Minterminos):
        NroBits += 1


    Tabla1 = {}
    for num in Minterminos:
        ValorBinario = DecimalABinario(num, NroBits)
        Tabla1[num] = [ValorBinario, ContarUnos(ValorBinario)]


    Orden = 0
    Tabla2 = {}
    for clave in Tabla1:
        for clave1 in Tabla1:
            if Tabla1[clave1][1] == Orden:
                key2 = (clave1,)
                Tabla2[key2] = [Tabla1[clave1][0], Tabla1[clave1][1]]
        Orden += 1
#

    Implicantes = []
    ListaAux = {}

    Simplificaiones = {}
    NroSimplificaciones = 0

    Simplificaiones[0] = Tabla2

    Chequeo = []

    while True:
        AuxSimplificaiones = {}
        Chequeo = []
        for clav in Simplificaiones[NroSimplificaciones]:
            for clav2 in Simplificaiones[NroSimplificaciones]:
                if(Simplificaiones[NroSimplificaciones][clav][1] == (Simplificaiones[NroSimplificaciones][clav2][1]) + 1) and ComprobarBitsDiferentes(Simplificaiones[NroSimplificaciones][clav][0], Simplificaiones[NroSimplificaciones][clav2][0]) == 1:

                    Nombre1 = list(clav)
                    Nombre2 = list(clav2)

                    if all(elemento in Chequeo for elemento in clav2) == False and all(elemento in Chequeo for elemento in clav) == False:
                        Chequeo.extend(list(set(clav2) - set(Chequeo)))
                        Chequeo.extend(list(set(clav) - set(Chequeo)))
                        key = tuple(Nombre2 + Nombre1)
                        AuxSimplificaiones[key] = [SustitucionBitsDiferentes(Simplificaiones[NroSimplificaciones][clav][0], Simplificaiones[NroSimplificaciones][clav2][0]) , Simplificaiones[NroSimplificaciones][clav2][1]]
                        ListaAux[NroSimplificaciones] = AuxSimplificaiones
        #

        Test = 0
        Test1 = 0
        for clave in Simplificaiones[NroSimplificaciones]:
            if all(elemento in Chequeo for elemento in clave) == False:
                Implicantes.append([Simplificaiones[NroSimplificaciones][clave][0], clave])
                Test += 1
            #
            Test1 += 1
        #
        if Test == Test1:
            break
    #
        Test1 = 0
        Test = 0
        Simplificaiones[NroSimplificaciones + 1] = AuxSimplificaiones
        NroSimplificaciones += 1
    #



    Implicantes.reverse()

    ImplicantesEsenciales = []
    TodosMin = []
    MinterIncluidos = []

    for Impli in Implicantes:
        TodosMin.extend(Impli[1])

    for Impli in Implicantes:
        for Min in Impli[1]:
            if Min in TodosMin and TodosMin.count(Min) == 1 and (Impli in ImplicantesEsenciales) == False:
                ImplicantesEsenciales.append(Impli)
                MinterIncluidos.extend(Impli[1])

    Resultado = ""
    for i in range(len(ImplicantesEsenciales)):
        if Resultado == "":
            Resultado = BinarioALetra(ImplicantesEsenciales[i][0])
        else:
            Resultado = Resultado + " + " + BinarioALetra(ImplicantesEsenciales[i][0])
    

    Resultados = {
        1 : Tabla1,
        "Resultado": Resultado
    }
    i = 2
    for Cantidad in range(NroSimplificaciones+1):
        Resultados[i] = Simplificaiones[Cantidad]
        i += 1

    Resultados = convertir_claves_a_string(Resultados)

    return Resultados
