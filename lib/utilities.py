import os
import csv

def strip_spaces_from_array(arr):
    stripped = []
    for el in arr:
        if el != ' ' and el != '':
            stripped.append(el)
    return stripped

def file_path(curr_file, *path_elements):
    dir = os.path.dirname(curr_file)
    return os.path.join(dir, *path_elements)

def open_file(curr_file, rel_path, protocol='r'):
    return open(file_path(curr_file, rel_path), protocol)

def read_csv(curr_file, rel_path, num_to_discard=0, delimiter=' ', preprocess=None):
    data_file = open_file(curr_file, rel_path)
    parsed_csv = csv.reader(data_file, delimiter=delimiter)
    all_rows = []

    count = 0
    for row in parsed_csv:
        if count >= num_to_discard:
            if preprocess is not None:
                row = preprocess(row)
            all_rows.append(row)
        count += 1
    data_file.close()
    return all_rows

def write_csv(curr_file, rel_path, delimiter='\t', to_dump=None):
    data_file = open_file(curr_file, rel_path, 'w')
    csv_writer = csv.writer(data_file, delimiter=delimiter)
    if to_dump is not None:
        for row in to_dump:
            csv_writer.writerow(row)
    data_file.close()
