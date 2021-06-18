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
       with open('file.csv') as csv_file:
           csv_reader = csv.reader(csv_file, delimiter=',')
           line_count = 0
           with open('file11.csv', mode='w+', newline='') as csv_file:
                for row in csv_reader:


                    nomicolonne = ['COGNOME',  'E-MAIL']
                    writer = csv.DictWriter(csv_file, fieldnames=nomicolonne)
                    writer.writeheader()
                    data= [ {'COGNOME': row[2] + " " + row[3] , 'NOME': row[3], 'E-MAIL': row[4]}]
                   ### writer.writerow(data)
                    writer.writerow({'COGNOME': row[2] + " " + row[3] , 'E-MAIL': row[4]})
                    print({'COGNOME': row[2] + " " + row[3] , 'NOME': row[3], 'E-MAIL': row[4]})
                    line_count += 1
   def write(self):
       import csv

       with open('file3.csv', mode='w') as csv_file:
           nomicolonne = ['nome', 'cognome', 'citta']
           writer = csv.DictWriter(csv_file, fieldnames=nomicolonne)
           writer.writeheader()

           writer.writerow({'nome': 'Luca', 'cognome': 'Bianchi', 'citta': 'Roma'})
           writer.writerow({'nome': 'Giovanni', 'cognome': 'Rossi', 'citta': 'Venezia'})