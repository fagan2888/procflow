"""
This module defines what the process parameters are. The flow of how the
processes are chained together is specified in the Makefile. Data files
such as csv files paths are defined relative to the DATA variable defined
in the Makefile. Keys ending with _VAR, e.g. _CSV, are keywords indicating
that this string should be interpreted in a special way, for example _CSV
indicates that the value should be read as a pandas dataframe. These rules
are defined in mio.py
"""

config = {
    "example": {"df_CSV": "example.csv",
                 "scalar": 5},
    "exampledata": {"seed": 123} 
}
