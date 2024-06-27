# Aspectos de diseño del sistema operativo

## Objetivos de diseño

*Hay dos objetivos de suma importancia en el diseño de sistema de E/S: **eficiencia y generalidad***

### Eficiencia

Es importante debido a que las operaciones de E/S usualmente significan un cuello de botella en un computador.

> La mayoría de los dispositivos de E/S son extremadamente lentos comparados con la memoria principal y el procesador.
>
> Una manera de afrontar este problema es la **multiprogramación**. Esta permite que algunos procesos esperen por la finalización de operaciones de E/S mientras se ejecutan otros.
>
> Sin embargo, se dará con cierta frecuencia la situación en la que la E/S no puede seguir el ritmo del procesador.
>
> Se puede utilizar el **intercambio** para poder tener más procesos listos, de manera que se pueda mantener ocupado al procesador.

Se ha dedicado un considerable esfuerzo en el diseño de la E/S. El área que ha recibido mayor atención es la E/S del disco.

### Generalidad

Es deseable manejar todos los dispositivos de manera uniforme, por simplicidad y para eliminar errores. Esto aplica tanto al modo en el que los procesos ven los dispositivos de E/S como a la manera en que el sistema operativo gestiona los dispositivos y las operaciones de E/S.

Debido a la diversidad de las características de los dispositivos, es difícil en la práctica alcanzar una total generalidad.

Se utiliza una estrategia modular jerárquica para diseñar las funciones de E/S. Esta estrategia esconde la mayoría de los detalles del dispositivo de E/S en las rutinas de nivel inferior, de manera que los procesos de usuario y los niveles más altos del sistema operativo contemplan los dispositivos en términos de funciones generales. `read, write, open, close, lock, unlock`



## Estructura lógica del sistema de E/S

La filosofía jerárquica se basa en que las funciones del sistema operativo deberían estar separadas dependiendo de su:

- Complejidad
- Escala de tiempo característica
- Nivel de abstracción

Esta estrategia conduce a una organización del sistema operativo en una serie de niveles.

Cada nivel realiza un subconjunto relacionado de las funciones requeridas del sistema operativo y **se apoya en el nivel inferior subyacente** para realizar funciones más básicas y ocultar los detalles de esas funciones, **proporcionando servicios al siguiente nivel superior**.

*Idealmente, los niveles se deberían definir de manera que los cambios en uno no requieran cambios en otros.*

> Los niveles inferiores, que interaccionan directamente con el hardware, tratan con una escala de tiempo mucho más corta.
>
> Las partes del sistema operativo que se comunican con el usuario emite mandatos a un ritmo mucho más sosegado (lento).

### Niveles o capas

#### E/S lógica

Trata a los dispositivos como un recurso lógico y no se ocupa de los detalles del control real del dispositivo.

Se ocupa de la gestión de las tareas general de E/S para los procesos de usuario, permitiéndoles tratar con el dispositivo a través de un identificador y mandatos sencillos `open, close, read, write`.

#### E/S del dispositivo

Las operaciones requeridas y los datos `caracteres en los buffers, registros, etc` se convierten en las secuencias apropiadas de instrucciones de E/S, mandatos del canal y órdenes del controlador.

Se pueden usar técnicas de uso de *buffers* para mejorar la utilización.

#### Planificación y control

Se produce la gestión real de la cola, la planificación de las operaciones E/S y el control de las mismas.

Se manejan las interrupciones, se recoge el estado de la E/S y se informa del mismo.

Este es el nivel de software que realmente interactúa con el módulo de E/S y, por lo tanto, con el hardware del dispositivo.



# Utilización de buffers de E/S

Realizar las transferencias de entrada antes de que se hagan las peticiones correspondientes y llevar a cabo las transferencias de salida un cierto tiempo después de que se haya hecho la petición.

Viene a resolver como interfiere la E/S con el intercambio. ***Ejemplo:** direcciones de memorias fijadas para leer una cinta `Leer_Bloque[xi, xj]`*

![image-20240625165833860](C:\Users\Valentín\AppData\Roaming\Typora\typora-user-images\image-20240625165833860.png)

# Planificación del disco

Los discos son actualmente al menos cuatro órdenes de magnitud **más lentos** que la memoria principal.

## Parámetros de rendimiento del disco

Cuando está en funcionamiento la unidad de disco, el disco rota a una velocidad constante.

![image-20240625170731267](C:\Users\Valentín\AppData\Roaming\Typora\typora-user-images\image-20240625170731267.png)

### Tiempo de búsqueda

Tiempo que se tarda en situar la cabeza en la pista.

### Retardo rotacional

