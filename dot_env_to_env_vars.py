import sys, os
from dotenv import dotenv_values

def dot_env_to_env_vars(dotenvfile):
    if not dotenvfile:
        raise Exception(f"No .env file provided, please run: python {os.path.basename(__file__)} FILE_NAME")

    config = dotenv_values(dotenvfile)

    output = ""
    for k, v in config.items():
        output += f"{k}='{v}' "

    print(output.strip())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"No .env file provided, please run: python {os.path.basename(__file__)} FILE_NAME")
        sys.exit(1)
    dotenvfile = str(sys.argv[1])
    dot_env_to_env_vars(dotenvfile)