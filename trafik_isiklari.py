import random
import time

class TrafficLight:
    def __init__(self, location):
        self.location = location
        self.state = "RED"
        self.green_time = 30
        self.red_time = 30

    def set_times(self, green_time, red_time):
        self.green_time = green_time
        self.red_time = red_time

    def update_state(self, traffic_density):
        if traffic_density > 70:
            self.green_time = 45
            self.red_time = 15
        elif traffic_density > 30:
            self.green_time = 30
            self.red_time = 30
        else:
            self.green_time = 15
            self.red_time = 45

    def cycle(self):
        self.state = "GREEN"
        print(f"{self.location} traffic light is GREEN for {self.green_time} seconds.")
        time.sleep(self.green_time)
        self.state = "RED"
        print(f"{self.location} traffic light is RED for {self.red_time} seconds.")
        time.sleep(self.red_time)

class TrafficManagementSystem:
    def __init__(self):
        self.traffic_lights = [
            TrafficLight("Intersection 1"),
            TrafficLight("Intersection 2"),
            TrafficLight("Intersection 3")
        ]

    def monitor_traffic(self):
        return random.randint(0, 100)  # trafik yoğunluğu randomize edilir

    def update_lights(self):
        for light in self.traffic_lights:
            traffic_density = self.monitor_traffic()
            light.update_state(traffic_density)
            print(f"Traffic density at {light.location}: {traffic_density}%")
            light.cycle()

class SmartNavigationApp:
    def __init__(self):
        self.traffic_management_system = TrafficManagementSystem()

    def show_traffic(self):
        for light in self.traffic_management_system.traffic_lights:
            traffic_density = self.traffic_management_system.monitor_traffic()
            print(f"Current traffic density at {light.location}: {traffic_density}%")

    def suggest_alternative_route(self):
        traffic_densities = [self.traffic_management_system.monitor_traffic() for _ in range(3)]
        min_density = min(traffic_densities)
        best_route = traffic_densities.index(min_density)
        print(f"Suggesting alternative route through Intersection {best_route + 1} with traffic density {min_density}%")

# Simulate the system
if __name__ == "__main__":
    tms = TrafficManagementSystem()
    app = SmartNavigationApp()

    for _ in range(3):  # farklı durumların oluşması için 3 kez simüle edilir
        print("\nUpdating traffic lights and monitoring traffic...\n")
        tms.update_lights()
        print("\nShowing traffic status in app...\n")
        app.show_traffic()
        print("\nSuggesting alternative routes...\n")
        app.suggest_alternative_route()
        time.sleep(2)
