class Knowledge():
    def __init__(self, upper, lower, current):
        self.upper = upper
        self.lower = lower
        self.current = current
        
        self.state = None
        self.action = None
        self.log = []
        
    def __str__(self):
        return f"Upper Threshold: {self.upper},\nLower Threshold: {self.lower},\nCurrent Temperature: {self.current}"
    
class AWARE():
    def __init__(self, knowledge):
        self.knowledge = knowledge
    
    def Assess(self):
        previous_temp = self.knowledge.current
        while True:
            user_input = input("Enter temperature: ")
            try:
                temp = int(user_input)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")

        self.knowledge.current = temp
        print(f"[Assess] Temperature updated from {previous_temp} to {self.knowledge.current}\n")
        
    def Weigh(self):
        temp = self.knowledge.current
        upper = self.knowledge.upper
        lower = self.knowledge.lower

        if temp > upper:
            options = ["cool"]
        elif temp < lower:
            options = ["heat"]
        else:
            options = ["idle"]

        self.knowledge.action = options[0]

        print(f"[Weigh] Current temperature: {temp}")
        print(f"[Weigh] Valid options: {options}")
        print(f"[Weigh] Selected action: {self.knowledge.action}\n")
        
    def Act(self):
        action = self.knowledge.action
        
        if action == "cool":
            print("[Act] AC is now ON.")
            self.knowledge.current = self.knowledge.upper
            print(f"[Act] Temperature is now {self.knowledge.current}\n")
        
        elif action == "heat":
            print("[Act] Heater is now ON.")
            self.knowledge.current = self.knowledge.lower
            print(f"[Act] Temperature is now {self.knowledge.current}\n")
            
        else:
            print("[Act] System is idle.\n")
    
    def Reflect(self):
        log_entry = {
            "temperature": self.knowledge.current,
            "action": self.knowledge.action
        }
        self.knowledge.log.append(log_entry)
        print(f"[Reflect] Action logged: {log_entry}\n")
        
    def Enrich(self):
        print("[Enrich] Current knowledge log:")
        for i, entry in enumerate(self.knowledge.log, 1):
            print(f"  {i}. Temperature: {entry['temperature']}, Action: {entry['action']}")
        print()
        

if __name__ == "__main__":
    knowledge = Knowledge(upper=25, lower=20, current=23)
    
    knowledge.log.append({
        "temperature": knowledge.current,
        "action": "idle"
    })
    
    system = AWARE(knowledge)
    while True:
        print("\n-----------------------------")
        print(system.knowledge)
        print("-----------------------------\n")

        system.Assess()
        system.Weigh()
        system.Act()
        system.Reflect()
        system.Enrich()