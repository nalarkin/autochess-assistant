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


import pandas, os


def create_database():
    os.chdir("C:\\Users\\Nathan\\Downloads")
    return pandas.read_csv("AutoChess_units.csv", index_col=0)


def import_compositions():
    os.chdir("C:\\MyPythonScripts\\autochess-assistant\\autochess-assistant")
    return pandas.read_csv("end_game_compositions.csv", index_col=0)


def create_unit_dict():
    unit_dict = {}
    unit_index = df.index
    for unit in unit_index:
        spec1 = df.loc[unit, "Spec"]
        spec2 = df.loc[unit, 'Unnamed: 2']
        synergy = df.loc[unit, 'Class']
        unit_dict[unit] = [[spec1, spec2], synergy]
    return unit_dict


def create_composition_dict():
    comp_dict = {}
    comp_index = compositions.index
    for comp in comp_index:
        if comp != "S" and comp != "A":
            comp_dict[comp] = compositions.loc[comp, "Unnamed: 1"]
    return comp_dict


def request_units():
    input_current_units = input("What units do you current have? (separate by "
                           "comma) ").split(sep=',')
    return input_current_units


def suggest_comps():
    # traverse through complete_comp_dict, if any key matches a unit they
    # they have, add the comp name to a new list
    # return list called potential_comps
    pass

def select_comps():
    # prompt user to select comp they want to play (they can respond with
    # numbers 1, 2, 3, etc. which corresponds to index[] + 1
    # save the comp name they choose as a variable string object
    # return selected_comp
    remaining_comps = {}
    print(current_units)
    for unit in current_units:
        print(complete_comp_dict.keys())
        for comp in complete_comp_dict.keys():
            search_units = [complete_comp_dict[comp]]
            print(search_units)
            if unit in search_units:
                print("unit = " + unit + "||| comp  = " + comp)






def initialize_comp():
    # use selected_comp to search complete_comp_dictionary's list of units
    # add all units to a list
    # print selected comp units (full list)
    # return list
    pass


def retrieve_pieces():
    # list of units in comp - owned_units = units_needed
    # return units_needed
    pass


def update_pieces():
    # ask user to type whenever they get a new unit that is part of the comp
    # add unit to the owned_units list
    pass


# def check_units(current_units):
#     for unit in current_units:
#         if unit in current_units:
#             pass
#         else:
#             # PROMPT USER TO RETYPE UNIT


df = create_database()
compositions = import_compositions()
complete_unit_dict = create_unit_dict()
complete_comp_dict = create_composition_dict()
current_units = request_units()
# print(complete_comp_dict)
select_comps()
