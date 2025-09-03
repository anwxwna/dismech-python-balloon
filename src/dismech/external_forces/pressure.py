import typing
import scipy.sparse as sp
import numpy as np

from ..soft_robot import SoftRobot


def compute_pressure_forces(robot: SoftRobot, q: np.ndarray, u: np.ndarray) -> typing.Tuple[np.ndarray, np.ndarray]:
    p = robot.env.p
    rho_med = robot.env.rho
    dt = robot.sim_params.dt
    Fp = np.zeros(robot.n_dof)
    Jp = np.zeros((robot.n_dof, robot.n_dof))
    face_as = robot.face_area
    face_nodes = robot.face_nodes_shell  # (n_faces, 3)



    return Fp, Jp
