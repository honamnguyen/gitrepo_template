from gym.envs.registration import register

register(
    id='name-v1',
    entry_point='gym_name.envs:CustomEnv',
)