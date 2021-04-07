#!/usr/bin/python3
# Erweiterte Interrupt Programmiereung
# 210316 HJM


# Import GPIO Library
import RPi.GPIO as GPIO

# Imoport Zeit Library
# time.sleep(sec)
import time
# Mail Bibliothek und OS-Funtionen wie [env]
import smtplib       # Mail Bibliothek
import os            # Bibliothek um z.B Umgebungsvariablen abzurufen

# Globale Variablen
counter = 0
#Channel Variablen
ch18 = 18  # Signal Low Level Dry security, Pump Off, Input, ext. Pull Up,
ch22 = 22  # Signal Low Level Pump Off, Input, ext. Pull Up
ch24 = 24  # Signal High Level Pump On, Input, ext. Pull Up
ch25 = 25  # Switch Turn On/Of Pump,    Output,ext. Pull Down

# Globale Callback Variable zur Kommunikation
glo_callback = 0

# Nutze GP# als Port Referenz
GPIO.setmode(GPIO.BCM)

# Ports einrichten
# GPIO 18.23 als Input definieren und ohne Pullup-Widerstand aktivieren
GPIO.setup(ch18, GPIO.IN)
GPIO.setup(ch22, GPIO.IN)
GPIO.setup(ch24, GPIO.IN)
# GPIO 24 als Output definieren und ohne Pullup-Widerstand aktivieren
GPIO.setup(ch25, GPIO.OUT)

# Callback-Funktion
def Int18(ch18):
  global counter
  # Counter um eins erhoehen und ausgeben
  counter = counter + 1
  print("\n counter Int18 " + str(counter))

# Interrupt hinzufügen
# GPIO.add_event_detect(channel, GPIO.BOTH, callback=<Name der Callback-Funktion>)
# GPIO.add_event_detect(channel, GPIO.RISING, ...)  Flanke 0->1
# GPIO.add_event_detect(channel, GPIO.Falling, ...) Flanke 1->0
# GPIO.add_event_detect(channel, GPIO.BOTH, ...)    Flanke 1->0 oder 0->1
# Bei both muss der Port ausgelesen werden um den Fall zu unterscheiden
# Port = 1, steigende Flanke. Port = 0 fallende Flanke

GPIO.add_event_detect(ch18, GPIO.FALLING, callback = Int18, bouncetime = 250)



#******     Hauptprogramm *******
while True:
    try:
        # Eingabe kann hier beliebig sein, keine Initialisierung
        # eingabe = " "
        eingabe = input ("press enter  to exit ")
        print("Dies war die Eingabe"+" "+eingabe)
        # print(eingabe)
        break
    except:
        print("\nException Abbruch mit Fehler!")
        #print("Cleaning up GPIO after Exception")
        print("Cleaning up GPIO later with finally")
        #GPIO.cleanup()
    else:
        print("\nNo Exception!")
        print("Cleaning up GPIO after No Exception")
        GPIO.cleanup()
    finally:
        print("\nFinally!")
        print("Cleaning up GPIO after Finally")
        GPIO.cleanup()
    # try End
# while End

#print("Sauberes Ende mit ENTER")
#GPIO.cleanup()
# **********Ende des Hauptprograms ************