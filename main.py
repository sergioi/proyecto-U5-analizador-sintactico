# -*- coding: utf-8 -*-
import ply.yacc as yacc
from analizador_lexico import tokens
#from analizador_lexico import analizador
import ply.lex as lex  # importacion de librerias necesarias
import re

# resultado del analisis
resultado_gramatica = []

# asignacion de funcion

precedence = (
    ('right', 'SI', 'SINO'),
    ('right', 'ASIGNAR'),
    ('left', 'TAGINICIO'),
    ('right', 'TAG_FINAL'),
    ('right', 'PUNTOYCOMA'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS'),
)
nombres = {}


# def p_declaracion_decimall(p):
#    'declaracion : DECIMAL'
#    print("decimal")
def p_declaracion_coditionelse(t):
    'declaracion : SI expresion '
    t[0] = t[1]
def p_declaracion_coditionif(t):
    'declaracion : SINO'
    t[0] = t[1]



# definicon de funcionamiento
def p_declaracion_asignar(t):
    'declaracion : VARIABLE ASIGNAR expresion PUNTOYCOMA'
    nombres[t[1]] = t[3]

    #  primera declaracion
def p_declaracion_taginicio(t):
    'declaracion : TAGINICIO'
    t[0] = t[1]


def p_declaracion_tagfinal(t):
    'declaracion :  TAG_FINAL'
    t[0] = t[1]





def p_declaracion_expr(t):
    'declaracion : expresion PUNTOYCOMA'
   
    t[0] = t[1]


def p_expresion_operaciones(t):
    '''
    expresion  :   expresion SUMA expresion 
                |   expresion RESTA expresion 
                |   expresion MULT expresion
                |   expresion DIV expresion
                |   expresion POTENCIA expresion
                |   expresion MODULO expresion

    '''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        i = t[3]
        t[0] = t[1]
        while i > 1:
            t[0] *= t[1]
            i -= 1








def p_expresion_uminus(t):
    'expresion : RESTA expresion %prec UMINUS'
    t[0] = -t[2]


def p_expresion_grupo(t):
    '''
    expresion  : PARIZQ expresion PARDER 
                | LLAIZQ expresion LLADER
                | CORIZQ expresion CORDER

    '''
    t[0] = t[2]




    
def p_expresion_logicas(t):
    '''
    expresion   :  expresion MENORQUE expresion 
                |  expresion MAYORQUE expresion 
                |  expresion MENORIGUAL expresion 
                |   expresion MAYORIGUAL expresion 
                |   expresion IGUAL expresion 
                |   expresion DISTINTO expresion
                |  PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER
                |  PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER
                |  PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER 
                |  PARIZQ  expresion PARDER MAYORIGUAL PARIZQ expresion PARDER
                |  PARIZQ  expresion PARDER IGUAL PARIZQ expresion PARDER
                |  PARIZQ  expresion PARDER DISTINTO PARIZQ expresion PARDER
    '''
    if t[2] == "<":
        t[0] = t[1] < t[3]
    elif t[2] == ">":
        t[0] = t[1] > t[3]
    elif t[2] == "<=":
        t[0] = t[1] <= t[3]
    elif t[2] == ">=":
        t[0] = t[1] >= t[3]
    elif t[2] == "==":
        t[0] = t[1] is t[3]
    elif t[2] == "!=":
        t[0] = t[1] != t[3]
    elif t[3] == "<":
        t[0] = t[2] < t[4]
    elif t[2] == ">":
        t[0] = t[2] > t[4]
    elif t[3] == "<=":
        t[0] = t[2] <= t[4]
    elif t[3] == ">=":
        t[0] = t[2] >= t[4]
    elif t[3] == "==":
        t[0] = t[2] is t[4]
    elif t[3] == "!=":
        t[0] = t[2] != t[4]


def p_expresion_numero(t):
    'expresion : ENTERO'
    t[0] = t[1]


def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = t[1]


# def p_expresion_cadena(t):
   # 'expresion : COMDOB expresion COMDOB'
   # t[0] = t[2]


def p_expresion_nombre(t):
    'expresion : VARIABLE'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("---------------------------------------------")
        print("SINTAXIS ERROR ")
        print("--------------------------------------------")
        print("")
        print("VERIFICAR: ", t[1])
        print("¿verificar si se definio o asigno un valor(en caso de operacion arimetica)?")
        t[0] = 0
        print("---------------------------------------------")


def p_error(t):
    global resultado_gramatica
    if t:
        # type: es para el tipo
        # value:valor que hace que falle
        # lineno: es para que linea pertenece
        # lexpos: para la posicion donde se encuentra
        resultado = "Error sintactico de tipo {:4} en el valor {:4}".format(
            str(t.type), str(t.value))
       # print("SINTAXIS ERROR")
       # print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
       # print(resultado)
    resultado_gramatica.append(resultado)


# instanciamos el analizador sistactico
parser = yacc.yacc()


def prueba_sintactica(data):
    global resultado_gramatica
   # resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else:
            print("")
    #print("result: ", resultado_gramatica)
    return resultado_gramatica
def p_expresion_numero(t):
    'expresion : ENTERO'
    t[0] = t[1]


def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = t[1]


# def p_expresion_cadena(t):
   # 'expresion : COMDOB expresion COMDOB'
   # t[0] = t[2]


def p_expresion_nombre(t):
    'expresion : VARIABLE'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("---------------------------------------------")
        print("SINTAXIS ERROR ")
        print("--------------------------------------------")
        print("")
        print("VERIFICAR: ", t[1])
        print("¿verificar si se definio o asigno un valor(en caso de operacion arimetica)?")
        t[0] = 0
        print("---------------------------------------------")



def p_error(t):
    global resultado_gramatica
    if t:
        # type: es para el tipo
        # value:valor que hace que falle
        # lineno: es para que linea pertenece
        # lexpos: para la posicion donde se encuentra
        resultado = "Error sintactico de tipo {:4} en el valor {:4}".format(
            str(t.type), str(t.value))
       # print("SINTAXIS ERROR")
       # print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
       # print(resultado)
    resultado_gramatica.append(resultado)


# instanciamos el analizador sistactico
parser = yacc.yacc()


def prueba_sintactica(data):
    global resultado_gramatica
   # resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else:
            print("")
    #print("result: ", resultado_gramatica)
    return resultado_gramatica


path = "index.php"

try:
    archivo = open(path, 'r')
except:
    print("el archivo no se encontro")
    quit()

text = ""
for linea in archivo:
    text += linea

print('-------------------------------------------------')
print(" ____    _   _   ____")
print("|  _ \  | | | | |  _ \ ")
print("| |_) | | |_| | | |_) |")
print("|  __/  |  _  | |  __/ ")
print("|_|     |_| |_| |_|")
print('-------------------------------------------------')

#if 2 == 2:
# print("")
# print('-------------------------------------------------')
#print("         COMPILACION EXITOSA")
# print('-------------------------------------------------')
prueba_sintactica(text)
print('------    RESULADOS OBTENIDOS     ---------------')
print('-------------------------------------------------')
print('\n'.join(list(map(''.join, resultado_gramatica))))
print('-------------------------------------------------')


