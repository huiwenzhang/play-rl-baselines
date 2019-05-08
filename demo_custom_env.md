## Create custom env
- follow the architecture of gym

### Interface
```python
import gym
from gym import spaces

class CustomEnv(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}

  def __init__(self, arg1, arg2, ...):
    super(CustomEnv, self).__init__()
    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions:
    self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
    # Example for using image as input:
    self.observation_space = spaces.Box(low=0, high=255,
                                        shape=(HEIGHT, WIDTH, N_CHANNELS), dtype=np.uint8)

  def step(self, action):
    ...
  def reset(self):
    ...
  def render(self, mode='human', close=False):
    ...
```
### Inteface function
- __init__: declare the action space and observation space
- ste(self, action): how to respond to a action, return `next_obs, reward, dones, info`
- reset(self): return obs when an episode is over
- render(self, mode='human',close=False): how to visualize the env

## Example
https://github.com/hill-a/stable-baselines/blob/master/stable_baselines/common/identity_env.py

## Use the custom env
https://github.com/hill-a/stable-baselines/blob/master/tests/test_identity.py

