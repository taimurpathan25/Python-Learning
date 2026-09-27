list = [1,5,15,25,15,5,15];

list.append(100); # add items in end
print(list);

list.insert(1,25); # insert at index
print(list);

list.extend([30,40]); # add given items in the end
print(list);

list.remove(5); # remove value from list, what u want to remove
print(list);

list.pop(); # by default remove from end
list.pop(0); # remove; by index , what u want to remove which which index value
print(list);

# list.clear() # it will do empty list
# print(list);

list_index=list.index(15);
print(list_index);

list_count = list.count(15); # counting the repeating value
print(list_count);

list.sort(); # sorting the list in ascending order
print(list);

list.reverse(); # the list in reverse order
print(list);

new = list.copy(); # copy the whole list 
print(list);
print(new, new,new);