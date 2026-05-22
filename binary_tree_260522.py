tree = {}

def make_tree(N):
    global tree
    tree = {}

    for _ in range(N):
        data, left, right = input("노드를 입력하세요 : ").split()
        tree[data] = [left, right]

# preorder (선위 순회)
def preorder(data):
    if data == ".": return

    print(data, end=" ")
    preorder(tree[data][0])
    preorder(tree[data][1])

# inorder (중위 순회)
def inorder(data):
    if data == ".": return

    inorder(tree[data][0])
    print(data, end=" ")
    inorder(tree[data][1])

# postorder (후위 순회)
def postorder(data):
    if data == ".": return

    postorder(tree[data][0])
    postorder(tree[data][1])
    print(data, end=" ")

N = int(input("노드의 개수를 입력하세요 : "))
make_tree(N)

root = input("뿌리 노드를 입력하세요 : ")
preorder(root)
print()
inorder(root)
print()
postorder(root)