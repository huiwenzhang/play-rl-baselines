"""
Show environment under the xmls folder
"""

from mujoco_py import load_model_from_path, MjSim, MjViewer
import math
import os

base_path = "/home/huiwen/paper/baselines/play"
xml_dir = os.path.join(base_path, 'mujoco_demos', 'xmls')

xml_files = [os.path.join(xml_dir, f) for f in os.listdir(xml_dir) if
             os.path.isfile(os.path.join(xml_dir, f))]

for path in xml_files:
    try:
        model = load_model_from_path(path)
        env_name = os.path.basename(path).split('.')[0]
        print('Simulation example: ' + env_name)
    except:
        print("Load xml file failed")

    # test specific env
    if env_name.startswith('simple'):
        sim = MjSim(model)
        viewer = MjViewer(sim)

        t = 0
        while True:
            t += 1
            sim.step()
            viewer.render()
            if t > 1500:
                break
