# read the data from data source
# savve it in the data/raw for further processing

import os
from get_data import read_params,get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    # replacing the space in csv file (header data)
    new_cols = [col.replace(" ","_") for col in df.columns]
    # storing the replaced data in raw folder. using the params.yaml
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path,sep=",",index=False,header=new_cols)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    # we just reading the params.yaml
    args.add_argument("--config",default = "params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path = parsed_args.config)