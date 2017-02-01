from parcels.grid import *  # noqa
from parcels.particle import *  # noqa
from parcels.particleset import *  # noqa
from parcels.field import *  # noqa
from parcels.kernel import *  # noqa
import parcels.rng as random  # noqa
from parcels.particlefile import *  # noqa
from parcels.kernels import *  # noqa

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
