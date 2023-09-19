# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 20:45:44 2023

@author: cesar
"""

def modus_tollens(P, Q):
    """
    Implementación de Modus Tollens.
    
    Argumentos:
    P (bool): Premisa P
    Q (bool): Negación de la premisa Q (es decir, Q es falso)
    
    Retorna:
    bool: El resultado de la conclusión basada en Modus Tollens
    """
    if P:
        if not Q:
            return False
        else:
            print("Q no es falso, Modus Tollens no se aplica.")
            return None
    else:
        print("P es falso, Modus Tollens no se aplica.")
        return None

# Ejemplo de uso
P = True
Q = False

print("Premisa P es verdadera.")
print("Premisa Q es falsa (negación de Q).")
print("Aplicando Modus Tollens...")
resultado = modus_tollens(P, Q)

if resultado is not None:
    print("Conclusión: P es falso por Modus Tollens.")
else:
    print("No se pudo aplicar Modus Tollens debido a premisas falsas.")
