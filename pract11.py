"""
Exercise one:
The user should be able to set the hard drive capacity of a laptop in addition to its RAM. 
The options for a laptop's hard drive are as follows:
a. 256 GB comes on default on all laptops and is free
b. 512 GB for £30
c. 1024 GB for £100
Begin by creating an instance variable ssd for the Laptop class.
Then write the accessor and mutator methods for this variable. Next, 
update the __str__ method of the Laptop class to include the value of ssd in the returned string. 
Finally, update the hard drive capacity of the laptop in the testLaptop function and see whether the new value is displayed.
"""

class Laptop:
    ramOptions = {4: 0, 8: 50, 16: 100, 32: 200}

    # Hard drive capacity options and prices
    ssdOptions = {"256GB": 0, "512GB": 30, "1024GB": 100}

    def __init__(self, brand, basePrice):
        self.brand = brand
        self.basePrice = basePrice
        self.ram = 4
        self.ssd = "256GB"  # Default hard drive capacity

    def getBrand(self):
        return self.brand

    def getRam(self):
        return self.ram

    def getSSD(self):
        return self.ssd

    def getPrice(self):
        ramPrice = self.ramOptions[self.ram]
        ssdPrice = self.ssdOptions[self.ssd]
        return self.basePrice + ramPrice + ssdPrice

    def setRam(self, ram):
        if ram in self.ramOptions:
            self.ram = ram

    def setSSD(self, ssd):
        if ssd in self.ssdOptions:
            self.ssd = ssd

    def __str__(self):
        output = f"{self.brand} Laptop with {self.ram} GB RAM and {self.ssd} SSD "
        output += f"priced at £{self.getPrice()}"
        return output


class ShoppingCart:

    def __init__(self):
        self.laptops = []
        self.total = 0

    def addLaptop(self, laptop):
        self.laptops.append(laptop)
        self.total += laptop.getPrice()

    def getLaptops(self):
        return self.laptops

    def getTotal(self):
        return self.total

    def __str__(self):
        output = "Shopping cart contains:\n"
        for laptop in self.laptops:
            output += f"{laptop}\n"
        output += f"Total price is £{self.total}"
        return output

class GamingLaptop(Laptop):

    gpuOptions = {
        "NVIDIA GTX 1650": 0,
        "NVIDIA RTX 3070": 250,
        "NVIDIA RTX 4080": 350,
        "AMD RX 6800M": 280
    }

    def __init__(self, brand, basePrice):
        super().__init__(brand, basePrice)
        self.gpu = "NVIDIA GTX 1650"

    def getGpu(self):
        return self.gpu

    def setGpu(self, gpu):
        if gpu in self.gpuOptions:
            self.gpu = gpu

    def getPrice(self):
        gpuPrice = self.gpuOptions[self.gpu]
        return super().getPrice() + gpuPrice

    def __str__(self):
        output = f"{self.brand} Laptop with {self.ram} GB RAM "
        output += f"and {self.gpu} priced at £{self.getPrice()}"
        return output

def testLaptop():
    laptop = Laptop("Dell", 999.99)
    print("laptop's brand is", laptop.getBrand())
    print("laptop's RAM is", laptop.getRam())
    print("laptop's SSD is", laptop.getSSD())
    print("laptop's price is", laptop.getPrice())  # 999.99

    laptop.setRam(32)
    print("laptop's RAM is now", laptop.getRam())
    laptop.setRam(30)
    print("laptop's RAM is still", laptop.getRam())

    laptop.setSSD("512GB")  # Test changing the hard drive capacity
    print("laptop's SSD is now", laptop.getSSD())

    print("laptop's price is now", laptop.getPrice())  # Updated price with new SSD option


def testShoppingCart():
    cart = ShoppingCart()
    dellLaptop = Laptop("Dell", 999.99)
    appleLaptop = Laptop("Apple", 1349.00)
    msiLaptop = GamingLaptop("MSI", 1599.00)
    msiLaptop.setRam(16)
    msiLaptop.setGpu("AMD RX 6800M0")
    cart.addLaptop(dellLaptop)
    cart.addLaptop(appleLaptop)
    cart.addLaptop(msiLaptop)

    print("Shopping cart contains:")
    for laptop in cart.getLaptops():
        print(laptop)
    print(f"Total price is £{cart.getTotal()}")

    print(cart)


