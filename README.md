# epistemic_diversity_RL
This repository contains python code for the simulations described in the paper titled "Epistemic diversity and industrial selection bias".

The code will run simulations for standard deviation values in the 0 to 0.2 range in 0.005 steps. For every standard deviation value a given number of games with a given number of cycles will be played. On the paper, values were for 100 games with 400 cycles each. The overall probability of A being the concensus will be printed for each standard deviation value. 

To carry out different types of simulations you can modify the definers located at the top of the code:

```
#economic agent variables
ECON_AGENT_PWR          = 100  -> Power of the economic agent
ECON_AGENT_ALPHA        = 1.05 -> Alpha parameter for the economic agent in Q-learning
ECON_AGENT_GAMMA        = 0.5  -> Gamma parameter for the economic agent in Q-learning
ECON_AGENT_EXPLORE_PROB = 0.5  -> Probability for the economic agent to explore (carry out a random action) instead of deciding an action according to its Q-learning knowledge.

#non-economic agent variables
NON_ECON_AGENT_PWR     = 0 -> Power of the economic agent, set to 100 and ECON_AGENT_PWR to 0 to simulate only the random, non-economic agent.

#global simulation variables
N_SCIENTISTS       = 100   -> Number of scientisits available
PA                 = 0.55  -> Prior probability of scientists carrying out a successful experiment
SIM_CYCLES         = 400   -> Number of simulation cycles per game
NUM_GAMES          = 100   -> Number of games played
```

