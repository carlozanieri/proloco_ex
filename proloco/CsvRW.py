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
       import csv
       with open('file.csv') as csv_file:
           csv_reader = csv.reader(csv_file, delimiter=',')
           line_count = 0
           for row in csv_reader:
               if line_count == 0:
                   print(f'Nomi delle colonne: {", ".join(row)}')
                   line_count += 1
               else:
                   with open('file3.csv', mode='w') as csv_filew:
                       nomicolonne = ['nome', 'cognome', 'citta']
                       writer = csv.DictWriter(csv_filew, fieldnames=nomicolonne)
                       writer.writeheader()

                   writer.writerow(f'\t{row[0]} , {row[1]} , {row[2]}.')
                   line_count += 1
               print(f'File contiene {line_count} linee.')

   def write(self):
       import csv

       with open('file3.csv', mode='w') as csv_file:
           nomicolonne = ['nome', 'cognome', 'citta']
           writer = csv.DictWriter(csv_file, fieldnames=nomicolonne)
           writer.writeheader()
           writer.writerow({'nome': 'Luca', 'cognome': 'Bianchi', 'citta': 'Roma'})
           writer.writerow({'nome': 'Giovanni', 'cognome': 'Rossi', 'citta': 'Venezia'})
