# Diagrama de Clases

Muestra un conjunto de clases, interfaces, colaboraciones y sus relaciones.

Contiene comúnmente:
- Clases
- Interfaces (tipo especial de clases)
- Relaciones

## Clasificación
- de Estructura
- Estático
- Lógico

## Uso
- Explorar conceptos del dominio
- Analizar **requerimientos**
- Mostrar el diseño detallado del software orientado a objetos

## ¿Cómo identificar clases?
Todo aquello que se necesita que el sistema administre **dentro del dominio de análisis**

- Cosas tangibles (Producto, Medicamento, Casa, Avión)
- Roles de personas (Proveedor, Cliente, Empleado)
- Lugares (Barrio, Provincia, País, Zona)
- Transacciones u operaciones (Venta, Préstamo, Pedido)
- Hechos o eventos (Vuelo, Accidente, Incidente)
- Otras organizaciones o áreas (Institución, Banco, Departamento de ventas)

## Relaciones

### Relación de Asociación
Representa la conexión existente entre dos clases. Un vínculo entre dos objetos es una instancia de una asociación.

Las asociaciones pueden tener:
- Nombre de asociación
- Nombres de roles
- Multiplicidad
- Navegabilidad

### Asociación reflexiva
Una clase tiene una relación consigo misma.

### Relación de Agregación
El elemento destino es parte del elemento origen. Representa una relación conceptual entre un "todo" y sus "partes".

Puede ser por referencia o por valor *(composición)*

### Relación de Generalización

Conecta clases generales *(padres)* con otras más especializadas *(hijos)*

Los objetos hijos se pueden emplear en cualquier lugar que pueda aparecer el padre. **No a la inversa**.

> "es-un-tipo-de"

## Patrones Estructurales

Realizan una descripción del problema que ocurre y de cómo solucionarlo *(estereotipos)*

Características:
- Plantea una solución al problema.
- Permite derivar soluciones.
- Describe relaciones.
- Cada patrón enfoca un solo aspecto del problema.
- Indica cuándo y en qué casos puede aplicarse.
- Especifica las consecuencias de la aplicación.

$$
\space
$$

$$
Filosofía \ de \ objetos
$$

$$
\downarrow
$$

$$
Reutilización
$$

$$
\downarrow
$$

$$
Experiencias - Soluciones \ de \ análisis \ y \ diseño - Códigos
$$
