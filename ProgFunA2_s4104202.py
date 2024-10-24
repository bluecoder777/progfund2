from datetime import datetime

class Inputer:
    
    @staticmethod
    def get_valid_positive_int(msg):
        """ Prompts the user to enter an interger not less 1
            Args:
            - msg (str): Prompt to the user
            Returns:
            - int: integer >= 1
        """
        while True:
            try:
                num = __class__.get_input(msg)
                num = int(num)
                if num<1:
                    raise InvalidPositiveInteger("The value should 1 or greater")
                return num
            except ValueError as v:
                print("Enter a valid integer")
            except InvalidPositiveInteger as i:
                print(i.message)
    
    @staticmethod
    def validate_name(full_name):
        """ Validates the names entered, valide names only have alphabets separated by blank spaces
            Args:
            - full_name (str): name to be validated
            Returns:
            - bool: True if it is a valid name False for invalid names
        """

        try:
            # Name must not be empty 
            if not full_name:
                raise InvalidGuest("Name is empty")
            names = full_name.split()
            for name in names:
                if not name.isalpha():
                    raise InvalidGuest("Invalid Name....")
            return True
        except InvalidGuest as e:
            print(e.message)
            return False
    
    @staticmethod
    def get_input(msg):
        """ Wrapper for input() that applies strip() on the input to avoid writing strip all the time
            Args:
            - msg (str): The prompt for the input.

            Returns:
            - str: string with strip() applied
        """
        return input(msg).strip()
    
    @staticmethod
    # Method to get a main menu choice from the user
    def get_choice():
        max_choice = 5
        while True:
            choice = Inputer.get_input("Enter your choice: ")
            try:
                choice = int(choice)
                if choice > max_choice or choice <0:
                    raise ValueError
                return choice
            except ValueError:
                print("Enter a valid choice 0-",max_choice)
    
    @staticmethod
    def get_valid_apartment(msg):
        valid_apartment = False
        while not valid_apartment:
            apartment_id = __class__.get_input(msg)
            #Adjusting the input case to match the U12name format
            if apartment_id: #check to prevent out of bounds access
                apartment_id = apartment_id[0] + apartment_id[1::].lower()
            valid_apartment = __class__.validate_apartment_id(apartment_id)
        return apartment_id
    @staticmethod
    def validate_apartment_id(id):
        """ Validates if the apartment Id is of the format 'U<aparment no><name of the building>
        Args:
        - id (str): Apartment id to be validated

        Returns:
        - bool: True if a valid id False otherwise
        """
        try:
            #Invalid blank id
            if not id:
                raise InvalidApartment("Apartment id can't be blank")
        
            #Id doesn't start with 'U'
            if id[0] != 'U':
                raise InvalidApartment("Aparment id must start with 'U'")
        #Checking for the 'U<unit_num><building_name>' format
            size = len(id)
            unit_num = ""
            for i in range(1,size):
                if id[i].isdigit():
                    unit_num += id[i]
                elif id[i].isalpha():
                    break
                else:
                    raise InvalidApartment("Invalid id")
            #For ids without a unit number
            if not unit_num:
                raise InvalidApartment("Apartment id needs a unit number")
            #The remaining portion should be the building name
            building_name = id[i::]
            #building name is not blank and is either swan, goose, or duck(case sensitive as it  is an id)
            building_name_list = ['swan', 'goose', 'duck']
            if not building_name or not building_name.isalpha() or building_name not in building_name_list:
                raise InvalidApartment("Building name not valid")
            else:
                return True
        except InvalidApartment as e:
            print(e.message)
            return False
    
    @staticmethod
    def get_valid_date(msg):
        """ Prompts the user to enter a date till a valid date is entered
            Args:
            - msg (str): Prompt for the user
            
            Returns:
            - str: The date in <d/m/yyyy> format
        """

        valid_date = False
        while not valid_date:
            date = __class__.get_input(msg)
            valid_date = __class__.validate_date(date)
        return date
    
    @staticmethod
    def validate_date(date):
        """ Check if the date entered is valid.
            Args:
            - date (str): String containing the date to be validated
            
            Returns:
            - bool: True for valid dates False otherwise
        """

        # Empty date string
        if not date:
            print("Invalid date")
            return False
        # Extracting day, month, year
        portions = date.split('/')
        if len(portions) != 3:
            print("Please enter in the d/m/yyyy format")
            return False
        day, month, year = [x.strip() for x in portions]
        
        if not day.isdigit() or not month.isdigit() or not year.isdigit():
            print("day,month,year should be non blank, positive integers")
            return False
        
        #year entered as yy format
        if len(year) != 4:
            print("year should be in yyyy format")
            return False

        day = int(day)
        month = int(month)
        year = int(year)

    # validating year
        if year<0:
            print("Enter a valid year")
            return False
        
        # validating month
        if month <1 or month>12:
            print("Enter a valid month")
            return False
        
        # validating day
        if day <1 or day > 31:
            print("Enter a valid day")
            return False
        # months with max 30 days
        if month in [4,6,9,11] and day ==31:
            print("This month has a maximum of 30 days")
            return False
        #Feb can have max 28 or 29 days
        elif month == 2:
            if  day>29:
                print("Feb has max 29 days")
                return False
            if day == 29:
                if year % 4 == 0:
                    if year % 100 == 0:
                        if year % 400 != 0:
                            print("Year is not a leap year")
                            return False
                else:
                    print("Year is not a leap year")
                    return False
        return True
    
    @staticmethod
    def compare_dates(date1, date2):
        """Functionn to compare if 1 date somes before or after the other
        Args:
        - date1 (str): First date to compare
        - date2 (str): Second date to compare

        Returns:
        - int: 0 if dates are equal, 1 if date2 is after date1, -1 if date 1 is after date2
        """
        day1, month1, year1 = [int(i) for i in date1.split('/')]
        day2, month2, year2 = [int(i) for i in date2.split('/')]

        # Check years then months then days
        if year1 < year2:
            return 1
        elif year1 > year2:
            return -1
        elif month1 < month2:
            return 1
        elif month1 > month2:
            return -1
        elif day1 < day2:
            return 1
        elif day1 > day2:
            return -1
        # Dates are =
        else:
            return 0
        
    @staticmethod
    def get_valid_supplementary_id():
        # Prompt the user to enter supplementary item id till a valid id is given
        is_valid_id = False
        while not is_valid_id:
            id = Inputer.get_input("Enter the supplementary item id: ")
            is_valid_id = __class__.validate_supplementary_id(id)
            if is_valid_id:
                is_valid_id = True
        return id

    @staticmethod    
    def get_date(message):
        while True:
            date_str = Inputer.get_input(message)
            try:
                # Parse the input date string to a datetime object
                date = datetime.strptime(date_str, "%d/%m/%Y")
                return date
            except ValueError:
                print("Invalid date format. Please use dd/mm/yyyy.")
    
    @staticmethod
    def calculate_days_between(checkin_date, checkout_date):
        return (checkout_date.date() - checkin_date.date()).days

    

