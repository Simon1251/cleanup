import csv
import sys

def cleanup(file):
    with open(file, newline='') as csvfile:
        contacts = csv.reader(csvfile, dialect='excel')
        for i in contacts:
            print(i)
            break

def main():
    if len(sys.argv) < 2:
        exit(1)
    else:
        cleanup(sys.argv[1])

if __name__ == "__main__":
    main()
