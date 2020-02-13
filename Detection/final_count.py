import RPi.GPIO as GPIO
#from threading import Thread
import multiprocessing
import numpy as np
import time
import cv2

contador_a = multiprocessing.Value('i') 
contador_b = multiprocessing.Value('i') 
contador_c = multiprocessing.Value('i') 
contador_total = multiprocessing.Value('i') 
contador_a.value = 0
contador_b.value = 0
contador_c.value = 0
contador_total.value = 0

def contador_hilo1(contador_a,contador_b,contador_c,contador_total):

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.IN)

    while  1:
        channel = GPIO.wait_for_edge(11,GPIO.FALLING,timeout=3000)
        if channel is None:
            #print('Timeout')
            if GPIO.input(11)==0:
                print('Translape Carril 1')
                contador_a.value = contador_a.value + 1
                print('-----------------------------------')
                print('cuenta 1:',contador_a.value)
                print('cuenta 2:',contador_b.value)
                print('cuenta 3:',contador_c.value)
                contador_total.value = contador_a.value + contador_b.value + contador_c.value
                print('cuenta total:',contador_total.value)
                print('-----------------------------------')
        else:
            contador_a.value = contador_a.value + 1
            print('-----------------------------------')
            print('cuenta 1:',contador_a.value)
            print('cuenta 2:',contador_b.value)
            print('cuenta 3:',contador_c.value)
            contador_total.value = contador_a.value + contador_b.value + contador_c.value
            print('cuenta total:',contador_total.value)
            print('-----------------------------------')
            time.sleep(0.5)
        k = cv2.waitKey(10) & 0xff
        if k == ord('q'):
            break

def contador_hilo2(contador_a,contador_b,contador_c,contador_total):
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.IN)

    while  1:
        channel2 = GPIO.wait_for_edge(12,GPIO.RISING,timeout=3000)
        if channel2 is None:
            #print('Timeout')
            if GPIO.input(12):
                print('Translape Carril 2')
                contador_b.value = contador_b.value + 1
                print('-----------------------------------')
                print('cuenta 1:',contador_a.value)
                print('cuenta 2:',contador_b.value)
                print('cuenta 3:',contador_c.value)
                contador_total.value = contador_a.value + contador_b.value + contador_c.value
                print('cuenta total:',contador_total.value)
                print('-----------------------------------')
        else:
            contador_b.value = contador_b.value + 1
            print('-----------------------------------')
            print('cuenta 1:',contador_a.value)
            print('cuenta 2:',contador_b.value)
            print('cuenta 3:',contador_c.value)
            contador_total.value = contador_a.value + contador_b.value + contador_c.value
            print('cuenta total:',contador_total.value)
            print('-----------------------------------')
            time.sleep(0.5)
        k = cv2.waitKey(10) & 0xff
        if k == ord('q'):
            break

def contador_hilo3(contador_a,contador_b,contador_c,contador_total):
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13,GPIO.IN)

    while  1:
        channel3 = GPIO.wait_for_edge(13,GPIO.RISING,timeout=3000)
        if channel3 is None:
            #print('Timeout')
            if GPIO.input(13):
                print('Translape Carril 3')
                contador_c.value = contador_c.value + 1
                print('-----------------------------------')
                print('cuenta 1:',contador_a.value)
                print('cuenta 2:',contador_b.value)
                print('cuenta 3:',contador_c.value)
                contador_total.value = contador_a.value + contador_b.value + contador_c.value
                print('cuenta total:',contador_total.value)
                print('-----------------------------------')
        else:
            contador_c.value = contador_c.value + 1
            print('-----------------------------------')
            print('cuenta 1:',contador_a.value)
            print('cuenta 2:',contador_b.value)
            print('cuenta 3:',contador_c.value)
            contador_total.value = contador_a.value + contador_b.value + contador_c.value
            print('cuenta total:',contador_total.value)
            print('-----------------------------------')
            time.sleep(0.5)
        k = cv2.waitKey(10) & 0xff
        if k == ord('q'):
            break

def video_hilo():
    #Captura una imagen
    cap = cv2.VideoCapture(0)

    while 1:
        #Se extrae la imagen
        ret, img = cap.read()
        #Mascara definida
        lower_black = np.array([0,0,0], dtype = "uint16")
        upper_black = np.array([40,40,40], dtype = "uint16")
        black_mask = cv2.inRange(img, lower_black, upper_black)
        #Se muestran el numero de pixeles asociados
        num_pixeles = np.sum(black_mask == 255)
        if num_pixeles > 40000:
            print('-----------------------------------')
            print('Determinación de masa')
            print('Número de pixeles:',num_pixeles)
            print('-----------------------------------')
       	    time.sleep(5)
	#Se muestra la imagen detectada
        cv2.imshow('Detección',black_mask)
        k = cv2.waitKey(30) & 0xff
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

hilo1 = multiprocessing.Process(target=contador_hilo1,args=(contador_a,contador_b,contador_c,contador_total))
hilo2 = multiprocessing.Process(target=contador_hilo2,args=(contador_a,contador_b,contador_c,contador_total))
hilo3 = multiprocessing.Process(target=contador_hilo3,args=(contador_a,contador_b,contador_c,contador_total))
hilo4 = multiprocessing.Process(target=video_hilo)

hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()

