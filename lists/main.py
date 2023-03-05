# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line


def alphabetical_order(lijst):
    a = lijst.copy()
    a.sort()
    return (a)


def won_golden_globe(i):
    i = i.lower()
    print(i)
    golden_globe_movies = [
        'house of the dragon', 'the fabelmans', "jaws", 'memoirs of a geisha'
    ]
    myBool = i in golden_globe_movies
    return myBool


def remove_toto_albums(total_list):
    removelist=['Fahrenheit','The Seventh One' \
        ,'Toto XX (lead vocals on "Last Night" and “In A Word”)'\
            ,'Falling in Between (co-lead vocals on "Bottom Of Your Soul")'\
                ,'Toto XIV','Old Is New']
    localcopy = total_list.copy()
    #print(total_list)
    #print(removelist)
    for i in removelist:
        print(f"interating for val {i}")
        if (i in localcopy):
            localcopy.remove(i)
            print(f"removing {i}")
    return localcopy


if __name__ == "__main__":
    a = alphabetical_order(['Star Wars', 'Terminator', '1984', 'Godfather'])
    print(a)
    b = won_golden_globe('House of the dragon')
    print(b)
    c = remove_toto_albums(['Joseph Williams (re-released 2002)', 'Toto XIV'])
    print(c)