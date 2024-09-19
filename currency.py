pesos = int(input('What do you have left in pesos'))
soles = int(input('What do you have left in soles'))
reais = int(input('What do you have left in reais'))

pesos_to_usd = 4182.30
soles_to_usd = 3.7506
reais_to_usd = 4.87

total_usd = (pesos / pesos_to_usd) + (soles / soles_to_usd) + (reais / reais_to_usd)


print(f"Total em USD: ${total_usd:.2f}")
