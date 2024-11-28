# Definisikan jarak dan penggunaan bahan bakar antara kota-kota
distances_and_fuel = {
    'Bandung': {'Yogyakarta': (485.3, 161.7), 'Semarang': (359.8, 119.9), 'Batu': (704.6, 234.8), 'Solo': (459.3, 153.1), 'Surabaya': (704.0, 234.6)},
    'Yogyakarta': {'Bandung': (485.3, 161.7), 'Semarang': (134.1, 44.7), 'Batu': (326.3, 108.7), 'Solo': (66.8, 22.2), 'Surabaya': (325.6, 108.5)},
    'Semarang': {'Bandung': (359.8, 119.9), 'Yogyakarta': (134.1, 44.7), 'Batu': (351.6, 117.2), 'Solo': (106.3, 35.4), 'Surabaya': (351.0, 117.0)},
    'Batu': {'Bandung': (704.6, 234.8), 'Yogyakarta': (326.3, 108.7), 'Semarang': (351.6, 117.2), 'Solo': (257.9, 85.9), 'Surabaya': (104.3, 34.7)},
    'Solo': {'Bandung': (459.3, 153.1), 'Yogyakarta': (66.8, 22.2), 'Semarang': (106.3, 35.4), 'Batu': (257.9, 85.9), 'Surabaya': (257.3, 85.7)},
    'Surabaya': {'Bandung': (704.0, 234.6), 'Yogyakarta': (325.6, 108.5), 'Semarang': (351.0, 117.0), 'Batu': (104.3, 34.7), 'Solo': (257.3, 85.7)}
}

# Fungsi untuk menghitung total jarak dan bahan bakar untuk suatu rute
def calculate_route(route):
    total_distance = 0
    total_fuel = 0
    for i in range(len(route) - 1):
        city_a = route[i]
        city_b = route[i + 1]
        if city_b in distances_and_fuel[city_a]:
            total_distance += distances_and_fuel[city_a][city_b][0]
            total_fuel += distances_and_fuel[city_a][city_b][1]
    return total_distance, total_fuel

# Fungsi untuk menghasilkan semua kemungkinan rute
def backtrack(current_city, end_city, visited, current_route):
    global best_route, best_cost, best_fuel

    if len(visited) == len(distances_and_fuel):
        if current_city == end_city:
            total_distance, total_fuel = calculate_route_distance_and_fuel(current_route, distances_and_fuel)
            if total_distance < best_cost:
                best_cost = total_distance
                best_fuel = total_fuel
                best_route = list(current_route)
        return

    for next_city in distances_and_fuel[current_city]:
        if next_city not in visited:
            visited.add(next_city)
            current_route.append(next_city)
            backtrack(next_city, end_city, visited, current_route)
            current_route.pop()
            visited.remove(next_city)

#Input kota tujuan
starting_city = input("Masukkan kota awal : ")
ending_city = input("Masukkan kota akhir: ")

# Cek Input
if starting_city not in distances_and_fuel or ending_city not in distances_and_fuel:
    print("Kota tidak valid")
else:
    #variabel untuk menyimpan rute terbaik
    best_route = None
    best_cost = float('inf')
    best_fuel = float('inf')

    # Mulai dari kota awal
    backtrack(starting_city, ending_city, {starting_city}, [starting_city])

     # Menghitung Execution Time
    start_time = time.time()
    end_time = time.time()


    # Print hasil rute terbaik (Kondisi)
    print("Algoritma Backtracking")
    if best_route:
        print("\nKota Awal        :", starting_city)
        print("Kota Tujuan      :", ending_city)
        print(f"Rute Terbaik     : {best_route}")
        print("Total jarak      :", best_cost, "KM")
        print("Total bahan bakar:", best_fuel, "L")
        print(f"Execution time   : {end_time - start_time} seconds")
    else:
        print("\nKota Awal        :", starting_city)
        print("Kota Tujuan      :", ending_city)
        print("Tidak ada rute yang ditemukan.")
        print(f"Execution time   : {end_time - start_time} seconds")