# FUNCIONES DE MÚLTIPLES VARIABLES $$f:U\subseteq \Re^n \rightarrow \Re^m$$
Regla que asocia a cada vector $X$ de $U$, un vector bien determinado $f(X)$ de $\Re^m$

Donde:
: $X = (x_1,x_2,...,x_n) =n-ada \; ordenada\;de\;números\;reales$
: $f(X)=(f_1(X),f_2(X),...,f_m(X))$

# FUNCIONES VECTORIALES

## **TIPOS**

- ### FUNCIONES DE CAMPO VECTORIAL $\Re^n \rightarrow \Re^m$

- ### FUNCIONES VECTORIALES REALES $\Re^n \rightarrow \Re$

Curvas de nivel
: Curvas proyectadas en el plano $xy$ obtenidas al intersectar superficies $k=z$ $\land$ $f(x,y)=z$

Dominio
: Conjunto de vectores del primer espacio, para el cual existe **una** imagen real en el segundo espacio $\land$ $D\subset \Re^{2}$

- ### FUNCIONES VECTORIALES DE VARIABLES REAL $\Re \rightarrow \Re^m$

<hr>

# LÍMITE

> Nunca se puede indeterminar *(para múltiples variables)*

## CÁLCULO DE LÍMITE

- ### Límite sucesivos
    Deben ser resueltos de forma secuencial
        $$
        \lim_{x\rightarrow x_0} [\lim_{y \rightarrow y_0} f(x,y)]=L_1
        $$
        $$
        \lim_{y\rightarrow y_0} [\lim_{x \rightarrow x_0} f(x,y)] = L_2
        $$
    
    $Si$ $L_1=L_2 \Rightarrow$ $probablemente$ $\exists \lim$
    $Si$ $L_1\neq  L_2 \Rightarrow \nexists \lim$
- ### Límite radial
    Toma caminos cercanos a $z$
    
    Convierte una de las variables en una función
    : - Ejemplos
        - $y=mx$
        - $x=my^2$
        - $y=m\sqrt{x}$
        - $x=\sqrt{my}$
- ### Límite inmediato *(métodos algebraicos)*
    - Casos de factoreo
    - Racionalizacion
    - Limite notable

## CONTINUIDAD
- ### CONTINUA
    *Si existe el límite **y** la función en el punto, es continua.*
    
    $\exists \lim_{X\rightarrow (x_0, y_0)} f(x,y) \; \land \;\exists f(x_0, y_0)\; \Rightarrow \;\lim_{X\rightarrow (x_0, y_0)} f(x,y)=f(x_0, y_0)$

- ### DISCONTINUIDAD EVITABLE
    - $\nexists f(x_0, y_0)\;\land\; \exists \lim_{X\rightarrow(x_0, y_0)}$

    - $\exists \lim_{X\rightarrow(x_0, y_0)} \neq \exists f(x_0, y_0)$

- ### DISCONTINUIDAD ESENCIAL
    $\nexists \lim f(x_0,y_0)$


# DERIVADAS PARCIALES
## DEFINICIÓN
$$f_x=\frac{\partial f(x,y)}{\partial x} =\lim_{\Delta x\rightarrow 0} \frac{f(x+\Delta x,y)-f(x,y)}{\Delta x}$$
$$f_y=\frac{\partial f(x,y)}{\partial y} =\lim_{\Delta y\rightarrow 0} \frac{f(x, y+ \Delta y)-f(x,y)}{\Delta y}$$


> *Se deriva una variable y la otra se cuenta como constante*

## INTERPRETACIÓN GEOMÉTRICA
Derivada parcial con respecto a $x$
: Pendiente de la recta tangente a la curva de intersección con el plano $y = y_0$

Derivada parcial con respecto a $y$
: Pendiente de la recta tangente a la curva de intersección con el plano $x = x_0$


## DERIVADAS PARCIALES DE ORDEN SUPERIOR $(f_{xy})$
### **IGUALDAD DE LAS DERIVADAS PARCIALES CRUZADAS** 
### $$f_{xy}(x,y) = f_{yx}(x,y)$$

## PLANO TANGENTE 
$$z=f(X_0)+f_X(X_0)(x-x_0)+f_y(X_0)(y-y_0)$$

Función Afín 
: El plano tangente en P es el plano que mejor aproxima a la superficie S cerca del punto P

# MATRIZ JACOBIANA ~ DERIVADA TOTAL


$$
{F}'(\vec {X_0}) =
\begin{pmatrix}
 \frac{\partial f_1(\vec{X_0})}{\partial x_1}   &.&.&.& \frac{\partial f_1(\vec{X_0})}{\partial x_n}\\ 
 .&.  & .&. & .\\
 .&.  & .&. & .\\
 .&.  & .&. & .\\
 \frac{\partial f_m(\vec{X_0})}{\partial x_1}  &.&.&.& \frac{\partial f_m(\vec{X_0})}{\partial x_n} 
\end{pmatrix}
$$

- **Filas:** Funciones $(f_1, f_2, f_3)$
- **Columnas:** Variables $(x, y, z)$

## GRADIENTE
Derivada total de $f(x)$
: $$F'(X) = (\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, ..., \frac{\partial f}{\partial x_n})$$

Vector gradiente *(Derivada total evaluda en un punto $X_0$ )*
: $$\triangledown f(X_0)= (\frac{\partial f(X_0)}{\partial x_1}, \frac{\partial f(X_0)}{\partial x_2}, ..., \frac{\partial f(X_0)}{\partial x_n})$$

## DIFERENCIAL



Diferencia total de una función $f: \Re^n \rightarrow \Re^m$

: $$df = f'(x)\Delta x$$

: $$ 
df(X)=
\begin{pmatrix}
\frac{\partial f_1}{\partial x_1}&\frac{\partial f_1}{\partial x_2}&.&.&\frac{\partial f_1}{\partial x_n}\\
\frac{\partial f_2}{\partial x_1}&\frac{\partial f_2}{\partial x_2}&.&.&\frac{\partial f_1}{\partial x_n}\\
.&.&.&.&.\\
.&.&.&.&.\\
\frac{\partial f_m}{\partial x_1}&\frac{\partial f_m}{\partial x_2}&.&.&\frac{\partial f_m}{\partial x_n}\\
\end{pmatrix}
\begin{pmatrix}
\Delta x_1\\
\Delta x_2\\
.\\
.\\
.\\
\Delta x_n\\
\end{pmatrix}
$$



## INCREMENTO
Incremento verdadero de una función $f:\Re^n \rightarrow \Re^m$
: $$ \Delta f(X) = 
\begin{pmatrix}
f_1(x_1 + \Delta x_1, x_2 + \Delta x_2, ..., x_n + \Delta x_n) & - &     f_1(x_1, x_2, ..., x_n) \\
f_2(x_1 + \Delta x_1, x_2 + \Delta x_2, ..., x_n + \Delta x_n) & - &     f_2(x_1, x_2, ..., x_n) \\
.&.&.\\
.&.&.\\
.&.&.\\
f_m(x_1 + \Delta x_1, x_2 + \Delta x_2, ..., x_n + \Delta x_n) & - &     f_m(x_1, x_2, ..., x_n)
\end{pmatrix}
$$ 