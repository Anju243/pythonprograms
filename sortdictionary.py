my_dict={'apple':5,'banan':2,'orange':8,'grape':3}
ascending_dict=dict(sorted(my_dict.items()))
print("ascending is",ascending_dict)
descending_dict=dict(sorted(my_dict.items(),reverse=True))
print("descending is",descending_dict)