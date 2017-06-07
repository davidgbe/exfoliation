# by Jin-Wu Jiang, jwjiang5918@hotmail.com, 28/05/13/Tue

# The Stillinger-Weber parameters in metal units, for MoS2, from fitting phonon dispersion using GULP.
# these entries are in LAMMPS "metal" units: 1eV = 23.060 9 kcal/mole, modified to kcal/mole(real)
#   epsilon = eV; sigma = Angstroms, has been  modified to kcal/mole
#   other quantities are unitless

# format of a single entry (one or more lines):
#   element 1, element 2, element 3, 
#   epsilon, sigma, a, lambda, gamma, costheta0, A, B, p, q, tol

Mo Mo Mo  80.8053936  0.6097  7.0034  0.0000  0.8568  0.1525  1.0 181.8799  4  0  0.0
Mo Mo  S  0.00000000  0.6097  7.0034  0.0000  0.8568  0.1525  1.0 181.8799  4  0  0.0
Mo  S Mo  0.00000000  0.6097  7.0034  0.0000  0.8568  0.1525  1.0 181.8799  4  0  0.0
Mo  S  S  139.915092  0.7590  4.1634  1.0801  0.8568  0.1525  1.0  45.4357  4  0  0.0
S  Mo Mo  139.915092  0.7590  4.1634  1.0801  0.8568  0.1525  1.0  45.4357  4  0  0.0
S  Mo  S  0.00000000  0.6097  7.0034  0.0000  0.8568  0.1525  1.0 181.8799  4  0  0.0
S   S Mo  0.00000000  0.6097  7.0034  0.0000  0.8568  0.1525  1.0 181.8799  4  0  0.0
S   S  S  10.7256246  0.6501  5.7837  0.0000  0.8568  0.1525  1.0 125.0923  4  0  0.0
