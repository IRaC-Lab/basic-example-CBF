# Import packages.
import cvxpy as cp
import numpy as np


def DI_cbf_solve(x1, x2, u_des, gamma):
    # Generate data.
    u_m = -5
    u_M = 5
    p_m = -1
    v_m = -1
    p_M = 1
    v_M = 1

    fx = np.array([[x2],
                [0]])
    gx = np.array([[0],
                [1]])
    
    if x2 > 0:
        dhdx = np.array([[-1, x2/u_m],
                        [1, 0],
                        [0, -1],
                        [0, 1]])
        # Barrier function
        hx = np.array([[p_M - x1 + x2**2/(2*u_m)], 
                [x1 - p_m],
                [v_M - x2],
                [x2 - v_m]])
    else:
         dhdx = np.array([[-1, 0],
                          [1, -x2/u_M],
                          [0, -1],
                          [0, 1]])
         # Barrier function
         hx = np.array([[p_M - x1], 
                [x1 - p_m - x2**2/(2*u_M)],
                [v_M - x2],
                [x2 - v_m]])
        

    P = np.eye(1)

    # Define and solve the CVXPY problem.
    u = cp.Variable(1)
    cost = cp.quad_form(u - u_des, P)
    constraint = [(dhdx @ fx).flatten() + dhdx @ gx @ u + (hx*gamma).flatten() >=0 ]
    prob = cp.Problem(cp.Minimize(cost), constraint)
    prob.solve()

    if prob.status == "optimal":
         return u.value[0]
    else:
         print("Status: ", prob.status)
         return None


def main():
    x1 = -0.356191735278949
    x2 = -0.993957962194644
    u_des = -1

    u_act, status = DI_cbf_solve(x1, x2, u_des)

    print(f"status: {status}, actual u: {u_act}")

if __name__ == "__main__":
	main()

