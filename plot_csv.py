import matplotlib.pyplot as plt
import csv

x = []
y = []
head = True
with open('Casos_COVID_clear.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')

    for row in plots:
        if head:
            head = False
            continue
        x.append(row[0])
        y.append(int(row[2]))

plt.plot(x, y, color='r', label="Óbitos")
plt.xlabel('Dias')
plt.ylabel('Óbitos')
plt.title('Óbitos pelo passar do tempo')
plt.legend()
plt.savefig("Óbitos_tempo.png")
