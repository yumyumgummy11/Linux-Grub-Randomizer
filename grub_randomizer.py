from os import listdir, system
from random import randrange

def get_grub_themes(): #get a list of all themes in the /boot/grub/themes directory
    theme_list = listdir('/boot/grub/themes')
    if len(theme_list) == 0:
        quit()
    return theme_list

def choose_random_theme(): #choose a random theme based on the list given from the get_grub_themes function
    theme_list = get_grub_themes()
    
    if len(theme_list) > 1:
        f = ""
        with open('/etc/default/grub','r') as file:
            f = file.readlines()
        
        remove_queue = []
        for i in f:
            if 'GRUB_THEME' in i:
                for x in theme_list:
                    if x in i:
                        remove_queue.append(x)
                        break
        
        for i in remove_queue:
            theme_list.remove(i)                

    new_theme = theme_list[randrange(0,len(theme_list))]
    return new_theme

def generate_command(): #generates the command for the grub
    new_theme = choose_random_theme()
    command = f'GRUB_THEME="/boot/grub/themes/{new_theme}/theme.txt"'
    return command

def make_backup(fp): #make a backup of the file
    f = ""
    with open(fp,'r') as file:
        f = file.read()

    with open(fp+".bak",'w') as file:
        file.write(f)

def edit_file(fp): #edit the grub file and repalce with new command
    with open(fp,'r') as file:
        data = file.readlines()
    
    command = generate_command()
    for index, i in enumerate(data):
        if 'GRUB_THEME' in i:
            data[index] = command + '\n'
        
    
    with open(fp,'w') as file:
        file.writelines(data)

fp = "/etc/default/grub"

make_backup(fp)
edit_file(fp)
system("sudo grub-mkconfig -o /boot/grub/grub.cfg") #run the grub config to apply the changes
