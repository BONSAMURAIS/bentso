from pyomo.environ import *
from pyomo.solvers.plugins import *
from pyomo.opt import SolverFactory

# LP model
     
def LoadModelData():
    data = DataPortal()
    data.load(filename= 'spot_prices.csv',format='set', set='H')
    data.load(filename= 'spot_prices.csv',index='H',param='ClearingPrice')
    data.load(filename= 'storage_generation.csv',index='H', param='gen_phs')
    data.load(filename= 'scalar.dat')
    
    return data
    
def StorageConsumptionAllocation():
    
    m = AbstractModel()
    # Sets
    m.H = Set() # time

    # Parameters
    m.ClearingPrice= Param(m.H) # get_day_ahead_prices from ENTSOE
    m.gen_phs = Param(m.H)
    m.cap_phs = Param()
    m.storage_hours = Param()
    m.roundtrip_eff = Param()
    m.initial_E_share = Param()

    # Variables
    m.CONSUMPTION_phs = Var(m.H, domain=NonNegativeReals)
    m.ENERGY_LEVEL_phs = Var(m.H, domain=NonNegativeReals)
    # m.cap_phs = Var(domain=NonNegativeReals) # if this code is enable then the parameter must be commented out. When m.cap_phs is variable the capacity is determined.
    
    def expression_max_ngr(m):
        return  m.storage_hours * m.cap_phs
    m.MAX_ENERGY_phs = Expression(rule=expression_max_ngr)
    
    def objective_rule(m):
        return sum(m.CONSUMPTION_phs[h]*m.ClearingPrice[h] for h in m.H)
        
    # verify the data of clearing price to check if the generation ocours at pick prices, in that case set 'sense=minimize'
    m.OBJ = Objective(rule=objective_rule,sense=maximize)
    
    def C1(m,h):
        if h == 0:
            return m.ENERGY_LEVEL_phs[h] == m.initial_E_share*m.MAX_ENERGY_phs + m.CONSUMPTION_phs[h]*(m.roundtrip_eff+1)/2 - m.gen_phs[h]/(m.roundtrip_eff+1)*2
        else:
            return m.ENERGY_LEVEL_phs[h] == m.ENERGY_LEVEL_phs[h-1] + m.CONSUMPTION_phs[h]*(m.roundtrip_eff+1)/2 - m.gen_phs[h]/(m.roundtrip_eff+1)*2
    m.C1 = Constraint(m.H, rule=C1)
    
    def C2(m,h):
        return m.ENERGY_LEVEL_phs[h] <= m.MAX_ENERGY_phs
    m.C2 = Constraint(m.H, rule=C2)
    
    def C3(m,h):
        return m.CONSUMPTION_phs[h] <= m.cap_phs - m.gen_phs[h]
    m.C3 = Constraint(m.H, rule=C3)
    
    return m
