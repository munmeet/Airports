#!/usr/bin/env python3
import time
import json

with open("airports.json", "r") as openfile:
    y = json.load(openfile)
x = y.keys()

gate = {"icao" : "S", "iata" : "S", "name" : "S", "city" : "S", "state" : "S", "country" : "S", "elevation" : "N", "lat" :  "N", "lon" : "N", "tz" : "S"}

def targeter(airport,taxi):
   z = y[airport]
   g = str(z.get(taxi)) #10 prints
   key1 = f"\"{taxi}\":"
   key2 = gate.get(taxi)
   key3 = g
   k = {key2:key3}
   m = key1 + str(k)
   return m
###################################

def targets():
    for target in x:
        folder= "tmp/"
        file = target + ".json"
        filepath = folder + file
        with open(filepath, "w") as disk:
            disk.write("{\n")
            disk.close()
            for targeted in gate:
                terminal = targeter(target,targeted)
                with open(filepath, "a") as disk:
                    disk.write(str(terminal))
                    disk.write(",\n")
                print("\n",target,"[OK]")
            with open(filepath, 'a') as disk:
                date = time.time()
                timestamp =  f"\"timestamp\":{{\"S\":\"{date}\"}}"
                disk.write(timestamp)
                disk.write("\n}")
targets()
