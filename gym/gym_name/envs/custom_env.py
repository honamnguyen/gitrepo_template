import gym
from gym import spaces
import numpy as np

class Custom_Env(gym.Env):
    metadata = {'render.modes': ['human']}
    '''
    Custom Environment
    
    state:
    
    action:
    
    reward:
           
    TO DO:
    - 
    '''

    def __init__(self, **kw):
        super().__init__()
        print('---Initiating Custom Environment---')
        self.rl_state = kw['rl_state']
        self.step_params = kw['step_params']
        self.tnow = 0

        # 
        self.sim_params = kw['sim_params']
        self.update_simulator(self.sim_params['name'])
        
        # Action and observation spaces
        self.action_space = spaces.Discrete(...)    
        obs_space_dict = {}
        obs_space_dict['...'] = spaces.MultiBinary(...)
        obs_space_dict['...'] = spaces.MultiDiscrete(...)
        self.observation_space = spaces.Dict(obs_space_dict)
        
        self.reset()
        
    def _get_metric(self, label):
        # return already calculated metric
        if label in self.metrics:
            return self.metrics[label]
        else:
            if label == ...:
                val = self.sim. ...
            elif label == ...:
                val = self.sim. ...
            else:
                raise NotImplementedError(f'`{label}` metric is not implemented')
            self.metrics[label] = val
            return val
        
    def reward_function(self):
        '''
        generic termination condition
        generic target
        
        combined termination condition
        
        target/obj:
        '''
        
        step_params = self.step_params
        self.metrics = {}
            
        done = False
        for i,label in enumerate(step_params['termination_metrics']):
            done = done or (self._get_metric(label) > step_params['termination_values'][i])
        
        if 'sparse' in step_params['reward_scheme']:
            if done:
                reward = self._get_metric(step_params['objective_metric'])
                self.reset()
            else:
                reward = 0
                
        elif 'dense' in step_params['reward_scheme']:
            if done:
                reward = 0
                self.reset()
            else:
                obj = self._get_metric(step_params['objective_metric'])
                reward = obj - self.prev_obj
                self.prev_obj = obj
                
        return reward, done
      
    def step(self, action):
        
        self.sim.evolve(action)
        self.state = self.sim.get_state(self.rl_state)
        reward, done = self.reward_function()
        return self.state, reward, done, {}
    
    def reset(self):
        self.sim.reset()
        self.metrics = {}
        self.prev_obj = self._get_metric(self.step_params['objective_metric'])
        self.state = self.sim.get_state(self.rl_state)
        return self.state
    
    def render(self, mode='human'):
        return 0
        
    def update_simulator(self, sim_name):
        if sim_name == '...':
            from ... import Simulator
            self.sim = Simulator(self.sim_params)            
        elif ...:
            from ... import OtherSimulator
            self.sim = OtherSimulator(self.sim_params)
        self.sim_name = sim_name