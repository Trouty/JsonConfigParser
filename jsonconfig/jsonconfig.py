import json

def _load_config(file_location):
    # Private function for loading JSON file into memory
    with open(file_location, "r") as config_file:
        config = json.load(config_file)
    
    return config

def _update_config(file_location, config, indent_size):
    # Private function for writing the config dictionary stored in memory to JSON file
    with open(file_location, "w") as config_file:
        json.dump(config, config_file, indent=indent_size)

class JsonConfig:
    def __init__(self, file_location, keep_structure=False):
        self.file_location = file_location
        self.config = _load_config(file_location)

        if keep_structure == True:
            self.keep_structure = 4
        else:
            self.keep_structure = 0
    
    def set_variable(self, section, variable, value):
        self.config[section][variable] = value

        _update_config(self.file_location, self.config, self.keep_structure)
    
    def get_variable(self, section, variable):
        value = self.config[section][variable]

        return value
    
    def get_section(self, section):
        value = self.config[section]

        return value
    
    def new_variable(self, section, variable, value):
        self.config[section][variable] = value

        _update_config(self.file_location, self.config, self.keep_structure)
    
    def new_section(self, section):
        self.config[section] = {}

        _update_config(self.file_location, self.config, self.keep_structure)
        
    def delete_section(self, section):
        del self.config[section]

        _update_config(self.file_location, self.config, self.keep_structure)

    def delete_variable(self, section, variable):
        del self.config[section][variable]

        _update_config(self.file_location, self.config, self.keep_structure)
