import math
import random

# 目标函数
def objective_function(x):
    return x ** 2

# 模拟退火算法
def simulated_annealing(initial_solution, initial_temperature, cool_down_rate):
    current_solution = initial_solution
    current_energy = objective_function(current_solution)

    for temperature in range(initial_temperature, 0, -1):
        next_solution = current_solution + random.uniform(-1, 1)
        next_energy = objective_function(next_solution)

        energy_change = next_energy - current_energy
        if energy_change < 0:
            current_solution = next_solution
            current_energy = next_energy
        elif random.random() < math.exp(-energy_change / temperature):
            current_solution = next_solution
            current_energy = next_energy

    return current_solution

# 参数设置
initial_solution = random.uniform(-10, 10)
initial_temperature = 100
cool_down_rate = 0.95

# 调用模拟退火算法进行优化
best_solution = simulated_annealing(initial_solution, initial_temperature, cool_down_rate)
print("最优解：", best_solution)