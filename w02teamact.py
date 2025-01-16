import math

can_list = [
    ['#1 Picnic', 6.83, 10.16, 0.28],
    ['#1 Tall', 7.78, 11.91, 0.43],
    ['#2', 8.73, 11.59, 0.45],
    ['#2.5', 10.32, 11.91, 0.61],
    ['#3 Cylinder', 10.79, 17.78, 0.86],
    ['#5', 13.02, 14.29, 0.83],
    ['#6Z', 5.40, 8.89, 0.22],
    ['#8Z short', 6.83, 7.62, 0.26],
    ['#10', 15.72, 17.78, 1.53],
    ['#211', 6.83, 12.38, 0.34],
    ['#300', 7.62, 11.27, 0.38],
    ['#303', 8.10, 11.11, 0.42]
]

# best_cost_efficiency = 99999
# best_storage_efficiency = 0
# best_cost_index = -1

def main():
    for [name, radius, height, cost] in enumerate(can_list):
        volume = compute_volume(radius, height)
        surface_area= compute_surface_area(radius, height)
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        cost_efficiency = compute_cost_efficiency(volume, cost)
        print(f"{name}: Storage Efficiency = {storage_efficiency:.2f} Cost Efficiency = {cost_efficiency:.2f}")

        # if best_cost_efficiency > cost_efficiency:
        #     best_cost_efficiency = cost_efficiency
        #     best_cost_index = index

    # print(best_cost_index)

        #print(f"Cost Efficiency = {cost_efficiency:.2f}")
        
        # Volume - pi x radius^2 x height
        # surface area - 2pi x radius x (radius + height)
        # storage efficiency - Volume/Surface Area

# function
def compute_volume(radius, height):
    return math.pi * radius ** 2 * height

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

# function
def compute_storage_efficiency(volume, surface_area):
    return volume / surface_area

def compute_cost_efficiency(volume, cost): #Cost Efficiency = Volume/Cost
    return volume / cost
main()