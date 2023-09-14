from .priority_queue_base import PriorityQueueBase, Empty, PositionalList


class SortedPriorityQueue(PriorityQueueBase):
    """Una cola de prioridad implementada con una lista ordenada."""

    def __init__(self):
        """Crea una nueva cola de prioridad vacía."""
        self._data = PositionalList()

    def __len__(self):
        """Devuelve el número de elementos en la cola de prioridad."""
        return len(self._data)

    def __str__(self):
        """Devuelve una representación de cadena de la cola de prioridad."""
        return ", ".join([str(item) for item in self._data])

    def add(self, key, value):
        """Añade un par clave-valor."""
        newest = self._Item(key, value)  # crea un nuevo elemento
        walk = self._data.last()  # camina hacia atrás, buscando el menor
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)  # nueva clave es la menor
        else:
            self._data.add_after(walk, newest)  # nueva clave va luego de walk

    def min(self):
        """Devuelve pero no elimina el par clave-valor con la clave mínima."""
        if self.is_empty():
            raise Empty("La cola de prioridad está vacía")
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Elimina y devuelve el par clave-valor con la clave mínima."""
        if self.is_empty():
            raise Empty("La cola de prioridad está vacía")
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
