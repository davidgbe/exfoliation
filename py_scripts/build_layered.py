from copy import deepcopy
from lib import utilities

def multi_dim_iterate(dims, base_specs=None, curr_iter=[]):
    if len(dims) == len(curr_iter):
        yield curr_iter
    else:
        if base_specs is None:
            base_specs = [1] * len(dims)
        curr_dim_idx = len(curr_iter)
        for j in range(0, dims[curr_dim_idx]):
            next_iter = deepcopy(curr_iter)
            next_iter.append(base_specs[curr_dim_idx] * j)
            for it in multi_dim_iterate(dims, base_specs, next_iter):
                yield it

def preprocess(row):
    row = utilities.strip_spaces_from_array(row)
    for i in [0, 1]:
        row[i] = int(row[i])
    for i in range(2, len(row)):
        row[i] = float(row[i])
    return row

def build_layered(rel_path, replication_vec, base_specs, num_to_discard):
    data = utilities.read_csv(__file__, rel_path, num_to_discard=num_to_discard, preprocess=preprocess)
    overall_structure = []
    vec_start = 2
    for disp_vec in multi_dim_iterate(replication_vec, base_specs=base_specs):
        new_cell = deepcopy(data)
        for row in new_cell:
            for i in range(len(base_specs)):
                row[vec_start + i] += disp_vec[i]
            overall_structure.append(row)
    for i in range(len(overall_structure)):
        overall_structure[i][0] = i + 1
    return overall_structure

if __name__ == '__main__':
    layered = build_layered('../samples/MoS2trueunit.xyz', [20, 20, 2], [3.170000, 5.490601, 12.288000], 21)
    utilities.write_csv(__file__, '../samples/replicated_mos2.xyz', to_dump=layered)
