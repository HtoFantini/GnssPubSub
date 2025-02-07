import os
import json

# TODO: load config is a definition from script, not from GPS remove from this repository


def load_config(config_file):
    """_summary_

    Args:
        config_file (_type_): _description_
    """
    if not os.path.exists(config_file):
        raise FileNotFoundError(
            f"Arquivo nao encontrado {config_file}"
        )

    with open(config_file, "r") as file:
        return json.load(file)


if __name__ == '__main__':
    d = load_config(r'C:\Users\Adm-Harpia\Desktop\Harpia_Harpyja_Projects\GpsPublisher\src\gpspublisher\config.json')
