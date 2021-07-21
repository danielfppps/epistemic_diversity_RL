# epistemic_diversity_RL
This repository contains python code for the simulations described in the paper titled "Epistemic diversity and industrial selection bias"

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

