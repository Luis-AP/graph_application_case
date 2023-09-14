class Empty(Exception):
    """Error al intentar acceder a un elemento de un contenedor vacío."""

    pass


class PriorityQueueBase:
    """Clase abstracta que representa una cola de prioridad."""

    class _Item:
        """Clase ligera que almacena un par clave-valor."""

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

        def __repr__(self):
            return f"({self._key}, {self._value})"

    def is_empty(self):
        """Devuelve True si la cola de prioridad está vacía."""
        return len(self) == 0


class _DoublyLinkedBase:
    """Una base de clase que implementa una lista enlazada doble."""

    class _Node:
        """Nodo ligado a otros nodos con referencias a los nodos previos y siguientes."""

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

        def __str__(self):
            return str(self._element)

    def __init__(self):
        """Crea una lista enlazada doble vacía."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Devuelve el número de elementos en la lista enlazada doble."""
        return self._size

    def is_empty(self):
        """Devuelve True si la lista enlazada doble está vacía."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Añade un elemento entre dos nodos existentes y devuelve el nuevo nodo."""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Elimina un nodo de la lista y devuelve su elemento."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


class PositionalList(_DoublyLinkedBase):
    """
    Un contenedor de secuencia que permite el acceso posicional a los elementos.
    """

    # -------------------------- clase Position anidada --------------------------
    class Position:
        """Una abstracción que representa la ubicación de un solo elemento."""

        def __init__(self, container, node):
            """Debe utilizar el método _make_position para crear instancias de posición."""
            self._container = container
            self._node = node

        def element(self):
            """Devuelve el elemento almacenado en esta posición."""
            return self._node._element

        def __eq__(self, other):
            """Devuelve True si otras es una posición que representa el mismo lugar."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Devuelve True si otras no representa el mismo lugar."""
            return not (self == other)  # opuesto de __eq__

    # ------------------------------- métodos de utilidad  -------------------------------
    def _validate(self, p):
        """Devuelve la posición del nodo, o genera una excepción adecuada si es inválida."""
        if not isinstance(p, self.Position):
            raise TypeError("p debe ser de tipo Position")
        if p._container is not self:
            raise ValueError("p no pertenece a este contenedor")
        if p._node._next is None:
            raise ValueError("p ya no es válido")
        return p._node

    def _make_position(self, node):
        """Devuelve la posición del nodo, o None si es una centinela."""
        if node is self._header or node is self._trailer:
            return None  # no se debe exponer el centinela
        else:
            return self.Position(self, node)  # instancia de posición legítima

    # ------------------------------- métodos de acceso -------------------------------
    def first(self):
        """Devuelve la posición del primer elemento de la lista, o None si está vacía."""
        return self._make_position(self._header._next)

    def last(self):
        """Devuelve la posición del último elemento de la lista, o None si está vacía."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Devuelve la posición justo antes de p, o None si p es el primer elemento."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Devuelve la posición justo después de p, o None si p es el último elemento."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Genera un iterador de las posiciones de los elementos de la lista."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # ------------------------------- métodos de mutación -------------------------------
    def _insert_between(self, e, predecessor, successor):
        """Añade un elemento entre dos nodos existentes y devuelve la nueva posición."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Añade un elemento nuevo al principio de la lista y devuelve su posición."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Añade un elemento nuevo al final de la lista y devuelve su posición."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Añade un elemento nuevo justo antes de p y devuelve su posición.

        Genera ValueError si p no es válido.
        """
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Añade un elemento nuevo justo después de p y devuelve su posición.

        Genera ValueError si p no es válido.
        """
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Elimina y devuelve el elemento en la posición p.

        Genera ValueError si p no es válido.
        """
        original = self._validate(p)
        return self._delete_node(original)  # método heredado

    def replace(self, p, e):
        """Reemplaza el elemento en la posición p con e.

        Genera ValueError si p no es válido.
        """
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
