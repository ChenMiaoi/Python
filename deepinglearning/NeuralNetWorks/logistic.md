# BinaryClassification
- The Red, Blue, Green :  
$$ \begin{bmatrix}
225 \\\
231 \\\
\vdots \\\
255 \\\
134 \\\
\vdots \\\
225
\end{bmatrix}
$$

- The Binary :
  - given the x, y :
$$ (x, y), x \in {\vec{R^{n_x}}}, y \in \{0, 1\} $$

- The ruled the m is training example :
$$ \{(x^1, y^1), (x^2, y^2), ..., (x^m, y^m)\} $$
- ruled the $m_{test}$ = m test example
- The ruled a matrix X :
$$ X = 
\begin{bmatrix}
\vdots & \vdots & \vdots & \vdots\\\
x^1 & x^2 & \cdots & x^m \\\
\vdots & \vdots & \vdots & \vdots 
\end{bmatrix}
, x \in {\vec R^{n_x}}, X \in {\vec R^{{n_x} \times m}}
$$ 
- The ruled a matrix Y :
$$ Y = 
\begin{bmatrix}
y^1 & y^2 & \cdots & y^m
\end{bmatrix}
, y \in \{0, 1\}, y \in {\vec R^{1 \times m}}
$$
> **Remember the X can't do the $X^T$**  
> **In Python:**  
> - X.shape($n_x$, m), Y.shape(1, m)
> - The X row is $n_x$, the col is $m$
> - The Y row is $1$, the col is $m$

---  

# Logistic Regression
- Given 'x',The probability is :
$$ \hat{y} = P\times(y = 1 | _x), x\in{\vec R^{n_x}} $$ 
  - The logistic parameter is :
$$ w \in {\vec {R^{n_x}}}, b \in R $$
  - The Output is :
$$ \hat{y} = w^T \times x + b , 0 \leq y \leq 1 $$
  - In this way, we can get the sigmoid function :
$$ \hat{y} = \sigma(w^T \times x + b), z = w^T + b \\
\Rightarrow \sigma(z) = \frac{1}{1 + e^{-z}}
$$
  - If the $z \rightarrow +\infty$ :
$$ \sigma(z) = \lim{\frac {1}{1 + 0}} = 1 $$
  - If the $z \rightarrow 0 \ or -\infty$ :
$$ \sigma(z) = \lim{\frac {1}{1 + \infty}} = 0 $$  
  - But if someone to designed the $x_0 = 1$ :
$$
    x \in \vec R^{n_x + 1} \\
    \hat y = \sigma(\theta^T \times x) \\
    \theta = 
    \begin{bmatrix}
    \theta_0 \\\
    \theta_1 \\\
    \theta_2 \\\
    \vdots \\\
    \theta_{n_x}
    \end{bmatrix} \\
    记:b = \theta_0, w = \{\theta_1, \theta_2,...,\theta_{n_x}\}
$$
