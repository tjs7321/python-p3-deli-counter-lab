# katz_deli = []

def line(katz_deli):
    queue_list = []
    queue_num = 1
    for name in katz_deli:
        queue_list.append(f'{queue_num}'+'.'+' '+name)
        queue_num += 1
    if katz_deli == []:
        print("The line is currently empty.")
    else: print(f"The line is currently: {' '.join(queue_list)}")
    pass

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")
    pass

def now_serving(katz_deli):
    if katz_deli == []:
        print('There is nobody waiting to be served!')
    else:
        print(f'Currently serving {katz_deli[0]}.')
        del katz_deli[0]
    pass