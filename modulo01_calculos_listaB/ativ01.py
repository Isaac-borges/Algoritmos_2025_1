#Entrada
investidoCDB = float(input('Valor investido no CDB      : '))
anoAtualCDB = int(input('Ano atual                   : '))
anoVencimentoCDB = int(input('Ano do fim do investimento  : '))
prazoCDC = int(input('Prazo do CDC (Até 60 meses) : '))

#Processamento
#CDB
prazoCDB = anoVencimentoCDB - anoAtualCDB

montanteCDBlow = investidoCDB * (1 + 0.01)** prazoCDB
montanteCDBhigh = investidoCDB * (1 + 0.20)** prazoCDB


jurosCDBhigh = montanteCDBhigh - investidoCDB
jurosCDBlow  = montanteCDBlow - investidoCDB

#CDC
parcelaLow = (investidoCDB * 0.01) / (1 - (1 + 0.01)**(-prazoCDC))
parcelaHigh = (investidoCDB * 0.17) / (1 - (1 +0.17)**(-prazoCDC))

montanteCDBlow = prazoCDC * parcelaLow
montanteCDBhigh = prazoCDC * parcelaHigh

jurosCDClow = montanteCDBlow - investidoCDB
jurosCDChigh = montanteCDBhigh - investidoCDB

#Lucro Banco
lucroBancoLow = jurosCDClow - jurosCDBlow 
lucroBancohigh = jurosCDChigh - jurosCDBhigh
#Saida
print(f'''
---------------------------------------------------
      CDB
      Valor investido  : R${investidoCDB:.2f}
      Taxa de Juros    : 1% a 20% a.a.
      Prazo            : {prazoCDB} anos
      Montante final   : R${montanteCDBlow:.2f} à R${montanteCDBhigh:.2f} 
      Juros            : R${jurosCDBlow:.2f} à R${jurosCDBhigh:.2f}
---------------------------------------------------
      CDC
      Valor emprestado : R${investidoCDB}
      Taxa de Juros    : 1% a 17% a.m.
      Prazo            : {prazoCDC} meses
      Valor parcelas   : R${parcelaLow:.2f} a R${parcelaHigh:.2f}
      Montante final   : R${montanteCDBlow:.2f} a R${montanteCDBhigh:.2f} 
      Juros pagos      : R${jurosCDClow:.2f} a R${jurosCDChigh:.2f}
---------------------------------------------------
      Lucro do Banco   : R${lucroBancoLow:.2f} a R${lucroBancohigh:.2f}
---------------------------------------------------

''')