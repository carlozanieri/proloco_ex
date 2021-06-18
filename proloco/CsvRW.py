#!/usr/bin/env python
#import os
#import time
#import logging
import os
import time
import logging
import csv

class CsvRW:

   def read(self):
       with open('tesserati.csv') as csv_file:
           csv_reader = csv.reader(csv_file, delimiter=',')
           line_count = 0
           with open('tesserati2021.csv', mode='w+', newline='') as csv_file:

                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        nomicolonne = ['NOME', 'E-MAIL']
                        writer = csv.DictWriter(csv_file, fieldnames=nomicolonne)
                        writer.writeheader()
                        line_count += 1
                    else:
                        writer.writerow({'NOME': row[0] + " " + row[1] , 'E-MAIL': row[2]})
                        print({'NOME': row[0] + " " + row[1] , 'NOME': row[2], 'E-MAIL': row[3]})
                        line_count += 1
   def write(self):
       import csv

       with open('file3.csv', mode='w') as csv_file:
           nomicolonne = ['nome', 'cognome', 'citta']
           writer = csv.DictWriter(csv_file, fieldnames=nomicolonne)
           writer.writeheader()

           writer.writerow({'nome': 'Luca', 'cognome': 'Bianchi', 'citta': 'Roma'})
           writer.writerow({'nome': 'Giovanni', 'cognome': 'Rossi', 'citta': 'Venezia'})