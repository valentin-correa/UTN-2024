# Guía de estudio

## 1. ¿Qué es un paradigma?

Conjunto de teorías, estándares, métodos que, unificados, representan una forma de organizar el conocimiento.

Forma de “ver” y “entender” el mundo, es una forma de abstraerlo dentro de nuestra cabeza.

## 2. ¿Qué define el paradigma OO?

El paradigma orientado a objetos define clases como abstracciones de los objetos del mundo real. Estas clases tienen atributos y métodos que definen su comportamiento y estado. A partir de estas clases, se crean instancias llamadas objetos que interactúan entre sí para resolver problemas.

## 3. Defina: Análisis OO, Diseño OO y programación OO.

### Análisis Orientado a Objetos
Se utilizan los objetos del mundo real como base para construir modelos.

### Diseño Orientado a Objetos
Los elementos que forman los sistemas del mundo real se corresponden con objetos de software.

### Programación Orientada a Objetos
Se organiza el software como una colección de objetos discretos que encapsulan **Estructuras de datos** y **Comportamiento**. Estos objetos colaboran y se comunican entre sí.

## 4. ¿Cuáles son las ventajas de la utilización del paradigma de objetos para el desarrollo de software?

• Componentes independientes y altamente reutilizables.
• Comunicación mediante colaboraciones.
• Bloques de construcción 🡪 objetos y clases.

Los objetos administran sus propios datos y son responsables de sus propias funciones.

Ayuda a combatir la complejidad.

## 5. ¿Cómo resuelve el paradigma de objetos la problemática de la complejidad del software? 

El paradigma orientado a objetos resuelve la problemaática de la complejidad del software mediante el uso del encapsulamiento, la abstracción, la herencia, el polimorfismo y la modularidad. Esto permite que el software sea más fácil de entender, de mantener y de reutilizar.

## 6. Definir clase y objeto. Dar ejemplos
### Clase

Descripción de un conjunto de objetos que comparten los mismos atributos, operaciones, relaciones y semántica. Pueden representar software, hardware o cosas puramente conceptuales.

Una clase es una abstracción de las cosas que forman parte del vocabulario. 

Una clase no es un objeto individual, sino que representa un conjunto de objetos.

> Auto, Profesor, Comida, etc.

### Objetos

Instancia de una clase.

Entidad discreta con identidad, estado y comportamiento que se puede invocar.

- El comportamiento está definido por los métodos con que puede operar dicho objeto, es decir, qué operaciones se pueden realizar con él.
- El estado representa uno o varios atributos a los que se habrán asignado unos valores concretos (datos).
- La identidad es una propiedad de un objeto que lo diferencia del resto, dicho con otras palabras, es su identificador.

> Fiat 600, Valeria Ortiz, Pizza, etc.

## 7. ¿Cuáles son las características de los objetos según su naturaleza?

Las características de un objeto son sus atributos. Estos son dependientes del dominio del problema.

> En un taller de pintura de vehículos, tenemos en cuenta el color del vehículo y no el estado de su motor.

> En la clase Alumno no nos interesa saber su color de pelo.

## 8. ¿Cuáles son los elementos esenciales y los secundarios del modelo orientado a objetos? Dá un ejemplo de cada uno (que no sean los del libro)

### Elementos esenciales

#### Abstracción
Extraer las propiedades esenciales de un objeto que lo distinguen de los demás tipos de objetos y proporciona fronteras conceptuales definidas respecto al punto de vista del observador, en un determinado dominio del problema.

> Clase Vehículo $\rightarrow$ Ruedas, Motor, Asientos 

#### Encapsulamiento
- Ocultación de detalles
- Implementación
- Concepto de Interfaz
- Independencia

> En una clase Tarjeta, sería conveniente ocultar atributos como el número, el CVV.

#### Jerarquía

Orden de abstracción organizado por niveles.

> $$
> Animal
> $$
> 
> $$
> \downarrow
> $$
> 
> $$
> Mamífero - \ Anfibios - \ Peces - \ Reptiles
> $$


### Elementos secundarios

#### Tipificación: 
Características precisas que comparten una serie de objetos. Puesta en vigencia de la clase de los objetos.

> Auto sus atributos serian: marca, modelo, color

#### Concurrencia: 
Permite a diferentes objetos actuar al mismo tiempo. Distingue objetos activos de inactivos.

> En un banco, la **concurrencia** permite la posibilidad de que varias personas puedan transferir, retirar y consultar su saldo al mismo tiempo.

> En un sistema operativo, la concurrencia es nesesaria para el funcionamiento de multiples programas al mismo tiempo

#### Persistencia: 
Cantidad de espacio que ocupa y tiempo que dura un objeto. Conservación del estado del objeto en el espacio y en el tiempo.

> En una biblioteca, la **persistencia** permite guardar Libros y Préstamos en un almacenamiento para luego poder ser consultado.

## 9. ¿Qué permite modelar el Modelo de Objetos del Dominio del Problema? ¿Qué herramienta se utiliza para desarrollarlo? [MAIL]

### DIAGRAMA DE CLASE
### UML

## 10. ¿Cómo se identifican las clases que participan de un dominio de problema?

Las clases son todo aquello que se necesita que el sistema administre dentro del dominio de análisis.

- Cosas tangibles (Producto, Medicamento, Casa, Avión)
- Roles de personas (Proveedor, Cliente, Empleado)
- Lugares (Barrio, Provincia, País, Zona)
- Transacciones u operaciones (Venta, Préstamo, Pedido)
- Hechos o eventos (Vuelo, Accidente, Incidente)
- Otras organizaciones o áreas (Institución, Banco, Departamento de ventas)

## 11. El diagrama de clases qué modela del sistema? ¿Qué vista del sistema muestra, dinámica o estática, interna o externa? Explique [Leer libro]

EL diagrama de clases modela la estructura y las relaciones estáticas entre las clases y objetos del sistema. No describe cómo interactúan los objetos, sino cómo están organizados y cómo se relacionan entre sí.

En relación con la vista del sistema, el diagrama de clases ofrece una perspectiva **estática**, como se mencionó anteriormente. Por otro lado, en los *diagramas de componentes*, que constituyen una variante de los diagramas de clases, se presenta la vista **interna** del sistema. Esto incluye la encapsulación de una clase, interfaces, puertos, etc.

## 12. ¿Cuáles son los elementos que conforman una clase?

Una clase está conformada por:

- **Nombre:** Cadena de texto. Puede ser un nombre simple o calificado `calificado: nombre de la clase precedido por el nombre del paquete en el que se encuentra`
- **Atributos:** Propiedades identificadas con un nombre que describen un rango de valores que pueden tomar las instancias de la propiedad.
- **Operaciones:** Implementación de un servicio que puede ser requerido a cualquier objeto de la clase para que muestre un comportamiento. Abstracción de algo que se puede hacer a un objeto y que es compartido por todos los objetos de la clase.
- **Responsabilidad:** Contrato u obligación de una clase. Las cosas que debe hacer.

## 13. ¿Cuáles son las vistas de una clase? [MAIL]

- Vista de diseño
- Vista de implementación

## 14. Envío de mensajes

El envío de mensajes es la forma en que los objetos interactúan entre sí. Un objeto envía un mensaje a otro objeto para solicitarle que realice una operación. El objeto que recibe el mensaje es el que decide cómo responder a ese mensaje. Esto es llevado a cabo a través de la **invocación de métodos**.