#
# Copyright (c) 2017 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from memories.episodic_experience_replay import EpisodicExperienceReplay
from memories.memory import MemoryGranularity, MemoryParameters


class SingleEpisodeBufferParameters(MemoryParameters):
    def __init__(self):
        super().__init__()
        del self.max_size
        self.discount = 0.99
        self.bootstrap_total_return_from_old_policy = False
        self.n_step = -1

    @property
    def path(self):
        return 'memories.single_episode_buffer:SingleEpisodeBuffer'


class SingleEpisodeBuffer(EpisodicExperienceReplay):
    def __init__(self,  discount: float,
                 bootstrap_total_return_from_old_policy: bool, n_step: int):
        """
        :param discount: the discount factor to use when calculating total returns
        :param bootstrap_total_return_from_old_policy: should the total return be bootstrapped from the values in the
                                                       memory
        :param n_step: the number of future steps to sum the reward over before bootstrapping

        """
        super().__init__((MemoryGranularity.Episodes, 1), discount, bootstrap_total_return_from_old_policy, n_step, 0)