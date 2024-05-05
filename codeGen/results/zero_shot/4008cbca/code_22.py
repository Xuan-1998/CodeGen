def is_valid_config(config):
    for i in range(len(config) - 2):
        if config[i] == config[i + 1] and config[i] == config[i + 2]:
            return False
    return True
