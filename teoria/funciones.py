# FUNCIONES
def funcion1 (param1 ='default'):
    """
    Esta es la documentacion de la funcion
    :param param1:
    :return:
    """
    print("estamos dentro de la funcion1 {p}".format(p=param1))
    return ("estamos dentro de la funcion1 {p}".format(p=param1))
funcion1()
pepe = funcion1()