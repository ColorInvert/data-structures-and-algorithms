from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    # Add a cat or dog to the shelter, sorting them into their
    # respective queues
    def enqueue(self, animal):

        if animal.species == "dog":
            # Incoming animal is a dog, put into dog queue
            self.dog_queue.enqueue(animal)
        elif animal.species == "cat":
            # Incoming animal is a cat, put into cat queue
            self.cat_queue.enqueue(animal)
        else:
            # Shelter only allows cats and dogs, return an error string if
            # any string provided apart from those two.
            # Not strictly required, but felt right to have.
            return "This is not a valid animal for our shelter!"

    # Remove an animal from dog_queue or cat_queue, based on if input is "dog" or "cat"
    def dequeue(self, species):

        if species == "dog":
            # Dog requested, dequeue and return next dog_object (or dobject, if you will)
            return self.dog_queue.dequeue()
        elif species == "cat":
            # Cat requested, dequeue and return next cat_object (or cobject, if you will)
            return self.cat_queue.dequeue()
        else:
            # Request is neither cat nor dog. return null.
            return None


class Dog:

    # All dogs have a species of dog, and a name that can be any string. "DEFAULTDOG" if
    # none is provided.
    def __init__(self, name="DEFAULTDOG"):
        self.species = "dog"
        self.name = name


class Cat:
    # All cats have a species of cat, and a name that can be any string. "DEFAULTCAT" if
    # none is provided.
    def __init__(self, name="DEFAULTCAT"):
        self.species = "cat"
        self.name = name
