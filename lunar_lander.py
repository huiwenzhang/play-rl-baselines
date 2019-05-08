import gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import A2C

env = gym.make('LunarLander-v2')
env = DummyVecEnv([lambda : env])
model = A2C(MlpPolicy, env, ent_coef=0.1, verbose=1)
model.learn(total_timesteps=100000)

# save agent
model.save("a2c_lunar")
del model

model = A2C.load("a2c_lunar")

# test
obs = env.reset()
for i in range(1000):
    action, _state = model.predict(obs)
    obs, rewards,dones, info = env.step(action)
    env.render()