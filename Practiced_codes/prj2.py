#3. Shopping List with Categories ● Use : Dictionary (category: list of items), functions, 
# loops ● Features : ○ Add item to category ○
# Show items by category ○ Remove item 
# ○ Show full shopping list
shoping_list={}
def add_item(category,item):
    if category in shoping_list:
        shoping_list[category].append(item)
    else:
        shoping_list[category]=[item]
        print(f"{item} added to {category}")
def show(category):
    if category in shoping_list and shoping_list[category]:
        print(f"\n Show items in {category}")
        for i,item in enumerate(shoping_list[category],1):
            print(f"{i}:{item}")
def remove_item(category,item):
    if category in shoping_list and shoping_list[category]:
        shoping_list[category].remove(item)
        print(f"{item} removed form {category}")
    if not shoping_list[category]:
        del shoping_list[category]
def show_info():
    if not shoping_list:
        print("The list is empty")
    print("\n The full Shopping List")
    for i,item in shoping_list.items():
        print(f"{i}:{','.join(item)}")

    
add_item("fruit","Aplpe")
add_item("vegetable","Brinjal")
add_item("vegetable","Onion")
add_item("fruit","mango")
remove_item("fruit","Aplpe")
show("fruit")
show("vegetable")
show_info()