"""
Demo showing how to wrap the env so tha video can be recorded and retrieved
"""

import gym
from stable_baselines.common.vec_env import VecVideoRecorder, DummyVecEnv

env_id = "Hopper-v2"
video_folder = 'logs/videos/'
video_length = 200

env = DummyVecEnv([lambda: gym.make(env_id)])

obs = env.reset()

# Record video from the first step
env = VecVideoRecorder(env, video_folder, record_video_trigger=lambda x: x == 0,
                       video_length=video_length, name_prefix='ramdom-agent-{}'.format(env_id))
env.reset()

for _ in range(video_length + 1):
    action = [env.action_space.sample()]
    obs, _, _, _ = env.step(action)
env.close()

"""
Note:
When using simulated env, such as the Reacher rendered by mujoco, we need to 
unset the LD_PRELOAD　env vaiable. otherwise it will throw failed to initialize
OpenGL error
"""