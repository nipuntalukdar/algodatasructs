'''
This module implements a Radix tree
'''

class RadixTree(object):

    def __init__(self):
        self.__root__ = Radix('', False, None)
        self.__root__.parent__ = None
    
    def insert(self, element):
        self.__root__.insert(element, 0)

def common_start(a, b):
    cmplen = min(len(a), len(b))
    i = 0
    while i < cmplen:
        if a[i] != b[i]:
            break
        i += 1
    return i

class Radix(object):
    def __init__(self, prefix, endhere, parent):
        self.__edges__ = []
        self.__endhere__ = endhere
        self.__prefix__ = prefix
        self.__parent__ = parent

    def __str__(self):
        prefix = None
        if self.__parent__:
            prefix = self.__parent__.__prefix__
        ret = '[prefix={},parent={},end={}'.format(self.__prefix__, prefix, self.__endhere__)
        if len(self.__edges__) > 0:
            ret += '[children={'
            for i in self.__edges__:
                ret += '({})'.format(i)
            ret += '}]'
        return ret


    def __put_in_edges__(self, element):
        cmplen = 0
        for i in self.__edges__:
            cmplen = common_start(i.__prefix__, element)
            if cmplen > 0:
                return i.insert(element, 0)
        self.__edges__.append(Radix(element, True, self))
        return True

    def insert(self, element, start):
        cmplen = common_start(self.__prefix__, element[start:])
        if cmplen == len(self.__prefix__):
            if cmplen == len(element[start:]):
                self.__endhere__ = True
                return
            else:
                self.__put_in_edges__(element[start + cmplen:])
        elif cmplen < len(self.__prefix__):
            newprefix = self.__prefix__[:cmplen]
            remaining = self.__prefix__[cmplen:]
            oldeges = self.__edges__
            self.__prefix__ = newprefix
            self.__edges__ = [Radix(element[cmplen:], True, self)]
            rsub = Radix(remaining, self.__endhere__, self)
            self.__endhere__ = False
            rsub.__edges__ = oldeges
            self.__edges__.append(rsub)

    def delete(self, element):
        # TBD
        pass 

if __name__ == '__main__':
    rt = RadixTree()
    rt.insert('abcd')
    rt.insert('abef')
    rt.insert('abce')
    print rt.__root__


