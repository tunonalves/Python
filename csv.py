import csv

with open("contacts.csv",newline="") as csvfile:
	micsv = csv.reader(csvfile, delimiter = ";", quotechar = "|")
	for linea in micsv:
		print("-".join(linea))

