import bs4
import requests
import csv
import json

Closure_Downtown = []
When_Downtown = []
Event_Downtown = []
count = 0

url = "http://www.cityoforlando.net/roadclosure/"
hdr = {"user-agent" : "Mozilla/5.0"}
req = requests.get(url, hdr)
if (req.status_code == 200):
    print("Everything is ok!")
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    results = soup.find_all("strong")
    for item in results:
        if item.get_text() == "Closure":
            Closure_Downtown.append(results[count+1].get_text())
        elif item.get_text() == "When":
            When_Downtown.append(results[count+1].get_text())
        elif item.get_text() == "Event":
            Event_Downtown.append(results[count+1].get_text())
        count += 1
    with open("Road_Closure_Data_Downtown.csv",'w') as csv_file:
        csv_file.write('Closure,When,Event\n')

        for r,h,l in zip(Closure_Downtown,When_Downtown,Event_Downtown):
            line = '"'+r+'"' + ',' + '"'+h +'"' + ',' + '"'+ l+'"'
            csv_file.write(line)
            csv_file.write('\n')

    csvfile = open('Road_Closure_Data_Downtown.csv', 'r')
    jsonfile = open('Road_Closure_Data_Downtown.json', 'w')

    fieldnames = ("Closure", "When", "Event")
    reader = csv.DictReader(csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')

    print(Closure_Downtown,"\n")
    print(When_Downtown,"\n")
    print(Event_Downtown,"\n")