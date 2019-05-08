"""
Deomo showing how to make a gif
"""

import imageio
import numpy as np

from stable_baselines.common.policies import MlpPolicy
from stable_baselines import A2C

model = A2C(MlpPolicy, 'LunarLander-v2').learn(100000)

images = []
obs = model.env.reset()
img = model.env.render(mode='rgb_array')
for _ in range(350):
    images.append(img)
    action, _ = model.predict(obs)
    obs, _, _, _ = model.env.step(action)
    img = model.env.render(mode='rgb_array')

imageio.mimsave('resource/lander_a2c.gif',
                [np.array(img[0]) for i, img in enumerate(images) if i % 2 == 0],
                fps=29)