def testGamingLaptop():
    gamingLaptop = GamingLaptop("Razer", 2399.99)
    print("Gaming laptop's brand is", gamingLaptop.getBrand())
    print("Gaming laptop's price is", gamingLaptop.getPrice())
    print("Gaming laptop's ram is", gamingLaptop.getRam())
    print("Gaming laptop's GPU is", gamingLaptop.getGpu())

    gamingLaptop.setGpu("NVIDIA RTX 3070")
    print("Gaming laptop's GPU is now", gamingLaptop.getGpu())
    print("Gaming laptop's price is now", gamingLaptop.getPrice())

    print(gamingLaptop)
if __name__ == "__main__":
    #testLaptop()
    #testShoppingCart()
    testGamingLaptop()


"""
Exercise two:
Download the lect11.py file from the lecture and familiarise yourself with it. 
Notice that we cannot make any modifications to the pizzas in an Order object. 
Add method(s) to the Order class to allow the user to update the size and the toppings of specific pizzas within an order. 
Make sure to test this functionality in the test function.
"""

class Pizza:
    pizzaPrices = {"small": 8, "medium": 10, "large": 12}

    def __init__(self, size):
        self.toppings = set()
        self.size = "small"
        if size.lower() in self.pizzaPrices:
            self.size = size.lower()

    def addTopping(self, topping):
        self.toppings.add(topping.lower())

    def removeTopping(self, topping):
        self.toppings.remove(topping.lower())

    def setSize(self, newSize):
        if newSize.lower() in self.pizzaPrices:
            self.size = newSize.lower()

    def updateSize(self, newSize):
        self.setSize(newSize)

    def updateToppings(self, newToppings):
        self.toppings = set(newToppings)

    def getSize(self):
        return self.size

    def getPrice(self):
        return self.pizzaPrices[self.size]

    def getToppings(self):
        return self.toppings

    def __str__(self):
        output = f"{self.size} pizza with:"
        for topping in self.toppings:
            output += f"\n- {topping}"
        output += f"\nPrice: £{self.getPrice()}\n"
        return output

class Order:

    def __init__(self):
        self.pizzas = []

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getTotalPrice(self):
        totalPrice = 0
        for pizza in self.pizzas:
            totalPrice += pizza.getPrice()
        return totalPrice

    def __str__(self):
        output = "Your order contains:\n"
        for pizza in self.pizzas:
            output += str(pizza)
        output += f"Total: £{self.getTotalPrice()}"
        return output


class StuffedCrustPizza(Pizza):
    
    crustTypes = ("cheese", "garlic", "hot dog")

    def __init__(self, size, crust):
        super().__init__(size)
        self.crust = "cheese"
        if crust.lower() in self.crustTypes:
            self.crust = crust.lower()

    def getCrust(self):
        return self.crust

    def setCrust(self, newCrust):
        if newCrust in self.crustTypes:
            self.crust = newCrust

    def getPrice(self):
        return super().getPrice() + 2

    def __str__(self):
        output = f"A {self.size} stuffed crust pizza with:"
        for topping in self.toppings:
            output += f"\n- {topping}"
        output += f"\nCrust type: {self.crust}"
        output += f"\nPrice: £{self.getPrice()}\n"
        return output
    
    def updatePizzaSize(self, pizzaIndex, newSize):
        if 0 <= pizzaIndex < len(self.pizzas):
            self.pizzas[pizzaIndex].setSize(newSize)

    def updatePizzaToppings(self, pizzaIndex, newToppings):
        if 0 <= pizzaIndex < len(self.pizzas):
            pizza = self.pizzas[pizzaIndex]
            pizza.toppings = set(newToppings)

