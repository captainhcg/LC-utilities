class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    @staticmethod
    def serialize(root):
        arr = []
        stack = []
        node = root
        while node or stack:
            while node:
                arr.append(str(node.val))
                stack.append(node)
                node = node.left
            arr.append("#")
            node = stack.pop().right
        arr.append("#")
        return ",".join(arr)

    @classmethod
    def deserialize(cls, s):
        it = iter(s.split(","))

        def makeNode(val):
            if val == "#":
                return None
            node = cls(int(val))
            node.left = makeNode(next(it))
            node.right = makeNode(next(it))
            return node
        return makeNode(next(it))
