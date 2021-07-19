# -*- coding: utf-8 -*-

from HARK.ConsumptionSaving.ConsIndShockModelOld \
    import ConsumerSolution as ConsumerSolutionOld
from HARK.ConsumptionSaving.ConsIndShockModel_AgentSolve \
    import (
        ConsumerSolution, ConsumerSolutionOneNrmStateCRRA,
        ConsPerfForesightSolver, ConsIndShockSetup,
        ConsIndShockSolverBasic, ConsIndShockSolver
        )

from HARK.ConsumptionSaving.ConsIndShockModel_KinkedRSolver \
    import ConsKinkedRsolver

from HARK.ConsumptionSaving.ConsIndShockModel_AgentTypes \
    import (consumer_terminal_nobequest_onestate, PerfForesightConsumerType,
            IndShockConsumerType, KinkedRconsumerType,
            onestate_bequest_warmglow_homothetic
            )

from HARK.ConsumptionSaving.ConsIndShockModel_AgentDicts \
    import (
        init_perfect_foresight,
        init_idiosyncratic_shocks,
        init_kinked_R,
        init_lifecycle,
        init_cyclical)

from HARK.utilities import CRRAutility as utility
from HARK.utilities import CRRAutilityP as utilityP
from HARK.utilities import CRRAutilityPP as utilityPP
from HARK.utilities import CRRAutilityP_inv as utilityP_inv
from HARK.utilities import CRRAutility_invP as utility_invP
from HARK.utilities import CRRAutility_inv as utility_inv
from HARK.utilities import CRRAutilityP as utilityP_invP

"""
Classes to define and solve canonical consumption-saving models with a single
state variable.  All models assume CRRA utility with geometric discounting,
and if income shocks exist they are fully transitory or fully permanent.

It currently solves three types of models:
   1) `PerfForesightConsumerType`
      * A basic perfect foresight consumption-saving model with no uncertainty.
      * Features of the model prepare it for convenient inheritance
   2) `IndShockConsumerType`
      * A consumption-saving model with transitory and permanent income shocks
      * Inherits from PF model
   3) `KinkedRconsumerType`
      * `IndShockConsumerType` model but with interest rate on debt, `Rboro`
        greater than the interest rate earned on savings, `Rboro > `Rsave`

See NARK https://HARK.githhub.io/Documentation/NARK for naming conventions.
See https://hark.readthedocs.io for descriptions of the models.
"""

__all__ = [
    "ConsumerSolutionOld",
    "ConsumerSolution",
    "ConsumerSolutionOneNrmStateCRRA",
    "ConsPerfForesightSolver",
    "ConsIndShockSetup",
    "ConsIndShockSolverBasic",
    "ConsIndShockSolver",
    "ConsKinkedRsolver",
    "consumer_terminal_nobequest_onestate",
    "PerfForesightConsumerType",
    "IndShockConsumerType",
    "KinkedRconsumerType",
    "init_perfect_foresight",
    "init_idiosyncratic_shocks",
    "init_kinked_R",
    "init_lifecycle",
    "init_cyclical",
    "utility",
    "utilityP",
    "utilityPP",
    "utilityP_inv",
    "utility_invP",
    "utility_inv",
    "utilityP_invP",
    "onestate_bequest_warmglow_homothetic"
]
