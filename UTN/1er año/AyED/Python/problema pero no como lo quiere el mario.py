def switch_lights(initial_config, num_changes):
    n = len(initial_config)
    final_config = list(initial_config)

    for i in range(min(num_changes, n)):
        if initial_config[i] == 'O':
            final_config[i] = 'X'
        else:
            final_config[i] = 'O'

    if n > 1:
        for i in range(1, min(num_changes, n)):
            if final_config[i - 1] == 'O':
                if final_config[i] == 'O':
                    final_config[i] = 'X'
                else:
                    final_config[i] = 'O'

    return ''.join(final_config)


def main():
    num_test_cases = int(input())

    for _ in range(num_test_cases):
        initial_config, num_changes = input().split()
        num_changes = int(num_changes)
        result = switch_lights(initial_config, num_changes)
        print(result)


if __name__ == "__main__":
    main()