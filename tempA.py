temperature = [14,18,21,20,19,16,15]

#durchschnitt berechnen
def durchschnitt(temperature):
  print(sum(temperature)/len(temperature))

#hoechste und niedrige temperature 
def maxtempspannweite(temperature):
  print(max(temperature))

def mintempspannweite(temperature):
    print( min(temperature))

#pruefen,ob die Durchschnittstemperatur warm oder kalt ist
def grad_temp(temperature):
  if temperature > 20:
    print("Woche war warm!")

print("Woche war kuehl")

if __name__ == "__main__":
  grad_temp = durchschnitt(temperature)
  max_temp = maxtempspannweite(temperature)
  min_temp = mintempspannweite(temperature)

print(f"Durchschnittstemparatur: {grad_temp} °c")
print(f"Höchste Temperatur : {max_temp}")
print(f"Niedrigste Temperatur: {min_temp}")
print(f"gradtemp(grad_temp)")

