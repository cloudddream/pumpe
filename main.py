#!/usr/bin/env python3

import home_fkt # Aufruf mit
# home_fkt.
import home_mail_get_usr
import time



# **** Funktionsaufruf für Credentials
usr = " "
pwd = " "
file = 'cred_goo.py'
usr = home_mail_get_usr.Findkey(file,"usr_")
pwd = home_mail_get_usr.Findkey(file,"pwd_")
print ('%s %s ' % ('Mail User = ',usr))
print ('%s %s ' % ('Mail Passwort = ',pwd))

start_up_time = time.localtime()     # System goes up in Human readible form YY MM DD
start_up_time_s = time.monotonic()  # Seconds since epoche for easy calculation
exit(0)
#
