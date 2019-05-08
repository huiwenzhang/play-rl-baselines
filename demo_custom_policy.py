"""
Demo showing how to define a policy using your own architecture
means different layers, units or type of units
"""
import gym
from stable_baselines.common.policies import FeedForwardPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import A2C

"""
Define a custom policy class. How
- inherent the parent policy class and modify the net_arch parameter
"""


class CustomPolicy(FeedForwardPolicy):
    def __init__(self, *args, **kargs):
        super(CustomPolicy, self).__init__(*args, **kargs,
                                           net_arch=[dict(pi=[128, 128, 128], vf=[128, 128, 128])],
                                           feature_extraction="mlp")


model = A2C(CustomPolicy, 'LunarLander-v2', verbose=1)
model.learn(total_timesteps=100000)

# test
env = gym.make("LunarLander-v2")
obs = env.reset()
for i in range(1000):
    action, _state = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
