class Knowledge():
    def __init__(self, upper, lower, current):
        self.upper = upper
        self.lower = lower
        self.current = current
        
        self.state = None
        self.action = None
        
    def __str__(self):
        return f"Upper Threshold: {self.upper},\nLower Threshold: {self.lower},\nCurrent Temperature: {self.current}"
    
class MAPE():
    def __init__(self, knowledge):
        self.knowledge = knowledge
    
    def Monitor(self):
        previous_temp = self.knowledge.current
        while True:
            user_input = input("Enter temperature: ")

            try:
                temp = int(user_input)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")

        self.knowledge.current = temp
        print(f"\n[Monitor] Temperature updated from {previous_temp} to {self.knowledge.current}\n")
        
    def Analyze(self):
        temp = self.knowledge.current
        
        if temp > self.knowledge.upper:
            self.knowledge.state = "too_hot"
            print("[Analyze] Temperature is above the upper threshold.\n")
        
        elif temp < self.knowledge.lower:
            self.knowledge.state = "too_cold"
            print("[Analyze] Temperature is below the lower threshold.\n")
            
        else:
            self.knowledge.state = "normal"
            print("[Analyze] Temperature is within the normal range.\n")
            
    def Plan(self):
        if self.knowledge.state == "too_hot":
            self.knowledge.action = "cool"
            print("[Plan] Turn on AC")
            print(f"[Plan] Reduce temperature from {self.knowledge.current} to {self.knowledge.upper}\n")
        
        elif self.knowledge.state == "too_cold":
            self.knowledge.action = "heat"
            
            print("[Plan] Turn on Heater")
            print(f"[Plan] Increase temperature from {self.knowledge.current} to {self.knowledge.lower}\n")
            
        else:
            self.knowledge.action = "Do nothing"
            print("[Plan] Do nothing\n")
    
    def Execute(self):
        if self.knowledge.action == "cool":
            print("[Execute] AC is now ON.")
            self.knowledge.current = self.knowledge.upper
            print(f"[Execute] Temperature is now {self.knowledge.current}\n")
            
        elif self.knowledge.action == "heat":
            print("[Execute] Heater is now ON.")
            self.knowledge.current = self.knowledge.lower
            print(f"[Execute] Temperature is now {self.knowledge.current}\n")
            
        else:
            print("[Execute] System is idle.\n")


if __name__ == "__main__":
    knowledge = Knowledge(
        upper=25,
        lower=20,
        current=23)
    
    system = MAPE(knowledge)
    
    while True:
        print("\n-----------------------------")
        print(knowledge)
        print("-----------------------------\n")
        system.Monitor()
        system.Analyze()
        system.Plan()
        system.Execute()
        
    
    
    
    