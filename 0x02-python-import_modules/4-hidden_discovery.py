#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    li = dir(hidden_4)
    for i in range(0, len(li)):
        if li[i][0] == '_' and li[i][1] == '_':
            continue
        else:
            print('{}'.format(li[i]))
