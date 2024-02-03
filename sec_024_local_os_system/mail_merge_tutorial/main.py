#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = "[name]"

with open(r"sec_024_local_os_system\mail_merge_tutorial\Input\Names\invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

with open(r"sec_024_local_os_system\mail_merge_tutorial\Input\Letters\starting_letter.txt", mode="r") as letter_file:
    template_letter = letter_file.read()
    
    for name in names:
        stripped_name = name.strip()
        new_letter = template_letter.replace(PLACEHOLDER, stripped_name)
        with open(f"sec_024_local_os_system\mail_merge_tutorial\Output\ReadyToSend\letter_for_{stripped_name}.txt", mode="w") as ready_to_send_letter: #create new .txt files 
            ready_to_send_letter.write(new_letter)



