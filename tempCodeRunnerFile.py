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
    return