#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    hidd = dir(hidden_4)
    for item in range(0, len(hidd)):
        if "__" != hidd[item][:2]:
            print(hidd[item])