class Guest:
    
    def __init__(self, ID, name,reward, reward_rate=100, redeem_rate=1):
        if not name.isalpha():
            raise ValueError("Invalid Name")
    
        self.ID= ID
        self.name = name
        self.reward_rate = reward_rate/100
        self.reward = reward
        self.redeem_rate = redeem_rate/100

    # Attribut getter methods
    def get_ID(self):
        return self.ID

    def get_name(self):
        return self.name

    def get_reward_rate(self):
        return self.reward_rate
    
    # Calculate the reward based on cost
    def get_reward(self,total_cost=None):
        if total_cost is None:
            return self.reward
        else:
            reward = round(total_cost * (self.reward_rate/100))
            return reward


    def get_redeem_rate(self):
        return self.redeem_rate

 
    # Method to update the reward
    def update_reward(self, value):# DO: validate the number passed in the call
        self.reward += value

    # Method to display guest information
    def display_info(self):
        print(f"ID: {self.get_ID()}", end=', ')
        print(f"Name: {self.get_name()}", end=', ')
        print(f"Reward Rate: {self.get_redeem_rate() * 100}%", end=', ')
        print(f"Reward: {self.get_reward()}",end=', ')
        print(f"Redeem Rate: {self.get_redeem_rate() * 100}%")

    # Method to set reward rate
    def set_reward_rate(self, new_rate): # DO: validate the number passed in the call
        if new_rate < 0:
            raise ValueError("Reward rate cannot be negative.")
        self.reward_rate = new_rate

    # Method to set redeem rate
    def set_redeem_rate(self, new_rate):# DO: validate the number passed in the call
        if new_rate < 0:
            raise ValueError("Redeem rate cannot be negative.")
        self.redeem_rate = new_rate

class Product:
    def __init__(self, ID, name, price):
        self.ID = ID #type: list[Product]
        self.name = name
        self.price = price


    def get_ID(self):
        return self.ID

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    # Method to display product information
    def display_info(self):
        # Empty super method, can be overridden by subclasses if needed
        pass

