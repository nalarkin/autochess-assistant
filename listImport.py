"""
TODO: Have program order the comp choice by number of unit matches

TODO: Tell the user what units they have left to complete comp, possibly use
pop()

TODO: fix internal style in select_comp()

TODO: Handle mistyped unit names

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


def create_composition_dict(compositions):
    comp_dict = {}
    comp_index = compositions.index
    for comp in comp_index:
        if comp != "S" and comp != "A":
            comp_dict[comp] = compositions.loc[comp, "Unnamed: 1"].split(
                sep=', ')
    return comp_dict


def request_units(unit_list=None):
    if unit_list:       # used to update a list of units that already exists
        print()
        response = input("Add more units here, or type "
                         "'s' to stop: "
                         "").split(
                sep=', ')
        if response[0] == 's':
            return None
        input_current_units = unit_list + response
        print()
    else:           # to create a new list
        input_current_units = input("What units do you current have? (separate by "
                           "comma) ").split(sep=', ')
    return input_current_units


# traverse through complete_comp_dict, if any key matches a unit they
# they have, add the comp name to a new list
# return list called potential_comps
def suggest_comps():
    pass


# find available comps the user can play with given pieces
def find_comps(complete_comp_dict):
    remaining_comps = []
    for comp, comp_units in complete_comp_dict.items():
        matching_unit_counter = 0
        for owned_unit in current_units:
            if owned_unit in comp_units:
                matching_unit_counter += 1
        if matching_unit_counter > 0:
            remaining_comps.append((matching_unit_counter, comp))
    remaining_comps.sort(reverse=True)
    return remaining_comps


# prompt user to select comp they want to play (they can respond with
# numbers 1, 2, 3, etc. which corresponds to index[] + 1
# save the  name they choose as a variable string object
# return final_comp
def select_comp(remaining_comps):
    counter = 1
    print()
    for comp in remaining_comps:
        print("#{0}: {1}-----{2} matching units".format(str(counter), comp[1],
                                                        comp[0]))

        counter += 1
    print()
    response = int(input("Which comp would you like to play (enter number)? "))
    print()
    selected_comp = remaining_comps[response - 1]       # returns tuple (
                                                        # matching units , comp name)
    selected_comp = selected_comp[1]        # selects the comp name out of tuple
    final_comp = complete_comp_dict[selected_comp]
    return final_comp


# use selected_comp to search complete_comp_dictionary's list of units
# add all units to a list
# print selected comp units (full list)
# return list
def initialize_comp():
    # print("Final Comp is: " + str(final_comp))
    print("final comp is = {}".format(final_comp))
    print()

# list of units in comp - owned_units = units_needed
# return units_needed
def retrieve_pieces():
    for unit in final_comp:
        if current_units.__contains__(unit):
            progress_list.append(final_comp.pop(final_comp.index(unit)))
    print("Collected Units =  {}".format(str(progress_list)))
    print("Units left  = {}".format(str(final_comp)))
    return final_comp

def keep_updating(current_units, final_comp):
    response = ""
    # print("current units: {}".format(current_units))
    while current_units:
        actual_final_comp = []
        for unit in final_comp:
            if not current_units.__contains__(unit):
                actual_final_comp.append(unit)
        print("You need these units!{}".format(actual_final_comp))
        print()
        current_units = request_units(current_units)

def check_units():
    #     for unit in current_units:
    #         if unit in current_units:
    #             pass
    #         else:
    #             # PROMPT USER TO RETYPE UNIT
    pass


unit_dataframe = create_database()  # pandas imported csv file
compositions = import_compositions()        # pandas imported csv file
complete_unit_dict = create_unit_dict(unit_dataframe)     # dictionary that contains all units
                                            # with synergys and class
complete_comp_dict = create_composition_dict(compositions)  # dict (composition, units) with meta
                                                #  unit compositions
current_units = request_units()     # first time user is requested for units
remaining_comps = find_comps(complete_comp_dict)      # find available comps
final_comp = select_comp(remaining_comps)      # give user choice in selecting comp
# progress_list = []
initialize_comp()
keep_updating(current_units, final_comp)        # process runs until user types 's'
# retrieve_pieces()

