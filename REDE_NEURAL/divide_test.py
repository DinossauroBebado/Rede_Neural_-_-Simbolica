import csv
import random


with open(r"REDE_NEURAL\info_COVID.csv", "r", newline='', encoding="utf-8") as csv_read:
    csv_read = csv.reader(csv_read, delimiter=';',
                          quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with open(r'REDE_NEURAL\info_COVID_test.csv', "w", newline='', encoding="utf-8") as csv_write_test:

        csv_writer_test = csv.writer(csv_write_test, delimiter=';',
                                     quotechar='"', quoting=csv.QUOTE_MINIMAL)

        with open(r'REDE_NEURAL\info_COVID_train.csv', "w", newline='', encoding="utf-8") as csv_write_train:

            csv_writer_train = csv.writer(csv_write_train, delimiter=';',
                                          quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for lines in csv_read:
                if(random.random() > 0.8):

                    csv_writer_test.writerow(
                        [lines[0], lines[1], lines[2], lines[3], lines[4]])
                else:

                    csv_writer_train.writerow(
                        ([lines[0], lines[1], lines[2], lines[3], lines[4]]))
