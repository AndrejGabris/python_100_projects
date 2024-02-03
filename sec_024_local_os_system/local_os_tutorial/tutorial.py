# file = open(r"sec_024_local_os_system\local_os\my_text.txt")
# contents = file.read()
# file.close()

# print(contents)


# ------------------------ CONSTRUCTOR WITH ----------------------------
# read-only mode
# with open(r"sec_024_local_os_system\local_os\my_text.txt") as file:
#     contents = file.read()
#     print(contents)
    
    
# writeable mode  
# with open(r"sec_024_local_os_system\local_os\my_text.txt", mode="w") as file:
#     file.write("New text.")
    
    
# append mode  
# with open(r"sec_024_local_os_system\local_os\my_text.txt", mode="a") as file:
#     file.write("New text.")


# create a new .txt file if path doesn"t exist
with open(r"sec_024_local_os_system\local_os\new_text.txt", mode="a") as file:
    file.write("New text.")