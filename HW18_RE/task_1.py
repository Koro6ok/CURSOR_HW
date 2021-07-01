import re

with open('django_success.log') as log_file:
    switch = ''.join(log_file.readlines())
    switch = re.sub(r'\/admin\/', '/secret/', switch)
    with open('new_django_success.log', 'a') as file:
        file.write(switch)