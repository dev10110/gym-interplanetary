from gym.envs.registration import register

register(
    id='interplanetary-v0',
    entry_point='gym_interplanetary.envs:InterplanetaryEnv',
)
register(
    id='interplanetary-extrahard-v0',
    entry_point='gym_interplanetary.envs:InterplanetaryExtraHardEnv',
)
