# QHEAP1 - HackerRank

## Descripción

Este proyecto contiene la solución al problema **QHEAP1** de HackerRank utilizando un **Min Heap** y la técnica de **Lazy Deletion**.

## Lenguaje

- Python 3

## Estructura del proyecto

```
.
├── heap.py
└── README.md
```

## Operaciones soportadas

El programa procesa tres tipos de consultas:

- `1 x`: Inserta el elemento `x` en el heap.
- `2 x`: Elimina el elemento `x`.
- `3`: Imprime el valor mínimo almacenado.

## Estrategia utilizada

Se utiliza:

- Un **Min Heap** implementado con la librería `heapq`.
- Un **set** llamado `deleted` para aplicar **Lazy Deletion**, evitando eliminar elementos directamente del heap.

## Complejidad computacional

| Operación | Complejidad |
|-----------|-------------|
| Insertar | O(log n) |
| Marcar como eliminado | O(1) |
| Imprimir mínimo | O(1) si no hay limpieza, O(log n) cuando se eliminan elementos marcados |

## Cómo ejecutar

```bash
python heap.py
```

Luego ingrese las consultas siguiendo el formato solicitado por HackerRank.

## Autor

Enrique Lozano Abella