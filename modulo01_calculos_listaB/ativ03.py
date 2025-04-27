# Inicio
distanciaPrevista = float(input('Distancia Prevista para viagem: '))
litroGasolina = float(input('Preço do litro de gasolina: '))
litroAlcool = float(input('Preço do litro de gasolina: '))
percentEletrico = float(input('Percentual da viagem utilizando eletricidade: '))

# Processamento
distanciaCombustao = distanciaPrevista - (percentEletrico * distanciaPrevista/100)

totalGasolinaLowEnd = distanciaCombustao / 15
custoGasolinaLowEnd = totalGasolinaLowEnd * litroGasolina
totalGasolinaHighEnd = distanciaCombustao / 10
custoGasolinaHighEnd = totalGasolinaHighEnd * litroGasolina

totalAlcoolLowEnd = distanciaCombustao / 12
custoAlcoolLowEnd = totalAlcoolLowEnd * litroAlcool
totalAlcoolHighEnd = distanciaCombustao / 8
custoAlcoolHighEnd = totalAlcoolHighEnd * litroAlcool


# Final
print(f'''
---------------------------------------------
Abastecimento (Gasolina) : {totalGasolinaLowEnd:.1f}L a {totalGasolinaHighEnd:.1f}L
Custo                    : R${custoGasolinaLowEnd:.2f} a R${custoGasolinaHighEnd:.2f}L

Abastecimento (Alcool)   : {totalAlcoolLowEnd:.1f}L a {totalAlcoolHighEnd:.1f}L
Custo                    : R${custoAlcoolLowEnd:.2f} a R${custoAlcoolHighEnd:.2f}
---------------------------------------------
''')