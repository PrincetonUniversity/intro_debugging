"""This script should print a list of non-furniture objects in
   alphabetical order.""" 

def remove_furniture(items):
  furniture = {'couch', 'table', 'desk', 'chair'}
  items_furniture_removed = [item for item in items if item not in furniture]
  return items_furniture_removed

if __name__ == '__main__':
  # input list of items
  items = ['book', 'pencil', 'desk', 'door']
  # remove furniture objects from items
  items = remove_furniture(items)
  # print remaining items in alphabetical order
  for item in items.sort():
    print(item)
