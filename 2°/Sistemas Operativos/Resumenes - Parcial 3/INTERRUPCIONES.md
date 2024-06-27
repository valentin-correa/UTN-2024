# Interrupciones
Mecanismo por el cual otros módulos (Memoria y E/S) pueden interrumpir el secuenciamiento normal del procesador.

Constituyen una manera de mejorar la utilización del procesador.

## Clases de interrupciones
**De programa:** Generada por alguna condición que se produce como resultado de la ejecución de una instrucción. `desbordamiento aritmético - división por cero - intento de ejecución de instrucción ilegal - referencias fuera del espacio de memoria permitido`

**Por temporizador:** Generada por un temporizador del procesador. `permite al sistema operativo realizar ciertas funciones de forma regular`

**De E/S:** Generada por un controlador de E/S para señalar la conclusión normal de una operación o para indicar diversas condiciones de error.

**Por fallo del hardware:** Generada por un fallo. `fallo en el suministro de energía - error de paridad en la memoria`



![image-20240623150546351](C:\Users\Valentín\AppData\Roaming\Typora\typora-user-images\image-20240623150546351.png)

> Se puede producir una interrupción en cualquier punto de la ejecución del programa principal, no sólo en una determinada instrucción.
>
> La operación de E/S se lleva a cabo de forma concurrente con la ejecución de instrucciones del programa de usuario.
>
> **¿Cómo funciona?**
>
> ​	Cuando el dispositivo externo está listo para ser atendido, el módulo de E/S de este dispositivo externo manda una señal de *petición de interrupción* al procesador.
>
> ​	El procesador responde suspendiendo la ejecución del programa actual, saltando a la rutina de servicio específica de este dispositivo de E/S (manejador de interrupción), y reanudando la ejecución original después de haber atendido al dispositivo.
>
> ​	
> $$
> (i) \rightarrow INTERRUPCION \rightarrow MANEJADOR \rightarrow (i+1)
> $$
> El procesador y el sistema operativo son responsables de suspender y reanudar el programa de usuario.
>
> ​	![image-20240623151046157](C:\Users\Valentín\AppData\Roaming\Typora\typora-user-images\image-20240623151046157.png)



## Tratamiento de una interrupción

![image-20240623152125866](C:\Users\Valentín\AppData\Roaming\Typora\typora-user-images\image-20240623152125866.png)

Cuando un dispositivo de E/S termina el trabajo asignado, produce una interrupción. Para ello, impone una señal en una línea de bus que se le haya asignado. Esta señal es detectada por el chip controlador de interrupciones en la tarjeta principal, que finalmente decide que hacer con ella.

## Ciclo de instrucción *con interrupciones*

![image-20240623180248928](C:\Users\Valentín\AppData\Roaming\Typora\typora-user-images\image-20240623180248928.png)

## Procesamiento de interrupciones

**La aparición de una interrupción:**

- Dispara varios eventos, tanto en el hardware del procesador como en el software.
- Es imprevisible.

![image-20240623185628213](C:\Users\Valentín\AppData\Roaming\Typora\typora-user-images\image-20240623185628213.png)

## Múltiples interrupciones

### Alternativas

#### Inhabilitar interrupciones

El procesador ignorará cualquier nueva señal de petición de interrupción. `cualquier interrupción producida durante ese tiempo permanecerá pendiente y solo se comprobará después que se rehabiliten`

Cuando se ejecuta un programa de usuario y se produce una interrupción, **se inhabilitan las interrupciones inmediatamente**.

Las interrupciones se manejan en **estricto orden secuencial**.

> **Desventaja:** No tiene en cuenta la prioridad relativa o el grado de urgencia de las interrupciones.

![image-20240623195842664](C:\Users\Valentín\AppData\Roaming\Typora\typora-user-images\image-20240623195842664.png)

#### Definir prioridades

![image-20240623200226632](C:\Users\Valentín\AppData\Roaming\Typora\typora-user-images\image-20240623200226632.png)

## Multiprogramación

Una solución para poder utilizar eficientemente el procesador puede ser permitir que **múltiples programas de usuario estén activos al mismo tiempo**.