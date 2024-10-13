def new_list():
    newlist={
        'elements':[],
        'size':0,
    }
    return newlist

def add_first(my_list, element):
    my_list['elements'].insert(0, element)
    my_list['size'] += 1
    
    return my_list

def add_last(my_list, element):
    my_list['elements'].append(element)
    my_list['size']+=1
    return my_list

def is_empty(my_list):

    return len(my_list['elements']) == 0

def size(my_list):
    return len(my_list['elements'])

def first_element (my_list):
    return my_list['elements'][0]

def last_element (my_list):
    return my_list['elements'][-1]

def get_element (my_list, pos):
    return my_list['elements'][pos-1]

def is_present (my_list, element, cmp_function):
    size = my_list['size']
    if size > 0:
        for keypos in range(size):
            info = my_list['elements'][keypos]
            if cmp_function(element, info) == 0:
                # Retorna la posición si se encuentra el elemento
                return keypos
    # Retorna -1 si no se encuentra el elemento
    return -1
    
def remove_first(my_list):
    if my_list['size'] == 0:
        return None
    else:
        first_element = my_list['elements'].pop(0)
        my_list['size'] -= 1
        return first_element

def remove_last(my_list):
    if my_list['size'] == 0:
        return None
    else:
        last_element = my_list['elements'].pop(-1)
        my_list['size'] -= 1
        return last_element
    
def insert_element(my_list, element, pos):
    my_list['elements'].insert(pos, element)
    my_list['size'] += 1
    return my_list
    
def delete_element(my_list, pos):
    if my_list['size'] == 0 and pos < 0 or pos >= my_list['size']:
        return None

    my_list['elements'].pop(pos)
    my_list['size'] -= 1
    return my_list

def change_info(my_list, pos, new_info):
    my_list['elements'][pos] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    my_list['elements'][pos1], my_list['elements'][pos2] = my_list['elements'][pos2], my_list['elements'][pos1]
    return my_list

def sub_list(my_list, pos, numelem):
    sublist = {
        'elements': my_list['elements'][pos:pos + numelem],
        'size': numelem,
        'type':'List'
        }
    return sublist