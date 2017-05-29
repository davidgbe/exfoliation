from lib import utilities

def merge_elementwise(*lists):
    merged = []
    # print(lists)
    for group in zip(*lists):
        merged.append(sum(group, []))
    return merged

def map_atom_to_type(atom):
    d = {
        'Mo': 1,
        'S': 2
    }
    return d[atom]

def preprocess(arr):
    arr = utilities.strip_spaces_from_array(arr)
    arr[0] = map_atom_to_type(arr[0])

    for i in range(1, len(arr)):
        arr[i] = float(arr[i])
    return arr

def label_layers(atoms, delta=0.001):
    # declare ordering of atom types by layer
    types = [1, 5, 1, 2, 6, 2, 3, 7, 3, 4, 8, 4]
    # sort by vertical displacement
    atoms = sorted(atoms, key=lambda params: params[3])
    # height for all atoms in layer
    layer_height = atoms[0][3]
    curr_layer = 0
    for a in atoms:
        if a[3] > layer_height + delta:
            layer_height = a[3]
            curr_layer = (curr_layer + 1) % len(types)
        a[1] = types[curr_layer]
    return atoms

def execute():
    data_path = '../samples/MoS2unitcell.xyz'
    layered_data = utilities.read_csv(__file__, data_path, 2, preprocess=preprocess)
    num_atoms = len(layered_data)
    ids = [[i] for i in range(1, num_atoms + 1)]
    atoms = merge_elementwise(ids, layered_data)

    atoms = label_layers(atoms)

    utilities.write_csv(__file__, '../samples/MoS2unit_new.xyz', to_dump=atoms, delimiter='\t')

if __name__ == '__main__':
    execute()
