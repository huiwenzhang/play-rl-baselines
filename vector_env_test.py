"""
Example to show how to use vector env so that training can be speed up
"""

import gym
import numpy as np
import  time

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import SubprocVecEnv
from stable_baselines.common import set_global_seeds
from stable_baselines import ACKTR


def make_env(env_id, rand, seed=0):
    """
    Utility function for mulitprocessing env
    :param env_id:env id
    :param rand: index of subprocess
    :param seed: seed
    :return:
    """
    def _init():
        env = gym.make(env_id)
        # env.unwrapped
        env.seed(seed + rand)
        return env
    set_global_seeds(seed)
    return _init


env_id = "CartPole-v1"
num_cpu = 1  # number of process
# vectorized environment
env = SubprocVecEnv([make_env(env_id, i) for i in range(num_cpu)])
model = ACKTR(MlpPolicy, env, verbose=1)

start = time.time()
model.learn(total_timesteps=25000)
end = time.time()
print("Training cost {} seconds".format(end-start))

# test
obs = env.reset()
for i in range(1000):
    action, _state = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
