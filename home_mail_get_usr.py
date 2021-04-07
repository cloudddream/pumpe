#!/usr/bin/env python3
# _*_ coding: utf8
# Function and Serchfile shoud be in the same directory
# otherwise you have to prvide full path of Searchfile like
# \home\user\py\..\seachfilename
# Function call
# findstring = f([searchfilename], [searchstring]) not optional
# searchfilenae: filename to seach for the keyword
# searchstring: keyword to search for
# Example
# If your file searchfilname contains two lines
# 1 usr1 = username
# 2 usr2 = surname
# mystring = Findkey('searchfilename',usr1)
# mysrring will contain 'username)


# Return findstring
import time
#time.sleep(sec)

def Findkey(file_,string):
#def Findkey(row,string):
    first = " " # Left  side from string usr_ = username separator [="]
    last = " "  # Right side from string usr_ = username divided by "="
    row = 0
    pos = 0
    #print('%s %s %s %s' % ("Suche ",string," in -> ",row))
    file = open(file_,'r')
    # Lies alle Zeilen
    for row in file:
        pos = row.find(string)
        #print ('%s %s' % ('Suchergebnis ',pos))
        #time.sleep(1)
        # Ist "string" in Zeile enthalten
        if pos > -1:
            #print ('%s %s' % ("Zeichen gefunden an Position ",pos))
            #time.sleep(1)
            # Suche Position von =
            pos = row.find("=")
            
            #print ('%s %s' % ("= Zeichen gefunden an Position ",pos))
            if pos > -1:
                # Strip all leading and Trailing whitespaces
                #row = row.strip()
                # split that Line at "="
                first, last = row.split("=")
                # cut of all space char
                first = first.strip()
                #print (first)
                # cut of all space char
                last = last.strip()
                #print ('%s %s' % ('Hurra da isser!',last))
                file.close()
                # Funktion beenden
                return (last)
            else:
                file.close()
                pass #print ('%s %s' % ("Benutzer falsch definiert = fehlt",row))
        else:
            #file.close()
            pass
            #print ('%s %s %s' % ('Gesuchten Text ** ',string,' ** nicht gefunden'))
            #print (row)
            #time.sleep(1)
          
#Findkey End *************************

# Funktion Schreiben einer Zeile in Datei
def writetolog(logtext):
    fobj_out = open("log.txt","a")    # Daten an Datei anhängen
    fobj_out.write(logtext)
    fobj_out.close()
#---END writelog----------




# Hauptprogramm
# oder Funktionsaufruf für Modulversion
#usr = " "
#pwd = " "
#file = 'cred_goo.py'
#usr = Findkey(file,"usr_")
#pwd = Findkey(pwd,"pwd_")
#print ('%s %s ' % ('Mail User = ',usr))
#print ('%s %s ' % ('Mail Passwort = ',pwd))