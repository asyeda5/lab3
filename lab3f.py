#!/usr/bin/env python3

# Place my_list below this comment (before the function definitions)
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    new_value = ordered_list[-1] + 1  # Get the last item and add 1
    ordered_list.append(new_value)     # Append the new value to the list

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values, found in items_to_remove list, from ordered_list
    for item in items_to_remove:
        while item in ordered_list:
            ordered_list.remove(item)  # Remove the item if it exists

# Main code
if __name__ == '__main__':
    print(my_list)  # Print the initial list
    add_item_to_list(my_list)  # Add items
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)  # Print the list after additions
    remove_items_from_list(my_list, [1, 5, 6])  # Remove specific items
    print(my_list)  # Print the final list
