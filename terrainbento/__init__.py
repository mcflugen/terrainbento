"""
Public classes of the terrainbento package.

terrainbento has two types of public classes: derived models and boundary
condition handlers. Derived models are models that have inherited from the
``ErosionModel`` base class. Boundary condition handlers are helper classes
that have been designed to modify model boundary conditions during a model run.
"""

from .base_class import ErosionModel
from .base_class import StochasticErosionModel

from .boundary_condition_handlers import PrecipChanger
from .boundary_condition_handlers import SingleNodeBaselevelHandler
from .boundary_condition_handlers import CaptureNodeBaselevelHandler

from .derived_models import Basic
from .derived_models import BasicTh
from .derived_models import BasicDd
from .derived_models import BasicHy
from .derived_models import BasicCh
from .derived_models import BasicSt
from .derived_models import BasicVs
from .derived_models import BasicSa
from .derived_models import BasicRt
from .derived_models import BasicCv
from .derived_models import BasicHyTh
from .derived_models import BasicDdHy
from .derived_models import BasicStTh
from .derived_models import BasicDdSt
from .derived_models import BasicHySt
from .derived_models import BasicThVs
from .derived_models import BasicDdVs
from .derived_models import BasicHyVs
from .derived_models import BasicStVs
from .derived_models import BasicHySa
from .derived_models import BasicChSa
from .derived_models import BasicSaVs
from .derived_models import BasicRtTh
from .derived_models import BasicDdRt
from .derived_models import BasicHyRt
from .derived_models import BasicChRt
from .derived_models import BasicRtVs
from .derived_models import BasicRtSa
from .derived_models import BasicChRtTh

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
