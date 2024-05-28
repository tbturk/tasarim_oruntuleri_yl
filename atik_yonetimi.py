import random
import time

class SmartTrashBin:
    def __init__(self, bin_id):
        self.bin_id = bin_id
        self.capacity = 100  # Default değerler belirlendi
        self.fill_level = 0  

    def update_fill_level(self):
        # atık kutularının doldurulması simüle ediliyor..
        self.fill_level = random.uniform(0, self.capacity)
        print(f"Trash Bin {self.bin_id} fill level: {self.fill_level:.1f} liters")

    def is_full(self):
        # doluluk oranı eşik değer ile kontrol ediliyor
        return self.fill_level >= 0.8 * self.capacity

class RecyclingStation:
    def __init__(self):
        self.materials = {"plastic": 0, "glass": 0, "metal": 0, "paper": 0}

    def classify_and_process_waste(self, waste):
        # atık sınıflandırma işlemi..
        material_type = random.choice(list(self.materials.keys()))
        amount = random.uniform(1, 10)  
        self.materials[material_type] += amount
        print(f"Classified {amount:.1f} kg of {material_type} waste. Total {material_type} recycled: {self.materials[material_type]:.1f} kg")

class WasteManagementSystem:
    def __init__(self):
        self.trash_bins = [SmartTrashBin(i) for i in range(5)]  
        self.recycling_station = RecyclingStation()

    def check_trash_bins(self):
        for bin in self.trash_bins:
            bin.update_fill_level()
            if bin.is_full():
                self.collect_and_recycle_waste(bin)

    def collect_and_recycle_waste(self, bin):
        # atık toplama ve geri dönüşüm işlemi..
        print(f"Collecting waste from Trash Bin {bin.bin_id}")
        waste_amount = bin.fill_level
        bin.fill_level = 0  

        self.recycling_station.classify_and_process_waste(waste_amount)

if __name__ == "__main__":
    waste_management_system = WasteManagementSystem()

    for _ in range(5):  #simülasyon 5 kez tekrarlanacaktır
        print("\nChecking trash bins...\n")
        waste_management_system.check_trash_bins()
        time.sleep(2)  
