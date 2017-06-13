import sys
from lib import utilities

def sample_trj(rel_path, sampling_period):
    trj_data = utilities.read_csv(__file__, rel_path, delimiter=' ')
    check_for_time_step = False
    include_step = False

    sampled = []
    for row in trj_data:
        if include_step:
            sampled.append(row)
        elif check_for_time_step:
            check_for_time_step = False
            time_step_num = int(row[0])
            if time_step_num % sampling_period == 0:
                sampled.append(['ITEM:', 'TIMESTEP'])
                sampled.append(row)
                include_step = True
        elif len(row) > 1 and row[1] == 'TIMESTEP':
            check_for_time_step = True
            include_step = False

    ext_start = -1
    for i in range(len(rel_path) - 1, 0, -1):
        if rel_path[i] == '.':
            ext_start = i
            break
    if ext_start == -1:
        raise ValueError('File name does not have an extension')
    ext = rel_path[ext_start:]
    new_rel_path = rel_path[:ext_start] + '_' + str(sampling_period) + '_sampled' + ext
    utilities.write_csv(__file__, new_rel_path, delimiter=' ', to_dump=sampled)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Incorrect number of arguments')
    else:
        sample_trj(sys.argv[1], int(sys.argv[2]))
