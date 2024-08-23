# Import packages.
import cvxpy as cp
import numpy as np


def manipulator_cbf(q, p, J, u_des, gamma):
    # Parameters
    R = 0.1
    R_w = 0.1
    p_obs = np.array([0, 0.4, 1])

    q = np.array(q)
    p = np.array(p)
    J = np.array(J)
    u_des = np.array(u_des)

    # Functions
    fx = np.zeros((6,1))
    gx = np.eye(6)
    
    # Derivative of Barrier function
    dhdx = 2*(p - p_obs).transpose() @ J[3:, :]
    
    # Barrier function
    hx = np.linalg.norm(p - p_obs)**2 - (R + R_w)**2
    
    P = np.eye(6)

    # Define and solve the CVXPY problem.
    u = cp.Variable(6)
    cost = cp.quad_form(u - u_des, P)
    constraint = [(dhdx @ fx).flatten() + dhdx @ gx @ u + (hx*gamma).flatten() >=0 ]
    prob = cp.Problem(cp.Minimize(cost), constraint)
    prob.solve()

    if prob.status == "optimal":
         return u.value
    else:
         print("Status: ", prob.status)
         return None


def main():

    # Test parameters
    q = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    p = [0.431800000631427, -0.129539999234082, 1.05565900023251]
    J = [[0, 0, 0, 0, 0, 0], 
         [0.0000, -1.0000,   -1.0000,         0,   -1.0000,         0],
    [1.0000,    0.0000,    0.0000,    1.0000 ,   0.0000,    1.0000],
    [0.1295,  -0.4854,   -0.4854,   -0.0000,   -0.0533,         0],
    [0.4318,    0.0000,    0.0000,         0,         0,         0],
   [-0.0000,    0.4318,    0.0000,         0,         0,         0]]
    u_des = [1, 0, 0, 0, 0, 0]
    gamma = 10

    u_act = manipulator_cbf(q, p, J, u_des, gamma)

    print(f"actual u: {u_act}")
          
if __name__ == "__main__":
	main()

