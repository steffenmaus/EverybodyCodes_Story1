from collections import defaultdict

with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]


class Node:
    def __init__(self, rank, symbol):
        self.rank = rank
        self.symbol = symbol
        self.child_l = None
        self.child_r = None

    def has_child_l(self):
        return self.child_l is not None

    def has_child_r(self):
        return self.child_r is not None

    def get_child_l(self):
        return self.child_l

    def get_child_r(self):
        return self.child_r

    def get_rank(self):
        return self.rank

    def get_symbol(self):
        return self.symbol

    def add(self, node):
        if node.get_rank() > self.rank:
            if self.has_child_r():
                self.child_r.add(node)
            else:
                self.child_r = node
        else:
            if self.has_child_l():
                self.child_l.add(node)
            else:
                self.child_l = node


root_l = None
root_r = None

for l in lines:
    _, _, l, r = l.split(" ")
    l_rank, l_symbol = l.split("=")[1][1:-1].split(",")
    r_rank, r_symbol = r.split("=")[1][1:-1].split(",")
    l_rank = int(l_rank)
    r_rank = int(r_rank)
    node_l = Node(int(l_rank), l_symbol)
    node_r = Node(int(r_rank), r_symbol)
    if not root_l:
        root_l, root_r = node_l, node_r
    else:
        root_l.add(node_l)
        root_r.add(node_r)


def get_all_levels(current, lvl, collector):
    collector[lvl].append(current)
    if current.has_child_l():
        get_all_levels(current.get_child_l(), lvl + 1, collector)
    if current.has_child_r():
        get_all_levels(current.get_child_r(), lvl + 1, collector)


def get_word_from_tree(root):
    levels = defaultdict(list)
    get_all_levels(root, 0, levels)
    word = "".join([n.get_symbol() for n in sorted(levels.items(), key=lambda t: len(t[1]))[-1][1]])
    return word


print(get_word_from_tree(root_l) + get_word_from_tree(root_r))
