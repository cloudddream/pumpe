#!/usr/bin/python
# Erweiterte Interrupt Programmiereung
# 210316 HJM

# Import GPIO Library
import RPi.GPIO as GPIO

# Import Zeit Library
import time



# Globale Variablen
#Channel Variablen
ch18 = 18
ch23 = 23
ch24 = 24
# Globale Callback Variable zur Kommunikation
glo_callback=0

# Zum Testen
# Zaehler-Variable, global
channel = 18  # GPIO-Pin
Counter = 0
Tic = 0

# Nutze GP# als Port Referenz
GPIO.setmode(GPIO.BCM)

# Test Port einrichten
# GPIO 18 (Pin 12) als Input definieren und Pullup-Widerstand aktivieren
GPIO.setup(ch18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Callback-Funktion
def Interrupt(ch18):
  global Counter
  # Counter um eins erhoehen und ausgeben
  Counter = Counter + 1
  print("Counter " + str(Counter))

# Interrupt hinzufügen
# GPIO.add_event_detect(channel, GPIO.BOTH, callback=<Name der Callback-Funktion>)
# GPIO.add_event_detect(channel, GPIO.RISING, ...)  Flanke 0->1
# GPIO.add_event_detect(channel, GPIO.Falling, ...) Flanke 1->0
# GPIO.add_event_detect(channel, GPIO.BOTH, ...)    Flanke 1->0 oder 0->1
# Bei both muss der Port ausgelesen werden um den Fall zu unterscheiden
# Port = 1, steigende Flanke. Port = 0 fallende Flanke

GPIO.add_event_detect(18, GPIO.RISING, callback = Interrupt, bouncetime = 250)

# Hauptprogramm
# Endlosschleife, bis Strg-C gedrueckt wird
# try:
#  while True:
    # nix Sinnvolles tun
#    Tic = Tic + 1
#    print("Tic %d" % Tic)
#    time.sleep(1)except KeyboardInterrupt:
#  GPIO.cleanup()
#  print ("\nBye")

#******     Hauptprogramm *******
while True:
    try:
        # Eingabe kann hier beliebig sein,keine Initialisierung
        # eingabe = " "
        eingabe = input ("press enter  to exit ")
        break
    except ValueError:
        GPIO.cleanup()
        print("Abbruch mit Fehler! Strg+C")
    # try End
# while End

print("Sauberes Ende mit ENTER")
GPIO.cleanup()
# **********Ende des Hauptprograms ************