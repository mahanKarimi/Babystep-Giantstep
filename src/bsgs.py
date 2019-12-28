from src import utils
from math import ceil 

"""
@param base -> the base of the logarithm 
@param x -> the value from the logarithm
@param n ->  mod of the prime residual class group 

"""
def bsgs(base , x , n):
    m = ceil((utils.phi(n)**0.5))
    giant_steps = [] 
    baby_steps = []
    mc = utils.magic_number(base,utils.phi(n),m) 

    for i in range(m): 
        gs = (base**i) % n 
        giant_steps.append(gs)

    for i in range(m):
        bs = (x * (mc)**i) % n 
        baby_steps.append(bs)

    return utils.get_indices(giant_steps,baby_steps)
      

    

