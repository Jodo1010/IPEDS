""" DESCRIPTION OF MODULES """


data_collection_all:

    This module contains individual functions that collects all available
    historical data for a given unit id.

data_collection_yearly:

    This module contains individual functions that collect data for a given unit id and
    data year(s).

master_function_all:

    This module calls several functions [TBD] from the data_collection_all module and stores the result
    of each function in separate worksheets in a workbook.

master_function_yearly:

    This module calls several functions [TBD] from the data_collection_yearly module and stores the result
    of each function in separate worksheets in a workbook.

institution_mapping:

    This module contains functions that output a dictionary and DataFrame with for all 6,400+ institution names
    and their unit ids.

    The dictionary is in the following takes a dictionary as values and the key is the institution's name. For
    example, {'Eastern Michigan University': {STABBR: 'MI', UNITID: 169798} }. A user can create subsets of the data
    by State.

references:

    This is a helper module to store useful references for the project e.g., MASU dictionary containing unit ids
    and their corresponding institution names.


""" VERSIONS AND RELEASE DATES """

1.0.0: 2024-08-11

1.1.0: 2024-08-19

(a) data_collection_yearly
(b) directory data
(c) references (institutional mapping with sub-setting features and MASU dictionary )


