#!/usr/bin/env python
#-*- coding: utf-8 -*-
#########################################
# Projeto: Gerador de senhas aleatorias #
# Autor: Joni                           #
# Versao atual: 0.1                     #
# Data: 27/01/2019                      #
#########################################

import random
import sys
import getopt

letrasminusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","w","y","z"]
letrasmaiusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","W","Y","Z"]
numeros = ["0","1","2","3","4","5","6","7","8","9"]

def usage():
    print "GERADOR DE SENHAS"
    print
    print "Instruções de uso:"
    print "./gerar.py numero_caracteres arg1 arg2 arg3"
    print "-t --tamanho     -entrada do tamanho desejado para a senha"
    print "-p --pequenas    -insere letras minusculas na senha"
    print "-g --grandes     -insere letras maiusculas na senha"
    print "-n --numeros     -insere numeros na senha"
    print "-h --help        -ajuda"
    print 
    print "Exemplo:"
    print "./gerar.py -t 10 -p"
    sys.exit(0)

def main():
    global pequena
    global grande
    global num
    global tamanho
    
    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:p:g:n:t:",["help","pequena","grande","num","tamanho"])
    except getopt.GetoptError as err:
        print str(err)

    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()            
        if o in ("-p", "--pequena"):
            pequena = True
        elif o in ("-g","--grande"):
            grande = True
        elif o in ("-n","--numero"):
            numero = True
        elif o in ("-t","--tamanho"):
            tamanho = int(sys.argv[3:])
        else:
            assert False, "Unhandled Option"
