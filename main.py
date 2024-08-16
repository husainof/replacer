import argparse


def read_config(config_file: str) -> dict[str, str]:
    replacements = {}
    with open(config_file, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            replacements[key] = value
    return replacements

def replace_value(config: dict[str, str], line: str) -> (str, int):
    new_line = line
    for key, value in config.items():
        if key in line:
            new_line = new_line.replace(key, value)
    changes = sum(1 for a, b in zip(line, new_line) if a != b)
    return new_line, changes

def replace_values(rules: dict[str, str], lines: list[str]) -> list[str]:
    changes = {}
    for i, line in enumerate(lines):
        lines[i], changes[i] = replace_value(rules, line)
    sorted_changes = sorted(changes.items(), key=lambda x: x[1], reverse=True)
    return [lines[i] for i, _ in sorted_changes]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Replace values in a text file')
    parser.add_argument('config_file', help='Path to the configuration file')
    parser.add_argument('text_file', help='Path to the text file')
    args = parser.parse_args()

    config = read_config(args.config_file)

    with open(args.text_file, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))

    replaced_lines = replace_values(config, lines)

    with open(args.text_file, 'w') as f:
        f.writelines(list(map(lambda x: x+"\n", replaced_lines)))

    for line in replaced_lines:
        print(line)
