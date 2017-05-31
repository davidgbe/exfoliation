from copy import deepcopy
from lib import utilities

def preprocess(row):
    row = utilities.strip_spaces_from_array(row)
    for i in range(3, len(row)):
        row[i] = float(row[i])
    return row

def same_suffix(arr):
    suffixes = list(map(lambda el: el[-1], arr))
    first_suf = suffixes[0]
    for suf in suffixes[1:]:
        if suf != first_suf:
            return False
    return True

def remove_last_from_each(elements):
    return list(map(lambda el: el[:-1], elements))

def create_tag(elements):
    return ' '.join(elements)

def read_cached_values(rel_path, num_to_discard=0):
    csv_dump = utilities.read_csv(__file__, rel_path, num_to_discard, preprocess=preprocess)
    all_values = {}
    for cached in csv_dump:
        tag = create_tag(cached[:3])
        all_values[tag] = cached[3:]
    return all_values

def generate_orderings(available_types, n, curr_ordering=[]):
    if len(curr_ordering) == n:
        yield curr_ordering
    else:
        for single_type in available_types:
            new_ordering = deepcopy(curr_ordering)
            new_ordering.append(single_type)
            for child_ordering in generate_orderings(available_types, n, new_ordering):
                yield child_ordering

def create_sw_file(available_types, cached_values, default_value):
    all_lines = []
    for ordering in generate_orderings(available_types, 3):
        tag = create_tag(remove_last_from_each(ordering[:3]))
        if tag in cached_values and same_suffix(ordering[:3]):
            all_lines.append(ordering + cached_values[tag])
        else:
            all_lines.append(ordering + default_value)
    return all_lines


if __name__ == '__main__':
    cached = read_cached_values('../mos2.sw', 11)
    options = ['S1', 'S2', 'S3', 'S4', 'Mo1', 'Mo2', 'Mo3', 'Mo4']
    sw_file = create_sw_file(options, cached, [0.0] * 11)
    utilities.write_csv(__file__, '../mos2_long.sw', to_dump=sw_file)