def test():
    myOrder = Order()
    pizza1 = Pizza("small")
    pizza1.addTopping("Pepperoni")
    pizza1.addTopping("Jalapenos")
    pizza1.setSize("large")

    pizza2 = StuffedCrustPizza("Medium", "Cheese")
    pizza2.addTopping("Ham")
    pizza2.addTopping("Mushrooms")
    pizza2.setCrust("Garlic")

    myOrder.addPizza(pizza1)
    myOrder.addPizza(pizza2)

    print("Original Order:")
    print(myOrder)

    # Update size and toppings of specific pizzas
    myOrder.pizzas[0].updateSize("medium")
    myOrder.pizzas[1].updateToppings(["Olives", "Onions"])

    print("\nUpdated Order:")
    print(myOrder)

if __name__ == "__main__":
    test()

"""
Exercise three:
In your lect11.py file, implement a new method in the Order class,
that lets the user upgrade a standard pizza to a stuffed crust pizza.
Try not to ask the user to provide the toppings or the size for the stuffed crust pizza. 

Hint: Python has a built-in isinstance function that you may use for this function. 
It lets you check whether a given object is an instance of (or a subclass of) a provided class.
"""

class Pizza:
    pizzaPrices = {"small": 8, "medium": 10, "large": 12}

    def __init__(self, size):
        self.toppings = set()
        self.size = "small"
        if size.lower() in self.pizzaPrices:
            self.size = size.lower()

    def addTopping(self, topping):
        self.toppings.add(topping.lower())

    def removeTopping(self, topping):
        self.toppings.remove(topping.lower())

    def setSize(self, newSize):
        if newSize.lower() in self.pizzaPrices:
            self.size = newSize.lower()

    def updateSize(self, newSize):
        self.setSize(newSize)

    def updateToppings(self, newToppings):
        self.toppings = set(newToppings)

    def getSize(self):
        return self.size

    def getPrice(self):
        return self.pizzaPrices[self.size]

    def getToppings(self):
        return self.toppings

    def __str__(self):
        output = f"{self.size} pizza with:"
        for topping in self.toppings:
            output += f"\n- {topping}"
        output += f"\nPrice: £{self.getPrice()}\n"
        return output

class Order:
    def __init__(self):
        self.pizzas = []

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getTotalPrice(self):
        totalPrice = 0
        for pizza in self.pizzas:
            totalPrice += pizza.getPrice()
        return totalPrice

    def __str__(self):
        output = "Your order contains:\n"
        for pizza in self.pizzas:
            output += str(pizza)
        output += f"Total: £{self.getTotalPrice()}"
        return output
    
    def upgradeToStuffedCrust(self, pizzaIndex):
        if 0 <= pizzaIndex < len(self.pizzas):
            standardPizza = self.pizzas[pizzaIndex]

            # Check if the pizza is a standard pizza (not already stuffed crust)
            if not isinstance(standardPizza, StuffedCrustPizza):
                # Replace the standard pizza with a stuffed crust pizza
                stuffedCrustPizza = StuffedCrustPizza(standardPizza.getSize(), "cheese")
                stuffedCrustPizza.toppings = standardPizza.toppings  # Copy toppings
                self.pizzas[pizzaIndex] = stuffedCrustPizza
class StuffedCrustPizza(Pizza):
    
    crustTypes = ("cheese", "garlic", "hot dog")

    def __init__(self, size, crust):
        super().__init__(size)
        self.crust = "cheese"
        if crust.lower() in self.crustTypes:
            self.crust = crust.lower()

    def getCrust(self):
        return self.crust

    def setCrust(self, newCrust):
        if newCrust in self.crustTypes:
            self.crust = newCrust

    def getPrice(self):
        return super().getPrice() + 2

    def __str__(self):
        output = f"A {self.size} stuffed crust pizza with:"
        for topping in self.toppings:
            output += f"\n- {topping}"
        output += f"\nCrust type: {self.crust}"
        output += f"\nPrice: £{self.getPrice()}\n"
        return output
    
    def updatePizzaSize(self, pizzaIndex, newSize):
        if 0 <= pizzaIndex < len(self.pizzas):
            self.pizzas[pizzaIndex].setSize(newSize)

    def updatePizzaToppings(self, pizzaIndex, newToppings):
        if 0 <= pizzaIndex < len(self.pizzas):
            pizza = self.pizzas[pizzaIndex]
            pizza.toppings = set(newToppings)

