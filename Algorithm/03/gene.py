import random

# 适应度函数
def fitness_function(solution, square_sizes, container_size):
    container_width, container_height = container_size
    total_width, total_height = 0, 0

    for i, selected in enumerate(solution):
        if selected:
            width, height = square_sizes[i]
            if total_width + width <= container_width:
                total_width += width
                total_height = max(total_height, height)
            else:
                total_height += height
                total_width = width

    return total_width * total_height

# 遗传算法
def genetic_algorithm(population_size, chromosome_length, generations, square_sizes, container_size):
    population = [[random.randint(0, 1) for _ in range(chromosome_length)] for _ in range(population_size)]

    for _ in range(generations):
        offspring = []
        for _ in range(population_size):
            parent1, parent2 = random.sample(population, 2)
            crossover_point = random.randint(1, chromosome_length - 1)
            child = parent1[:crossover_point] + parent2[crossover_point:]
            offspring.append(child)

        population = offspring
        for solution in population:
            for i in range(chromosome_length):
                if random.random() < mutation_probability:
                    solution[i] = 1 if solution[i] == 0 else 0

    best_solution = max(population, key=lambda x: fitness_function(x, square_sizes, container_size))
    return best_solution

# 参数设置
population_size = 100
chromosome_length = 5
generations = 50
mutation_probability = 0.01

# 方形件和容器尺寸
square_sizes = [(1, 2), (2, 3), (2, 4), (3, 5), (1, 3)]
container_size = (5, 10)

import matplotlib.pyplot as plt

def visualize_solution(solution, square_sizes, container_size):
    container_width, container_height = container_size

    # 绘制容器边界
    plt.plot([0, container_width, container_width, 0, 0], [0, 0, container_height, container_height, 0], 'b-')

    # 绘制方形件（仅绘制最优解）
    x_coords = []
    y_coords = []
    for i, selected in enumerate(solution):
        if selected:
            width, height = square_sizes[i]
            x = sum(square_sizes[j][0] for j in range(i) if solution[j])
            y = sum(square_sizes[j][1] for j in range(i) if solution[j])
            plt.plot([x, x, x + width, x + width, x], [y, y + height, y + height, y, y], 'r-')
            x_coords.append(x)
            y_coords.append(y)

    plt.axis('equal')
    plt.show()

# 使用前面遗传算法得到的最优解进行可视化
best_solution = genetic_algorithm(population_size, chromosome_length, generations, square_sizes, container_size)
visualize_solution(best_solution, square_sizes, container_size)