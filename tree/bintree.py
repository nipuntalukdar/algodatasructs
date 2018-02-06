import random

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.r = None
        self.l = None

    def print_paths(self, nodes):
        if self.leaf():
            a = [str(x.val) for x in nodes]
            a.append(str(self.val))
            print(','.join(a))
            return
        nodes.append(self)
        if self.l:
            self.l.print_paths(nodes)
        if self.r:
            self.r.print_paths(nodes)
        nodes.pop()

    def count(self):
        count = 1
        if self.l:
            count += self.l.count()
        if self.r:
            count += self.r.count()
        return count

    def add(self, val):
        cur = self
        while True:
            if cur.val > val:
                if not cur.l:
                    cur.l = TreeNode(val)
                    break
                else:
                    cur = cur.l
            elif cur.val < val:
                if not cur.r:
                    cur.r = TreeNode(val)
                    break
                else:
                    cur = cur.r
            else:
                return

    def print_in_order(self):
        if self.l:
            self.l.print_in_order()
        print(self.val)
        if self.r:
            self.r.print_in_order()

    def print_post_order(self):
        if self.r:
            self.r.print_in_order()
        if self.l:
            self.l.print_in_order()
        print(self.val)

    def print_pre_order(self):
        print(self.val)
        if self.r:
            self.r.print_in_order()
        if self.l:
            self.l.print_in_order()

    def leaf(self):
        return not self.l and not self.r

    def if_right_child(self, parent):
        return parent.r == self

    def min_value(self):
        if not self: return None
        ret = self
        while ret.l:
            ret = ret.l
        return ret.val

    def max_value(self):
        if not self: return None
        ret = self
        while ret.r:
            ret = ret.r
        return ret.val

    def max_depth(self):
        depthl = 0
        depthr = 0
        if self.l:
            depthl += self.l.max_depth()
        if self.r:
            depthr = self.r.max_depth()
        return 1 + max(depthl, depthr)

    def kth_max(self, k):
        if self.r:
            val, k, found = self.r.kth_max(k)
            if k == 0 and found:
                return val, k, found
        if k == 0:
            return self.val, 0, True
        k -= 1
        if self.l:
            val, k, found = self.l.kth_max(k)
            return val, k, found
        return self.val, k, False

    def delete(self, val):
        if self.val == val:
            if not self.r:
                return self.l
            elif not self.l:
                return self.r
            else:
                next_max = self.l.max_value()
                self.l = self.l.delete(next_max)
                self.val = next_max
                return self
        elif self.val < val:
            if self.r:
                self.r = self.r.delete(val)
        else:
            if self.l:
                self.l = self.l.delete(val)
        return self


class Tree(object):
    def __init__(self, root):
        self.root = root

    def max_depth(self):
        if not self.root:
            return 0
        return self.root.max_depth()

    def print_paths(self):
        if not self.root:
            return
        self.root.print_paths([])

    def count(self):
        if not self.root:
            return 0
        return self.root.count()

    def add(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self.root.add(val)

    def print_in_order(self):
        if self.root:
            self.root.print_in_order()

    def print_pre_order(self):
        if self.root:
            self.root.print_pre_order()

    def print_post_order(self):
        if self.root:
            self.root.print_post_order()

    def delete(self, val):
        if not self.root:
            return
        self.root = self.root.delete(val)

    def max_value(self):
        if not self.root:
            return None
        return self.root.max_value()

    def min_value(self):
        if not self.root:
            return None
        return self.root.min_value()

    def kth_max(self, k):
        if not self.root:
            return -1, k
        return self.root.kth_max(k)

def check_kth():
    tree = Tree(None)
    j = 500
    x = [random.randint(1, 10000000) for a in range(0,j)]
    for a in x:
        tree.add(a)
    i = 0
    x = [a for a in set(x)]
    x.sort()
    while i < j:
        val = tree.kth_max(i)
        if val[0] != x[j - 1 - i]:
            print "Problem ", val[0], x[j - 1 - i], j - 1 -i, x
            break
        i += 1

if __name__ == '__main__':
    tree = Tree(None)
    tree.add(100)
    tree.add(2)
    tree.add(1)
    tree.add(4)
    tree.print_in_order()
    print ""
    tree.print_post_order()
    print ""
    tree.print_pre_order()
    print ""
    print tree.max_value()
    print ""
    print tree.min_value()

    print("...")
    tree.delete(4)
    tree.delete(100)
    tree.delete(4)
    tree.delete(100)
    tree.delete(1)
    tree.delete(2)
    x = []
    i = 0
    while i < 100:
        x.append(random.randint(1, 100))
        i += 1
    for num in x:
        tree.add(num)
    print("Size after adding 100 random numbers {}".format(tree.count()))
    i = 0
    while i < 50:
        tree.delete(x[i])
        i += 1
    print("Size after removing 50 random numbers {}".format(tree.count()))
    x = []
    i = 0
    while i < 100:
        x.append(random.randint(1, 10000))
        i += 1
    for num in x:
        tree.add(num)
    print("Size after adding 100 random numbers {}".format(tree.count()))
    tree.print_paths()
    check_kth()
