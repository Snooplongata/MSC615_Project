import numpy as np
import pulp


#matrix = []        
#for k in transportation_costs.keys():
#    v = list(transportation_costs[k].values())
#    row = [0]*(len(df)-len(v))+v
#    matrix.append(row)
#    
#matrix = np.array(matrix)
#matrix = matrix.T

def pulp_example_code():
    # create the LP object, set up as a maximization problem
    prob = pulp.LpProblem('Giapetto', pulp.LpMaximize)
    
    # set up decision variables
    soldiers = pulp.LpVariable('soldiers', lowBound=0, cat='Integer')
    trains = pulp.LpVariable('trains', lowBound=0, cat='Integer')
    
    # model weekly production costs
    raw_material_costs = 10 * soldiers + 9 * trains
    variable_costs = 14 * soldiers + 10 * trains
    
    # model weekly revenues from toy sales
    revenues = 27 * soldiers + 21 * trains
    
    # use weekly profit as the objective function to maximize
    profit = revenues - (raw_material_costs + variable_costs)
    prob += profit  # here's where we actually add it to the obj function
    
    # add constraints for available labor hours
    carpentry_hours = soldiers + trains
    prob += (carpentry_hours <= 80)
    
    finishing_hours = 2*soldiers + trains
    prob += (finishing_hours <= 100)
    
    # add constraint representing demand for soldiers
    prob += (soldiers <= 40)
    
    print(prob)
    
    # solve the LP using the default solver
    optimization_result = prob.solve()
    
    # make sure we got an optimal solution
    assert optimization_result == pulp.LpStatusOptimal
    
    # display the results
    for var in (soldiers, trains):
        print('Optimal weekly number of {} to produce: {:1.0f}'.format(var.name, var.value()))


def test_pulp_hw(sample):
    # create the LP object, set up as a minimization problem
    prob = pulp.LpProblem('Delivery', pulp.LpMinimize)
    
    # set up decision variables
    route1 = pulp.LpVariable('route1', lowBound=0, upBound=1, cat='Integer')
    route2 = pulp.LpVariable('route2', lowBound=0, upBound=1, cat='Integer')
    route3 = pulp.LpVariable('route3', lowBound=0, upBound=1, cat='Integer')
    route4 = pulp.LpVariable('route4', lowBound=0, upBound=1, cat='Integer')
    route5 = pulp.LpVariable('route5', lowBound=0, upBound=1, cat='Integer')
    route6 = pulp.LpVariable('route6', lowBound=0, upBound=1, cat='Integer')
    route7 = pulp.LpVariable('route7', lowBound=0, upBound=1, cat='Integer')
    route8 = pulp.LpVariable('route8', lowBound=0, upBound=1, cat='Integer')
    route9 = pulp.LpVariable('route9', lowBound=0, upBound=1, cat='Integer')
    route10 = pulp.LpVariable('route10', lowBound=0, upBound=1, cat='Integer')
    
    selection = np.array([route1,route2,route3,route4,route5,route6,route7,
                          route8,route9,route10])
    costs = sample[:,0]
    total_cost = sum(costs*selection)
    
    bip = np.zeros((9,len(costs)))
    for j,route in enumerate(sample):
        for stop in route[1:]:
            bip[stop-1,j] = 1
    
    #Objective Function
    prob += total_cost
    
    #Add constraints
    constraint1 = sum(selection)
    prob += (constraint1 == 3)
    contraint2 = sum(bip[0] * selection)
    prob += (contraint2 >= 1)
    contraint3 = sum(bip[1] * selection)
    prob += (contraint3 >= 1)
    contraint4 = sum(bip[2] * selection)
    prob += (contraint4 >= 1)
    contraint5 = sum(bip[3] * selection)
    prob += (contraint5 >= 1)
    contraint6 = sum(bip[4] * selection)
    prob += (contraint6 >= 1)
    contraint7 = sum(bip[5] * selection)
    prob += (contraint7 >= 1)
    contraint8 = sum(bip[6] * selection)
    prob += (contraint8 >= 1)
    contraint9 = sum(bip[7] * selection)
    prob += (contraint9 >= 1)
    contraint10 = sum(bip[8] * selection)
    prob += (contraint10 >= 1)
    
    print(prob)
    
    # solve the LP using the default solver
    optimization_result = prob.solve()
    
    # make sure we got an optimal solution
    assert optimization_result == pulp.LpStatusOptimal
    
    # display the results
    for i,var in enumerate(selection):
        print('{} was chosen: {}'.format(var.name, bool(var.value())))
    
test_pulp_hw(hw)

import pickle

data = {'permutations': perm, 'tc': transportation_costs}

with open('data.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    
with open('data.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    data = pickle.load(f)
