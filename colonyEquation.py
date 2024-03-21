#Colony Equation 
''' 
r = (b-d)/n
 P = Pr

 Dn/Dt = rN(1-N/K)
'''
import math



class growth:
  def population_growth(self,N0, r, K, timesteps):
      """
      Simulate population growth using the logistic growth equation.

      Parameters:
          N0 (float): Initial population size.
          r (float): Intrinsic growth rate.
          K (float): Carrying capacity of the environment.
          timesteps (int): Number of time steps for simulation.

      Returns:
          list: List of population sizes over time.
      """
      population = [0] * timesteps
      population[0] = N0

      dt = 1  # time step size (can be adjusted)

      for t in range(1, timesteps):
          dN_dt = r * population[t-1] * (1 - population[t-1] / K)
          population[t] = population[t-1] + dN_dt * dt

      

      for x in range(len(population)):
        population[x] = math.floor(population[x])
        
      #print(population)
      return population




