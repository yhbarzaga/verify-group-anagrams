## Solution for group anagrams given a list

---
## How to Run?
1. Open a terminal placed in the same folder as `main.py` file
2. Execute following command
```shell
python ./main.py --list <each value separate by space only, no brackets>
```

e.g.
```shell
python ./main.py --list "affx" "a" "ab" "ba" "nnx" "xnn" "cde" "edc" "dce" "xffa"
```
then you should get printed something like:
```
[['affx', 'xffa'], ['a'], ['ab', 'ba'], ['nnx', 'xnn'], ['cde', 'edc', 'dce']]
```
