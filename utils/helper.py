import configparser

# time constants
SECONDS_PER_MINUTE, SECONDS_PER_HOUR, SECONDS_PER_DAY = 60, 60 * 60, 24 * 60 * 60

# ===========================
# === common utils below ====
# ===========================

# reads properties from config.ini file
def read_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config
