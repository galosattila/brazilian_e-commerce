import yaml
import argparse


from core.etl import prepare_dataset



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", type=str, choices=["dev", "test", "prod"])

    args = parser.parse_args()
    
    env = args.env

    with open(f'./config/{env}.yaml', 'r') as file:
        config_dict = yaml.safe_load(file)

    input_path = config_dict["input_path"]
    output_path = config_dict["output_path"]
    partition_cols = config_dict["partition_cols"]

    prepare_dataset(input_path, output_path, partition_cols)
    


if __name__ == "__main__":
    main()