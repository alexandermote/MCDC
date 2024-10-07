import math
import numpy as np
import numba as nb


# Data index
TALLY = 0

# Tally bins
TALLY_SCORE = 0
TALLY_SUM = 1
TALLY_SUM_SQ = 2
TALLY_UQ_BATCH = 3
TALLY_UQ_BATCH_VAR = 4

# Tally scores
SCORE_FLUX = 0
SCORE_DENSITY = 1
SCORE_TOTAL = 2
SCORE_FISSION = 3
SCORE_NET_CURRENT = 4

# Boundary condition
BC_NONE = 0
BC_VACUUM = 1
BC_REFLECTIVE = 2

# Cell fill
FILL_MATERIAL = 0
FILL_UNIVERSE = 1
FILL_LATTICE = 2

# Region
REGION_HALFSPACE = 0
REGION_INTERSECTION = 1
REGION_UNION = 2
REGION_COMPLEMENT = 3
REGION_ALL = 4

# Boolean operator
BOOL_AND = -1
BOOL_OR = -2
BOOL_NOT = -3

# Universe
UNIVERSE_ROOT = 0

# Events
# The << operator represents a bitshift. Each event is assigned 1 << X, which is equal to 2 to the power of X.
EVENT_NONE = 1 << 0
# Geometry events
EVENT_SURFACE_CROSSING = 1 << 1
EVENT_LATTICE_CROSSING = 1 << 2
EVENT_DOMAIN_CROSSING = 1 << 3
EVENT_LOST = 1 << 4
# Collision/reaction events
EVENT_COLLISION = 1 << 5
EVENT_SCATTERING = 1 << 6
EVENT_FISSION = 1 << 7
EVENT_CAPTURE = 1 << 8
# Miscellanies
EVENT_TIME_CENSUS = 1 << 9
EVENT_TIME_BOUNDARY = 1 << 10
EVENT_IQMC_MESH = 1 << 11

# Gyration raius type
GYRATION_RADIUS_ALL = 0
GYRATION_RADIUS_INFINITE_X = 1
GYRATION_RADIUS_INFINITE_Y = 2
GYRATION_RADIUS_INFINITE_Z = 3
GYRATION_RADIUS_ONLY_X = 4
GYRATION_RADIUS_ONLY_Y = 5
GYRATION_RADIUS_ONLY_Z = 6

# Population control
PCT_NONE = 0
PCT_COMBING = 1
PCT_COMBING_WEIGHT = 2
PCT_SPLITTING_ROULETTE = 3
PCT_SPLITTING_ROULETTE_WEIGHT = 4

# Misc.
TINY = 1e-12
COINCIDENCE_TOLERANCE = TINY
INF = 1e10
PI = math.acos(-1.0)
PI_SQRT = math.sqrt(PI)
PI_HALF = PI / 2.0
BANKMAX = 100  # Default maximum active bank

# Mesh crossing flags
MESH_X = 0
MESH_Y = 1
MESH_Z = 2
MESH_T = 3
MESH_NONE = 0

# RNG LCG parameters
RNG_G = nb.uint64(2806196910506780709)
RNG_C = nb.uint64(1)
RNG_MOD_MASK = nb.uint64(0x7FFFFFFFFFFFFFFF)
RNG_MOD = nb.uint64(0x8000000000000000)

# RNG splitter seeds
SEED_SPLIT_CENSUS = nb.uint64(0x43454D654E54)
SEED_SPLIT_SOURCE = nb.uint64(0x43616D696C6C65)
SEED_SPLIT_SOURCE_PRECURSOR = nb.uint64(0x546F6464)
SEED_SPLIT_BANK = nb.uint64(0x5279616E)
SEED_SPLIT_PARTICLE = nb.uint64(0)
SEED_SPLIT_UQ = nb.uint64(0x5368656261)

# Physics
NEUTRON_MASS = 1.67492749804e-27  # kg
EV_TO_J = 1.6022e-19
SQRT_E_TO_SPEED = math.sqrt(2.0 * EV_TO_J / NEUTRON_MASS) * 100
BOLTZMAN_K = 8.61733326e-5  # eV/K
T_ROOM = 294  # K
E_THERMAL_THRESHOLD = 400 * BOLTZMAN_K * T_ROOM

# Cross Section Type
XS_TOTAL = 0
XS_SCATTER = 1
XS_CAPTURE = 2
XS_FISSION = 3
XS_NU_FISSION = 4
XS_NU_FISSION_PROMPT = 5
XS_NU_FISSION_DELAYED = 6
XS_NU_SCATTER = 7

NU_FISSION = 0
NU_FISSION_PROMPT = 1
NU_FISSION_DELAYED = 2
