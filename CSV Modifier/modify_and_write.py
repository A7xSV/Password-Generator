import csv, re

def check_and_replace(matched_obj):
    matched_value = matched_obj.group(0)[1:3]
    if matched_obj.group(0)[1:3] > '15':
        return ':19' + matched_value + '-'
    else:
        return ':20' + matched_value + '-'


file_to_read  = raw_input('Enter file name without extension: ')
column_number = input('Enter column number to modify : ')

print 'Processing...',

reader = csv.reader(open(file_to_read + '.csv', 'rb'))
writer = csv.writer(open(file_to_read + '_formatted.csv','wb'))
for row in reader:
    # You can change the Regex as needed in the first argument of re.sub()
    row[column_number] = re.sub(':[0-9]{2}-', check_and_replace, row[column_number])[0:15]
    writer.writerow(row)