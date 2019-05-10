"""
TODO:   Add more comps to use
TODO:   Look into reducing the number of function arguments and global
        constants in each function by using classes
TODO:   Look at functions and refractor them to follow SOLID principles
TODO:   Handle mistyped unit names
TODO:   Ignore capitalization of inputted units

"""

import pandas, os

"""
This program keeps track of suggests team comps and keeps track of user
pieces they input. Then it displays the units they need to buy to complete
composition.

"""

"""
Workflow:

- user enters units they currently have
- program suggests comps
- user selects comp
- program prints full comp
- program prints the pieces they need to complete comp
- user updates pieces they have
- program retrieves new list of pieces to print
"""


def create_database():
    # os.chdir("C:\\MyPythonScripts\\autochess-assistant\\autochess-assistant")
    return pandas.read_csv("AutoChess_units.csv", index_col=0)


def import_compositions():
    # os.chdir("C:\\MyPythonScripts\\autochess-assistant\\autochess-assistant")
    return pandas.read_csv("end_game_compositions.csv", index_col=0)


def create_unit_dict(unit_dataframe):
    unit_dict = {}
    unit_index = unit_dataframe.index
    for unit in unit_index:
        spec1 = unit_dataframe.loc[unit, "Spec"]
        spec2 = unit_dataframe.loc[unit, 'Unnamed: 2']
        synergy = unit_dataframe.loc[unit, 'Class']
        unit_dict[unit] = [[spec1, spec2], synergy]
    return unit_dict


# key, value where key is composition name, value is a set() of units in comp
def create_composition_dict(compositions):
    comp_dict = {}
    comp_index = compositions.index
    for comp in comp_index:
        if comp != "S" and comp != "A":
            unit_list = compositions.loc[comp, "Unnamed: 1"].split(
                    sep=', ')
            comp_set = turn_list_into_set(unit_list)
            comp_dict[comp] = comp_set
    return comp_dict


def ask_user_for_units(previously_owned_units=None):
    if previously_owned_units:
        print()
        response = input("Add more units here, or type 's' to stop: -> "
                         ).split(sep=', ')

        if response[0] == 's':
            return None
        new_units = turn_list_into_set(response)
        previously_owned_units = previously_owned_units.union(new_units)
        print()
        return previously_owned_units
    else:           # to create a new list
        input_current_units = input("What units do you current have? (separate "
                                    "by comma) ").split(sep=', ')
        unit_set = turn_list_into_set(input_current_units)
    return unit_set


def turn_list_into_set(unit_list):
    unit_set = set()
    assert(unit_list), "supplied list is empty"
    for element in unit_list:
        unit_set.add(element)
    return unit_set


# find available comps the user can play with given pieces
def find_total_unit_match_count(complete_comp_dict, current_units):
    comps_with_unit_count = []
    for comp, comp_units in complete_comp_dict.items():
        matching_unit_counter = 0
        for owned_unit in current_units:
            if owned_unit in comp_units:
                matching_unit_counter += 1
        if matching_unit_counter > 0:
            comps_with_unit_count.append((matching_unit_counter, comp))
    # sort comps in descending order of unit matches
    comps_with_unit_count.sort(reverse=True)
    return comps_with_unit_count


# prompt user to select comp they want to play (they can respond with
# numbers 1, 2, 3, etc. which corresponds to index[] + 1
# save the  name they choose as a variable string object
# return final_comp
def user_selects_comp_to_play(remaining_comps):
    response = print_comp_options(remaining_comps)
    # remaining_comps[] returns tuple (units , comp name)
    selected_comp = remaining_comps[response - 1]
    selected_comp = selected_comp[1]
    final_comp = complete_comp_dict[selected_comp]
    return final_comp


def print_comp_options(remaining_comps):
    counter = 1
    print()
    for comp in remaining_comps:
        print("#{0}: {1}-----{2} matching units".format(str(counter), comp[1],
                                                        comp[0]))

        counter += 1
    print()
    response = int(input("Which comp would you like to play (enter number)? "))
    print()
    return response


# use selected_comp to search complete_comp_dictionary's list of units
# add all units to a list
# print selected comp units (full list)
# return list
def print_final_comp():
    # print("Final Comp is: " + str(final_comp))
    print("final comp is = {}".format(final_comp))
    print()


def keep_updating_current_units(units_owned, final_comp):
    response = ""
    # print("current units: {}".format(current_units))
    while units_owned:
        updated_units_need = final_comp.difference(units_owned)
        print("=+=" * 35)
        print("You need these units!{}".format(updated_units_need))
        print("=+=" * 35)
        units_owned = ask_user_for_units(units_owned)


unit_dataframe = create_database()  # pandas imported csv file
compositions = import_compositions()        # pandas imported csv file
complete_unit_dict = create_unit_dict(unit_dataframe)     # dictionary that contains all units
                                            # with synergys and class
complete_comp_dict = create_composition_dict(compositions)  # dict (composition, units) with meta
                                                #  unit compositions
current_units = ask_user_for_units()     # first time user is requested for units
comps_with_unit_count = find_total_unit_match_count(complete_comp_dict, current_units)      # find available comps
final_comp = user_selects_comp_to_play(comps_with_unit_count)      # give user choice in selecting comp
# progress_list = []
print_final_comp()
keep_updating_current_units(current_units, final_comp)        # process runs until user types 's'
# retrieve_pieces()

