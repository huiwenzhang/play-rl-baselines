"""
Demo to show customized callback func.
"""

import os
import gym
import numpy as np
import matplotlib.pyplot as plt

from stable_baselines.ddpg.policies import MlpPolicy
from stable_baselines.common.vec_env.dummy_vec_env import DummyVecEnv
from stable_baselines.bench import Monitor
from stable_baselines.results_plotter import load_results, ts2xy
from stable_baselines import DDPG
from stable_baselines.ddpg.noise import AdaptiveParamNoiseSpec

best_mean_reward, n_steps = -np.inf, 0


def callback(_locals, _globals):
    """
    callback called at each step
    :param _locals:
    :param _globals:
    :return:
    """
    global n_steps, best_mean_reward
    if (n_steps + 1) % 1000 == 0:
        # evaluate policy performace
        x, y = ts2xy(load_results(log_dir), 'timesteps')
        if len(x) > 0:
            mean_reward = np.mean(y[-100:])
            print(x[-1], 'timesteps')
            print("Best mean reward: {:.2f} - last mean reward per episode: {:.2f} ".format(
                best_mean_reward, mean_reward))
            if mean_reward > best_mean_reward:
                best_mean_reward = mean_reward
                print("Save new best model")
                _locals['self'].save(log_dir + 'best_model.pkl')
        n_steps += 1
        return True


# Log dir
log_dir = "/tmp/gym/"
os.makedirs(log_dir, exist_ok=True)

# Create and warp the environment
env = gym.make('LunarLanderContinuous-v2')
env = Monitor(env, log_dir, allow_early_resets=True)
env = DummyVecEnv([lambda: env])

param_noise = AdaptiveParamNoiseSpec(initial_stddev=0.2, desired_action_stddev=0.2)
model = DDPG(MlpPolicy, env, param_noise=param_noise, memory_limit=int(1e6), verbose=0)
# Train the agent
model.learn(total_timesteps=int(2e5), callback=callback)
