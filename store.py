import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Your software must demonstrate the ability 
# to insert, modify, delete, and retrieve 
# (or query) data.


def main():
    db = connect()
    menu(db)

def connect():
    # Use a service account
    cred = credentials.Certificate('madis-store-database-8ca6512ac2f9.json')
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db

def add_data(db):
    # Get the product dictionary
    product = get_product()

    # Convert the product name into an appropriate id by replacing spaces with underscores.
    id = product["name"].replace(" ", "_")
   
    # Add the values from the dict to the database.
    doc_ref = db.collection(u'products').document(f"u'{id}'")
    doc_ref.set({
        u'name':product["name"],
        u'price': product["price"],
        u'description': product["description"]
    })


def read_data(db):
    product_ref = db.collection(u'products')
    docs = product_ref.stream()

    for doc in docs:
        row = doc.to_dict()
        print(f'\n{row["name"]}:\n{row["price"]}\n{row["description"]}')
        

def get_product():
    # Get the three values that make up a product dictionary.
    name = input("\nWhat is the product name? ")
    price = float(input("What is the price of the product? $"))
    description = input("Describe the product: ")

    # Store the values in a dict.
    product = dict()
    product["name"] = name
    product["price"] = price
    product["description"] = description

    return product

def delete_row(db):
    product_ref = db.collection(u'products')
    docs = product_ref.stream()

    names = []
    ids = []

    for doc in docs:
        row = doc.to_dict()
        names.append(row["name"])
        ids.append(doc.id)

    for i in range(len(names)):
        print(f'{i+1}. {names[i]}')

    choice = int(input("What is the number of the item you want to delete? "))
    print(ids[choice - 1])

    # Hack to get around bug. did nothing.
    #for doc in docs:
    #    if doc.id == ids[choice - 1]:
    #        print("delete called.")
    #        doc.delete()
    #        break

    # The following line throws an error.
    # db.collections(u'products').document(ids[choice - 1]).delete()

    print("Product Deleted\n")

def mod_row(db):
    product_ref = db.collection(u'products')
    docs = product_ref.stream()

    names = []
    prices = []
    ids = []

    for doc in docs:
        row = doc.to_dict()
        names.append(row["name"])
        prices.append(row["price"])
        ids.append(doc.id)

    for i in range(len(names)):
        print(f'{i+1}. {names[i]} ${prices[i]}')

    choice = int(input("What is the number of the item you want to reprice? "))
    new_price = float(input("What is the new price: $"))
    
    # The following line throws an error.
    product_ref = db.collections(u'products').document(ids[choice - 1])
    product_ref.update({u'price': new_price})

    print("Price updated.")

def menu(db):
    quit = False

    while not quit:
        # "Delete a Product", "Reprice a Product", These options removed because of bugs.
        options = ["View Products", "Add a Product",  "Quit Program"]
        for i in range(len(options)):
            print(f'{i+1}. {options[i]}')
        
        choice = int(input("Enter the number for your choice: "))

        if choice == 1:
            read_data(db)
        elif choice == 2:
            add_data(db)
        # elif choice == 3:
            # delete_row(db)
        # elif choice == 4:
            # mod_row(db)
        elif choice == 3:
            quit = True
            print("\nThank You. Goodbye")
        else:
            print("Choice not recognized.\n")
        

main()