# -*- coding: utf-8 -*-
import hashlib

print """

██████╗ ██╗   ██╗     ██╗   ██╗████████╗██╗██╗     ███████╗
██╔══██╗╚██╗ ██╔╝     ██║   ██║╚══██╔══╝██║██║     ██╔════╝
██████╔╝ ╚████╔╝█████╗██║   ██║   ██║   ██║██║     ███████╗
██╔═══╝   ╚██╔╝ ╚════╝██║   ██║   ██║   ██║██║     ╚════██║
██║        ██║        ╚██████╔╝   ██║   ██║███████╗███████║
╚═╝        ╚═╝         ╚═════╝    ╚═╝   ╚═╝╚══════╝╚══════╝
                                                           """

print "choose an option"
print "Press 1 for password generator"
print ""
menu = input()
if menu == 1:
 message = raw_input('The name of your mom:')
 hashlib.sha224(message).hexdigest()
 
