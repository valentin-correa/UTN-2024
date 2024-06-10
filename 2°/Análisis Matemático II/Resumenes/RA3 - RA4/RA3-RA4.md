# Funciones de campo vectorial

## Integral de línea de campos vectoriales

$W = \vec{F}.\vec{D}$

$W = \int_{a}^{b} F[g(t)].g'(t).dt$

## Campo vectorial conservativo

Un campo vectorial $F(x,y)=(M,N)$ es conservativo $\Leftrightarrow \frac{\partial N}{\partial x} = \frac{\partial M}{\partial y}$

<hr>

Si un campo es conservativo, es el **Gradiente de una función vectorial real** (Función potencial de $F$ `que lo origina`)

$F(x,y) = \triangledown f(x,y)$

<hr>

## **Teorema fundamental de la integral de línea**
El trabajo realizado por un campo vectorial conservativo sobre una partícula que se mueve entre dos puntos $a$ y $b$ es **independiente del camino seguido (`independiente de la trayectoria`)**.

$W = f(x_{b}, y_{b}) - f(x_{a}, y_{a}) \ \ | \ \  f = Función \ Potencial$

Si la trayectoria es cerrada $\rightarrow$ $W = 0$


## **Teorema de Green**

Sea una región simple del plano cuyo borde es una curva cerrada C, suave a trozos (`sin picos`), orientada en sentido antihorario, y si M y N tienen derivadas parciales continuas en una región abierta que contiene a D, se cumple:

$\int_C Mdx + Ndy = \iint_D (\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y}) dA$

Establece la relación entre una integral de línea a lo largo de la curva $C$ cerrada y simple, y una integral doble sobre una regíon plana $D$, limitada por $C$. `La circulación antihoraria de un campo vectorial alrededor de una curva cerrada simple es la integral doble del Rotor del campo sobre la región encerrada por la curva.`



<hr>

**Para funciones de $R^{2}$**

$\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y}$ representa el Rotor de $F$, este se indica $Rot(F)$ 

$\space$

**Para funciones de $R^{3}$**

$$
Rot F(x,y,z) = \triangledown \times F(x,y,z) = \begin{vmatrix} i & j & k \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ M & N & P  \end{vmatrix} = [(\frac{\partial P}{\partial y} - \frac{\partial N}{\partial z})i - (\frac{\partial P}{\partial x} - \frac{\partial M}{\partial z})j + (\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y})k]
$$


<hr>

# Integrales Dobles

## Teorema de Fubini

### Verticalmente simple
$V = \iint f(x,y)dA = \int_{a}^{b}\int_{g_1(x)}^{g_2(x)}f(x,y)dydx$

>Se analiza de Izquierda->Derecha->Abajo->Arriba
>$a$ es el inicio de extremo de integracion, $b$ es donde termina en $x$
>$g_1(x) g_2(x)$ son las funciones entre las que varia en el eje $y$

### Horizontalmente simple
$V = \iint f(x,y)dA = \int_{c}^{d}\int_{h_1(y)}^{h_2(y)}f(x,y)dxdy$

## Cálculo de Área

Podemos hacer uso de la integral doble para el cálculo de Áreas, para esto consideramos a la
función $f(x,y)=1$ recuerden que la función nos da la altura de cada prisma y si lo
consideramos $=1$ el valor calculado por la integral nos representa el área de la región R.

$A = \iint dA = \int_{a}^{b}\int_{g_1(x)}^{g_2(x)}f(x,y)dydx  \longrightarrow$ `Si es verticalmente simple`

$A = \iint dA = \int_{c}^{d}\int_{h_1(y)}^{h_2(y)}f(x,y)dxdy \longrightarrow$ `Si es horizontalmente simple`




























