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
    def __init__(self, name, phone, room, reservation):
        """Initialize the parameters"""
        self.name = name
        self.phone = phone
        self.room = room
        self.reservation = reservation

class Reservation():
    """Handles the reservation details"""
    def __init__(self, guest, room):
        """Initialize the parameters"""
        self.guest = guest
        self.room = room