`from proteus import *
from proteus.default_p import *
from proteus.ctransportCoefficients import smoothedHeaviside
from dambreak import *
from proteus.mprans import VOF

LevelModelType = VOF.LevelModel
coefficients = VOF.Coefficients(LS_model=1,V_model=0,RD_model=3,ME_model=2,
                                checkMass=False,useMetrics=useMetrics,
                                epsFact=epsFact_vof,sc_uref=vof_sc_uref,sc_beta=vof_sc_beta)
 
def getDBC_vof(x,flag):
    if x[2] > L[2] - 1.0e-8:
        return lambda x,t: 1.0

dirichletConditions = {0:getDBC_vof}

def getAFBC_vof(x,flag):
    if x[2] > L[2] - 1.0e-8:
    	return None
    else:
    	return lambda x,t: 0.0

advectiveFluxBoundaryConditions = {0:getAFBC_vof}
diffusiveFluxBoundaryConditions = {0:{}}

class PerturbedSurface_H:
    def uOfXT(self,x,t):
        if signedDistance(x) < 0.0:
            return 0.0
	else:
	    return 1.0  
	    
initialConditions  = {0:PerturbedSurface_H()}
