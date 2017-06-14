import sys
from lib import utilities
import os

def sample_trj(rel_path, sampling_period):
    ext_start = -1
    for i in range(len(rel_path) - 1, 0, -1):
        if rel_path[i] == '.':
            ext_start = i
            break
    if ext_start == -1:
        raise ValueError('File name does not have an extension')
    ext = rel_path[ext_start:]
    new_rel_path = rel_path[:ext_start] + '_' + str(sampling_period) + '_sampled' + ext

    trj_data = utilities.open_file(__file__, rel_path)
    sampled_trj = utilities.open_file(__file__, new_rel_path, protocol='w')

    include_step = False
    check_for_time_step = False
    ignore_num = 0
    check_for_ignore_count = False
    for row in trj_data:
        if ignore_num > 0:
            ignore_num -= 1
        elif row.startswith('ITEM: TIMESTEP'):
            check_for_time_step = True
            include_step = False
        elif include_step:
            sampled_trj.write(row)
        elif check_for_time_step:
            check_for_time_step = False
            time_step_num = int(row)
            if time_step_num % sampling_period == 0:
                sampled_trj.write('ITEM: TIMESTEP' + os.linesep)
                sampled_trj.write(row)
                include_step = True
        elif check_for_ignore_count:
            ignore_num = int(row)
            check_for_ignore_count = False
        elif row.startswith('ITEM: NUMBER OF ATOMS'):
            check_for_ignore_count = True

    trj_data.close()
    sampled_trj.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Incorrect number of arguments')
    else:
        sample_trj(sys.argv[1], int(sys.argv[2]))
