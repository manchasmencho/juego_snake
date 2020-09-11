import tkinter
import turtle
import time
import random

posponer = 0.1

#marcador
score = 0
high_score =0

#configuracion de la ventana
wn = turtle.Screen()
wn.title('Juego de snake')
wn.bgcolor('#ff0099')
wn.setup(width=800, height=600)
wn.tracer(0)

#cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square')
cabeza.color('#1E9600')
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = 'stop'

#comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.color('#f7ff00')
comida.penup()
comida.goto(0,100)

#cuerpo de la serpiente
segmentos = []

texto = turtle. Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write('score: 0       High Score: 0', align= 'center', font=('courier', 24, 'normal'))

#funciones
def arriba():
    cabeza.direction = 'up'
def abajo():
    cabeza.direction = 'down'
def derecha():
    cabeza.direction = 'right'
def izquierda():
    cabeza.direction = 'left'    

def mov():
    if cabeza.direction =='up':
        y = cabeza.ycor()
        cabeza.sety(y +20)

    if cabeza.direction =='down':
        y = cabeza.ycor()
        cabeza.sety(y -20)

    if cabeza.direction =='left':
        x = cabeza.xcor()
        cabeza.setx(x -20)

    if cabeza.direction =='right':
        x = cabeza.xcor()
        cabeza.setx(x +20)

#teclado
wn.listen()
wn.onkeypress(arriba, 'Up')
wn.onkeypress(abajo, 'Down')
wn.onkeypress(izquierda, 'Left')
wn.onkeypress(derecha, 'Right')

while True:
    wn.update()

    #colisiones bordes
    if cabeza.xcor() > 370 or cabeza.xcor() < -370 or cabeza.ycor() > 270 or cabeza.ycor() < -270:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = 'stop'

        #esconder los segmentos
        for segmento in segmentos:
            segmento.goto(1200,1200)

        #limpiar lista de segmentos
        segmentos.clear()

        #resetear marcador
        score = 0
        texto.clear()
        texto.write('score: {}      High Score: {}'.format(score, high_score), align= 'center', font=('courier', 24, 'normal'))


    #colisiones comida
    if cabeza.distance(comida) <20:
        x = random.randint(-370,370)
        y = random.randint(-270,270)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.color('#0082c8')
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        #aumentar marcador
        score += 10

        if score > high_score:
            high_score = score
        
        texto.clear()
        texto.write('score: {}      High Score: {}'.format(score, high_score), align= 'center', font=('courier', 24, 'normal'))

#mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0,-1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
    


    mov()

    #colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = 'stop'

            #esconder los segmentos
            for segmento in segmentos:
                segmento.goto(1200,1200)
            
            segmentos.clear()

    time.sleep(posponer)