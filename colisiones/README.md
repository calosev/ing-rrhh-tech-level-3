Uso de la función count_collisions
La función count_collisions recibe como parámetro una lista de robots representados por las letras 'R' (hacia la derecha) 
y 'L' (hacia la izquierda) y devuelve una lista con la cantidad de colisiones que ha tenido cada robot.

Ejemplo de uso:
 
count_collisions(['R', 'L', 'R', 'L', 'R'])
# Devuelve: [2, 2, 2, 0, 0]

Para ejecutar las pruebas de unidad, simplemente correr el script de pruebas:
python test_collision_count.py

Esto debería imprimir "All tests passed" en caso de que todas las pruebas hayan sido exitosas.
