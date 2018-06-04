from configurations import *
from block_factories.basic_rl_factory import BasicRLFactory


class HopperBullet_A3C(Hopper_A3C):
    def __init__(self):
        Hopper_A3C.__init__(self)
        pass


class EnvParams(Mujoco):
    def __init__(self):
        super().__init__()
        self.level = 'HopperBulletEnv-v0'


class VisParams(VisualizationParameters):
    def __init__(self):
        super().__init__()

factory = BasicRLFactory(agent_params=AgentParams, env_params=EnvParams, vis_params=VisParams)