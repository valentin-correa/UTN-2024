# Requerimientos
## Definicion
:   - “Un requerimiento es una característica que debe incluirse en
un nuevo sistema y puede consistir en una forma de captar o
procesar datos, producir información, controlar una actividad o
dar apoyo a la gerencia”
    - “Condición o capacidad que necesita el usuario para resolver
un problema o alcanzar un objetivo”
    - “Condición o capacidad que debe satisfacer o poseer un
sistema o un componente de un sistema para satisfacer un
contrato, un standard, una especificación u otro documento
formalmente impuesto”
- Todo lo que creen que debe de tener un software es un requerimiento

## Ingenieria de software

El proceso de Ingeniería de Requerimientos (IR) consiste en desarrollar requerimientos a través de un proceso cooperativo e iterativo de:
- analizar el problema,
- documentar las observaciones resultantes (Modelos) y
- chequear a precisión de la comprensión obtenida.



¿Que es una ingenieria?
: Disciplina en la cual los ingenieros resuelven problemas construyen soluciones

Elicitar requerimientos es mencionar los requerimientos

## Tipos de requerimientos

### Funcional
- Un requerimiento funcional describe lo que el sistema hará sin considerar aspectos de implementación
- Lo que el sistema debe hacer sin importar aspectos de implementacion
- **Que debe hacer el sistema**

*Implementacion: son los metodos que utilises para solucionar los requerimientos*

Tienen que ver con las caracteristicas que tiene el sistema.
### No funcional
- Un requerimiento funcional describe una restriccion sobre el sistema que limita nuestra elecciones en la construcción de una solución al problema
- No son solo aquellos requerimientos de har
- Concurrencia (Controla que no )
- Tiempo de respuesta (No puede tardas x cantidad de tiempo por ejemlo)
- Integraciones entre sistemas (APIs)
- **El como lo debe hacer**

#### Ejemplos
En el caso de una alarma 
Requerimientos funcionales
- Que la alarma se pueda configurar
- Que se emita la alarma
- Registrar alarma
Requerimientos no funcionales
- Cuando se emita la alarma haga un sonido/vibre

## Proceso de ingeniería de requerimientos

### Definicion:
- La Ingeniería de Requerimientos es un
proceso iterativo que comprende:

- __Análisis de factibilidad.__
Si es posible o no y las diferentes razones (economicos, tecnicos, operativos)
Factibilidad economica si puede o sicuenta con los recursos economicos para todo el desarrollo del sistema 
Factibilidad tecnica 
Factibilidad operativa si se cuenta si se puede capacitar a los usuarios para usar el sistema
- __Elicitación.__
Descubrimos como son los procesos
Hacemos toda la investigacio sobre todos los requerimientos que debe tener. Aplicando tecnicas de recoleccion de datos (Consultarlo con el cliente, Cosultarlo con el futuro usuario, Consultarlo con alguien experto en el dominio del problema) mediante entrevistas, charla cortita con preguntas en base a una investigacion previa, encuestas.
- __Especificación.__
El detalle de que es lo que se tiene que hacer para cumplir un requerimiento
- __Validación.__
Valido con el cliete/usuario

En el power point hay más informacion
Link https://cvirtual.frvm.utn.edu.ar/pluginfile.php/125074/mod_resource/content/1/ingenier%C3%ADa%20de%20requerimientos.pdf

### Ejemplo proceso de alquiler de reservas de cancha de padel
__Requerimientos globales__(Organización englobamiento de los detallados)

ADMINISTRAR CLIENTE

ADMINISTRAR CANCHAS

GESTIONAR ALQUILER DE CANCHAS

- __Requerimientos detallados__
    __ADMINISTRAR CLIENTE__

    - Registrar datos personales del cliente

    - Cosultar datos del cliente

    - Modificar datos del cliente

    - Generar listado de clientes

    __ADMINISTRAR CANCHAS__

    - Registrar cancha

    - Consultar disponibilidad de canchas

    - Consultar precio de alquiler de canchas 

    - Generar listado de cancha

    - Modificar preciode alquiler

    __GESTIONAR ALQUILER DE CANCHAS__

    - Registrar turnos

    - Registrar reserva de turno

    - Generar comprobante de reservas

    - Registrar el cobro de seña

    - Generar comprobante de seña

    - Registrar fin de turno