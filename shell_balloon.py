import numpy as np

import dismech


geom = dismech.GeomParams(rod_r0=0.005,
                          shell_h=0.0001)

material = dismech.Material(density=1000,
                            youngs_rod=0,
                            youngs_shell=10e7,
                            poisson_rod=0,
                            poisson_shell=0.5)

shell_contact_sim = dismech.SimParams(static_sim=False,
                                  two_d_sim=False,   # no twisting
                                  use_mid_edge=False,
                                  use_line_search=False,
                                  show_floor=False,
                                  log_data=True,
                                  log_step=1,
                                  dt=1e-4,
                                  max_iter=100,
                                  total_time=0.001,
                                  plot_step=1,
                                  tol= 1e1, #1e-4,
                                  ftol=1e-4,
                                  dtol=1e-2)

env = dismech.Environment()
env.add_force('gravity', g=np.array([0.0, 0.0, 0.0])) # neutral bouyancy
env.add_force('pressure',rho=1000, p=50e6 )

geo = dismech.Geometry.from_txt('input_for_cyl_shell_3_4.txt')

robot = dismech.SoftRobot(geom, material, geo, shell_contact_sim, env)
