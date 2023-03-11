from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


def unique_koala_facts(number_of_iter):
    # my_set = set()
    my_unique_list = []
    i = 0
    while i < number_of_iter:
        my_unique_list.append(random_koala_fact())
        print(len(my_unique_list))
        i += 1
    # make unique
    my_unique_list = list(set(my_unique_list))
    nr_of_uniq = []
    nr_of_uniq.append(len(my_unique_list))
    return nr_of_uniq


def num_joey_facts():
    return True


def koala_weight():
    return True


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())
    a = unique_koala_facts(1000)
    print(a)

    a = int()
    a = 10
    a = 11
    print(a)
