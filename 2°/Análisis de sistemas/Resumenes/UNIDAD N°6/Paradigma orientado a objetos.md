# ¿Qué es un paradigma?

Forma de "ver" y "entender" el mundo. Abstracción a nuestra cabeza.

Conjunto de teorías, estándares, métodos que, unificados, representan una forma de organizar el conocimiento.

## Paradigma estructurado
- Pasos
- Secuencia de actividades
- Algoritmos lineales
- Se divide en procesos y datos

> Complejo en softwares grandes
> Dificultoso de mantener en sistemas complejos

## Paradigma orientado a objetos
- Componentes independientes y reutilizables
- Comunicación mediante colaboraciones
- Bloques de construcción *(objetos y clases)*

> Objetos administran sus datos y funciones
> Ayuda a combatir la complejidad

### ¿Qué es la orientación a objetos?
Forma de entender un problema identificando las entidades principales que se encuentran en él. `Identificar entidades involucradas = Reconocer características y acciones qe realizan`

### ¿Qué es un objeto?
Entidades del mundo real que combinan **estado, comportamiento e identidad**

Comportamiento
: Métodos con que puede operar. Operaciones que se pueden realizar con él.

Estado
: Uno o varios atributos a los que se habrán asignado valores concretos *(datos)*

Identidad
: Propiedad de un objeto que lo diferencia del resto. **Identificador**.

### ¿Qué es una clase?
Agrupación de objetos.

Está compuesta por **características *(atributos)*** y **comportamientos *(métodos)***. `Ambos están determinados por el contexto del problema`

Estado de un objeto
: Valores de los atributos.

Interfaz
: Atributos y métodos del objeto.

Implementación
: Código usado para construir las clases.


### Conceptos básicos

**Envío de mensajes**
: Invocación de métodos. Medio de colaboración entre objetos.

**Polimorfismo**
: Mismo nombre, distinta función.
- Permite al modelador hablar el lenguaje del cliente
- Evita asignar identificadores artificiosos para distinguir operaciones
- Contribuye a la reutilización de código

**Abstracción**
: Extraer propiedades esenciales de un objeto.

### Elementos fundamentales

**Encapsulamiento**
- Ocultación de detalles
- Implementación
- Concepto de interfaz
- Independencia

**Modularidad**
: Sistema compuesto en módulos coherentes e independientes.
> Alta cohesión y bajo acoplamiento.

**Jerarquía**
: Orden de abstracción organizado en niveles.

**Herencia**
: Los objetos "heredan" las características de la clase. Las clases pueden heredar de otras clases.

- Tipo de jerarquía
- Generalización / Especialización
- Utilidad
  - Abstracción
  - Reutilización

### Elementos secundarios

Tipificación
: Características precisas que comparten una serie de objetos.

Concurrencia
: Diferentes objetos actuan al mismo tiempo. Distinue objetos activos de inactivos.

Persistencia
: Cantidad de espacio que ocupa y tiempo que dura un objeto. Conservación del estado del objeto en el espacio y en el tiempo.

### Parte estructural o estática del modelo
- Objeto
- Clase
- Herencia

### Parte del comportamiento dinámico
- Envío de mensajes
