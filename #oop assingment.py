# Step 1–3: Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def describe(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery}mAh battery."

    def make_call(self, number):
        return f"Calling {number} from {self.model}."


# Step 4: Inherited class
class iPhone(Smartphone):
    def __init__(self, model, storage, battery, ios_version):
        super().__init__("Apple", model, storage, battery)
        self.ios_version = ios_version

    def describe(self):  # Polymorphism: method override
        return f"{self.brand} {self.model} running iOS {self.ios_version}, {self.storage}GB, {self.battery}mAh."


# Example usage
phone1 = Smartphone("vivo", "y19s", 128, 4000)
iphone1 = iPhone("iPhone 15 pro", 256, 4200, "iOS 17")

print(phone1.describe())
print(phone1.make_call("0796693977"))

print(iphone1.describe())
print(iphone1.make_call("0707180016"))
