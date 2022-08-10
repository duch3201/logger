import os
import sys
from datetime import date

#made by duch3201 on github, this lib does not come with any warrenty,
#if you wish to modify this code and re distribute it please give credit to og author https://github.com/duch3201

def info(message):
    mes = "[I] " + str(date.today()) + " | " + message
    with open("logs.log", 'a') as logfile:
        logfile.write(mes + "\n")

def warning(message):
    mes = "[W] " + str(date.today()) + " | " + message
    with open("logs.log", 'a') as logfile:
        logfile.write(mes + "\n")

def error(message):
    mes = "[E] " + str(date.today()) + " | " + message
    with open("logs.log", 'a') as logfile:
        logfile.write(mes + "\n")

def debug(message):
    mes = "[D] " + str(date.today()) + " | " + message
    with open("logs.log", 'a') as logfile:
        logfile.write(mes + "\n")

