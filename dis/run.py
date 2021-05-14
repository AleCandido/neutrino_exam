import pathlib

import numpy as np
import yaml
import yadism

here = pathlib.Path(__file__).absolute().parent


def input_kinematics():
    # values from Fig.2 hep-ph/1106.3723
    #  x = np.geomspace(1e-10, 0.65, 30)
    x = np.geomspace(1e-6, 0.65, 30)
    Q2 = np.geomspace(10, 1e11, 20)
    # values from Fig.6-11 hep-ph/1106.3723
    s = np.geomspace(100, 1e12, 20)
    return x, Q2, s


def xq2y_grid(x, Q2, s):
    y = s
    return np.transpose(np.array(np.meshgrid(x, Q2, y)), (1, 2, 3, 0))


def load_theory():
    with open(here / "theory.yaml") as f:
        card = yaml.safe_load(f)

    return card


def load_observables(kinematics):
    with open(here / "observables.yaml") as f:
        card = yaml.safe_load(f)

    card["observables"] = {obs: kinematics for obs in ["F2_light"]}
    return card


if __name__ == "__main__":
    grid = xq2y_grid(*input_kinematics())
    kinematics = [dict(x=el[0], Q2=el[1], y=el[2]) for el in grid.reshape(-1, 3)]
    theory = load_theory()
    observables = load_observables(kinematics)
    yadism.run_yadism(theory, observables)
    __import__("pdb").set_trace()
