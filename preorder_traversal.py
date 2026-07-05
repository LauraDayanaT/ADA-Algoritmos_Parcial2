class Node:
    def __init__(self, d):
        self.info = d
        self.left = None
        self.right = None

def preOrder(root):
#Solucion implementada
    if root is None:
        return
    
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data <= root.info:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

if __name__ == '__main__':
    print("--- EJECUCIÓN AUTOMÁTICA: TREE PREORDER ---")
    
    nodos_input = 6
    valores_input = [1, 2, 5, 3, 4, 6]
    
    print(f"Cantidad de nodos cargados: {nodos_input}")
    print(f"Valores del árbol cargados: {valores_input}")
    
    root = None
    for valor in valores_input:
        root = insert(root, valor)
    
    print("\nResultado del recorrido en Preorden:")
    preOrder(root)
    print("\n-------------------------------------------")
