import yaml
import argparse


from core.etl import prepare_dataset



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", type=str, choices=["dev", "test", "prod"], required=True)

    args = parser.parse_args()
    
    env = args.env

    try:
        with open(f'./config/{env}.yaml', 'r') as file:
            config_dict = yaml.safe_load(file)
    except FileNotFoundError as e:
        print(f"Error: Configuration file not found for environment {env}. Exception: {e}")
        exit(1)

    try:
        input_path = config_dict["input_path"]
        output_path = config_dict["output_path"]
        partition_cols = config_dict["partition_cols"]
    except KeyError as e:
        print(f"Error: Missing key(s) in configuration file for environment {env}. Missing key: {e}")
        exit(1)

    prepare_dataset(input_path, output_path, partition_cols)
    


if __name__ == "__main__":
    main()