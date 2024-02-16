import argparse
import os
import sys
from collections import defaultdict


def group_anagrams(collection: list[str]) -> list[list[str]]:
    """Given a list of anagrams group them"""
    group = defaultdict(list)

    for word in collection:
        group["".join(sorted(word))].append(word)

    result = list(group.values())

    return result


if __name__ == "__main__":
    sys.path.append(os.getcwd())
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', type=str, nargs='+')
    args = parser.parse_args()

    print(group_anagrams(list(args.list)))
