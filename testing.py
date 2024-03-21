import colonyEquation

instance = colonyEquation.growth()


N0 = 100
r = 0.1
K = 10000
timesteps = 100

print(instance.population_growth(N0, r, K, timesteps))