from stable_baselines import  PPO2
import gym
model = PPO2('MlpPolicy', 'CartPole-v1').learn(10000)

# test
env = gym.make('CartPole-v1')
# env = DummyVecEnv([lambda: env])  # The algorithms require a vectorized environment to run
obs = env.reset()
for i in range(1000):
    a, _s = model.predict(obs)
    obs, rewards, dones, info = env.step(a)
    env.render()