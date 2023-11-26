# 1. Порівняти два об'єкти. Перевірка рівності нодів в бінарному дереві. Мати на увазі, що ноди рівні, коли їхні нащадки є еквівалентними.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

def is_equel(root1, root2)-> bool:
    if root1 == None and root2 == None:
            return True
    elif (root1 != None or root2 != None) and (root1 == None or root2 == None):
        return False
    
    if root1.value != root2.value:
        return False
    left = is_equel(root1.left, root2.left)
    # перевірка чи однакові по кількості нащадки (без перевірки щодо правої сторони)
    if not left:
        return False
    right = is_equel(root1.right, root2.right)
    if left and right:
        return True
    return False



