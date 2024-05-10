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
 \frac{\partial f_1}{\partial x_1}(\vec{X_0})   &.&.&.& \frac{\partial f_1}{\partial x_n}(\vec{X_0})\\ 
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

# DERIVADA DIRECCIONAL $f:\Re^n \rightarrow \Re$
Derivadas parciales de funciones vectoriales reales en una dirección cualquiera.
$$\frac{\partial f}{\partial \vec{u}} (\vec{X_0}) = f'(\vec{X_0}).\widehat{u} = \triangledown f(\vec{X_0}).\widehat{u}$$

Donde:
: $f'(\vec{X_0}) = (f_{x_1}(\vec{X_0}), f_{x_2}(\vec{X_0}), ..., f_{x_n}(\vec{X_0}))$ *~ Matriz jacobiana de una función real, **que evaluada en un punto** resulta en un vector de dimensión $1xn$*
    > Ese vector es el $Gradiente\; de\; f$
: $\widehat{u} =(u_1, u_2, ...,u_n) =Versor \in \Re^n$

: $\triangledown f = (f_{x_1}, f_{x_2}, ..., f_{x_n})$

> $Si\; \widehat{u} = (1,0) \Leftrightarrow f_{\widehat{u}} (\vec{X_0})=f_x(\vec{X_0})$
$Si\; \widehat{u} = (0,1) \Leftrightarrow f_{\widehat{u}} (\vec{X_0})=f_y(\vec{X_0})$

## INTERPRETACIÓN GEOMÉTRICA
Pendiente de la recta tangente a la curva $C$ en el punto $P$ es la razón de cambio de la función en la dirección del vector $\vec{u}$.

## PROPIEDADES
1. $Si\; \triangledown f(\vec{X_0})=\vec{0}\; \Rightarrow \; f_{\widehat{u}}=0 \;\forall \widehat{u}$
2. Dirección de máximo crecimiento en $X_0$
    : $\triangledown f(\vec{X_0})$

    Valor máximo ó Derivada direccional máxima
    : $\|\triangledown f(\vec{X_0})\|$
    
3. Dirección de mínimo crecimiento en $X_0$
    : $-\triangledown f(\vec{X_0})$

    Valor mínimo ó Derivada direccional mínima
    : $-\|\triangledown f(\vec{X_0})\|$

4. $Si\; f(x_1, x_2,...)$ es diferenciable en $X_0\; \Leftrightarrow \; \triangledown f(x_1,x_2,...)$ **es perpendicular a la curva de nivel que pasa por** $X_0$
    > $Gradiente\; en\; X_0\; es\; perpendicular\; a\; la\; curva$

5. $\|\triangledown f(X)\|.\|\widehat{u}\|.cos(\theta)$ 
    : - $\theta = 90°\Rightarrow \cos (\theta) = 0 \longrightarrow Derivada\;Direccional\;Nula$
    : - $\theta = 0°\Rightarrow \cos (\theta) = 1 \longrightarrow Derivada\;Direccional\;Máxima$
    : - $\theta = 180°\Rightarrow \cos (\theta) = -1 \longrightarrow Derivada\;Direccional\;Mínima$

# VALORES EXTREMOS $\Re^2 \rightarrow \Re$
1. Existe al menos un punto en $D$  donde $f(x,y)$ alcanza un valor **máximo local o relativo en** $\vec{X_0}$ si:
    $$\forall \vec{X} \in \Re^n \; se \; verifica\; f(\vec{X}) \le f(\vec{X_0})$$
2. Existe al menos un punto en $D$  donde $f(x,y)$ alcanza un valor **mínimo local o relativo en** $\vec{X_0}$ si:
    $$\forall \vec{X} \in \Re^n \; se \; verifica\; f(\vec{X}) \ge f(\vec{X_0})$$

Donde:
- $f(\vec{X_0}) \longrightarrow$  *Punto extremo de la función*
- $D \longrightarrow$ *Región abierta*

## CONDICIONES PARA LA EXISTENCIA DE PUNTOS CRÍTICOS
1. $\triangledown f(\vec{X_0}) = \vec{0}$
    > $\triangledown f(\vec{X_0}) = \vec{0} \Longrightarrow$ *existe un **plano tangente horizontal** en* $\vec{X_0}$

2. $\triangledown f(\vec{X_0})\; \nexists$ $[(f_x\nexists) \lor f_y\nexists]$

## NATURALEZA DE LOS EXTREMOS RELATIVOS $f_x(\vec{X_0}) = 0\  \land\ f_y(\vec{X_0}) = 0$


$$\Delta=f_{xx}(\vec{X_0}).f_{yy}(\vec{X_0})-[f_{xy}(\vec{X_0})]^{2}$$


1. __Mínimo relativo:__ Si $\Delta > 0\ \land\ f_{xx}(\vec{X_0}) > 0$ 

2. __Máximo relativo:__ Si $\Delta > 0\ \land\ f_{xx}(\vec{X_0}) < 0$

3. __Punto silla:__ Si $\Delta < 0$

4. __No hay conclusión:__ Si $\Delta = 0$

### HESSIANO
<hr>

$$
\Delta=H(\vec{X_0})=
\begin{vmatrix}
f_{xx}(\vec{X_0}) & f_{xy}(\vec{X_0})\\
f_{xx}(\vec{X_0}) & f_{yy}(\vec{X_0})\\
\end{vmatrix}
$$

1. Si el __SIGNO__ de $f_{xx}(\vec{X_0})$ es **DISTINTO** al de $f_{yy}(\vec{X_0}) \Longrightarrow \Delta < 0 \ (Punto \ Silla)$

2. Si $\Delta > 0, f_{xx}(\vec{X_0})\ \land f_{yy}(\vec{X_0})$ deben tener el __MISMO SIGNO__.

### INTERPRETACIÓN GEOMÉTRICA
<hr>

- Si $\Delta > 0:$
    - Se curva hacia __arriba__ si $f_{xx} < 0$
    - Se curva hacia __abajo__ si $f_{xx} > 0$
    
- Si $\Delta < 0:$
    - Se curva hacia arriba y hacia abajo en __distintas direcciones__ $\longrightarrow Punto\ Silla$

## EXTREMOS CONDICIONADOS

### MULTIPLICADORES DE LAGRANGE
Se utiliza este método para maximizar o minimizar una función $f(\vec{X_0})$ sujeta a una restricción o condición de la forma $G(\vec{X_0})$

$F(\vec{X_0};\lambda_i)=f(\vec{X_0})+\lambda_1.G_1(\vec{X_0})+\lambda_2.G_2(\vec{X_0})+...+\lambda_n.G_n(\vec{X_0}) \longrightarrow$ **Función auxiliar**

Donde:
: - $f(\vec{X_0}) \longrightarrow$ *Función objetivo que se pretende maximizar o minimizar*

