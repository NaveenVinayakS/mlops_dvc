# Read params
# process
# return dataframe

import os
import yaml
import pandas as pd
import argparse

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def get_data(config_path):
    config = read_params(config_path)
    #print(config)
    # getting the path for data
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path,sep=",",encoding = 'utf-8')
    #print(df.head())
    return df
# simple comment


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    # we just reading the params.yaml
    args.add_argument("--config",default = "params.yaml")
    parsed_args = args.parse_args()
    data = get_data(config_path = parsed_args.config)