import os
command = ''


class Manipulator:
    @staticmethod
    def create(create_command):
        with open(create_command.split('-')[-1], 'w') as twinkle: pass

    @staticmethod
    def add(add_command):
        with open(add_command.split('-')[1], "a") as sylvan: sylvan.write(f"{add_command.split('-')[-1]}\n")

    @staticmethod
    def check_file(check_command):
        try:
            with open(check_command.split('-')[1], 'r') as silhouette: content = silhouette.read()
        except FileNotFoundError:
            return 'Failed'

    @staticmethod
    def replace(replace_command):
        with open(replace_command.split('-')[1], 'r') as stellar: content = stellar.read()
        with open(replace_command.split('-')[1], 'w') as quell: quell.write(content.replace(replace_command.split('-')[2], replace_command.split('-')[-1]))

    @staticmethod
    def delete(delete_command):
        try:
            print(f"The file '{delete_command.split('-')[-1]}' has been deleted."), os.remove(delete_command.split('-')[-1])
        except FileNotFoundError:
            print(f"An error occurred")


while command != 'End':
    command = input()
    if command == 'End':
        continue
    if 'Create' in command:
        Manipulator().create(command)
    elif 'Add' in command:
        Manipulator().add(command)
    elif 'Replace' in command:
        print("An error occurred") if Manipulator().check_file(command) == 'Failed' else Manipulator().replace(command)
    elif 'Delete' in command:
        print("An error occurred") if Manipulator().check_file(command) == 'Failed' else Manipulator().delete(command)
