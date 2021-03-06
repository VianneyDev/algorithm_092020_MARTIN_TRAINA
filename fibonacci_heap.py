class Heap(object):
    """
    Une heap est une structure de données sous forme d'arbre.
    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """
    

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        pass

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        pass

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        """
        Fusionne deux arbres
        """
        pass


class Tree(object):
    def __init__(self):
        self.nodes = []
        self.count = 0

    def add_value(self, value):
        self.nodes.append(value)
        self.count = self.count + 1

    def __repr__(self):
        return repr(self.nodes)

class FibonacciHeap(Heap):
    """
    Une fibonnaci heap est un arbre permettant de stocker et trier des donnés efficacement
    https://en.wikipedia.org/wiki/Fibonacci_heap
    L'implémentation est décrite en anglais : https://en.wikipedia.org/wiki/Fibonacci_heap#Implementation_of_operations
    et en français : https://fr.wikipedia.org/wiki/Tas_de_Fibonacci#Implémentation_des_opérations
    """
        
    def __init__(self):
        self.nodes = []
        self.count = 0
        self.min_node = None

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        new_tree = Tree()
        new_tree.add_value(value)
        if self.min_node is None or self.min_node > value:
            self.min_node = value
        self.nodes.append(new_tree)
        self.count = self.count + 1


    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        return self.min_node

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """


    def merge(self, fibonnaci_heap: Heap) -> None:
        """
        Fusionne deux arbres
        """
        


new_heap = FibonacciHeap()
data = [10, 12, 14, 52, 54, 101, 152, 4, 7, 17]

# data = [[10, [17]], [12], [14], [52], [101], [152], [4], [7]]
# data = [[10, [17]], [14], [52], [101], [152], [4], [7, [12]]]

for value in data:
    new_heap.insert(value)


print("La liste est donc :")
print(new_heap.nodes)
print ("Le minimum est :")
print(new_heap.find_min())

new_heap.insert(3)
print ("Valeur insérée est 3")

print ("La nouvelle liste est donc :")
print(new_heap.nodes)
print("Le nouveau minimum est donc :")
print(new_heap.find_min())