def test():
    myOrder = Order()
    pizza1 = Pizza("small")
    pizza1.addTopping("Pepperoni")
    pizza1.addTopping("Jalapenos")
    pizza1.setSize("large")

    pizza2 = StuffedCrustPizza("Medium", "Cheese")
    pizza2.addTopping("Ham")
    pizza2.addTopping("Mushrooms")
    pizza2.setCrust("Garlic")

    myOrder.addPizza(pizza1)
    myOrder.addPizza(pizza2)

    print("Original Order:")
    print(myOrder)

    # Upgrade a standard pizza to stuffed crust
    myOrder.upgradeToStuffedCrust(0)

    print("\nUpgraded Order:")
    print(myOrder)

if __name__ == "__main__":
    test()

"""
Exercise four:
Write a program, library.py, to manage a library system that includes both physical and digital books.
Every book, regardless of its type, has a title, author, and an International Standard Book Number (ISBN). 
Books also have an attribute to indicate whether they are currently available for borrowing.
A digital book has an extra attribute: compatibility, which could be PDF, Kindle or Apple. 

Initially, a digital book is compatible with only one specified format, 
but the user should be able to add additional compatibilities. Digital books are always available for borrowing.
Your program needs to include a Library class that stores a collection of books. 
The user should be able to add a book to a library (making it available) but they could only borrow a book if it is available.
When displaying a library, the titles, and availability statuses of all the books should be shown.

Test your classes, with the following books, using a test function:
Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
Book("1984", "George Orwell", "978-0451524935")
DigitalBook("1984", "George Orwell", "978-0451524935", "Kindle")
"""

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Available' if self.available else 'Not Available'}"


class DigitalBook(Book):
    def __init__(self, title, author, isbn, compatibility):
        super().__init__(title, author, isbn)
        self.compatibility = [compatibility]

    def addCompatibility(self, new_compatibility):
        self.compatibility.append(new_compatibility)

    def __str__(self):
        compatibilities = ", ".join(self.compatibility)
        return f"{super().__str__()} - Compatible Formats: {compatibilities}"


class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def displayLibrary(self):
        for book in self.books:
            print(book)


def testLibrary():
    library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    book2 = Book("1984", "George Orwell", "978-0451524935")
    digitalBook = DigitalBook("1984", "George Orwell", "978-0451524935", "Kindle")

    library.addBook(book1)
    library.addBook(book2)
    library.addBook(digitalBook)

    print("Library Contents:")
    library.displayLibrary()


if __name__ == "__main__":
    testLibrary()

"""
Exercise five:
Write a program spotify.py that simulates Spotify's playlist management features. 
You need to satisfy the requirements listed below:
The image below shows a playlist with multiple songs. 
Note the data stored for every playlist and the songs. 
Assume that each playlist has a unique name and the length of a song is measured in seconds.
Your system should start with a few existing playlists and allow the user to create/manage other playlists. 
The user should be able to add or remove songs to/from playlists of their choice. Additionally, 
your program needs to have predefined songs but also let the user add new songs.
To demonstrate the function of your system, 
add an interactive menu so that the user can view the existing playlists and the songs within them.

Cut - 1990 Demo (The Cure)
Grace (Jeff Buckley)
It's Oh So Quiet (Bjork)
Sour Times (Portishead)
Beetlebum - 2012 Remaster (Blur)
"""

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __str__(self):
        return f"{self.title} by {self.artist}"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def addSong(self, song):
        self.songs.append(song)

    def removeSong(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def displayPlaylist(self):
        print(f"Playlist: {self.name}")
        for song in self.songs:
            print(f"- {song}")


class Spotify:
    def __init__(self):
        self.playlists = []

    def createPlaylist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)
        return playlist

    def displayPlaylists(self):
        print("Existing Playlists:")
        for playlist in self.playlists:
            print(f"- {playlist.name}")

    def displayMenu(self):
        print("\nSpotify Playlist Management Menu:")
        print("1. Create Playlist")
        print("2. Display Playlists")
        print("3. Add Song to Playlist")
        print("4. Remove Song from Playlist")
        print("5. View Songs in Playlist")
        print("6. Quit")