class ApartmentUnit(Product):
    def __init__(self, ID, name, price, capacity):
        super().__init__(ID, name, price)  # Use Product constructor
        self.capacity = capacity

    # Getter method for capacity
    def get_capacity(self):
        return self.capacity

    # Method to display apartment unit information
    def display_info(self):
        print(f"Apartment Unit ID: {self.get_ID()}", end=', ')
        print(f"Name: {self.get_name()}", end=', ')
        print(f"Rate per Night: {self.get_price()}", end=', ')
        print(f"Capacity: {self.get_capacity()} guests")

class SupplementaryItem(Product):
    def __init__(self, ID, name, price):
        super().__init__(ID, name, price)  # Use Product constructor



    # Method to display supplementary item information
    def display_info(self):
        print(f"Supplementary Item ID: {self.get_ID()}", end=', ')
        print(f"Name: {self.get_name()}", end=', ')
        print(f"Price: {self.get_price()}")

class Bundle(Product):
    def __init__(self, ID, name, products):
        # Calculate total price with 80% discount
        total_price = 0.8 * sum(product.cost for product in products)
        super().__init__(ID, name, total_price)
        self.products = products  # type: list[OrderItem]

    def display_info(self):
        print(f"{self.ID:<5}",sep='',end='')
        print(f"{self.name:<40}",sep='',end='')
        components =''
        for product in self.products:
            q =''
            if product.quantity >1:
                q = str(product.quantity) + ' x '
            component = q+product.product_id + ','
            components = components + component
        
        # Remove the last ','
        components = components[:-1]
        print(f"{components:<60}",sep='',end='')
        print(f"{self.get_price():<7.2f}",sep='',end='')
        print()

        

class OrderItem:
    def __init__(self, product_id, product_name, quantity, cost):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.cost = cost

class Order:
    def __init__(self,booking_id, guest_name, order_item_list, final_price, reward, booking_date):
        self.booking_id = booking_id
        self.guest = guest_name  # Odering guest
        self.order_item_list = order_item_list #type: list[OrderItem]
        self.final_price = final_price
        self.reward = reward

        self.booking_date = booking_date

    # Method to compute cost, discount, and rewards
    def compute_cost(self):
        # Original total cost
        original_cost = 0.0
        for item in self.order_item_list:
            original_cost += (item.quantity * item.cost)
        
        discount = original_cost - self.final_price

        return original_cost, discount, self.final_price, self.reward

    # Display order information
    def display_order_info(self):
        print(self.guest, end=',', sep='')
        self.display_ordered_products()
        print(self.final_price, self.reward, self.booking_date, sep=',')
    
    def display_ordered_products(self):
        # print appartment info
        for item in self.order_item_list:
            if item.product_id.startswith("U"):
                print(" ", item.quantity, " X ", item.product_id, ",", sep='', end='')
                break
        # print other items
        for item in self.order_item_list:
            if not item.product_id.startswith("U"):
                print(" ", item.quantity, " X ", item.product_id, ",", sep='', end='')
        
