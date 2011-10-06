from math import *
import proteus.MeshTools
from proteus import Domain
from proteus.default_n import *   
   
#  Discretization -- input options    
Refinement=4
spaceOrder=1
useHex=False
useRBLES   = 1.0
useMetrics = 1.0

# Input checks and output name generation 

soname="marin"   

if spaceOrder == 1:
    soname=soname+"_lin"
elif spaceOrder == 2:
    soname=soname+"_quad"
else:
    print "INVALID: spaceOrder"
    sys.exit()    

if useHex:
    soname=soname+"_hex"
else:
    soname=soname+"_tet"   

soname=soname+"_Ref"+`Refinement`  
    
if useRBLES == 0.0:
    soname=soname+"_SUPG"
elif useRBLES == 1.0:
    soname=soname+"_RBLES"
else:
    print "INVALID: useRBLES"
    sys.exit()

if useMetrics == 0.0:
    soname=soname+"_h"
elif useMetrics == 1.0:
    soname=soname+"_G"
else:
    print "INVALID: useMetrics"
    sys.exit()
    
soname=soname+"_p"

print soname

#  Discretization   
nd = 3
if spaceOrder == 1:
    hFactor=1.0
    if useHex:
	 basis=C0_AffineLinearOnCubeWithNodalBasis
         elementQuadrature = CubeGaussQuadrature(nd,2)
         elementBoundaryQuadrature = CubeGaussQuadrature(nd-1,2)     	 
    else:
    	 basis=C0_AffineLinearOnSimplexWithNodalBasis
         elementQuadrature = SimplexGaussQuadrature(nd,2)
         elementBoundaryQuadrature = SimplexGaussQuadrature(nd-1,2) 	    
elif spaceOrder == 2:
    hFactor=0.5
    if useHex:    
	basis=C0_AffineLagrangeOnCubeWithNodalBasis
        elementQuadrature = CubeGaussQuadrature(nd,4)
        elementBoundaryQuadrature = CubeGaussQuadrature(nd-1,4)    
    else:    
	basis=C0_AffineQuadraticOnSimplexWithNodalBasis	
        elementQuadrature = SimplexGaussQuadrature(nd,4)
        elementBoundaryQuadrature = SimplexGaussQuadrature(nd-1,4)


# Domain and mesh
nLevels = 1
parallelPartitioningType = proteus.MeshTools.MeshParallelPartitioningTypes.element
nLayersOfOverlapForParallel = 1

if useHex: 
    hex=True 

    comm=Comm.get()	
    if comm.isMaster():	
        size = numpy.array([[0.520,0.510,0.520],
	                    [0.330,0.340,0.330],
			    [0.320,0.325,0.000]])/Refinement
        numpy.savetxt('size.mesh', size)
        failed = os.system("marinHexMesh")      
     
    domain = Domain.MeshHexDomain("marinHex") 
