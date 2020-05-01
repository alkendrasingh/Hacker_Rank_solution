def split_and_join(line):
    # write your code here
    a=line
    b='-'.join(a.split(' '))
    return b

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
