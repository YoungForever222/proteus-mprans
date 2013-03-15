from proteus import *
from ls_p import *

timeIntegration = BackwardEuler_cfl
stepController  = Min_dt_controller

femSpaces = {0:basis}

massLumping       = False
numericalFluxType = None
conservativeFlux  = None
numericalFluxType = DoNothing
subgridError      = HamiltonJacobi_ASGS_opt(coefficients,nd,lag=False)
shockCapturing    = NCLS.ShockCapturing(coefficients,nd,shockCapturingFactor=ls_shockCapturingFactor,lag=False)

fullNewtonFlag  = True
multilevelNonlinearSolver = Newton
levelNonlinearSolver      = Newton

nonlinearSmoother = None
linearSmoother    = None

matrix = SparseMatrix

if useOldPETSc:
    multilevelLinearSolver = PETSc
    levelLinearSolver      = PETSc
else:
    multilevelLinearSolver = KSP_petsc4py
    levelLinearSolver      = KSP_petsc4py

if useSuperlu:
    multilevelLinearSolver = LU
    levelLinearSolver      = LU

linear_solver_options_prefix = 'ncls_'
levelNonlinearSolverConvergenceTest = 'r'
linearSolverConvergenceTest         = 'r-true'

tolFac = 0.0
linTolFac = 0.0
l_atol_res = 1.0e-5
nl_atol_res = 100.0*l_atol_res
useEisenstatWalker = False#True

maxNonlinearIts = 25
maxLineSearches = 0

