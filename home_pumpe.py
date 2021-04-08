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
#Channel Variablen (GPIO#)
ch18 = 18  # PIN 12 (R) Signal Low Level Dry security, Pump Off, Input, ext. Pull Up,
ch22 = 22  # PIN 15 (L) Signal Low Level Pump Off, Input, ext. Pull Up
ch24 = 24  # PIN 18 (L) Signal High Level Pump On, Input, ext. Pull Up
ch25 = 25  # PIN 22 (R) Switch Turn On/Of Pump,    Output,ext. Pull Down
ch17 = 17  # PIN 11 (L) LED Pumpe aktiv            Output,ext. Basis Transistor
ch27 = 27  # PIN 13 (L) Reset PI after 5 sec.      Input, ext. SW1
ch5 = 5   # PIN 29 (L)
ch6 = 6   # pin 31 (L)
ch12 = 12  # pin 32 (R)
ch13 = 13  # PIN 33 (L)
ch19 = 19  # PIN 35 (L)
ch16 = 16  # PIN 36 (R)
ch16 = 26  # PIN 37 (L)
ch20 = 20  # PIN 38 (R)
ch21 = 21  # PIM 40 (R)


# Globale Callback Variable zur Kommunikation
glo_callback = 0

# Nutze GPIO# als Port Referenz
GPIO.setmode(GPIO.BCM)

# Port Initializing
# GPIO Defined as Input without intern pullup resistor.
# All Output is hard wired to VCC or GND!
# Because there might be undefined states at GPIO
# before the system is fully initializend and cause
# unattended activation of the pump
GPIO.setup(ch18, GPIO.IN)  # Dry  level Indicator
GPIO.setup(ch22, GPIO.IN)  # Low  level Indicator
GPIO.setup(ch24, GPIO.IN)  # High level Indicator
GPIO.setup(ch5, GPIO.IN)   # Extra High level Indicator

# GPIO 25 define as output without intern pullup resistor
GPIO.setup(ch25, GPIO.OUT) # Pump On/Of
GPIO.setup(ch17, GPIO.OUT) # LED for Status Information
GPIO.setup(ch24, GPIO.IN)  # Reset(5s), Shutdown(10s) Button


# Callback-Funktion
def Int18(ch18):
  global counter
  # For testing! Increase counter and print
  #counter = counter + 1
  #print("\n counter Int18 " + str(counter))
  print("\n Int18. Dry level reached! Pumpe wird ausgeschaltet")
  # Log Datei schreiben
  # Mail senden
  
 def Int22(ch22):
  global counter
  # For testing! Increase counter and print
  #counter = counter + 1
  #print("\n counter Int18 " + str(counter))
  print("\n Int22: Dry level reached! Pumpe wird ausgeschaltet")
  # Log Datei schreiben
  # Mail senden
  
  def Int24(ch24):
  global counter
  # For testing! Increase counter and print
  #counter = counter + 1
  #print("\n counter Int18 " + str(counter))
  print("\n Int24: High level reached! Pump started")
  # Log Datei schreiben
  # Mail senden
    
def Int5(ch5):
  global counter
  # For testing! Increase counter and print
  #counter = counter + 1
  #print("\n counter Int18 " + str(counter))
  print("\n Int5: Alert level reached! Pump maybe defect")
  # Log Datei schreiben
  # Mail senden
  
# Interrupt hinzufügen
# GPIO.add_event_detect(channel, GPIO.BOTH, callback=<Name der Callback-Funktion>)
# GPIO.add_event_detect(channel, GPIO.RISING, ...)  Flanke 0->1
# GPIO.add_event_detect(channel, GPIO.Falling, ...) Flanke 1->0
# GPIO.add_event_detect(channel, GPIO.BOTH, ...)    Flanke 1->0 oder 0->1
# Bei both muss der Port ausgelesen werden um den Fall zu unterscheiden
# Port = 1, steigende Flanke. Port = 0 fallende Flanke

# Trigger für Wasserstände
GPIO.add_event_detect(ch18, GPIO.FALLING, callback = Int18, bouncetime = 250)
GPIO.add_event_detect(ch22, GPIO.FALLING, callback = Int22, bouncetime = 250)
GPIO.add_event_detect(ch24, GPIO.FALLING, callback = Int24, bouncetime = 250)



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
        print("Cleaning up GPIO after Finally Procedure")
        GPIO.cleanup()
    # try End
# while End

#print("Sauberes Ende mit ENTER")
#GPIO.cleanup()
# **********Ende des Hauptprograms ************