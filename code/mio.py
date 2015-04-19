# TODO 
# refactor this into a class, remove globals, encode the types of reading and
# writing formats that are supported explicitly, e.g. for csv file types

import os
import pandas as pd


def read_parameter(configdict):
    """
    Parse dictionary and replace keywords with data, currently supports
    reading static data and data from csv through keyword _CSV
    """
    newdict = {}
    for key in configdict.keys():
        if key.endswith("_CSV"):
            newkey = key.split("_CSV")[0]
            filepath = configdict[key]
            filepath = os.path.join(DATA_DIR, filepath)  # NOQA
            newval = pd.read_csv(filepath, index_col="date", parse_dates=True)
            newdict[newkey] = newval
        else:
            newdict[key] = configdict[key]
    return newdict


def write_output(df, filename, index_label="date"):
    """
    Handles writing of output, currently supports a pandas DataFrame
    """
    filepath = os.path.join(OUTPUT_DIR, filename)  # NOQA
    df.to_csv(filepath, index_label=index_label)


def main_input(configkey):
    """
    This serves as the interface for any calls to a process. The only command
    line arguments that should be passed are the output directory to write
    process output, the datadir to read data from and a monitoring directory
    to write intermittent data and graphs

    Returns
    -------
    Dictionary of parameters to be passed to the process
    function
    """
    import argparse
    from config import config
    from mio import read_parameter
    parser = argparse.ArgumentParser()
    parser.add_argument("outputdir", help="Directory to write output")
    parser.add_argument("--datadir", "-d", help="Directory to read input from",
                        default=None)
    parser.add_argument("--monitoring", "-m", help="Folder to ouput "
                        "intermittent data, if nothing given defaults to None",
                        default=None)
    args = parser.parse_args()
    global DATA_DIR
    DATA_DIR = args.datadir
    global OUTPUT_DIR
    OUTPUT_DIR = args.outputdir
    params = read_parameter(config[configkey])
    if args.monitoring:
        params["monitoring"] = args.monitoring
    return params
