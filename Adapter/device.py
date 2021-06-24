class Device:
    max_voltage = 12

    def __try_charge(self, input_voltage):
        if input_voltage > self.max_voltage:
            print(f"too much voltage warning! your device burned")
        else:
            print("charging")
    
    def charge(self, input_voltage):
        self.__try_charge(input_voltage)