class Phone():
    '''This is a phone class that can be used for inheritance purposes'''

    def __init__(self, phone_number, color):
        self.phone_number = phone_number
        self.color = color

    def __str__(self):
        return f"this phone belongs to {self.phone_number}"    

    def call(self, other_number):
        print(f"calling number: {other_number}") 

    def text(self, other_number, message):
        print(f'{self.phone_number} sent a text message to {other_number}')
        print(f'{message}')

    def open_app(self, app_name):
        print(f'Opening {app_name}')           


class Android(Phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 50

    def __str__(self):
        return f"Android phone that belongs to {self.phone_number}"

    def set_passcode(self, passcode):
        self.passcode = passcode

    def unlock_phone(self, passcode):
        if passcode == self.passcode:
            print('Phone unlocked')   

    def view_battery_life(self):     
        print(f"Battery life: {self.battery}")  

    def charge_phone(self, charge_amount):
        self.battery += charge_amount
        if self.battery > 100:
            self.battery = 100
        print(f'Battery life: {self.battery}')    

frank_phone = Android('888-777-3333', 'black')

frank_phone.view_battery_life()
frank_phone.charge_phone(140)
frank_phone.call('729480123')
frank_phone.open_app('zoom')
frank_phone.text('4834932473', 'Whats up bro?')
