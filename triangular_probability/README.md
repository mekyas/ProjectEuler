# Problem Description

Create a function that draws an integer from a probability distribution uniquely determined by the minimum [s], maximum [m], and most frequent [c] values.
The probability distribution forms a triangle such that the base is [s-1] and [m+1] and the most frequent value [c] is the vertex.
s, m, and c are integers, and the relationship is s ≤ c ≤ m.
For example, in the case of minimum value [2], maximum value [7], and maximum frequency value [6], the probability distribution is determined as follows.
In this case, the base of the triangle is [1] and [8]. The most frequent value [6] is the vertex.

![Image](./img.png)
# Instructions

`python3 solution.py`

# O(1) solution

we will consider the triangular shape as the `pdf` of the probability distribution that we want to estimate. In order to estimate the distribution in O(1), we will consider it as a continuous distribution.

To get random values with the desired distribution, we will use [the inverse transform sampling](https://en.wikipedia.org/wiki/Inverse_transform_sampling).
so we will generete random value with Uniform [0, 1] and get the variable with the desired distribution.

So we will first calculate the CDF and get it's inverse.

For it to be a valid distribution, the sum of all probability should be equal to 1.


![\Large equation1](https://latex.codecogs.com/svg.latex?\Large&space;\int_{-\infty}^{\infty}f(x)=1)

the function is defined between s-1 and m+1:

![\Large equation2](https://latex.codecogs.com/svg.latex?\Large&space;\int_{s-1}^{m+1}f(x)=1)


this is equal to the area of the triangle where `v` is the probability at `c`:

![\Large equation3](https://latex.codecogs.com/svg.latex?\Large&space;\frac{v(m-s+2)}{2}=1)

from the previous equation we can get the probability of the point at `c`

![\Large equation4](https://latex.codecogs.com/svg.latex?\Large&space;v=\frac{2}{m-s+2})

the CDF of this probability distribution is defined as :

![\Large equation5](https://latex.codecogs.com/svg.latex?\Large&space;F(x)=P(X<=x)=\int_{s-1}^{x}f(y)dy)

### **For x <= c:**

![\Large equation6](https://latex.codecogs.com/svg.latex?\Large&space;F(x)=\frac{h.(x-s+1)}{2})

where `h` is the probability at point `x`

to calculate the `h` we will use the equality between tangente of the left angle:

![\Large equation7](https://latex.codecogs.com/svg.latex?\Large&space;\tan(\alpha)=\frac{h}{x-s+1}=\frac{v}{c-s+1})

so the CDF becomes:

![\Large equation6](https://latex.codecogs.com/svg.latex?\Large&space;F(x)=\frac{v.(x-s+1)^{2}}{2.(c-s+1)})


By solving the equation

![\Large equation6](https://latex.codecogs.com/svg.latex?\Large&space;F(F^{-1}(u))=u)

we get the inverse transform:

![\Large equation6](https://latex.codecogs.com/svg.latex?\Large&space;F^{-1}(u)=\sqrt{\frac{2u(c-s+1)}{v}}+s-1)

### **For x >= c:**

The CDF is the area under the curve for `x>=c` it is equals to `1-P(X>x)`

![\Large equation6](https://latex.codecogs.com/svg.latex?\Large&space;F(x)=1-\frac{h.(m+1-x)}{2})

where `h` is the probability as point `x`

we calculate `h` from the equation:

![\Large equation7](https://latex.codecogs.com/svg.latex?\Large&space;\tan(\beta)=\frac{h}{m+1-x}=\frac{v}{m+1-c})

the CDF becomes:

![\Large equation6](https://latex.codecogs.com/svg.latex?\Large&space;F(x)=1-\frac{v.(m+1-x)^{2}}{2(m+1-c)})

By solving the equation

![\Large equation6](https://latex.codecogs.com/svg.latex?\Large&space;F(F^{-1}(u))=u)

we get the inverse transform:

![\Large equation6](https://latex.codecogs.com/svg.latex?\Large&space;F^{-1}(u)=m+1-\sqrt{\frac{2(1-u)(m+1-c)}{v}})

### **generation**

Last but not least, to get the discrete values from the continues values.

- we will generate interger value `x` for all float values between `x-0.5` and `x+0.5`

- we will generate integer value `c` from the previous rule and for float values between `s-1` and `s-0.5` and between `m+0.5` and `m+1`.

those rules are deduced from the geometric relation of the rectangles area.
