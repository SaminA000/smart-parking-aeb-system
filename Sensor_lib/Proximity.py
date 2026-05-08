from Sensor_lib.ParkingSensor import ParkingSensor
# from Sensor_lib.ParkingSensor import Car

class Proximity(ParkingSensor):
    def __init__(self, sensor_id, location, threshold):
        super().__init__(sensor_id, location)
        self.threshold = threshold
        self.last_reading = 0.0 # Initialize this so 'get' doesn't crash


    def alert(self, distance, car):
        if not self.status:
            print(f"Sensor {self.sensor_id} at {self.location} is inactive. Cannot alert.")
            return
        
        if distance < 0.2:
            print (f"ALERT: Object very close! {distance}m detected. BEEEP \a")
            car.mph = 0  # Assume the car should stop immediately
            self.occupied = True  # Mark the spot as occupied when an object is very close
            return
        elif distance < 0.5:
            print (f"Warning: Object nearby! {distance}m detected.beep beep \a")
            delay = 0.1  # Shorter delay for closer objects
        elif distance < 1.5:
            print (f"Caution: Object detected at {distance}m. Beep \a")
            delay = 0.5  # Longer delay for farther objects
        else:
            print (f"Clear: No object closeby.")

        print(f"Current proximity reading: {distance}m")


    def check_proximity(self, curr_proximity):
        if not self.status:
            print("Error: Sensor power is OFF.")
            return None

        self.last_reading = curr_proximity # Store the reading
        
        if curr_proximity < self.threshold:
            print(f"Object detected! {curr_proximity}m is within {self.threshold}m limit.")
            return True
        else:
            print(f"Clear: {curr_proximity}m is safe.")
            return False
    
    def get_last_reading(self):
        return self.last_reading
    
    def get_threshold(self):
        return self.threshold
    def set_threshold(self, new_threshold):
        self.threshold = new_threshold
        print(f"Threshold updated to {self.threshold}m.")