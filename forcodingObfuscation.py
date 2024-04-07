import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

random_string_unique = generate_random_string(10)
random_string_final = generate_random_string(10)

payload = f'cmd /V /C "set {random_string_unique}='

command = input("Enter the command: ")
end_index = random.randint(len(command)+1, 2*len(command))

unique_dict = {char: index for index, char in enumerate(set(command))}

payload += "".join(unique_dict.keys())
payload += "&&FOR %A IN ("

char_dict = {index: char for index, char in enumerate(command)}

for k in char_dict.values():
    payload += str(unique_dict[k])+" "

payload += f'{end_index}) DO set {random_string_final}=!{random_string_final}!!{random_string_unique}:~%A,1!&& IF %A=={end_index} CALL %{random_string_final}:~-{len(char_dict.values())}%"'
print("Your obfuscated payload is: ", payload)
