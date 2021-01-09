# Hashtable

In this project, we created a data structure called **Hashtable** in Python.

**Hashtable** included the following:

    _Attributes_:
         1. `size`.
         2. `map`.

    _methods_:
        * `add`: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
        * `get`: takes in the key and returns the value from the table.
        * `contains`: takes in the key and returns a boolean, indicating if the key exists in the table already.
        * `hash`: takes in an arbitrary key and returns an index in the collection.


**User acceptance tests** are included with the following test cases:

*Hashtable* test cases:

    1. Adding a key/value to your hashtable results in the value being in the data structure
    2. Retrieving based on a key returns the value stored
    3. Successfully returns null for a key that does not exist in the hashtable
    4. Successfully handle a collision within the hashtable
    5. Successfully retrieve a value from a bucket within the hashtable that has a collision
    6. Successfully hash a key to an in-range value
    7. Successfully checks if a key exists in the hashtable.
