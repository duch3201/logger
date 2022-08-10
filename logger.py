import os
import sys
from datetime import date

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

