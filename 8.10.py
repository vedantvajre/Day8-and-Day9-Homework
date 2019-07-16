magicians_list = ['Derren Brown', 'Michael Carbonaro', 'David Blaine', 'David Copperfield']


def show_magicians(magicians_name):
    for magician_name in magicians_list:
        print(magician_name.title())


show_magicians(magicians_list)


def make_great(magicians):
    for magicians in magicians_list:
        print('The Great ' + magicians)


make_great(magicians_list)