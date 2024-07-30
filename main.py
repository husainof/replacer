import argparse

def read_config(config_file):
    replacements = {}
    with open(config_file, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            replacements[key] = value
    return replacements

def replace_values(config, lines):
    changes = {}
    for i, line in enumerate(lines):
        old_line = line
        for key, value in config.items():
            line = line.replace(key, value)
        if line != old_line:
            changes[i] = sum(1 for a, b in zip(old_line, line) if a != b)
            lines[i] = line

    sorted_changes = sorted(changes.items(), key=lambda x: x[1], reverse=True)
    for i, _ in sorted_changes:
        print(lines[i].strip())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Replace values in a text file')
    parser.add_argument('config_file', help='Path to the configuration file')
    parser.add_argument('text_file', help='Path to the text file')
    args = parser.parse_args()
    config = read_config(args.config_file)
    with open(args.text_file, 'r') as f:
        lines = f.readlines()
    replace_values(config, lines)