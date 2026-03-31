class Knowledge():
    def __init__(self, upper, lower, current):
        self.upper = upper
        self.lower = lower
        self.current = current
        
        self.history = [current]
        self.predicted = current
        
        self.action = None
        self.log = []

    def __str__(self):
        return (
            f"Internal states:\nUpper Threshold: {self.upper}\nLower Threshold: {self.lower}\nPredicted: {self.predicted}\n\n"
            f"Managed system:\nCurrent Temperature: {self.current}"
        )


class AWARE():
    def __init__(self, knowledge):
        self.k = knowledge

    def Assess(self):
        prev = self.k.current

        while True:
            try:
                temp = int(input("Enter temperature (External Environment): "))
                break
            except:
                print("Invalid input.\n")

        self.k.current = temp
        self.k.history.append(temp)

        if len(self.k.history) >= 2:
            trend = self.k.history[-1] - self.k.history[-2]
            self.k.predicted = self.k.current + trend
        else:
            self.k.predicted = self.k.current

        print(f"\n[Assess] Updated from {prev} -> {temp}")
        print(f"[Assess] Predicted next temp: {self.k.predicted}\n")


    def Weigh(self):
        temp = self.k.current
        pred = self.k.predicted
        upper = self.k.upper
        lower = self.k.lower

        options = []

        if temp > upper or pred > upper:
            options.append("cool")
        if temp < lower or pred < lower:
            options.append("heat")
        if lower <= temp <= upper:
            options.append("idle")

        if "cool" in options:
            action = "cool"
        elif "heat" in options:
            action = "heat"
        else:
            action = "idle"

        self.k.action = action

        print(f"[Weigh] Current: {temp}, Predicted: {pred}")
        print(f"[Weigh] Options considered: {options}")
        print(f"[Weigh] Selected: {action}\n")


    def Act(self):
        action = self.k.action
        before = self.k.current

        if action == "cool":
            print("[Act] Cooling...")
            self.k.current -= 2

        elif action == "heat":
            print("[Act] Heating...")
            self.k.current += 2

        else:
            print("[Act] Idle...")

        print(f"[Act] Temperature: {before} -> {self.k.current}\n")


    def Reflect(self):
        success = self.k.lower <= self.k.current <= self.k.upper

        entry = {
            "temp": self.k.current,
            "action": self.k.action,
            "success": success
        }

        self.k.log.append(entry)

        print(f"[Reflect] Result: {'GOOD' if success else 'BAD'}")
        print(f"[Reflect] Logged: {entry}\n")


    def Enrich(self):
        if len(self.k.log) < 3:
            return

        recent = self.k.log[-3:]
        failures = [e for e in recent if not e["success"]]

        if len(failures) >= 2:
            print("[Enrich] Too many failures -> adjusting thresholds")

            self.k.upper += 1
            self.k.lower -= 1

        print(f"[Enrich] Updated thresholds: ({self.k.lower}, {self.k.upper})\n")


if __name__ == "__main__":
    k = Knowledge(upper=25, lower=20, current=23)
    system = AWARE(k)

    while True:
        print("\n-----------------------------")
        print(k)
        print("-----------------------------\n")

        system.Assess()
        system.Weigh()
        system.Act()
        system.Reflect()
        system.Enrich()