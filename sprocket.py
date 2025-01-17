#!/usr/bin/env python3
import json

with open('airports.json', 'r') as openfile:
    
    y = json.load(openfile)

x = y.keys()

#class airport: 
#    index = "rcmp"
#    timestamp = "2025-01-16 15:20:37.855291"

def targeter(airport):
   z = y[airport]
   print(z,"\n")

def targets():    
    for index in x: 
        target = index
        #print(target, "[OK]")
        targeter(target)
targets()
