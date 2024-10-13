from . import list_node as node_list
def new_list():
    newlist={'first':None,
             'last':None,
             'size':0,
             }
    return newlist

def add_first(my_list, element):
    new_node = node_list.new_single_node(element)
    if my_list['size'] == 0: 
        my_list['first'] = new_node
        my_list['last'] = new_node 
    else:
        new_node['next'] = my_list['first']
        my_list['first'] = new_node
    my_list['size'] += 1
    return my_list

def add_last(my_list, element):
    new_node = node_list.new_single_node(element)
    if my_list['size'] == 0: 
        my_list['first'] = new_node
        my_list['last'] = new_node  
    else:
        my_list['last']['next'] = new_node
        my_list['last'] = new_node
    my_list['size'] += 1
    return my_list

def is_empty(my_list):
    return my_list['size'] == 0

def first_element(my_list):
    if my_list['size'] == 0: 
        first= None
    else:
        first= my_list['first']['info']
    return first

def last_element(my_list):
    if my_list['size'] == 0: 
        last= None
    else:
        last= my_list['last']['info']
    return last

def size(my_list):
    return my_list['size']

def get_element(my_list, pos):
   
    if pos == 0:
        return my_list['first']['info']

    nodo = my_list['first']
    for i in range(pos):
        nodo = nodo['next']
    return nodo['info']

def remove_first(my_list):
    
    if my_list['size'] == 0:
        return None

    primer_valor = my_list['first']['info']
    my_list['first'] = my_list['first']['next']
    my_list['size'] -= 1
    return primer_valor

def remove_last(my_list):
    if my_list['size'] == 0:
        return None

    nodo = my_list['first']
    
    if nodo['next'] is None:
        ultimo_valor = nodo['info']
        my_list['first'] = None
        my_list['last'] = None 
    else:
        while nodo['next']['next'] is not None:
            nodo = nodo['next']
        ultimo_valor = nodo['next']['info']
        
        nodo['next'] = None
        my_list['last'] = nodo
        
    my_list['size'] -= 1
    return ultimo_valor

def insert_element(my_list, element, pos):
    nuevo_nodo = {'info': element, 'next': None}
    if pos == 0:
        nuevo_nodo['next'] = my_list['first']
        my_list['first'] = nuevo_nodo
        if my_list['size'] == 0:
            my_list['last'] = nuevo_nodo 
    else:
        nodo = my_list['first']
        for i in range(pos - 1):
            nodo = nodo['next']
    
        nuevo_nodo['next'] = nodo['next']
        nodo['next'] = nuevo_nodo
        if pos == my_list['size']:
            my_list['last'] = nuevo_nodo
            
    my_list['size'] += 1
    return my_list

def is_present(my_list, element, cmp_function):
    nodo = my_list['first']
    position = 0

    while nodo is not None:
        if cmp_function(nodo['info'], element) == 0:
            return position
        nodo = nodo['next']
        position += 1
    return -1

def delete_element(my_list, pos):
    if pos == 0:
        nodo_eliminado = my_list['first']
        my_list['first'] = nodo_eliminado['next']
        if my_list['size'] == 1:
            my_list['last'] = None 
    else:
        nodo = my_list['first']
        for i in range(pos - 1):
            nodo = nodo['next']
    
        nodo_eliminado = nodo['next']
        nodo['next'] = nodo_eliminado['next']
    
        if pos == my_list['size'] - 1:
            my_list['last'] = nodo

    my_list['size'] -= 1
    return my_list

def change_info(my_list, pos, new_info):
    nodo = my_list['first']
    for i in range(pos):
        nodo = nodo['next']
    
    nodo['info'] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 == pos2:
        return my_list
    
    nodo1 = my_list['first']
    nodo2 = my_list['first']
    
    for i in range(pos1):
        nodo1 = nodo1['next']
    for _ in range(pos2):
        nodo2 = nodo2['next']

    nodo1['info'], nodo2['info'] = nodo2['info'], nodo1['info']
    return my_list

def sub_list(my_list, pos, num_elem):
    num_elem = min(num_elem, my_list['size'] - pos)

    sub_list = {'first': None, 'last': None, 'size': 0}
    nodo = my_list['first']
    
    for i in range(pos):
        nodo = nodo['next']

    for i in range(num_elem):
        nodo_nuevo = {'info': nodo['info'], 'next': None}
        
        if sub_list['first'] is None:
            sub_list['first'] = nodo_nuevo
        else:
            sub_list['last']['next'] = nodo_nuevo
        
        sub_list['last'] = nodo_nuevo
        sub_list['size'] += 1
        nodo = nodo['next']

    return sub_list