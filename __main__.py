import An
import hashlib
from sys import argv


def md5_checksum(name, md5_hash='', block_size=81920):
    m = hashlib.md5()
    b = 128 * block_size

    try:
        with open(name, 'rb') as f:
            data = f.read(b)
            while len(data) > 0:
                m.update(data)
                data = f.read(b)
    except IOError:
        print('Error: Can not open file!')

    md5 = An.trim(md5_hash)
    if md5 == '':
        return m.hexdigest()
    else:
        return m.hexdigest() == md5


if __name__ == '__main__':
    l = len(argv)

    if l == 1:
        print('Error: no file input!')
    else:
        fname = argv[1]
        if l == 2:
            print(md5_checksum(fname))
        else:
            fname = argv[1]
            md5_org = argv[2]
            print(md5_checksum(fname, md5_org))
