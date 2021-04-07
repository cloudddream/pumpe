# Librarys im Hauptmodul
import smtplib       # Mail Bibliothek
#import os            # Bibliothek um z.B Umgebungsvariablen abzurufen
import time
import home_mail_get_usr

#import sys           # Nur für redirection sys.stdout sys.stderr 8Test)


#Setting up log redirection
#orig_std = (sys.stdout, sys.stderr)
#sys.stdout = sys.stderr = open("/home/hans/pi/smtp.log", "a")
# Do smtplib stuff
# Set up debug level
# debuglevel = 1
# smtp = SMTP()
# smtplib.SMTP.set_debuglevel(debuglevel)
# server = smtplib.SMTP.set_debuglevel(debuglevel)

# Funktion zum Lesen der Credentials aufrufen
# import fktsammlung
# fktsammlung.hallomeister()
# nam_smtp =
user = home_mail_get_usr.Findkey("cred_goo.py", "usr_")
pwd = home_mail_get_usr.Findkey("cred_goo.py", "pwd_")
nam_smtp = home_mail_get_usr.Findkey("cred_goo.py", "smtp_")

sm = "   -  "
so = "  -   "
su = "   1  "
st = "  -   "


txt1 = '    Stati der Wasserstand Sensoren\n\n' 
txt2 = ' %s %s %s %s\n' % ("  Motor", " Oben ", " Unten", "Trocken")   
txt3 = '  %s %s %s %s\n' % (sm, so, su, st)

time_mail=time.asctime()

#mail_text = '%s %s %s' % (txt1, txt2, txt3)
#mail_text = "Verry important Test"
mail_text = txt1+txt2+txt3
print(mail_text)
subject = 'Statusbericht Home '

#MAIL_FROM = 'test@example.com'
MAIL_FROM = 'raspberry@pi.de'

#RCPT_TO  = 'test@example.com'
RCPT_TO = user

DATA = 'From:%s\nTo:%s\nSubject:%s\n\n%s' % (MAIL_FROM, RCPT_TO, subject, mail_text) 


# Funktion Schreiben einer Zeile in Datei
# Ausgelagert in Modul
# def writetolog(logtext):
#    fobj_out = open("log.txt","a")    # Daten an Datei nhängen
#    fobj_out.write(logtext)
#    fobj_out.close()
#---END writelog----------

# Beispiel SMTP Objekt erzeugen
# server = smtplib.SMTP('secure.emailsrvr.com:587')
# Achtung secure ist kein Befehl,
# sondern das Präfix des externen Servers!
# Bei GMX   = mail
# Bei Gmail = smtp

logtext = '---------------\n\n'
home_mail_get_usr.writetolog(logtext)
logtext = '%s %s' % (time.asctime(), 'Entering send Mail\n')
home_mail_get_usr.writetolog(logtext)

try:
    #print(time.asctime())
    #server = smtplib.SMTP(nam_smtp)
    #print(time.asctime())
    
    logtext = '%s %s' % (time.asctime(), 'Connection to mailserver established\n')
    home_mail_get_usr.writetolog(logtext)
    
    # Zum Test, Schreiben in die Log datei deaktiviert 
    #server.starttls()
    #server.login(user,pwd)
    #server.sendmail(MAIL_FROM, RCPT_TO, DATA)
    
    logtext = '%s %s' % (time.asctime(), 'Mail send succesfully\n')
    home_mail_get_usr.writetolog(logtext)
    home_mail_get_usr.writetolog(mail_text)
    # Zum Test, Schreiben in die Log datei deaktiviert
    #server.quit()
    
except:
    logtext = '%s %s' % (time.asctime(), 'Error while sending mail\n\n')
    home_mail_get_usr.writetolog(logtext)
    #print('Error while sending mail\n\n')
    #server.quit()
    exit(1)
    #sys.stdout, sys.stderr = orig_std
exit(0)