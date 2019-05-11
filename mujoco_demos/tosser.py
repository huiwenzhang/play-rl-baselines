"""
Shows how to toss a capsule to a container.
"""
from mujoco_py import load_model_from_path, MjSim, MjViewer
import os

model = load_model_from_path("xmls/tosser.xml")
sim = MjSim(model)

viewer = MjViewer(sim)

sim_state = sim.get_state()

while True:
    sim.set_state(sim_state)

    for i in range(2000):
        if i < 500:
            sim.data.ctrl[:] = 1.0
        else:
            sim.data.ctrl[:] = -5.0
        sim.step()
        viewer.render()

    break
