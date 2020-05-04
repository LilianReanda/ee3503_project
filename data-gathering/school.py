import os
import pathlib
import csv
import process
def output_schools(input):
    columns = ['school_id','schoolname','schooladdress','school_city','school_state',"school_type"]
    schools = open('data-gathering/GuatED.csv','w')
    writer = csv.DictWriter(schools, fieldnames = columns)
    writer.writerheader()
    for data in input:
        writer.writerow(data)
    schools.close()
def output_schoolsJSON(input):
    schools = open('data-gathering/GuatED.json','w')
    