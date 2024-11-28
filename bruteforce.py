import time
from itertools import permutations

# Dataset
distances_and_fuel = {
    'Bandung': {'Yogyakarta': (485.3, 161.7), 'Semarang': (359.8, 119.9), 'Batu': (704.6, 234.8), 'Solo': (459.3, 153.1), 'Surabaya': (704.0, 234.6)},
    'Yogyakarta': {'Bandung': (485.3, 161.7), 'Semarang': (134.1, 44.7), 'Batu': (326.3, 108.7), 'Solo': (66.8, 22.2), 'Surabaya': (325.6, 108.5)},
    'Semarang': {'Bandung': (359.8, 119.9), 'Yogyakarta': (134.1, 44.7), 'Batu': (351.6, 117.2), 'Solo': (106.3, 35.4), 'Surabaya': (351.0, 117.0)},
    'Batu': {'Bandung': (704.6, 234.8), 'Yogyakarta': (326.3, 108.7), 'Semarang': (351.6, 117.2), 'Solo': (257.9, 85.9), 'Surabaya': (104.3, 34.7)},
    'Solo': {'Bandung': (459.3, 153.1), 'Yogyakarta': (66.8, 22.2), 'Semarang': (106.3, 35.4), 'Batu': (257.9, 85.9), 'Surabaya': (257.3, 85.7)},
    'Surabaya': {'Bandung': (704.0, 234.6), 'Yogyakarta': (325.6, 108.5), 'Semarang': (351.0, 117.0), 'Batu': (104.3, 34.7), 'Solo': (257.3, 85.7)}
}

def calculate_route_distance_and_fuel(route, distances_and_fuel):
    total_distance = 0
    total_fuel = 0
    for i in range(len(route) - 1):
        city_from = route[i]
        city_to = route[i + 1]
        distance, fuel = distances_and_fuel[city_from][city_to]
        total_distance += distance
        total_fuel += fuel
    return total_distance, total_fuel

def bruteforce(start_city, end_city, distances_and_fuel):
    cities = list(distances_and_fuel.keys())
    cities.remove(start_city)
    cities.remove(end_city)
    
    best_route = None
    best_distance = float('inf')
    best_fuel = float('inf')
    
    all_possible_routes = []
    
    for perm in permutations(cities):
        route = [start_city] + list(perm) + [end_city]
        total_distance, total_fuel = calculate_route_distance_and_fuel(route, distances_and_fuel)
        all_possible_routes.append((route, total_distance, total_fuel))
        if total_distance < best_distance or (total_distance == best_distance and total_fuel < best_fuel):
            best_route = route
            best_distance = total_distance
            best_fuel = total_fuel
    
    return all_possible_routes, best_route, best_distance, best_fuel

def main():
    start_city = input("Masukkan kota awal: ")
    end_city = input("Masukkan kota tujuan: ")
    
    all_possible_routes, best_route, best_distance, best_fuel = bruteforce(start_city, end_city, distances_and_fuel)
    
    # Menghitung Execution Time
    start_time = time.time()
    end_time = time.time()

    print("\nSemua kemungkinan rute yang dilalui:")
    for route, distance, fuel in all_possible_routes:
        print(f"Rute: {route}, Total Jarak: {distance} km, Total Bensin: {fuel} liter")

    print("\nRute terbaik:")
    print(f"Rute: {best_route}")
    print("Total Jarak: {best_distance} km")
    print("Total Bensin: {best_fuel} liter")
    print(f"Execution time   : {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
