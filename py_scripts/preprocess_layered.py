from lib import utilities
import sys

def merge_elementwise(*lists):
    merged = []
    # print(lists)
    for group in zip(*lists):
        merged.append(sum(group, []))
    return merged

def map_atom_to_type(atom):
    print(atom)
    d = {
        'S': 1,
        'Mo': 2
    }
    return d[atom]

def preprocess(arr):
    arr = utilities.strip_spaces_from_array(arr)
    arr = arr[2:]
    # arr[0] = map_atom_to_type(arr[0])

    for i in range(1, len(arr)):
        arr[i] = abs(float(arr[i]))
    arr = arr[0:0] + arr[3:]
    return arr

def label_layers(atoms, delta=0.005):
    # declare ordering of atom types by layer
    types = [1, 2, 3, 4, 5, 6]
    # sort by vertical displacement
    sort_idx = 4
    atoms = sorted(atoms, key=lambda params: params[sort_idx])
    # height for all atoms in layer
    layer_height = atoms[0][sort_idx]
    curr_layer = 0
    for a in atoms:
        if a[sort_idx] > layer_height + delta:
            layer_height = a[sort_idx]
            curr_layer = (curr_layer + 1) % len(types)
        a[1] = types[curr_layer]
    return atoms

def cleave_last_atoms_along_direction(atoms, direction):
    atoms = sorted(atoms, key=lambda params: params[direction])
    i = len(atoms) - 1
    approx_val = atoms[i][direction]
    i -= 1
    while atoms[i][direction] > approx_val - 0.005:
        i -= 1
    return atoms[:i+1] 

def execute(input_file):
    data_path = '../samples/' + input_file
    layered_data = utilities.read_csv(__file__, data_path, delimiter=' ', preprocess=preprocess)
    # layered_data = cleave_last_atoms_along_direction(layered_data, 1)

    num_atoms = len(layered_data)
    print(num_atoms)
    ids = [[i] for i in range(1, num_atoms + 1)]
    atoms = merge_elementwise(ids, layered_data)

    atoms = label_layers(atoms)

    utilities.write_csv(__file__, '../samples/processed_' + input_file, to_dump=atoms, delimiter='\t')

if __name__ == '__main__':
    input_file = sys.argv[1]
    execute(input_file)
