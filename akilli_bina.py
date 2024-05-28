import random
import time

class SmartBuildingSystem:
    def __init__(self):
        self.temperature = 22.0  # default olarak sıcaklık belirlenir
        self.light_level = 300  # default olarak aydınlanma miktarı belirlenir (lumen)
        self.occupancy = False

    def adjust_hvac(self):
        # belirlenen sıcaklık aralığında düzenlemeler yapılır
        desired_temp = 22.0
        if self.temperature < desired_temp - 1:
            self.temperature += 1  # sıcaklık arttırımı
            action = "Heating"
        elif self.temperature > desired_temp + 1:
            self.temperature -= 1  # sıcaklık düşürülür
            action = "Cooling"
        else:
            action = "Stable"
        print(f"HVAC system action: {action}, Current temperature: {self.temperature:.1f}°C")

    def adjust_lighting(self):
        # belirlenen düzeyde aydınlatma ayarlanır
        desired_light_level = 300
        if self.occupancy:
            if self.light_level < desired_light_level:
                self.light_level += 50  
                action = "Increasing light level"
            elif self.light_level > desired_light_level:
                self.light_level -= 50  
                action = "Decreasing light level"
            else:
                action = "Lighting stable"
        else:
            self.light_level = 0  
            action = "Lights off (no occupancy)"
        print(f"Lighting system action: {action}, Current light level: {self.light_level} lumens")

    def read_occupancy(self):
       
        self.occupancy = random.choice([True, False])
        print(f"Occupancy detected: {self.occupancy}")

    def get_feedback(self):
        # kullanıcı feedback durumu alınır
        feedback_options = ["Comfortable", "Too Cold", "Too Hot", "Too Bright", "Too Dim"]
        feedback = random.choice(feedback_options)
        print(f"User feedback: {feedback}")
        return feedback

    def adjust_systems_based_on_feedback(self, feedback):
        # feedback durumuna göre düzenlemeler yapılır
        if feedback == "Too Cold":
            self.temperature += 1
            print("Adjusting temperature: Increasing by 1°C")
        elif feedback == "Too Hot":
            self.temperature -= 1
            print("Adjusting temperature: Decreasing by 1°C")
        elif feedback == "Too Bright":
            self.light_level -= 50
            print("Adjusting lighting: Decreasing light level by 50 lumens")
        elif feedback == "Too Dim":
            self.light_level += 50
            print("Adjusting lighting: Increasing light level by 50 lumens")

if __name__ == "__main__":
    smart_building = SmartBuildingSystem()

    for _ in range(5):  # farklı durumlar incelenebilmesi için 5 kez simüle edilir
        print("\nAdjusting systems...\n")
        smart_building.read_occupancy()
        smart_building.adjust_hvac()
        smart_building.adjust_lighting()
        print("\nGetting user feedback...\n")
        feedback = smart_building.get_feedback()
        print("\nAdjusting systems based on feedback...\n")
        smart_building.adjust_systems_based_on_feedback(feedback)
        time.sleep(2)  
