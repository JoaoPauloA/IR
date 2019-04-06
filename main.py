from ind_inveted import Index_inverted

index = Index_inverted()

h = index.sref('/home/marcus/Dropbox/Semestre 2018.1/Recuperação da informação/Indice_invertido/avaliacao/arquivos/')

doc = index.busca('What are the effects of calcium on the physical properties of mucus from CF patients')
#index.printf()
for d in doc:
   print(d)
   print()