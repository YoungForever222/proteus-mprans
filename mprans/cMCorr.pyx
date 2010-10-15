import numpy
cimport numpy
from proteus import *
from proteus.Transport import *
from proteus.Transport import OneLevelTransport

cdef extern from "MCorr.h" namespace "proteus":
    cdef cppclass MCorr_base:
        void calculateResidual(double* mesh_trial_ref,
				       double* mesh_grad_trial_ref,
                                       double* mesh_dof,
                                       int* mesh_l2g,
                                       double* dV_ref,
                                       double* u_trial_ref,
                                       double* u_grad_trial_ref,
                                       double* u_test_ref,
                                       double* u_grad_test_ref,
                                       double* mesh_trial_trace_ref,
                                       double* mesh_grad_trial_trace_ref,
                                       double* dS_ref,
                                       double* u_trial_trace_ref,
                                       double* u_grad_trial_trace_ref,
                                       double* u_test_trace_ref,
                                       double* u_grad_test_trace_ref,
                                       double* normal_ref,
                                       double* boundaryJac_ref,
                                       int nElements_global,
				       double useMetrics,
                                       double epsFactHeaviside,
                                       double epsFactDirac,
                                       double epsFactDiffusion,
                                       int* u_l2g, 
                                       double* elementDiameter,
                                       double* u_dof,
                                       double* q_phi,
				       double* q_normal_phi,
                                       double* q_H,
                                       double* q_u,
                                       double* q_r,
                                       int offset_u, int stride_u, 
                                       double* globalResidual)
        void calculateJacobian(double* mesh_trial_ref,
                                       double* mesh_grad_trial_ref,
                                       double* mesh_dof,
                                       int* mesh_l2g,
                                       double* dV_ref,
                                       double* u_trial_ref,
                                       double* u_grad_trial_ref,
                                       double* u_test_ref,
                                       double* u_grad_test_ref,
                                       double* mesh_trial_trace_ref,
                                       double* mesh_grad_trial_trace_ref,
                                       double* dS_ref,
                                       double* u_trial_trace_ref,
                                       double* u_grad_trial_trace_ref,
                                       double* u_test_trace_ref,
                                       double* u_grad_test_trace_ref,
                                       double* normal_ref,
                                       double* boundaryJac_ref,
                                       int nElements_global,
				       double useMetrics,
                                       double epsFactHeaviside,
                                       double epsFactDirac,
                                       double epsFactDiffusion,
                                       int* u_l2g,
                                       double* elementDiameter,
                                       double* u_dof, 
                                       double* q_phi,
				       double* q_normal_phi,
                                       double* q_H,
                                       int* csrRowIndeces_u_u,int* csrColumnOffsets_u_u,
                                       double* globalJacobian)
    MCorr_base* newMCorr(int nSpaceIn,
                       int nQuadraturePoints_elementIn,
                       int nDOF_mesh_trial_elementIn,
                       int nDOF_trial_elementIn,
                       int nDOF_test_elementIn,
                       int nQuadraturePoints_elementBoundaryIn,
                       int CompKernelFlag)

