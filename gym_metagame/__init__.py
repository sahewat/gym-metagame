import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='maze-v0',
    entry_point='gym_metagame.envs:MazeEnv',
)
