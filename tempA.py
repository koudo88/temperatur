temperature = [14,18,21,20,19,16,15]

def durchschnitt(werte):
    return sum(werte) / len(werte)

def max_temperatur(werte):
    return max(werte)


def min_temperatur(werte):
  return min(werte)

def wochenfazit(avg):
    if avg > 20:
        return "Woche war warm!"
    return "Woche war eher kühl"

grad_temp = durchschnitt(temperature)
max_temp = max_temperatur(temperature)
min_temp = min_temperatur(temperature)
wochen = wochenfazit(grad_temp)

print(f"Durchschnittstemparatur: {grad_temp:.2f} °c")
print(f"Höchste Temperatur : {max_temp}")
print(f"Niedrigste Temperatur: {min_temp}")
print(f"{wochen}")

