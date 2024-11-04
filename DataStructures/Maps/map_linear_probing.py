from . import map_functions as mf
from . import map_entry as me
from DataStructures.List import array_list as al
import random as rd

def new_map(num_elements, load_factor, prime=109345121):
    n_map = {"prime": prime,
             "capacity": 0,
             "scale": 0,
             "shift": 0,
             "table": None,
             "current_factor": 0,
             "limit_factor": 0,
             "size": 0,
             "type": "PROBING"}
    
    n_map["capacity"] = mf.next_prime(num_elements/load_factor)
    n_map["scale"] = rd.randint(1, prime-1)
    n_map["shift"] = rd.randrange(1, prime-1)
    n_map["limit_factor"] = load_factor
    
    n_map["table"] = al.new_list()
    
    for i in range(n_map["capacity"]):
        al.add_last(n_map["table"], me.new_map_entry(None, None))
    
    return n_map

def put(my_map, key, value):
    entry = me.new_map_entry(key, value)
    hash_v =  mf.hash_value(my_map, key)
    slot_found = find_slot(my_map, key, hash_v)
    
    if slot_found[0] == False:
        my_map["size"] += 1
    
    al.change_info(my_map["table"], slot_found[1], entry)
    
    if my_map["size"] > my_map["capacity"]*my_map["limit_factor"]:
        rehash(my_map)
    
    return my_map

def is_available(table, pos):
    
    result = False 
    entry = al.get_element(table, pos)
    
    if me.get_key(entry) == None or me.get_key(entry) == "__EMPTY__":
        result = True 
        
    return result 

def remove(my_map, key): 
    
    hash_val = mf.hash_value(my_map, key)
    
    while True:
        entry = al.get_element(my_map["table"], hash_val)
        if entry is None or entry == "__EMPTY__":
            return my_map 
        
        if entry['key'] == key:
            al.change_info(my_map["table"], hash_val, {'key': '__EMPTY__', 'value': '__EMPTY__'})
            
            if my_map["size"] > 0: 
                my_map["size"] -= 1
            return my_map  
        
        hash_val = (hash_val+ 1) % my_map['capacity']
        
        return my_map

def rehash(my_map):
    new_capacity = my_map["capacity"]*2
    num_elements = new_capacity * my_map["limit_factor"]
    
    other_map = new_map(num_elements, my_map["limit_factor"], my_map["prime"])
    
    for element in my_map["table"]["elements"]:
        if element["key"] != None and element["key"] != "__EMPTY__":
            put(other_map, element["key"], element["value"])
    
    my_map["table"] = other_map["table"]
    my_map["capacity"] = other_map["capacity"]
    my_map["scale"] = other_map["scale"]
    my_map["shift"] = other_map["shift"]
        
    return my_map

def size(my_map):
    return my_map["size"]

def contains (my_map, key):
    
    if is_empty(my_map):
        return False
    
    hash_v = mf.hash_value(my_map, key)
    element_on_pos = al.get_element(my_map["table"], hash_v)
    
    if default_compare(key, element_on_pos) == 1:
        return True
    else:
        i = (hash_v + 1) % my_map["capacity"]
        while i != hash_v:
            element_here = al.get_element(my_map["table"], i)
            if default_compare(key, element_here) == 1:
                return True
            elif default_compare(None, element_here) == 1:
                return False
            
            i = (i + 1) % my_map["capacity"]
        return False
    
def find_slot(my_map, key, hash_value): 
    
    pos_disponible = None 
    encontrada = False 
    ocupada = False 
    
    while not encontrada:
        current_element = al.get_element(my_map["table"], hash_value)
       
        if default_compare(key, current_element) == 1:
            encontrada = True
            pos_disponible = hash_value
            ocupada = True
        elif is_available(my_map["table"], hash_value):
            encontrada = True
            pos_disponible = hash_value
            ocupada = False
        else: 
            hash_value = (hash_value + 1) % my_map["capacity"] 
            
    return ocupada, pos_disponible 

def default_compare(key, element):
    el_key = me.get_key(element)
    if key == el_key:   # Según la documentación, debe hacerse una comparación mayor/menor acá, pero es ambiguo lo que esto quiere decir considerando que la llave no es necesariamente int e incluso puede ser None.
        return 1
    else:
        return -1
    
def get(my_map, key):
    hash_v = mf.hash_value(my_map, key)
    el_on_pos = al.get_element(my_map["table"], hash_v)
    pair = None
    
    if is_empty(my_map):
        return None
    
    if default_compare(key, el_on_pos) == 1:
        pair = al.get_element(my_map["table"], hash_v)
    else:
        i = (hash_v + 1) % my_map["capacity"]
        encontrado = False
        while not encontrado:
            element_here = al.get_element(my_map["table"], i)
            if default_compare(key, element_here) == 1:
                pair = al.get_element(my_map["table"], i)
                encontrado = True
            elif default_compare(None, element_here) == 1 or i == hash_v:
                return None
            
            i = (i + 1) % my_map["capacity"]
    
    return me.get_value(pair)

def is_empty(my_map):
    if size(my_map) == 0:
        return True
    return False

def key_set(my_map):
    
    llaves = al.new_list()
    
    if is_empty(my_map):
        return llaves
    
    for pair in my_map["table"]["elements"]:
        key = me.get_key(pair)
        if key != None and key != "__EMPTY__":
            al.add_last(llaves, key)
        if al.size(llaves) >= size(my_map):
            return llaves
        
def value_set(my_map):
    
    valores = al.new_list()
    
    if is_empty(my_map):
        return valores
    
    for pair in my_map["table"]["elements"]:
        value = me.get_value(pair)
        if value != None and value != "__EMPTY__":
            al.add_last(valores, value)
        if al.size(valores) >= size(my_map):
            return valores