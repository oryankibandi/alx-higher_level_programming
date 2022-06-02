#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for item in range(0, len(dir(hidden_4))):
        if "__" != dir(hidden_4)[item][:2]:
            print(dir(hidden_4)[item])
