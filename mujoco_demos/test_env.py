"""
Show environment under the xmls folder
"""

from mujoco_py import load_model_from_path, MjSim, MjViewer
import os

base_path = os.path.dirname(__file__)
xml_dir = os.path.join(base_path, 'xmls')

xml_files = [os.path.join(xml_dir, f) for f in os.listdir(xml_dir) if
             os.path.isfile(os.path.join(xml_dir, f))]

for path in xml_files:
    try:
        model = load_model_from_path(path)
        env_name = os.path.basename(path).split('.')[0]
        print('Simulation example: ' + env_name)
    except:
        print("Load xml file failed")

    sim = MjSim(model)
    viewer = MjViewer(sim)

    t = 0
    while True:
        sim.step()
        viewer.render()
        t += 1
        if t > 500:
            break
