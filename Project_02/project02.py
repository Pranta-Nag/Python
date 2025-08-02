from random import randint

class Train:
    def __init__(self, train_no, name, total_seats, routes):
        self.train_no = train_no
        self.name = name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.routes = routes  # e.g., {"Dhaka-Chittagong": 350, "Dhaka-Sylhet": 250}

    def book_ticket(self, from_station, to_station):
        route = f"{from_station}-{to_station}"
        if self.available_seats > 0:
            if route in self.routes:
                self.available_seats -= 1
                print(f"✅ Ticket booked: {from_station} to {to_station} on Train {self.train_no} - {self.name}")
            else:
                print(f"❌ This train does not go from {from_station} to {to_station}")
        else:
            print("❌ No seats available.")

    def get_status(self):
        print(f"🚆 Train No: {self.train_no}, Name: {self.name}")
        print(f"Seats Available: {self.available_seats}/{self.total_seats}")

    def get_fare(self, from_station, to_station):
        route = f"{from_station}-{to_station}"
        fare = self.routes.get(route)
        if fare:
            print(f"💰 Fare from {from_station} to {to_station} is ৳{fare}")
        else:
            print(f"❌ Fare not found for route: {route}")


# Sample Usage
routes = {
    "Dhaka-Chittagong": 350,
    "Dhaka-Sylhet": 250,
    "Chittagong-Cox's Bazar": 200
}

train = Train(3566, "Sonar Bangla Express", 5, routes)

train.book_ticket("Dhaka", "Chittagong")
train.get_status()
train.get_fare("Dhaka", "Chittagong")
