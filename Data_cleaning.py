import csv
from playground import sort_dates


def casos():
    contaminados = 0
    obitos = 0
    data_prev = None
    head = True

    with open(r'Casos_Covid_19_-_Base_de_Dados.csv', "r", newline='') as csvread:
        with open(r'Casos_COVID_clear.csv', "w", newline='', encoding="utf-8") as csv_write:

            CASOS = csv.reader(csvread, delimiter=';')

            csv_clear = csv.writer(csv_write, delimiter=';',
                                   quotechar='"', quoting=csv.QUOTE_MINIMAL)

            csv_clear.writerow(['data', 'contaminados', 'obitos'])

            for caso in CASOS:

                if head:
                    head = False
                    continue

                if data_prev == None:
                    data_prev = caso[0]

                data = caso[0]
                emcerramento = caso[7]

                if data == data_prev:
                    contaminados += 1
                    if emcerramento == "ÓBITO CONF":
                        obitos += 1

                else:
                    csv_clear.writerow([data_prev, contaminados, obitos])
                    print(f'{data_prev};{contaminados};{obitos}')
                    contaminados = 1
                    obitos = 0

                data_prev = data

# 2021-11-10
# 2021-01-11


'''vacinas = sort_dates("vacinas.csv")
with open(r'Vacinas_COVID_clear.csv', "w", newline='', encoding="utf-8") as csv_write:
    csv_clear = csv.writer(csv_write, delimiter=';',
                           quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_clear.writerow(['data', '1', '2'])
    for datas, doses in vacinas.items():
        csv_clear.writerow([datas, doses[0], doses[1]])'''


vacinas = {}
Pop = 1963726
sum_one = 0
sum_two = 0

with open(r'Vacinas_COVID_clear.csv', "r", newline='', encoding="utf-8") as csv_write:
    csv_read = csv.reader(csv_write, delimiter=';',
                          quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for dias in csv_read:
        sum_one = sum_one+int(dias[1])
        sum_two = sum_two+int(dias[2])
        vacinas[dias[0]] = [f'{((sum_one)/Pop)*100:.3f}',
                            f'{((sum_two)/Pop)*100:.3f}']

with open(r'Casos_COVID_clear_porc.csv', "w", newline='', encoding="utf-8") as csv_write:
    csv_writer = csv.writer(csv_write, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['data', '1%', '2%'])
    for datas, doses in vacinas.items():
        csv_writer.writerow([datas, doses[0], doses[1]])
