import yaml
import io


class ConfigParser():
    def __init__(self):
        self.config = None
        self.load()
        
    def load(self):
        with open("config/config.yml", 'r') as stream:
            self.config = yaml.safe_load(stream)

    def save(self):
        with io.open('config/config.yml', 'w', encoding='utf8') as outfile:
            yaml.dump(self.config, outfile, default_flow_style=False, allow_unicode=True)
