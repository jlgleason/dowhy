import logging

from dowhy.causal_identifier import EstimandType, auto_identify_effect, id_identify_effect, identify_effect
from dowhy.causal_model import CausalModel

logging.getLogger(__name__).addHandler(logging.NullHandler())

#
# 0.0.0 is standard placeholder for poetry-dynamic-versioning
# any changes to this should not be checked in
#
__version__ = "0.0.0"


__all__ = ["EstimandType", "auto_identify_effect", "id_identify_effect", "identify_effect", "CausalModel"]
