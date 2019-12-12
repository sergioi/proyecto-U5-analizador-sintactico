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








#inicion kauil (eliminar comentario)///////////////////////////////////////////////////////////////////////////////////////



# fin kauil (eliminar comentario cuando subas)/////////////////////////////////////////////////////////////////////////////////




#incio de geo (eliminar comentario) //////////////////////////////////////////////////////////////////////////////////////////




# fin de geo (elimianr comentrario)/////////////////////////////////////////////////////////////////////////////////////////////////////


