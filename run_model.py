#!/usr/bin/python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

######## MODEL CONFIGURATION ######

#economic agent variables
ECON_AGENT_PWR          = 100
ECON_AGENT_ALPHA        = 1.05
ECON_AGENT_GAMMA        = 0.5
ECON_AGENT_EXPLORE_PROB = 0.5

#non-economic agent variables
NON_ECON_AGENT_PWR     = 0

#global simulation variables
N_SCIENTISTS       = 100
PA                 = 0.55
SIM_CYCLES         = 400
NUM_GAMES          = 100

####################################

#actions
DONT_FINANCE       = 0
FINANCE            = 1

SIM_TYPE = 1


def get_max_beta_dist(a, b, k, n):
    return (a+k-1)/(a+b+n-2)
    
def choose_action(qtable, state):   

    if np.random.random() > ECON_AGENT_EXPLORE_PROB:
        if qtable[state][0] > qtable[state][1] :
            max_q_idx = DONT_FINANCE
        elif qtable[state][0] < qtable[state][1] :
            max_q_idx = FINANCE
        elif qtable[state][0] == qtable[state][1] :
            randomDraw = np.random.random()
            if randomDraw > 0.5 :
                max_q_idx = DONT_FINANCE
            else:
                max_q_idx = FINANCE
    else:
	randomDraw = np.random.random()
	if randomDraw > 0.5 :
	    max_q_idx = DONT_FINANCE
	else:
	    max_q_idx = FINANCE
	
    return max_q_idx
    
def run_sim(STD):

    #initialize agents
    economic_agent     = {"power":ECON_AGENT_PWR    , "alpha": ECON_AGENT_ALPHA,     "gamma": ECON_AGENT_ALPHA,     "qtable": {}} 
    non_economic_agent = {"power":NON_ECON_AGENT_PWR}
    
    #initialize scientists
    scientists = []  
    for i in range(N_SCIENTISTS ):
        alpha = np.random.uniform(0, 1000)
        beta  = np.random.uniform(0, 1000)
        Ps    = np.random.normal(PA, STD, 1)[0] 
        s     = {"a": alpha, "b": beta, "p": 0.0, "actions": 1, "Ps": Ps}
        scientists.append(s)
        
    believes = []    
        
    #run simulation    
    for i in range(SIM_CYCLES):
        #reset scientist experiment variables
        k = 0.0
        nt = 0.0
        believe_a = 0
        believe_b = 0
        
        #reset power levels for agents when each round starts
        economic_agent["power"]     = ECON_AGENT_PWR
        non_economic_agent["power"] = NON_ECON_AGENT_PWR
        
        if i == 0 or SIM_TYPE == 0:
            for ns, s in enumerate(scientists):   

                Ps = s["Ps"]
                state = "{}".format(ns)
                economic_agent["qtable"][state] = [0.0, 0.0]  
                                
                for n in range(s["actions"]):
                    nt += 1.0
                    if np.random.random() <= Ps:
                        k += 1.0   
        else:
            for ns, s in enumerate(scientists):
                
                Ps = s["Ps"]
                state = "{}".format(ns)                            
                economic_agent_action = choose_action(economic_agent["qtable"], state)
                    
                k_a = 0.0
                if economic_agent_action == FINANCE and economic_agent["power"] > 0:
                    nt += 1.0
                    if np.random.random() <= Ps:
                        k += 1.0
                        k_a = -1.0
                    else:
                        k_a = 1.0                            
                    economic_agent["power"] -= 1
                                                               
                if k_a != 0:                           
                    next_state_max_q = max(economic_agent["qtable"][state])
                    economic_agent["qtable"][state][economic_agent_action] += economic_agent["alpha"]*(k_a+economic_agent["gamma"]*next_state_max_q-economic_agent["qtable"][state][economic_agent_action])                     
                    
                if non_economic_agent["power"] > 0:
                    if np.random.random() > 0.5:
                        non_economic_agent_action = FINANCE
                    else:
                        non_economic_agent_action = DONT_FINANCE
                
                    if non_economic_agent_action == FINANCE:
                        nt += 1.0
                        if np.random.random() <= Ps:
                            k += 1.0  
                        non_economic_agent["power"] -= 1
                                                                                   
        prev_believe_a = believe_a
        prev_believe_b = believe_b 
      
        for s in scientists:
            s["p"] =  int(get_max_beta_dist(s["a"], s["b"], k, nt)*100)
            s["a"] += k
            s["b"] += nt - k           
            if s["p"] > 50:
                believe_a += 1
            else:
                believe_b += 1 
                
        believes.append({"believe_a": 100.0*believe_a/float(N_SCIENTISTS), "believe_b": 100.0*believe_b/float(N_SCIENTISTS)})    
         
    believes = pd.DataFrame(believes)
    
    #for ns, s in enumerate(scientists):
    #    print "{}, {}".format(ns, s)
             
    #print "ECONOMIC_AGENT"   
    #for s in economic_agent["qtable"]:    
    #    print "{} : {}".format(s, economic_agent["qtable"][s]) 
    
    #print "NONE_ECONOMIC_AGENT"    
    #for s in non_economic_agent["qtable"]:    
    #    print "{} : {}".format(s, non_economic_agent["qtable"][s]) 
           
    return believes
                
def main():    
    num_games = NUM_GAMES
    stds = np.arange(0.0,0.2,0.005)
    
    for s in stds:
        ba = 0
        bb = 0
        for i in range(num_games):
            b = run_sim(s)      
            plt.scatter(b.index, b["believe_a"], s=0.1)
            if b["believe_a"].iloc[-1] == 100:
                ba += 1
            if b["believe_b"].iloc[-1] == 100:
                bb += 1
        
        print "STD_DEV {}, A PROBABILITY {}%".format(s, 100*ba/num_games) 
        #plt.title("Random Agent (std=0.2)")
        #plt.ylabel("Agents converged to A (%)")
        #plt.xlabel("Number of cycles")
        #plt.show()
        
        
            
##################################
###           MAIN           ####
##################################

if __name__ == "__main__": main()