cdef class cMCorr_base:
   cdef MCorr_base* thisptr
   def __cinit__(self,
                 int nSpaceIn,
                 int nQuadraturePoints_elementIn,
                 int nDOF_mesh_trial_elementIn,
                 int nDOF_trial_elementIn,
                 int nDOF_test_elementIn,
                 int nQuadraturePoints_elementBoundaryIn,
                 int CompKernelFlag):
       self.thisptr = newMCorr(nSpaceIn,
                              nQuadraturePoints_elementIn,
                              nDOF_mesh_trial_elementIn,
                              nDOF_trial_elementIn,
                              nDOF_test_elementIn,
                              nQuadraturePoints_elementBoundaryIn,
                              CompKernelFlag)
   def __dealloc__(self):
       del self.thisptr
   def calculateResidual(self,
                         numpy.ndarray mesh_trial_ref,
                         numpy.ndarray mesh_grad_trial_ref,
                         numpy.ndarray mesh_dof,
                         numpy.ndarray mesh_l2g,
                         numpy.ndarray dV_ref,
                         numpy.ndarray u_trial_ref,
                         numpy.ndarray u_grad_trial_ref,
                         numpy.ndarray u_test_ref,
                         numpy.ndarray u_grad_test_ref,
                         numpy.ndarray mesh_trial_trace_ref,
                         numpy.ndarray mesh_grad_trial_trace_ref,
                         numpy.ndarray dS_ref,
                         numpy.ndarray u_trial_trace_ref,
                         numpy.ndarray u_grad_trial_trace_ref,
                         numpy.ndarray u_test_trace_ref,
                         numpy.ndarray u_grad_test_trace_ref,
                         numpy.ndarray normal_ref,
                         numpy.ndarray boundaryJac_ref,
                         int nElements_global,
			 double useMetrics,
                         double epsFactHeaviside,
                         double epsFactDirac,
                         double epsFactDiffusion,
                         numpy.ndarray u_l2g, 
                         numpy.ndarray elementDiameter,
                         numpy.ndarray u_dof,
                         numpy.ndarray q_phi,
			 numpy.ndarray q_normal_phi,
                         numpy.ndarray q_H,
                         numpy.ndarray q_u,
                         numpy.ndarray q_r,
                         int offset_u, 
                         int stride_u, 
                         numpy.ndarray globalResidual):
       self.thisptr.calculateResidual(<double*> mesh_trial_ref.data,
                                       <double*> mesh_grad_trial_ref.data,
                                       <double*> mesh_dof.data,
                                       <int*> mesh_l2g.data,
                                       <double*> dV_ref.data,
                                       <double*> u_trial_ref.data,
                                       <double*> u_grad_trial_ref.data,
                                       <double*> u_test_ref.data,
                                       <double*> u_grad_test_ref.data,
                                        <double*> mesh_trial_trace_ref.data,
                                       <double*> mesh_grad_trial_trace_ref.data,
                                       <double*> dS_ref.data,
                                       <double*> u_trial_trace_ref.data,
                                       <double*> u_grad_trial_trace_ref.data,
                                       <double*> u_test_trace_ref.data,
                                       <double*> u_grad_test_trace_ref.data,
                                       <double*> normal_ref.data,
                                       <double*> boundaryJac_ref.data,
                                       nElements_global,
				       useMetrics,
                                       epsFactHeaviside,
                                       epsFactDirac,
                                       epsFactDiffusion,
                                       <int*> u_l2g.data, 
                                       <double*> elementDiameter.data,
                                       <double*> u_dof.data,
                                       <double*> q_phi.data,
				       <double*> q_normal_phi.data,
                                       <double*> q_H.data,
                                       <double*> q_u.data,
                                       <double*> q_r.data,
                                       offset_u, 
                                       stride_u, 
                                       <double*> globalResidual.data)
   def calculateJacobian(self,
                         numpy.ndarray mesh_trial_ref,
                         numpy.ndarray mesh_grad_trial_ref,
                         numpy.ndarray mesh_dof,
                         numpy.ndarray mesh_l2g,
                         numpy.ndarray dV_ref,
                         numpy.ndarray u_trial_ref,
                         numpy.ndarray u_grad_trial_ref,
                         numpy.ndarray u_test_ref,
                         numpy.ndarray u_grad_test_ref,
                         numpy.ndarray mesh_trial_trace_ref,
                         numpy.ndarray mesh_grad_trial_trace_ref,
                         numpy.ndarray dS_ref,
                         numpy.ndarray u_trial_trace_ref,
                         numpy.ndarray u_grad_trial_trace_ref,
                         numpy.ndarray u_test_trace_ref,
                         numpy.ndarray u_grad_test_trace_ref,
                         numpy.ndarray normal_ref,
                         numpy.ndarray boundaryJac_ref,
                         int nElements_global,
			 double useMetrics,
                         double epsFactHeaviside,
                         double epsFactDirac,
                         double epsFactDiffusion,
                         numpy.ndarray u_l2g,
                         numpy.ndarray elementDiameter,
                         numpy.ndarray u_dof, 
			 numpy.ndarray q_phi,
                         numpy.ndarray q_normal_phi,
                         numpy.ndarray q_H,
                         numpy.ndarray csrRowIndeces_u_u,
                         numpy.ndarray csrColumnOffsets_u_u,
                         globalJacobian):
       cdef numpy.ndarray rowptr,colind,globalJacobian_a
       (rowptr,colind,globalJacobian_a) = globalJacobian.getCSRrepresentation()
       self.thisptr.calculateJacobian(<double*> mesh_trial_ref.data,
                                       <double*> mesh_grad_trial_ref.data,
                                       <double*> mesh_dof.data,
                                       <int*> mesh_l2g.data,
                                       <double*> dV_ref.data,
                                       <double*> u_trial_ref.data,
                                       <double*> u_grad_trial_ref.data,
                                       <double*> u_test_ref.data,
                                       <double*> u_grad_test_ref.data,
                                       <double*> mesh_trial_trace_ref.data,
                                       <double*> mesh_grad_trial_trace_ref.data,
                                       <double*> dS_ref.data,
                                       <double*> u_trial_trace_ref.data,
                                       <double*> u_grad_trial_trace_ref.data,
                                       <double*> u_test_trace_ref.data,
                                       <double*> u_grad_test_trace_ref.data,
                                       <double*> normal_ref.data,
                                       <double*> boundaryJac_ref.data,
                                       nElements_global,
				       useMetrics,
                                       epsFactHeaviside,
                                       epsFactDirac,
                                       epsFactDiffusion,
                                       <int*> u_l2g.data,
                                       <double*> elementDiameter.data,
                                       <double*> u_dof.data, 
                                       <double*> q_phi.data,
				       <double*> q_normal_phi.data,
                                       <double*> q_H.data,
                                       <int*> csrRowIndeces_u_u.data,
                                       <int*> csrColumnOffsets_u_u.data,
                                       <double*> globalJacobian_a.data)
