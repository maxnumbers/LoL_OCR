import configparser

# TODO implement properties in OCR
def parse_lol_config(config_file):

    config = configparser.ConfigParser()
    config.read(config_file)

    # TODO Add other fields as they become relevant
    try:
        self.cfg_height = int(config["General"]["Height"])
        self.cfg_width = int(config["General"]["Width"])
        self.cfg_mapscale = float(config["HUD"]["MinimapScale"])
        self.cfg_globscale = float(config["HUD"]["GlobalScale"])
    except:
        pass