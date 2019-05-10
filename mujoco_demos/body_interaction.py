"""
Example of how bodies interact with each other.
such as collide
"""

from mujoco_py import load_model_from_path, MjSim, MjViewer
import math
import os

path = os.path.join(os.getcwd(), 'body_interaction.xml')
print(path)
model = load_model_from_path(path)
sim = MjSim(model)
viewer = MjViewer(sim)

t = 0
while True:
    sim.data.ctrl[0] = math.cos(t / 10.) * 0.01
    sim.data.ctrl[1] = math.sin(t / 10.) * 0.01
    t += 1
    sim.step()
    viewer.render()
    if t > 100 and os.getenv('TESTING') is not None:
        break