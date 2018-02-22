class lstnode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def __str__(self):
        return str(self.val)

class lst(object):
    def __init__(self, *args):
        self.begin = None
        self.count = 0
        self.end = {'blackhole' : 'yes', 'last' : None}
        for i in args:
            node = lstnode(i)
            node.next = self.end
            if not self.begin:
                self.begin = node
                node.next = self.end
                self.end['last'] = node
                self.count = 1
            else:
                self.end['last'].next = node
                self.end['last'] = node
                self.count += 1

    def move_even_to_end(self):
       if not self.begin or self.count < 2:
           return
       penultimate = self.end['last']
       it = self.begin
       while it != penultimate and it.next != penultimate:
           evenel = it.next
           it.next = evenel.next
           evenel.next = penultimate.next
           penultimate.next = evenel
           it = it.next


    def __str__(self):
        if self.begin is None:
            return ''
        it = self.begin
        ret = ''
        while it != self.end:
            ret += str(it.val) + ' '
            it = it.next
        return ret
        
x = lst(1,2,3,4,5,6,7,8,9,10,11,12)
print x
x.move_even_to_end()
print x