else:
    L      = [3.22,1.0,1.0]
    box_L  = [0.161,0.403,0.161]
    box_xy = [2.3955,0.2985]
    he = L[0]/float(6.5*Refinement)
    boundaries=['left','right','bottom','top','front','back','box_left','box_right','box_top','box_front','box_back',]
    boundaryTags=dict([(key,i+1) for (i,key) in enumerate(boundaries)])
    bt = boundaryTags
    holes = [[0.5*box_L[0]+box_xy[0],0.5*box_L[1]+box_xy[1],0.5*box_L[2]]]
    vertices=[[0.0,0.0,0.0],#0
              [L[0],0.0,0.0],#1
              [L[0],L[1],0.0],#2
              [0.0,L[1],0.0],#3
              [0.0,0.0,L[2]],#4
              [L[0],0.0,L[2]],#5
              [L[0],L[1],L[2]],#6
              [0.0,L[1],L[2]],#7
              [box_xy[0],box_xy[1],0.0],#8
              [box_xy[0]+box_L[0],box_xy[1],0.0],#9
              [box_xy[0]+box_L[0],box_xy[1]+box_L[1],0.0],#10
              [box_xy[0],box_xy[1]+box_L[1],0.0],#11
              [box_xy[0],box_xy[1],box_L[2]],#12
              [box_xy[0]+box_L[0],box_xy[1],box_L[2]],#13
              [box_xy[0]+box_L[0],box_xy[1]+box_L[1],box_L[2]],#14
              [box_xy[0],box_xy[1]+box_L[1],box_L[2]]]#15
    vertexFlags=[boundaryTags['left'],
                 boundaryTags['right'],
                 boundaryTags['right'],
                 boundaryTags['left'],
                 boundaryTags['left'],
                 boundaryTags['right'],
                 boundaryTags['right'],
                 boundaryTags['left'],
                 boundaryTags['box_left'],
                 boundaryTags['box_left'],
                 boundaryTags['box_left'],
                 boundaryTags['box_left'],
                 boundaryTags['box_left'],
                 boundaryTags['box_left'],
                 boundaryTags['box_left'],
                 boundaryTags['box_left']]
    facets=[[[0,1,2,3],[8,9,10,11]],
            [[0,1,5,4]],
            [[1,2,6,5]],
            [[2,3,7,6]],
            [[3,0,4,7]],
            [[4,5,6,7]],
            [[8,9,13,12]],
            [[9,10,14,13]],
            [[10,11,15,14]],
            [[11,8,12,15]],
            [[12,13,14,15]]]
    facetFlags=[boundaryTags['bottom'],
                boundaryTags['front'],
                boundaryTags['right'],
                boundaryTags['back'],
                boundaryTags['left'],
                boundaryTags['top'],
                boundaryTags['box_front'],
                boundaryTags['box_right'],
                boundaryTags['box_back'],
                boundaryTags['box_left'],
                boundaryTags['box_top']]
    domain = Domain.PiecewiseLinearComplexDomain(vertices=vertices,
                                                 vertexFlags=vertexFlags,
                                                 facets=facets,
                                                 facetFlags=facetFlags,
                                                 holes=holes)
						 
						 
    #go ahead and add a boundary tags member 
    domain.boundaryTags = boundaryTags
    domain.writePoly("mesh")
    domain.writePLY("mesh")
    domain.writeAsymptote("mesh")
    triangleOptions="VApq1.5q1.5ena%21.16e" % ((he**3)/6.0,)


# Time stepping
T=6.00
dt_fixed = 0.1/Refinement
nDTout = int(round(T/dt_fixed))

# Numerical parameters
ns_shockCapturingFactor  = 0.2
ls_shockCapturingFactor  = 0.2
ls_sc_uref  = 1.0
ls_sc_beta  = 1.0
vof_shockCapturingFactor = 0.2
vof_sc_uref = 1.0
vof_sc_beta = 1.0
rd_shockCapturingFactor  = 0.2

epsFact_density    = 1.5
epsFact_viscosity  = 1.5
epsFact_redistance = 0.33
epsFact_curvature  = 1.5
epsFact_consrv_heaviside = 1.5
epsFact_consrv_dirac     = 1.5
epsFact_consrv_diffusion = 10.0
epsFact_vof = 1.5

# Water
rho_0 = 998.2
nu_0  = 1.004e-6

# Air
rho_1 = 1.205
nu_1  = 1.500e-5 

# Surface tension
sigma_01 = 0.0

# Gravity
g = [0.0,0.0,-9.8]

# Initial condition
waterLine_x = 1.20
waterLine_z = 0.55

def signedDistance(x):
    phi_x = x[0]-waterLine_x
    phi_z = x[2]-waterLine_z 
    if phi_x < 0.0:
        if phi_z < 0.0:
            return max(phi_x,phi_z)
        else:
            return phi_z
    else:
        if phi_z < 0.0:
            return phi_x
        else:
            return sqrt(phi_x**2 + phi_z**2)


