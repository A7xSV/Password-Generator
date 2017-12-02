import csv

reader = csv.reader(open('p_c.csv', 'rb'))
read_file = open('c_f.csv', 'rb');
reader_search = csv.reader(read_file)
names_file = open('n_f.csv', 'rb');
names_search = csv.reader(names_file)

def search_names(case_id, case_num):
    names_file.seek(0)
    for row in names_search:
        if case_id == row[0] and case_num == row[1]:
            print row

def search_for(court_n, case_num):
    read_file.seek(0)
    pacer_court_n = court_name.split()[0].lower()
    print pacer_court_n, " ", case_num
    for row in reader_search:
        if pacer_court_n in row[4].lower():
            if (case_num == row[1]):
                print row
                search_names(row[0], row[1])

i = 0;
for row in reader:
    i += 1
    if i == 1:
        continue
    search_for(row[2], row[4])
    if i > 6:
        break
    print "\n"