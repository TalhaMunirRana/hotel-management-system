class Hotel():
    """Handles all the aspects of a Hotel."""
    def __init__(self, name):
        """Initialize the parameters"""
        self.name = name
        self.rooms = []
        self.guests = []
        self.reservations = []
    
    def add_room(self):
        """Adds the room in the hotel management"""
        ...

    def register_guest(self):
        """Registers the guest in the hotel's system"""
        ...

    def make_reservation(self):
        """Books the reservation for the guest"""
        ...

    def cancel_reservation(self):
        """Cancels the reservation and make the room available again"""
        ...

    def show_available_rooms(self):
        """Lists all the available rooms in the hotel."""
        ...

    def show_guests(self):
        """Show all the guests with their information reservation"""
        ...

    def find_reservation(self):
        """Find the specific reservation and it's information"""
        ...

class Room():
    """Contains the implementation of room"""
    def __init__(self, room_number, room_type, price, availability, cleanliness, maintenance_status):
        """Initialize the parameters"""
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.availability = availability
        self.cleanliness = cleanliness
        self.maintenance_status = maintenance_status

    def check_availability(self):
        """Checks the rooms availability"""
        ...

    def updated_status(self):
        """Updates the current status of the room"""
        ...

    def mark_clean(self):
        """Marks the room as cleaned"""
        ...

    def mark_dirty(self):
        """Marks the room as dirty."""
        ...

    def put_under_maintainance(self):
        """Change the maintenance status of the room as under maintenance"""
        ...

    def remove_from_maintainance(self):
        """Change the maintenance status of the room as maintained"""
        ...

class Guest():
    """Handles the guest information"""
    def __init__(self, name, phone, guest_id):
        """Initialize the parameters"""
        self.name = name
        self.phone = phone
        self.guest_id = guest_id
        self.reservations = []

    def add_reservation(self):
        """Adds the reservation in reservations"""
        ...

    def cancel_reservation(self):
        """Cancels and removes the reservation from the reservations"""
        ...

    def show_reservations(self):
        """Lists all the reservations of the guest"""
        ...

class Reservation():
    """Handles the reservation details"""
    def __init__(self, guest, room, check_in, check_out, number_of_nights, total_price, status):
        """Initialize the parameters"""
        self.guest = guest
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
        self.number_of_nights = number_of_nights
        self.total_price = total_price
        self.status = status

    def calculate_nights(self):
        """Calculates the number of nights"""
        ...

    def calculate_total_price(self):
        """Calculates the total price"""
        ...

    def cancel(self):
        """Cancels the reservation"""
        ...

    def check_in_guest(self):
        """Checks in the guest"""
        ...

    def check_out_guest(self):
        """Checks out the guest"""
        ...

    def change_room(self):
        """Changes the room of the guest"""
        ...

class Payment():
    """Handles the payment"""

    def __init__(self, payment_id, reservation, amount, payment_date, payment_method, status):
        """Initialize the attributes"""
        self.payment_id = payment_id
        self.reservation = reservation
        self.amount = amount
        self.payment_date = payment_date
        self.payment_method = payment_method
        self.status = status

    def process_payments(self):
        """Processes the payment"""
        ...

    def refund(self):
        """Refunds the payment"""
        ...

    def check_payment_status(self):
        """Checks the payment status"""
        ...