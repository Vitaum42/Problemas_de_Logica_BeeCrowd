# 1042 - Coordenadas de um Ponto

# Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).
#Se o ponto estiver na origem, escreva a mensagem “Origem”.
#Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

#Entrada
#A entrada contem as coordenadas de um ponto.

#Saída
#A saída deve apresentar o quadrante em que o ponto se encontra.#

def cord (x,y):
    
    if x == 0 and y == 0:
        return 'Origem'
    elif x == 0:
        return 'Eixo Y'
    elif y == 0:
        return 'Eixo X'
        
    elif x > 0 and y > 0:
        return 'Q1'
    elif x > 0 and y < 0:
        return 'Q4'
    elif x < 0 and y > 0:
        return 'Q2'
    elif x < 0 and y < 0:
        return 'Q3'
    else:
        return 'Origem'

x, y = map(float, input('').split())

print(cord(x,y))