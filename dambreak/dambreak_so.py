from proteus.default_so import *
import dambreak
from dambreak import *

pnList = [("twp_navier_stokes_p", "twp_navier_stokes_n"),
          ("ls_p",                "ls_n"),
          ("vof_p",               "vof_n"),
          ("redist_p",            "redist_n"),
          ("ls_consrv_p",         "ls_consrv_n")]

    
name = soname

systemStepControllerType = Sequential_FixedStep
    
needEBQ_GLOBAL = False
needEBQ = False

tnList = [i*dambreak.dt_fixed for i in range(0,dambreak.nDTout+1)] 
