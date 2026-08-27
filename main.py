class Hotel():
    """Handles all the aspects of a Hotel."""
    def __init__(self, name):
        """Initialize the parameters"""
        self.name = name
        self.rooms = []
        self.guests = []


class Room():
    """Contains the implementation of room"""
    def __init__(self, room_number, guest):
        """Initialize the parameters"""
        self.room_number = room_number
        self.guest = guest

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

class Payment():
    """Handles the payment processng"""
    def __init__(self, reservation, guest, room):
        """Initialize the parameters"""
        self.reservation = reservation
        self.guest = guest
        self.room = room
