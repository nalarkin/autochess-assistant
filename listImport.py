"""
TODO: Make list of comps that are viable, make the list of unit names in each
TODO: Use console to input units you have into a list
TODO: Select a archetype to follow using console
TODO: Given you select this archetype and have these units, recommend which
    units you are looking for to complete build
TODO: Sugguest which comp you should go based on the least amount of units
        you would need to buy to complete synergies





"""

import pandas, os
os.chdir("C:\\Users\\Nathan\\Downloads")

df = pandas.read_csv("AutoChess_units.csv", index_col=0)
unit_index = df.index
unit_columns = df.columns
unit_dict = {}

for unit in unit_index:
    spec1 = df.loc[unit, "Spec"]
    spec2 = df.loc[unit, 'Unnamed: 2']
    synergy = df.loc[unit, 'Class']
    unit_dict[unit] = [[spec1, spec2], synergy]

print(unit_dict)
