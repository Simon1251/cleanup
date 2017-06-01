import csv
import sys


def merge(first, second):
    new_contact = list()
    for i in range(0, 92):
        new_contact.append(first[i] if len(first[i]) > len(second[i]) else second[i])
    return new_contact

def cleanup(file):
    out = open("people.csv", 'w', newline='')
    csvout = csv.writer(out, delimiter=',', quotechar='"')
    with open(file, newline='') as csvfile:
        contacts = csv.reader(csvfile, delimiter=",", quotechar='"')
        header = next(contacts)
        csvout.writerow(header)
        current = next(contacts)
        for person in contacts:
            if current[57] != person[57] or current[57] == '':
                csvout.writerow(current)
                current = person
                continue
            else:
                csvout.writerow(merge(current, person))
                current = next(contacts)
                continue

    out.close()


def main():
    if len(sys.argv) < 2:
        print("Need to provide file.")
        exit(1)
    else:
        cleanup(sys.argv[1])


if __name__ == "__main__":
    main()
