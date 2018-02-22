def get(k,base):
    out = []
    while True:
        rem = k % base
        k = k / base
        out.insert(0, rem)
        if k == 0:
            break
    return ''.join([str(a) for a in out])
if __name__ == '__main__':
    print get(1020, 9)
