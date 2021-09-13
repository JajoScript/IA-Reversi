import copy

def minimax(juego,estado,profundidad,etapa):
    if juego.Estado_final(profundidad):
        return [-1*juego.utilidad]

    if etapa == 1:
        valor = [-1000, None]
        jugadas_posibles = juego.Generador_Jugadas_validas(1)
    else:
        valor = [1000, None]
        jugadas_posibles = juego.Generador_Jugadas_validas(2)
    for jugada in jugadas_posibles:
        if etapa == 1:
            if juego.Esta_vacia(jugada) and juego.Es_adyacente(jugada) and juego.Permite_salto_negra(jugada):
                juego.ESTADO_JUEGO[jugada[0]][jugada[1]]=2
        else:
            if juego.Esta_vacia(jugada) and juego.Es_adyacente(jugada) and juego.Permite_salto_blanca(jugada):
                juego.ESTADO_JUEGO[jugada[0]][jugada[1]]=1
        estado_de_juego=copy.deepcopy(juego.ESTADO_JUEGO)
        opcion = minimax(juego,estado_de_juego,profundidad+1,etapa*-1)
        #maximizar
        if etapa == 1:
            if valor[0] < opcion[0]:
                valor = [opcion[0], jugada]
        else:
            #minimizar
            if valor[0] > opcion[0]:
                valor = [opcion[0], jugada]
        juego.Devolver_estado(estado)
    return valor