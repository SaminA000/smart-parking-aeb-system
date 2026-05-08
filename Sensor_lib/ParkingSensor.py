class ParkingSensor:
    def __init__(self, sensor_id, location):
        self.sensor_id = sensor_id
        self.location = location
        self.status = False  # False means inactive, True means active
        self.occupied = False  # False means available, True means occupied

    def activate(self):
        if self.status:
            print(f"Sensor {self.sensor_id} at {self.location} is already active.")
            return
        
        self.occupied = True  # Assume the spot is occupied when activating the sensor
        self.status = True
        print(f"Sensor {self.sensor_id} at {self.location} is now active.")

    def deactivate(self):
        if not self.status:
            print(f"Sensor {self.sensor_id} at {self.location} is already inactive.")
            return   
        self.occupied = False  # Reset occupancy status when deactivating
        self.status = False
        print(f"Sensor {self.sensor_id} at {self.location} is now inactive.")
    
    def is_occupied(self, occupied):
        self.occupied = occupied

        if not self.status:
            print(f"Sensor {self.sensor_id} at {self.location} is inactive. Cannot determine occupancy.")
            return
        
        if occupied:
            print(f"Parking spot at {self.location} is {occupied}.")
        else:
            print(f"Parking spot at {self.location} is {occupied}.")
        
        return occupied


