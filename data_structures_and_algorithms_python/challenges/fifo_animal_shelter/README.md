# Stacks and Queues

Ih this project, we created an animal shelter which holds only dogs and cats. It is called **AnimalShelter**, which depends on the FIFO data structure _Queue_.

**AnimalShelter** included the following:

    _Attributes_:
        1. `front`.
        2. `rear`.


    _methods_:
        1. `enqueue(animal)`: adds animal to the shelter. animal can be either a dog or a cat object.
        2. `dequeue(pref)`: returns either a dog or a cat. If pref is not "dog" or "cat" then return null.




**User acceptance tests** are included with the following test cases:

*AnimalShelter* test cases:

    1. Creating a shelter instance.
    2. Enqueue one Animal into the shelter.
    3. Enqueue multiple Animals into the shelter.
    4. Return None when enqueueing not dog or cat into the shelter.
    5. Dequeue a preferred animal from the shelter.
    6. Refuse dequeuing from an empty shelter.
