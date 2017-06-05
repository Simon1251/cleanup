__author__ = "James Johnson"


import csv
import sys


def merge(first: list, second: list) -> list:
    """
    Merges two contacts. Function assumes that the two contacts represent the same person.
    Function simply takes the longer string for non phone number and non email entries.

    When duplicated email or phone entries are detected and they are not the same, the extra one
    will be thrown into the notes entry.

    :param first:
    :param second:
    :rtype list:
    """
    phone_range = [29, 31, 32, 33, 34, 35, 37, 38, 40, 42, 44]
    email_range = [57, 58, 59, 60, 61, 62, 63, 64, 65]
    new_contact = [None] * 92
    new_contact[77] = ""
    for i in range(0, 92):
        if i in phone_range:
            if len(first[i]) == 0:
                new_contact[i] = second[i]
                continue
            elif len(second[i]) == 0:
                new_contact[i] = first[i]
                continue
            elif first[i] == second[i]:
                new_contact[i] = first[i]
                continue
            else:
                new_contact[i] = first[i]
                new_contact[77] = " " + second[i]
                continue

        if i in email_range:
            continue
        new_contact[i] = first[i] if len(first[i]) > len(second[i]) else second[i]

        if len(first[57]) == 0:
            new_contact[57] = second[57]
            new_contact[58] = second[58]
            new_contact[59] = second[59]
        elif len(second[57]) == 0:
            new_contact[57] = first[57]
            new_contact[58] = first[58]
            new_contact[59] = first[59]
        elif first[57] == second[57]:
            new_contact[57] = first[57]
            new_contact[58] = first[58]
            new_contact[59] = first[59] if len(first[59]) > len(second[59]) else second[59]
        else:
            new_contact[57] = first[57]
            new_contact[58] = first[58]
            new_contact[59] = first[59]
            new_contact[77] += " " + second[57]

        if len(first[60]) == 0:
            new_contact[60] = second[60]
            new_contact[61] = second[61]
            new_contact[62] = second[62]
        elif len(second[60]) == 0:
            new_contact[60] = first[60]
            new_contact[61] = first[61]
            new_contact[62] = first[62]
        elif first[60] == second[60]:
            new_contact[60] = first[60]
            new_contact[61] = first[61]
            new_contact[62] = first[62] if len(first[62]) > len(second[62]) else second[62]
        else:
            new_contact[60] = first[60]
            new_contact[61] = first[61]
            new_contact[62] = first[62]
            new_contact[77] += " " + second[60]

        if len(first[63]) == 0:
            new_contact[63] = second[63]
            new_contact[64] = second[64]
            new_contact[65] = second[65]
        elif len(second[63]) == 0:
            new_contact[63] = first[63]
            new_contact[64] = first[64]
            new_contact[65] = first[65]
        elif first[63] == second[63]:
            new_contact[63] = first[63]
            new_contact[64] = first[64]
            new_contact[65] = first[65] if len(first[65]) > len(second[65]) else second[65]
        else:
            new_contact[63] = first[63]
            new_contact[64] = first[64]
            new_contact[65] = first[65]
            new_contact[77] += " " + second[63]

    return new_contact


def cleanup(file: object) -> None:
    """
    Main function for cleaning up files. Takes in a csv file and will write all unique contacts to a new
    csv file called 'people.csv'.
    
    All non-unique contacts will be merged into a single contact and written to the new file.
    
    :rtype None:
    :param file: 
    """

    # Counts the number of modified contacts.
    modified = 0

    out = open("people.csv", 'w', newline='')
    csv_out = csv.writer(out, delimiter=',', quotechar='"')
    # noinspection PyTypeChecker
    with open(file, newline='') as csv_file:
        contacts = csv.reader(csv_file, delimiter=",", quotechar='"')
        header = next(contacts)
        csv_out.writerow(header)
        current = next(contacts)
        for person in contacts:
            if current[57] == person[57] and len(current[57]) > 0:
                modified += 1
                csv_out.writerow(merge(current, person))
                current = next(contacts)
                continue
            elif current[1] == person[1] and current[2] == person[2] and current[3] == person[3] and len(current[1]) > 0\
                    and len(current[3]) > 0:
                modified += 1
                csv_out.writerow(merge(current, person))
                current = next(contacts)
                continue
            else:
                csv_out.writerow(current)
                current = person
                continue

        csv_out.writerow(current)
        out.close()
        print("{} modified or deleted contacts.".format(modified))


def main():
    if len(sys.argv) < 2:
        print("Need to provide file.")
        exit(1)
    else:
        cleanup(sys.argv[1])


if __name__ == "__main__":
    main()
