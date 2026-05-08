# main.py
from Sensor_lib.ParkingSensor import ParkingSensor 
from Sensor_lib.Proximity import Proximity         
from VehicleInformation.Car import Car             
import time

def run_test_simulation():
    print("--- PARKING SENSOR SYSTEM STARTING ---")
    
    # 1. Initialize our Objects
    # NOTE: Car __init__ expects (make, model, year) based on your Car.py
    my_car = Car("Tesla", "Model 3", 2024) 
    
    # Setting a threshold of 0.5 meters for the safety system
    safety_sensor = Proximity(sensor_id=101, location="Front Bumper", threshold=0.5)
    
    # 2. Power on the hardware
    safety_sensor.activate()
    
    # 3. Simulate Driving
    print(f"\nDriving {my_car.get_car_info()}...")
    my_car.accelerate(15) 
    
    # 4. Simulate the approach to a wall
    # We pass the 'my_car' object so the sensor can modify my_car.mph
    approach_distances = [2.0, 1.2, 0.4, 0.15]
    
    for dist in approach_distances:
        print(f"\n--- Scanning at {dist}m ---")
        
        # This calls your logic in Proximity.py
        safety_sensor.alert(dist, my_car) 
        
        # Check if the car was stopped by the sensor logic
        if my_car.mph == 0:
            print(">>> AEB SYSTEM ACTIVE: The car has been brought to a halt.")
            break
        
        time.sleep(1) # Wait between pings to see the 'beeping' effect

    print("\n--- TEST COMPLETE ---")
    print(f"Final Vehicle Speed: {my_car.mph} MPH")
    print(f"Sensor Occupied Status: {safety_sensor.occupied}")

if __name__ == "__main__":
    run_test_simulation()

print("\nend of function")