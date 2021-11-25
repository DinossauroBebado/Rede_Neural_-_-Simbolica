import matplotlib.pyplot as plt
import csv

x = []
y = []
z = []
head = True
with open('Vacinas_COVID_clear.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')

    for row in plots:
        if head:
            head = False
            continue
        x.append(row[0])
        y.append(int(row[2]))
        z.append(int(row[1]))

plt.plot(x, y, color='b', label="2 Dose")
plt.plot(x, z, color='g', label="1 Dose")
plt.xlabel('Dias')
plt.ylabel('Dose')
plt.title('Doses')
plt.legend()
plt.savefig("dose.png")
