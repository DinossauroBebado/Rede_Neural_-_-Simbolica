import matplotlib.pyplot as plt
import csv

x = []
y = []
z = []
head = True
with open('Casos_COVID_clear.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')

    for row in plots:
        if head:
            head = False
            continue
        x.append(row[0])
        y.append(int(row[2]))
        z.append(int(row[1]))
'''
plt.plot(x, y, color='b', label="Contaminados resultando em Óbitos")
plt.plot(x, z, color='g', label="Contaminados")
plt.xlabel('Dias')
plt.ylabel('Casos')
plt.title('Contaminação de COVID-19 na cidade de Curitiba')
plt.legend()
plt.savefig("casos_curitiba.png")'''

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Tempo')
ax1.set_ylabel('Óbitos', color=color)
ax1.plot(x, y, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
# we already handled the x-label with ax1
ax2.set_ylabel('Contaminados', color=color)
ax2.plot(x, z, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Contaminação de COVID-19 na cidade de Curitiba')
plt.savefig("casos_curitiba.png")