class Records:
    def __init__(self):
        self.guests = [] # type: list[Guest]
        self.products = [] # type: list[Product]
        self.orders = [] # type: list[Order]

    def read_guests(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                guest_id = int(data[0].strip())
                name = data[1].strip()
                reward_rate = float(data[2].strip())
                reward = float(data[3].strip())
                redeem_rate = float(data[4].strip())
                guest = Guest(guest_id, name, reward, reward_rate, redeem_rate)
                self.guests.append(guest)

    def read_products(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                product_id = data[0].strip()
                name = data[1].strip()
                if product_id.startswith("B"):
                    items = data[2:-1]
                    items = [p.strip() for p in items]
                    bundle_products = []    #type: list[OrderItem]
                    # Start by adding the appartment to the bundle
                    qty = 0
                    apartment = ''
                    for item in items:
                        if item.startswith("U"):
                            qty += 1
                            apartment = item
                    
                    apartment = self.find_product(apartment)
                    order_item = OrderItem(apartment.get_ID(), apartment.get_name(), qty, apartment.get_price())

                    bundle_products.append(order_item)

                    # Add suplementary items of the bundle
                    for item in items:
                        
                        if item.startswith("SI"):
                            suplement = self.find_product(item)
                            item_in_list = False
                            for product in bundle_products:
                                if suplement.get_ID() == product.product_id:
                                    product.quantity += 1
                                    item_in_list = True
                            if not item_in_list:
                                bundle_products.append(OrderItem(item, suplement.get_name(), 1, suplement.get_price() * 0.8))
                    
                    # Update the total of all bundle items

                    for item in bundle_products:
                        item.cost *= item.quantity
                    product = Bundle(product_id, name, bundle_products)


                elif product_id.startswith('U'):    
                    price = float(data[2].strip())
                    capacity = int(data[3].strip())
                    product = ApartmentUnit(product_id, name, price, capacity)
                    
                else:
                    price = float(data[2].strip())
                    product = SupplementaryItem(product_id, name, price)
                
                self.products.append(product)

    def find_guest(self, search_value):
        for guest in self.guests:
            if guest.get_ID() == search_value or guest.get_name() == search_value:
                return guest
        return None

    def find_product(self, search_value):
        for product in self.products:
            if product.get_ID() == search_value or product.get_name() == search_value:
                return product
        return None

    def list_guests(self):
        for guest in self.guests:
            print(f"ID: {guest.ID}, Name: {guest.name}, Reward Rate: {guest.reward_rate}, Reward: {guest.reward}, Redeem Rate: {guest.redeem_rate}")

    def list_products(self, product_type):
        for product in self.products:
            if product_type == "apartment" and product.capacity is not None:
                product.display
                print(f"ID: {product.product_id}, Name: {product.name}, Rate per Night: {product.price}, Capacity: {product.capacity}") 
            elif product_type != "apartment":
                print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}")

    def list_all_products(self):
        for product in self.products:
            if product.ID.startswith('U') and product.capacity is not None:
                product.display_info
                print(f"ID: {product.ID}, Name: {product.name}, Rate per Night: {product.price}, Capacity: {product.capacity}") 
            else:
                print(f"ID: {product.ID}, Name: {product.name}, Price: {product.price}")

    def find_order(self,booking_id):
        for order in self.orders:
            if order.booking_id == booking_id:
                return order
        return None
    
    def update_order(self, booking_id, new_guest_name=None, new_order_item_list=None, new_final_price=None, new_reward=None):
        """Update an existing order based on booking ID."""
        order = self.find_order(booking_id)
        if order is None:
            print(f"Order with booking ID {booking_id} not found.")
            return
        
        # Update attributes if new values are provided
        if new_guest_name is not None:
            order.guest = new_guest_name
        if new_order_item_list is not None:
            order.order_item_list = new_order_item_list
        if new_final_price is not None:
            order.final_price = new_final_price
        if new_reward is not None:
            order.reward = new_reward



class Operations:

    def __init__(self):
        self.records = Records()
        self.booking_id = 1

    def start_exec(self):
        guest_filename = "guests.csv"
        product_filename = "products.csv"

        self.records.read_guests(guest_filename)
        self.records.read_products(product_filename)


        self.records.list_guests()
        self.records.list_all_products()
        self.show_menu()

    def show_menu(self):
        print("Welcome to Pythonia Bookings")
        choice = -1
        while choice != 0:
            print("="*10)
            print("Please choose from the following options")
            print("1. Make a booking")
            print("2. Display existing guests")
            print("3. Display existing apartment units")
            print("4. Display existing supplementary items")
            print("5. Display existing bundles")
           
            print("0. Exit the program")
            print("="*10)
            
            choice = Inputer.get_choice()

            if choice == 1:
                self.new_booking()
            elif choice == 2:
                self.display_existing_guests()
            elif choice == 3:
                self.display_existing_apartment_units()
            elif choice == 4:
                self.display_existing_supplementary_items()
            elif choice == 5:
                self.display_existing_bundles()
            elif choice == 0:
                print("Exiting the program......")

    def new_booking(self):

        guest_name = self.get_valid_guest_name()
        

        guest = self.records.find_guest(guest_name)

        if guest is not None:
            print("Welcome back, ",guest_name )
    
        guest_num = Inputer.get_valid_positive_int("Number of Guests: ")


        available_apartment = False
        while not available_apartment:
            try:
                apartment_id = Inputer.get_valid_apartment("Apartment Id: ")
                apartment = self.records.find_product(apartment_id)
                

                if apartment is None:
                    raise InvalidApartment("Appartment is not in system")
                else:
                    available_apartment = True
                    # For search by name
                    apartment_id = apartment.get_ID()
                    apartment_price = apartment.get_price()
            except InvalidApartment as e:
                print(e.message)
        try:        
            required_beds = __class__.check_if_extra_beds_required(guest_num,apartment.get_capacity())
            # Abort due to capacity restrictions
            if required_beds == -1:
                raise InvalidApartment("Aborting Transaction")
        except InvalidApartment as e:
            print(e.message)
            return

        #show apartment rate
        print("Cost per night: ", apartment_price)
        
        current_date = datetime.now()
        valid_checkin_date = False
        while not valid_checkin_date:
            try:
                
                    checkin_date = Inputer.get_date("Check-in Date(d/m/yyyy): ")
                    if checkin_date.date()<current_date.date():
                        raise InvalidDate("Check-in/check-out date cannot be earlier than the booking date.")
                    valid_checkin_date =True
            except InvalidDate as e:
                print(e.message)
        
        
        valid_checkout_date = False
        while not valid_checkout_date:
            try:
                
                    checkout_date = Inputer.get_date("Check-out Date(d/m/yyyy): ")
                    if checkout_date.date()<checkin_date.date():
                        raise InvalidDate("Check-out date must be after checkin date.")
                    if checkout_date.date()==checkin_date.date():
                        raise InvalidDate("Checkin and Checkout can't be on the same day")
                    valid_checkout_date = True
            except InvalidDate as e:
                print(e.message)
        
        length_of_stay = Inputer.calculate_days_between(checkin_date, checkout_date)
        
        checkin_date = checkin_date.strftime('%d/%m/%Y').lstrip('0').replace('/0', '/')
        checkout_date = checkout_date.strftime('%d/%m/%Y').lstrip('0').replace('/0', '/')
        
        
        current_date = current_date.strftime("%d/%m/%Y %H:%M")  
        current_date = current_date.lstrip('0').replace('/0', '/') # Format D/M/YYYY h:m
            
        # Add the apparment to the order
        apartment_item_list= []
        apartment_item_list.append(OrderItem(apartment.get_ID(), apartment.get_name(), length_of_stay, apartment_price))

        apartment_total_price = apartment_price * length_of_stay
        self.records.orders.append(Order(self.booking_id, guest_name, apartment_item_list, apartment_total_price, 0,current_date))
        
        cost = apartment_total_price
        add_supplements = 'y'
        while add_supplements !='n':
            add_supplements = Inputer.get_input("Do you want to add suplementary item(y/n): ").lower()
            if 'y' == add_supplements:
                self.book_supplements(apartment)
        
        order = self.records.find_order(self.booking_id)

        bundle_booked = False
        # Validate bundle quantity
        for item in order.order_item_list:
            if item.product_id.startswith('B'):
                if self.check_if_valid_bundle_qty(length_of_stay):
                    bundle_booked =True
                else:
                    print("Bunddle quantity not sufficient...Aborting")
                    self.records.orders.remove(order)
                    return
        
        # Do the breakdown of the bunddled items
        if bundle_booked:
            bundle_qty = 0
            order = self.records.find_order(self.booking_id)

            # Get the total quantity of bundles booked
            for item in  order.order_item_list:
                if item.product_id.startswith('B'):
                    bundle_qty += item.quantity

            # Get the apartment cost
            """If booked no of bunddles is greater than length of stay, then the user is still paying for the extra day
            but the length of stay is the same"""

            for item in order.order_item_list:
                if item.product_id.startswith('U'):
                    apartment_price = 0.8 * apartment_price
                    item.cost = bundle_qty * apartment_price
                    item.quantity = bundle_qty
                    apartment_total_price = item.cost
                    
                    break
            
            # Adjust quantity and final price of suplements
            # Loop throught order to find 'Bundles'
            for item in order.order_item_list:
                if item.product_id.startswith('B'):
                    bundle = self.records.find_product(item.product_id) #type: Bundle
                    # Loop through products in bunddle to add to order
                    for product in bundle.products:
                        if product.product_id.startswith('SI'):
                            # Find the item in the order
                            product_in_order = False
                            for suplement in order.order_item_list:
                                if suplement.product_id == product.product_id:
                                    suplement.quantity += product.quantity
                                    suplement.cost += product.cost
                                    product_in_order = True
                            # Product was not booked separately
                            if not product_in_order:
                                order.order_item_list.append(OrderItem(product.product_id, product.product_name, product.quantity, round(product.cost,2)))

                    # Remove the bundle after merging to the item list
                    order.order_item_list.remove(item)





        #Check if extra beds conditions are met
        if not self.check_if_valid_extra_beds_booked(required_beds, length_of_stay):
            if order is not None:
                # Remove supplements booked in aborted transaction
                self.records.orders.remove(order)
            return
        
        self.check_if_enough_parking(length_of_stay)

        sub_tot = self.booked_supplement_cost(self.booking_id)
        sub_tot = round(sub_tot,2)

        cost += sub_tot

        # Calculate points
        reward = cost
        #Check discounts if user is eligible
        reward_points_used, discount = self.check_discount(guest_name, cost)

        cost -= discount
        
        # Discount max upto $0
        if cost<0:
            cost = 0.0

        # Apply reward rate if applicable
        if guest is not None:
            reward = reward*guest.get_reward_rate()
        
        reward = round(reward)
        self.save_reward(guest_name, reward)
        self.records.update_order(booking_id=self.booking_id, new_final_price=cost, new_reward=reward)
        
        self.display_booking(guest_name= guest_name,
                            guest_num=guest_num,
                            apartment_name=apartment.get_name(),
                            apartment_rate=apartment_price,
                            apartment_total_price=apartment_total_price,
                            checkin_date=checkin_date,
                            checkout_date=checkout_date,
                            length_of_stay=length_of_stay,
                            booking_date=current_date,
                            supplement_total_cost=sub_tot,
                            price_before_discount=cost+discount,
                            redeemed_points= reward_points_used,
                            discount=discount,
                            final_price=cost,
                            reward=reward
                            )
        self.booking_id += 1

    def display_booking(self, guest_name, guest_num, apartment_name, apartment_rate, apartment_total_price, checkin_date, checkout_date, length_of_stay, booking_date, supplement_total_cost, price_before_discount, redeemed_points, discount, final_price, reward):


        print("="*50)

        print("Pythonia Serviced Apartments - Booking Receipt")
        print(f"{'Guest Name:':<20}",guest_name,sep='')
        print(f"{'Number of guests:':<20}",guest_num,sep='')
        print(f"{'Apartment id:':<20}",apartment_name,sep='')
        print(f"{'Apartment rate:$':<20}",f"{apartment_rate:.2f}","AUD",sep='')
        print(f"{'Check-in date:':<20}",checkin_date,sep='')
        print(f"{'Check-out date:':<20}",checkout_date,sep='')
        print(f"{'Length of stay:':<20}",length_of_stay,sep='')
        print(f"{'Booking date:':<20}",booking_date,sep='')
        print(f"{'Sub-total: $'}",f"{apartment_total_price:.2f}",sep='')

        print("-"*50)

        self.display_booked_supplements(supplement_total_cost)

        print(f"{'Total cost:':<20}",f"{price_before_discount:.2f}", sep='')
        print(f"{'Reward points to redeem:':<20}",redeemed_points, sep='')
        print(f"{'Discount based on points:$':<20}",f"{discount:.2f}","AUD", sep='')
        print(f"{'Final total cost: $ ':<20}",f"{final_price:.2f}","AUD", sep='')
        print(f"{'Earned rewards: ':<20}",reward, sep='')

        print("\nThank you for your booking!  \nWe hope you will have an enjoyable stay")
        print("="*50)
    
    def display_booked_supplements(self, supplement_cost):
        """Display the supplements booked in a booking"""

        order = self.records.find_order(self.booking_id)
        if order is not None:
            is_bunddle = False
            for item in order.order_item_list:
                if item.product_id.startswith("B"):
                    is_bunddle = True
            if len(order.order_item_list)<2 and not is_bunddle:
                return
            print("Supplementary items")
            print(f"{'ID':<5}",f"{'Name':<40}",f"{'Quantity':<10}",f"{'Unit Price$':<14}", f"{'Cost$':<7}",sep='')
            for item in order.order_item_list:
                if item.product_id.startswith("B"):
                    print(f"{item.product_id:<5}",
                          f"{item.product_name:<40}",
                          f"{item.quantity:<10}",
                          f"{round(item.cost/item.quantity,2):<14.2f}",
                          f"{round(item.cost,2):<7}",sep='')
                    
            for item in order.order_item_list:
                if not item.product_id.startswith("B") and not item.product_id.startswith("U"):
                    print(f"{item.product_id:<5}",
                          f"{item.product_name:<40}",
                          f"{item.quantity:<10}",
                          f"{round(item.cost/item.quantity):<14.2f}",
                          f"{item.cost:<7.2f}",sep='')
            
            print(f"{'Sub-total: $':<5}", supplement_cost,sep='')
            print("-"*50)

    def display_existing_bundles(self):
        """Displays all the bundles in the system"""
        print(f"{'ID':<5}", sep='', end='')
        print(f"{'Name':<40}", sep='', end='')
        print(f"{'Components':<60}", sep='', end='')
        print(f"{'Price$':<7}", sep='', end='')
        print()
        for product in self.records.products:
            if isinstance(product, Bundle):
                product.display_info()


    def check_if_valid_extra_beds_booked(self, beds_required, length_of_stay):
        """ Checks the number of extra beds booked to see if enough beds are present and if bed are over booked
        Args:
        - booking_id (int): booking for which booked beds is to be validated
        - beds_required (int): minimum no of extra bed required to be a valid booking

        Returns:
        - bool: True if booking meets all criterial False otherwise
        """
        beds_booked = 0

        # Beds are now only for 1 day
        beds_required *= length_of_stay
        order = self.records.find_order(self.booking_id)
        for item in order.order_item_list:
            if item.product_id == "SI6":
                beds_booked += item.quantity
        # If more than 2 beds per day booked, it is invalid
        if beds_booked>2*length_of_stay:
            print("Booked more than 2 extra beds per day. Aborting Transaction")
            return False
        
        # If not enough beds booked
        if beds_booked<beds_required:
            print("Booked extra beds not enough. Aborting Transaction")
            return False
        
        return True
    
    def check_if_enough_parking(self, length_of_stay):
        """Show warning if not enough parking is booked"""
        parking_booked = 0

        order = self.records.find_order(self.booking_id)
        for item in order.order_item_list:
            if item.product_id == "SI1":
                parking_booked += item.quantity

        # If parking is booked but not for the entire stay
        if parking_booked>0 and parking_booked<length_of_stay:
            print("Not enough parking for the entire stay")

        
        return True
    @staticmethod
    def check_if_extra_beds_required(guest_num,capacity):
        """Checks if extra beds are required and warns the user. if capacity is too low cancel booking
        Args:
        - apartment_id (str): apartment of which capacity is to be checked
        - guest_num (str): number of guests in booking
        
        Returns:
        - int: min no of addidtional beds required/ -1 if capacity is too low
        """
        diff = guest_num - capacity
        # Too many people for chosen room
        if diff> 4:
            print("Chosen room can't accomodate all the guests.")
            return -1
        # 2 beds needed if 3/4 people extra
        elif diff>2:
            print("2 Extra beds required per day")
            return 2
        # Atleast 1 bed needed if 1/2 people extra
        elif diff>0:
            print("Atleast 1 extra bed required per day")
            return 1
        # No additional beds req
        else:
            return 0
    
    def check_if_valid_bundle_qty(self, length_of_stay):
        order = self.records.find_order(self.booking_id)
        quantity = 0

        # Iterate every item in order
        for item in order.order_item_list:
            if item.product_id.startswith('B'):
                bundle = self.records.find_product(item.product_id)
                # Every supplement in bundle
                for supplement in bundle.products:
                    # Check for the aparment in the bundle
                    if supplement.product_id.startswith("U"):
                        quantity += supplement.quantity*item.quantity

        if quantity == length_of_stay:
            return True
        elif quantity> length_of_stay:
            print("The bundle quantity is more than the length of stay(you will be charged for the entire bundle)...proceeding with the booking")
            return True
        else:
            return False

    def book_supplements(self, apartment: ApartmentUnit):
        """Peform the booking of supplements for a booking
        Args:
        - booking_id (int): booking_id of the current booking
        = apartment (ApartmentUnit): appartment chosen
        Returns:
        """
        # Check if supplement is in system
        item_found = False
        while not item_found:
            try:
                item = Inputer.get_input("Enter the item id/name: ")
                supplement = self.records.find_product(item)
                if supplement is None:
                    raise InvalidSupplement("Item does not match existing names or ids")
                else:
                    
                    if isinstance(supplement, Bundle):
                        valid_bundle = False
                        for bundle_item in supplement.products:
                            if bundle_item.product_id == apartment.get_ID():
                                item_found = True
                                valid_bundle = True
                                break
                        if not valid_bundle:
                            raise InvalidSupplement("Bundle is not for the chosen apartment")
                        else:
                            item_found = True
                    else:
                        item_found = True
                       
            except InvalidSupplement as e:
                print(e.message)
        
        print("Item: ", supplement.get_name())
        # Show rate of item chosen
        print("Item rate: ", f"{supplement.get_price():.2f}")
        
        qty = Inputer.get_valid_positive_int("Enter the quantity: ")
        cost = qty*supplement.get_price()

    
    #diplay price upto 2 decimal places
        print("The selected item price is ", f"{cost:.2f}")
        
        #Get confirmation to book supplement(y/n)
        valid_confirmation = False
        while not valid_confirmation:
            order_confirmation = Inputer.get_input("Confirm order(y/n): ").lower()
            
            if order_confirmation == 'y':
                booked_item = OrderItem(supplement.get_ID(), supplement.get_name(), qty, cost)
                order = self.records.find_order(self.booking_id)
                # Initial supplement
                # Add the following supplements to the list
                # if an item is booked then we just need to change the quantity not add to list again
                already_booked_supplement = False
                for ordered_item in order.order_item_list:
                    if ordered_item.product_id == booked_item.product_id:
                        already_booked_supplement = True
                        ordered_item.quantity += qty
                        ordered_item.cost += cost
                if not already_booked_supplement:
                    order.order_item_list.append(booked_item)
                print("Suplementary order placed")
                valid_confirmation = True
            elif order_confirmation == 'n':
                print("Suplementary order declined")
                valid_confirmation = True
            else:
                print("Enter a valid confirmation")


    def booked_supplement_cost(self, booking_id):
        """Find the sub total of due to all supplements booked
        Args:
        - booking_id (int): booking for which sub total is calculated
        
        Returns:
        - float: sub-total(total cost of all supplements in booking)
        """
        total_supplement_cost = 0.0
        # Check if supplements were added to the booking
        order = self.records.find_order(booking_id)
        
        if order is not None:
            for item in order.order_item_list:
                if not item.product_id.startswith('U'):
                    total_supplement_cost += item.cost

        return total_supplement_cost
    
    def check_discount(self,guest_name, cost):
        """Checks if a discount can be applied and asks the user if to redeem. redeems if chosen
            Args:
            - guest_name (str): name of the booking guest to check points
            - cost (float): cost of the current booking
            Returns:
            - list: [Points Redeemed, Amount to be discounted]
        """
    
        
        guest = self.records.find_guest(guest_name)
        if guest is not None:
            points = guest.get_reward()
            redeem_rate = guest.get_redeem_rate()
            discount = round(min(redeem_rate*points, cost),2)
            if discount >0:
                print("You are eligible for a discount of $",discount)
                while True:
                    choice = Inputer.get_input("Would you like to redeem?(y/n)").lower()
                    if choice == 'y':
                        print("Redeemed")
                        points_used = discount/guest.get_redeem_rate()
                        if not points_used.is_integer():
                            points_used = int(points_used)+1
                        # Reduce the redeemed points from the user
                        self.save_reward(guest_name,-points_used)
                        return int(points_used), discount
                    elif choice == 'n':
                        print("Points not redeemed")
                        return 0, 0.0
            else:
                return 0, 0.0
        else:
            return 0, 0.0
    def save_reward(self,guest_name, points):
        """This function takes either the number of points to deduct or add(after the rates are applied) and saves it to the records"""
        guest = self.records.find_guest(guest_name) #type: Guest
        if guest is None:
            guest = Guest(len(self.records.guests)+1, guest_name, points)
            self.records.guests.append(guest)
        else:
            guest.reward = guest.get_reward() +  points

    def get_valid_guest_name(self):
        """Gets the guest name based on id or name"""
        valid_input = False
        while not valid_input:
            try:
            
                string = Inputer.get_input("Guest name/id:")
                # Check id
                if string.isdigit():
                    guest = self.records.find_guest(int(string)) 
                    if guest is not None:
                        return guest.get_name()
                    else:
                        raise InvalidGuest("ID not in system")
                else:
                    if Inputer.validate_name(string):
                        return string
            except InvalidGuest as e:
                print(e.message)
    def display_existing_guests(self):
        """Displays all the existing guests' information."""
        print("\nDisplaying All Guests:")
        for guest in self.records.guests:
            print("-" * 40)
            guest.display_info()
        print("-" * 40)
    
    def display_existing_apartment_units(self):
        """Displays all existing apartment units' information."""
        print("\nDisplaying All Apartment Units:")
        for product in self.records.products:
            if isinstance(product, ApartmentUnit):
                print("-" * 40)
                product.display_info()
        print("-" * 40)

    def display_existing_supplementary_items(self):
        """Displays all existing supplementary items' information."""
        print("\nDisplaying All Supplementary Items:")
        for product in self.records.products:
            if isinstance(product, SupplementaryItem):
                print("-" * 40)
                product.display_info()
        print("-" * 40)
    


       
class InvalidGuest(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class InvalidApartment(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class InvalidPositiveInteger(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class InvalidSupplement(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class InvalidDate(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

initializer = Operations()
initializer.start_exec()