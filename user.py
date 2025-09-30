from utils import generate_id, validate_phone, validate_nin, title_case

class User:
    def __init__(self, name, phone, password, nin, location):
        self.id = generate_id()
        self.name = title_case(name)
        self.phone = phone
        self.password = password
        self.nin = nin
        self.location = title_case(location)
