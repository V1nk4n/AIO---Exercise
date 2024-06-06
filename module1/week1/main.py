import ex01
import ex02
import ex03
import ex04
import ex05

if __name__ == "__main__":

    print("Exercise 01")
    ex01.exercise1(tp=2, fp=3, fn=4)

    print("Exercise 02")
    ex02.exercise2()

    print("Exercise 03")
    ex03.exercise3()
    
    print("Exercise 04")
    print(ex04.approx_sin(x=3.14, n=10))
    print(ex04.approx_cos(x=3.14, n=10))
    print(ex04.approx_sinh(x=3.14, n=10))
    print(ex04.approx_cosh(x=3.14, n=10))

    print("Exercise 05")
    print(ex05.md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1))