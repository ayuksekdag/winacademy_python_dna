from helpers import get_countries
""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"
""" Write your functions here. """


def shortest_names(lijst):
    shortest_length = len(min(lijst, key=len))
    print(f"length of shortest name is {shortest_length}")
    list_of_shortest_names = []
    for i in lijst:
        if len(i) == shortest_length:
            list_of_shortest_names.append(i)
    return list_of_shortest_names


def most_vowels(lijst):
    vowels = ['a', 'e', 'i', 'o', 'u']
    all_vowels_length = []

    for i in lijst:
        i = i.lower()
        #print(i)
        total_vows_in_string = sum([1 for char in set(i) if char in vowels])

        #print(f"{i} has {tot_vows_in_string}")
        all_vowels_length.append([i, total_vows_in_string])
    #print(all_vowels_length)
    all_vowels_length.sort(key=lambda x: x[1], reverse=True)

    #print(all_vowels_length)

    returnlist = []
    for i in range(3):
        # i index in list [0] is the first kolom of every interation
        returnlist.append(all_vowels_length[i][0])
    return returnlist


def sub_alphabet_set(lijst, vowels):
    rank_list = []
    for i in lijst:
        j = i.lower()
        #print(i)
        total_vows_in_string = sum([1 for char in set(j) if char in vowels])
        #print(f"{i} has {tot_vows_in_string}")
        rank_list.append([i, total_vows_in_string])
    #print(all_vowels_length)
    rank_list.sort(key=lambda x: x[1], reverse=True)
    returnlist = []
    #print(all_vowels_length)
    val1 = rank_list[0][0]
    print(val1)
    returnlist.append(rank_list[0][0])
    return returnlist


def alphabet_set(lijst):
    vowels = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    #lijst = [x.lower() for x in lijst]

    endlist = []
    while bool(len(vowels)):
        a = sub_alphabet_set(lijst, vowels)
        endlist.append(a)
        b = a[0].lower()

        vowels = list(set(vowels) - set(b))
        print(a)
        print(type(a))
        lijst.remove(a[0])
        #print(f"step{i}\n")
        print(vowels)

    print(endlist)
    return endlist


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
    """ Write the calls to your functions here. """
    shortest_list = shortest_names(countries)
    print(shortest_list)
    top_List_Vowels = most_vowels(countries)
    #print(top_List_Vowels)
    top_List_Aphabet = alphabet_set(countries)
    print(top_List_Aphabet)