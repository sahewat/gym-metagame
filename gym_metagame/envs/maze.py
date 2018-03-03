import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import matplotlib.pyplot as plt

def random_map(map_shape=(16,16)):
    x_dim, y_dim = map_shape
    map_array = np.zeros(map_shape)

    n_anchors = 6
    start_idx = np.random.randint(map_shape[0], size=(n_anchors, 2))
    n_moves = 20
    map_array = np.zeros(map_shape)
    start_position = map_array[0,0] = 2
    end_position = map_array[-1,-1] = 3

    for idx in start_idx:
        position = idx
        map_array[idx[0]-2:idx[0], idx[1]-2:idx[1]] = 1

    plt.imshow(map_array)
    return map_array

class MazeEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
      pass

  def _step(self, action):
      pass

  def _reset(self):
      pass

  def _render(self, mode='human', close=False):
      pass

class GridEnv(gym.Env):
    def __init__(self):
        self.state = random_map()
        self.old_state = self.state.copy()
        self.start_state = [0,0]
        self.position = [0,0]
        self.end_state = [-1,-1]
        self.path = [self.start_state]

    def _move(self, row, col, a):
            ncol = nrow = self.state.shape[0]
            new_row = row
            new_col = col
            if a==0: # left
                new_col = max(col-1,0)
            elif a==1: # down
                new_row = min(row+1,nrow-1)
            elif a==2: # right
                new_col = min(col+1,ncol-1)
            elif a==3: # up
                new_row = max(row-1,0)
            return (new_row, new_col)

    def reset(self):

        obs = self.old_state.copy()
        obs[self.position[1], self.position[0]] = 5
        self.start_state = [0,0]
        self.position = [0,0]
        self.end_state = [-1,-1]
        self.path = [self.start_state]

        return obs


    def step(self, action):
        new_position = self._move(*self.position, action)
        #current_map[new_position[0], new_position[1]] = 0
        if self.state[new_position[1], new_position[0]] == 1:
            print(new_position)
            new_position = self.position
            assert new_position == self.position
        self.path.append(new_position)

        self.position = new_position
        if self.state[new_position[0], new_position[1]] == 3:
            complete = True
            print("DONE")
        else:
            complete = False

        obs = self.state.copy()
        obs[new_position[1], new_position[0]] = 5

        return obs, new_position, complete, None

    def render(self, mode='human'):
        current_map = self.state.copy()
        #current_map[self.position[0], self.position[1]] = 4
        path = np.array(self.path)
        plt.plot(*path.T, 'o')
        plt.imshow(current_map, cmap='gray')
