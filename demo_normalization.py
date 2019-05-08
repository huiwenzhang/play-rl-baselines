"""
Demo to show how to mormalize feature input
"""

import gym
from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv, VecNormalize
from stable_baselines import PPO2

env = DummyVecEnv([lambda: gym.make('Reacher-v2')])
env = VecNormalize(env, norm_obs=True, norm_reward=False, clip_obs=10.)

model = PPO2(MlpPolicy, env)
model.learn(total_timesteps=80000)

obs = env.reset()
for i in range(2000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
