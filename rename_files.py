# Pedro Henrique Cruz Silva
# Script para renomear arquivos de videos e suas respctivas legendas, a partir de um arquivo .txt contendo os novos nomes(um nome por linha).
# Os arquivos de video e suas legendas devem estar organizados em ordem alfabetica. Ex: S01E01.x, S01E02.x.

import os
lista_leg = [];
lista_vid = [];

#faz uma lista com todas as legendas
for arq in os.listdir('.'):  # os.listdir('.'): lista os arquivos no diretorio
	if (arq[-3:]) == 'srt':
		lista_leg.append(arq.rstrip()); # rstrip() retorna uma copia das leg, que eh adicionado a lista de leg
	
lista_leg.sort();

#faz uma lista com todos os videos
for arq in os.listdir('.'):  # os.listdir('.'): lista os arquivos no diretorio
	if (arq[-3:]) != 'srt' and (arq[-3:]) != 'txt' and (arq[-3:]) != '.py':
		lista_vid.append(arq.rstrip()); # rstrip() retorna uma copia dos vid, que eh adicionado a lista de vid
	
lista_vid.sort();

arquivo = open('nomes.txt');
lista_nomes = [];
for nomes in arquivo:
	lista_nomes.append(nomes.rstrip()); # rstrip() retorna uma copia de nomes, que eh adicionado a lista de nomes

lista_nomes.sort();

#renomeando legendas: n1 -> nome antigo, n2 -> nome novo
for (n1, n2) in zip(lista_leg, lista_nomes):
	os.rename(n1, n2+(n1[-4:]));
	
#renomeando videos: n1 -> nome antigo, n2 -> nome novo
for (n1, n2) in zip(lista_vid, lista_nomes):
	os.rename(n1, n2+(n1[-4:]));	

#print lista_vid;

arquivo.close();
raw_input("Press ENTER to exit")