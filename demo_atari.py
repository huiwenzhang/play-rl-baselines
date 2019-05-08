"""
Play with atari games with RL agent
"""

from stable_baselines.common.cmd_util import make_atari_env
from stable_baselines.common.vec_env import VecFrameStack
from stable_baselines import ACER

env = make_atari_env('PongNoFrameskip-v4', num_env=4, seed=0)
env = VecFrameStack(env, n_stack=4)

model = ACER('CnnPolicy', env, verbose=1)
model.learn(total_timesteps=25000)

obs = env.reset()
for i in range(5000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
