import csv

reader = csv.reader(open('pacer_cases.csv', 'rb'))
read_file = open('cases_formatted.csv', 'rb');
reader_search = csv.reader(read_file)
names_file = open('names_formatted.csv', 'rb');
names_search = csv.reader(names_file)

def search_names(case_row_id, case_num):
    names_file.seek(0)
    for row in names_search:
        if case_row_id == row[0] and case_num == row[1]:
            print row

def search_for(court_name, case_num):
    read_file.seek(0)
    pacer_court_name = court_name.split()[0].lower()
    print pacer_court_name, " ", case_num
    for row in reader_search:
        if pacer_court_name in row[4].lower():
            if (case_num == row[1]):
                print row
                search_names(row[0], row[1])
                # return

i = 0;
for row in reader:
    i += 1
    if i == 1:
        continue
    search_for(row[2], row[4])
    if i > 6:
        break
    print "\n"