def testSpotify():
    spotify = Spotify()

    playlist1 = spotify.createPlaylist("My Favorites")
    playlist2 = spotify.createPlaylist("Chill Vibes")

    song1 = Song("Cut - 1990 Demo", "The Cure")
    song2 = Song("Grace", "Jeff Buckley")
    song3 = Song("It's Oh So Quiet", "Bjork")
    song4 = Song("Sour Times", "Portishead")
    song5 = Song("Beetlebum - 2012 Remaster", "Blur")

    playlist1.addSong(song1)
    playlist1.addSong(song2)
    playlist2.addSong(song3)
    playlist2.addSong(song4)
    playlist2.addSong(song5)

    while True:
        spotify.displayMenu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter the name of the new playlist: ")
            new_playlist = spotify.createPlaylist(name)
            print(f"Playlist '{new_playlist.name}' created.")
        elif choice == "2":
            spotify.displayPlaylists()
        elif choice == "3":
            spotify.displayPlaylists()
            playlist_name = input("Enter the name of the playlist: ")
            playlist = next((pl for pl in spotify.playlists if pl.name == playlist_name), None)
            if playlist:
                title = input("Enter the title of the song: ")
                artist = input("Enter the artist of the song: ")
                new_song = Song(title, artist)
                playlist.addSong(new_song)
                print(f"Song '{new_song}' added to the playlist '{playlist_name}'.")
            else:
                print("Playlist not found.")
        elif choice == "4":
            spotify.displayPlaylists()
            playlist_name = input("Enter the name of the playlist: ")
            playlist = next((pl for pl in spotify.playlists if pl.name == playlist_name), None)
            if playlist:
                print("Songs in the playlist:")
                for idx, song in enumerate(playlist.songs):
                    print(f"{idx + 1}. {song}")
                song_idx = int(input("Enter the number of the song to remove: ")) - 1
                if 0 <= song_idx < len(playlist.songs):
                    removed_song = playlist.songs.pop(song_idx)
                    print(f"Song '{removed_song}' removed from the playlist '{playlist_name}'.")
                else:
                    print("Invalid song number.")
            else:
                print("Playlist not found.")
        elif choice == "5":
            spotify.displayPlaylists()
            playlist_name = input("Enter the name of the playlist: ")
            playlist = next((pl for pl in spotify.playlists if pl.name == playlist_name), None)
            if playlist:
                playlist.displayPlaylist()
            else:
                print("Playlist not found.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    testSpotify()

"""
Exercise six:
Assume for this exercise that the messaging and social media platform Discord has three types of users: 
Unverified users, a user that has verified their contact information, and a Nitro user who pays a subscription fee.
Every user has a unique ID (string) and a collection of messages that they have received. 
However, as depicted in the table below, the users have limitations on sending messages to other users based on their tiers.
Nitro users can pin messages, making them easier to locate. 
Pinned messages are displayed at the top of the user's messages when they are printed.

Type of user  /  Send Messages  /  Message Limit  /  Pinning Messages
Unverified           ❌                  ❌                 ❌
Verified             ✅           max 100 characters        ❌
Nitro                ✅              unlimited              ✅
Write a program discord.py that allows the creation of any type of user. 
You also need to test the user's ability to send, receive, view, and pin messages.
"""

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.messages = []

    def send_message(self, content):
        self.messages.append(content)

    def view_messages(self):
        print(f"Messages for User {self.user_id}:")
        for message in self.messages:
            print(message)

    def pin_message(self, message_index):
        pass  # Pinned messages not supported for this user type


class UnverifiedUser(User):
    pass  # Unverified users cannot send, pin, or view messages


class VerifiedUser(User):
    def send_message(self, content):
        if len(content) <= 100:
            super().send_message(content)
        else:
            print("Message length exceeds the limit of 100 characters.")

    pass  # Verified users cannot pin messages


class NitroUser(User):
    def pin_message(self, message_index):
        if 0 <= message_index < len(self.messages):
            pinned_message = self.messages.pop(message_index)
            self.messages.insert(0, f"Pinned: {pinned_message}")

    pass  # Nitro users can send, pin, and view messages


# Test the Discord messaging system
def test_discord():
    user1 = UnverifiedUser("123")
    user2 = VerifiedUser("456")
    user3 = NitroUser("789")

    user1.send_message("Hello, Unverified User!")
    user2.send_message("This is a verified user sending a message.")
    user3.send_message("Nitro users can send unlimited messages!")

    user1.view_messages()
    user2.view_messages()
    user3.view_messages()

    user2.send_message("This message is too long to be sent by a verified user" * 10)

    user3.pin_message(0)
    user3.pin_message(1)

    print("\nAfter pinning messages:")
    user3.view_messages()


if __name__ == "__main__":
    test_discord()

"""
Exercise seven:
A growing business is finding it increasingly difficult to manage all the workers they have. 
So, the CEO asks you to develop a system to keep track of everyone. 
Write your solutions based on the requirements below and save it as company.py.
Each worker they have has their own unique identifier, 
name, and job title. These are just some details you may choose to store for each worker.
The company has two kinds of workers: employees and contractors. 
The employees are on a fixed monthly salary. But there's a catch: they can be promoted, 
and when that happens, their salary goes up (starting with £500, £1000 and then £2000 increase).
As for the contractors, they're paid by the hour. Sometimes they work extra hours, 
and the CEO needs the system to account for that because it affects how much they're paid.
Finally, the business is growing, so they are always adding new people. Sometimes employees,
sometimes contractors. On the flip side, the business does have to let people go from time to time. 
So, the system should be able to remove someone based on their unique identifier.
One more thing: For budgetary reasons, 
the CEO needs to know how much they are spending on salaries for everyone—both employees and contractors, 
and the system should be able to tell me how many employees and contractors there are.
"""


class Worker:
    def __init__(self, identifier, name, job_title):
        self.identifier = identifier
        self.name = name
        self.job_title = job_title

    def __str__(self):
        return f"{self.job_title} {self.name} (ID: {self.identifier})"


class Employee(Worker):
    def __init__(self, identifier, name, job_title, salary):
        super().__init__(identifier, name, job_title)
        self.salary = salary

    def promote(self):
        self.salary += 500

    def get_salary(self):
        return self.salary


class Contractor(Worker):
    def __init__(self, identifier, name, job_title, hourly_rate, hours_worked=0):
        super().__init__(identifier, name, job_title)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def add_hours_worked(self, hours):
        self.hours_worked += hours

    def get_salary(self):
        return self.hourly_rate * self.hours_worked


class Company:
    def __init__(self):
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def remove_worker(self, identifier):
        self.workers = [worker for worker in self.workers if worker.identifier != identifier]

    def get_total_salary_budget(self):
        total_salary_budget = sum(worker.get_salary() for worker in self.workers)
        return total_salary_budget

    def get_num_employees(self):
        return sum(isinstance(worker, Employee) for worker in self.workers)

    def get_num_contractors(self):
        return sum(isinstance(worker, Contractor) for worker in self.workers)


# Test the company system
def test_company_system():
    company = Company()

    employee1 = Employee("E001", "John Doe", "Software Engineer", 60000)
    contractor1 = Contractor("C001", "Alice Smith", "Freelancer", 25, 40)

    company.add_worker(employee1)
    company.add_worker(contractor1)

    print("Initial Workers:")
    for worker in company.workers:
        print(worker)

    print("\nTotal Salary Budget:", company.get_total_salary_budget())
    print("Number of Employees:", company.get_num_employees())
    print("Number of Contractors:", company.get_num_contractors())

    employee1.promote()
    contractor1.add_hours_worked(10)

    print("\nAfter Promotion and Extra Hours:")
    for worker in company.workers:
        print(worker)

    print("\nUpdated Total Salary Budget:", company.get_total_salary_budget())


if __name__ == "__main__":
    test_company_system()
