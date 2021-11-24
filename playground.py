import datetime
import csv
import pandas as pd
from datetime import datetime


def sort_dates(file):
    vacinas = {}

    for i in pd.date_range(start="2021-01-11", end="2021-11-10"):
        vacinas[str(i.date())] = [0, 0]

    head = True

    with open(file, "r", newline='') as csvread:

        CASOS = csv.reader(csvread, delimiter=';')
        for caso in CASOS:

            if head:
                head = False
                continue
            data = str(caso[-8])
            dose = caso[-1]
            if dose == "1":
                vacinas[data][0] += 1
            elif dose == "2":
                vacinas[data][1] += 1
            else:
                print(dose)
    return vacinas
