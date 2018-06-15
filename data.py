import sys
import csv

def read_csv(csv_file):
    data = []
    with open(csv_file) as f:
        reader = csv.reader(f)
        for line in reader:
            data.append(line)
    return data

def write_csv(csv_file, data):
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def get_record(src_file, target_file):
    data = read_csv(src_file)
    for d in data[1:]:
        if d[-1] != 'Y':
            write_csv(target_file, [data[0][:-1],d[:-1]])
            d[-1] = 'Y'
            write_csv(src_file,data)
            return


if __name__ == '__main__':
    file_name = sys.argv[1]
    get_record('D:\\agent\\data\\%s.csv' %file_name, 'data.csv')