Tiempo que tarda en llegar el comienzo del sector hasta debajo de la cabeza.

### Tiempo de acceso

La suma del **tiempo de búsqueda** y **retardo rotacional**.

Tiempo que se tarda en llegar a estar en posición para realizar la lectura/escritura.

### Tiempo de transferencia

Tiempo requerido para la transferencia.

### Otros retardos

- **Espera del dispositivo:** El proceso que emite una petición de E/S debe esperar en una cola del dispositivo hasta que esté disponible.
- ***(Si el dispositivo comparte canales de E/S con otras unidades de disco)* Espera del canal:** El dispositivo debe esperar a que el canal esté disponible.

## Políticas de planificación del disco

### FIFO

Procesa los elementos de la cola en orden secuencial.

Es el más equitativo de todos.

Conveniente sólo si:

- Pocos procesos requieren acceso al disco
- Gran parte de las peticiones corresponden con sectores agrupados de ficheros

![image-20240625171944613](C:\Users\Valentín\AppData\Roaming\Typora\typora-user-images\image-20240625171944613.png)

### Primero el de tiempo de servicio más corto (SSTF)

Seleccionar la petición de E/S del disco que requiera un menor movimiento del brazo desde su posición actual.

Buena utilización en colas pequeñas.

![image-20240625172309073](C:\Users\Valentín\AppData\Roaming\Typora\typora-user-images\image-20240625172309073.png)

### Algoritmo del ascensor o SCAN

El brazo sólo debe moverse en una dirección, satisfaciendo todas las peticiones pendientes que encuentre en su camino. Luego, busca en dirección opuesta.

Mejor distribución del servicio.

![image-20240625172702909](C:\Users\Valentín\AppData\Roaming\Typora\typora-user-images\image-20240625172702909.png)

### SCAN Circular o C-SCAN

Restringe la búsqueda a una sola dirección. Luego, vuelve al extremo opuesto y busca de nuevo.

Menor variabilidad del servicio.

![image-20240625172857209](C:\Users\Valentín\AppData\Roaming\Typora\typora-user-images\image-20240625172857209.png)

![image-20240625171747609](C:\Users\Valentín\AppData\Roaming\Typora\typora-user-images\image-20240625171747609.png)



# RAID ~ VECTOR REDUNDANTE DE DISCOS INDEPENDIENTES

## Características comunes

1. RAID corresponde con un conjunto de unidades físicas de disco tratado por el sistema operativo como un único dispositivo lógico

2. Los datos están distribuidos a lo largo de las unidades físicas de un vector

3. La capacidad de redundancia del disco se utiliza para almacenar información de paridad, que garantiza que los datos se pueden recuperar en caso de que falle un disco.

> [!IMPORTANT]
>
> **RAID 0 y RAID 1** no incluyen la tercera característica.

## Niveles

![image-20240625173713127](C:\Users\Valentín\AppData\Roaming\Typora\typora-user-images\image-20240625173713127.png)

<center>Prestar atención a los dos últimos campos</center>

### RAID 0

No incluye redundancia para mejorar la fiabilidad.

Los datos de los usuarios y del sistema están distribuidos a lo largo de todos los discos del vector.

Los datos están distribuidos *en bandas* a lo largo de los discos disponibles.

El disco lógico está dividido en bandas; estas bandas pueden ser bloques físicos, sectores o alguna otra unidad.

### RAID 1

Se consigue la redundancia mediante la duplicación de todos los datos.

#### Aspectos positivos

- Una petición de lectura puede servirse de cualquiera de los dos discos (original o copia), **aquél que implique un menor tiempo de acceso**.
- Una petición de escritura requiere actualizar ambas bandas, pero se puede hacer en paralelo. El rendimiento de escritura lo establece el de **mayor tiempo de acceso**, pero no hay *penalización de escritura* como en RAID 2-6.
- La recuperación de un fallo es sencilla. Se pueden acceder a los datos de la copia.

#### Su principal desventaja es el coste

Requiere el doble de espacio de disco que el correspondiente al disco lógico proporcionado.

# CACHE DE DISCO

**Memoria cache:** Memoria que es más pequeña y más rápida que la memoria principal. Se encuentra entre la memoria principal y el procesador.

**Cache de disco:** Buffer en memoria usado para almacenar sectores del disco. Contiene una copia de algunos de los sectores del disco.

## Estrategias de reemplazo

El algoritmo más frecuentemente utilizado es el **Menos usado recientemente(LRU)**.

Otra posibilidad es el **Menos frecuentemente usado(LFU)**. Puede tener problemas ya que se puede inflar el número de referencias y llevar a que el algoritmo tome decisiones inadecuadas.	