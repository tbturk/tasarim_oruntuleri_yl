import random
import time

class SmartMeter:
    def __init__(self, meter_id):
        self.meter_id = meter_id
        self.energy_consumption = 0  # kWh

    def read_energy_consumption(self):
        # simülasyon için rastgele enerji tüketimi değeri üretilir
        self.energy_consumption = random.uniform(0, 10)
        return self.energy_consumption

class EnergyGrid:
    def __init__(self):
        self.total_energy_consumption = 0
        self.sustainable_energy_production = 0  # kWh
        self.meters = [SmartMeter(i) for i in range(10)]  # 10 smart meters

    def update_energy_consumption(self):
        self.total_energy_consumption = sum(meter.read_energy_consumption() for meter in self.meters)
        print(f"Total energy consumption: {self.total_energy_consumption:.2f} kWh")

    def optimize_energy_production(self):
        # anlık tüketime göre optimizasyon gerçekleşir
        # varsayım olarak üretimin yarısı yenilenebilir enerji kabul edilir
        self.sustainable_energy_production = self.total_energy_consumption * 0.5
        print(f"Sustainable energy production: {self.sustainable_energy_production:.2f} kWh")

class DemandManagementSystem:
    def __init__(self, energy_grid):
        self.energy_grid = energy_grid

    def manage_demand(self):
        peak_hours = range(18, 22)  # 6 PM to 10 PM
        current_hour = time.localtime().tm_hour
        if current_hour in peak_hours:
            # pik saat durumu hesaplanır
            reduction_factor = 0.8
            self.energy_grid.total_energy_consumption *= reduction_factor
            print(f"Peak hour detected. Reducing energy consumption by 20%. New consumption: {self.energy_grid.total_energy_consumption:.2f} kWh")
        else:
            print("Non-peak hour. No demand reduction applied.")

if __name__ == "__main__":
    energy_grid = EnergyGrid()
    demand_management = DemandManagementSystem(energy_grid)

    for _ in range(5):  # farklı durumları incelemek için 5 kez simüle edilir
        print("\nUpdating energy consumption and optimizing production...\n")
        energy_grid.update_energy_consumption()
        energy_grid.optimize_energy_production()
        print("\nManaging energy demand...\n")
        demand_management.manage_demand()
        time.sleep(1)  
