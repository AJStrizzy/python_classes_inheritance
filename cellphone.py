class Phone():
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
        self.charge = 100

    def __str__(self):
        return "{}, {}, {}".format(self.model, self.color, self.year)     


    def ig(self):
        self.charge -= 15
        print('Your instagram addiction has cost you 15 percent of your battery')
        print(f'current battery level is {self.charge}')
    
    def phone_call(self):
        self.charge -= 5
        print('Your phone call has cost you 5 percent of your battery')
        print(f'current battery level is {self.charge}')

    def plug_in(self):
        self.charge = 100   
        print(f"Battery is fully charged to {self.charge}") 

phone1 = Phone('iPhone XS Max', 'Silver', '2018')        

print(phone1)
phone1.ig()
phone1.phone_call()
phone1.plug_in()