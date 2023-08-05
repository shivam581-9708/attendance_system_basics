def exiting_statement():
    print('thanks for peforming with us ')
    exit()
def wrong_input():
    print('invalid id or password\n')
    exit()

def adding():
    new_user_id =(input('enter the user id to be registered\n'))
    if new_user_id not in user_details:
        new_user_password = input('enter password')
        user_details[new_user_id] = new_user_password
        print('id', new_user_id, '\npassword', new_user_password)
        print('thank u for registering')
    else:
        print('username already exists')
        exit()

def viewing():
    # user_details.get(inp_user_id, 'not found')
    # user_details.get(user_pass, 'not found')
    print('user id:',inp_user_id)
    print('user password',user_pass)


def update():
    updating_number = input('enter the new password\n')
    user_details[inp_user_id] = updating_number
    print('password changed\nthank you')

def deleting():
    deleting_number = int(input('enter the id to be deleted:\n'))
    deleted = user_details.index(deleting_number)
    user_details.pop(deleted)


while True:
    user_details = {'1001': 'ash', '1002': 'shivoham', '1003': 'idk@qwe'}
    inp_user_id = (input('enter your user_id (Press "w" to exit):\n'))

    if inp_user_id == 'w':  # Press 'w' to exit the loop
        exiting_statement()
    else:

        found = False
        for element in user_details:
            if element == inp_user_id:
                found = True
                break

    if found:
        print('valid input, proceed further\n')
    else:
        wrong_input()

    user_pass = input('enter your password:\n')

    if user_pass == user_details.get(inp_user_id):
        print('valid id password proceed further:\n')
    else:
        wrong_input()

    operating_value = input('enter 1 for adding\nenter 2 for view\nenter 3 for changing password(update)\n'
                            'enter 4 for delete\npress w for exit\npress any other key for proceeding to mark attendance\n')

    if operating_value == '1':
        adding()
    elif operating_value == '2':
        viewing()
    elif operating_value == '3':
        update()
    elif operating_value == '4':
        deleting()
    elif operating_value=='w':
        exiting_statement()
    else:
        attendance = input('press "p" for marking the attendance (Press "w" to exit): ')
        if attendance=='w':
            exiting_statement()
        elif attendance == 'p':
            attendance_list = {inp_user_id: 'p'}
            inp_user_id_attendance=open(inp_user_id,'a')
            inp_user_id_attendance.write('p')
            print('attendance marked\nthank you')
            print(attendance_list)

        else:
            attendance_list = {inp_user_id: 'ab'}
            inp_user_id_attendance = open(inp_user_id, 'a')
            inp_user_id_attendance.write('\nab')

