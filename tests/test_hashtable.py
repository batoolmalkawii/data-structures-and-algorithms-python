from data_structures_and_algorithms_python.data_structures.hashtable.hashtable import Hashtable


"""
Test Cases:
    1. Adding a key/value to your hashtable results in the value being in the data structure
    2. Retrieving based on a key returns the value stored
    3. Successfully returns null for a key that does not exist in the hashtable
    4. Successfully handle a collision within the hashtable
    5. Successfully retrieve a value from a bucket within the hashtable that has a collision
    6. Successfully hash a key to an in-range value
    7. Successfully checks if a key exists in the hashtable.
"""

def test_hash_create():
    ht = Hashtable(10)
    assert ht.map == [None, None, None, None, None, None, None, None, None, None]

def test_hash_add():
    ht = Hashtable(1024)
    ht.add('name', 'batool')
    assert ht.map[945][0][0] == 'name'
    assert ht.map[945][0][1] == 'batool'

def test_hash_get():
    ht = Hashtable(1024)
    ht.add('name', 'batool')
    assert ht.get('name') == 'batool'

def test_hash_get_not():
    ht = Hashtable(1024)
    assert ht.get('name') == None

def test_hash_add_collision():
    ht = Hashtable(1024)
    ht.add('name', 'batool')
    ht.add('mane', 'not batool')
    assert ht.get('name') == 'batool'
    assert ht.get('mane') == 'not batool'

def test_hash_hash():
    ht = Hashtable(1024)
    key = 'name'
    assert ht.hash(key) == 945

def test_hash_contains():
    ht = Hashtable(1024)
    ht.add('name', 'batool')
    assert ht.contains('name') == True
    assert ht.contains('phone') == False







    



