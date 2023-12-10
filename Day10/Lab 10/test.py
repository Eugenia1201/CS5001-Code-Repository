
import jsonpickle

global config
with open("forestconfig.json", "r", newline="") as in_file:
    config_en = in_file.read()
    config_de = jsonpickle.decode(config_en)
    print(config_de.__dict__)
