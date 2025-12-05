temperature = [14,18,21,20,19,16,15]

#durchschnitt berechnen
def durchschnitt(werte):
return sum(werte)/len(werte)

#hoechste und niedrige temperature 
def tempspannweite(werte)
return max(werte), min(werte)

#pruefen,ob die Durchschnittstemperatur warm oder kalt ist
def gradtemp(grad):
if grad > 20:
return "Woche war warm!"
else:
return "Woche war kuehl"
