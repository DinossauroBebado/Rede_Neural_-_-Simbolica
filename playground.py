import datetime
import csv
import pandas as pd
from datetime import datetime


def sort_dates(file):
    vacinas = {}

    for i in pd.date_range(start="2021-01-11", end="2021-11-10"):
        vacinas[str(i.date())] = [0, 0]

    head = True

    with open(file, "r", newline='', encoding="utf8") as csvread:

        CASOS = csv.reader(csvread, delimiter=';')
        for caso in CASOS:
            # print(".")
            if head:
                head = False
                continue

            if caso[9] != "CURITIBA":
                continue

            data = str(caso[-8])
            dose = caso[-1]
            if dose == "1":
                try:
                    vacinas[data][0] += 1
                except:
                    print("data fora")
                    continue
            elif dose == "2":
                try:
                    vacinas[data][1] += 1
                except:
                    print("data fora")
                    continue

    return vacinas

# COVID-19 JANSSEN = > 8
# COVID-19 PFIZER => 37,38
