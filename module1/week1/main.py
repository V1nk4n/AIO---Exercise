<<<<<<< HEAD
import ex01_metric
import ex02_activation_func
import ex03_loss_func
import ex04_approx
import ex05_mean_root_error
=======
import ex01
import ex02
import ex03
import ex04
import ex05
>>>>>>> 00150ec31e1e7c85dc13795ce7aefc530e8a98c6

if __name__ == "__main__":

    print("Exercise 01")
<<<<<<< HEAD
    ex01_metric.compute_metric(tp=2, fp=3, fn=4)

    print("Exercise 02")
    ex02_activation_func.compute_activation_function()

    print("Exercise 03")
    ex03_loss_func.compute_loss_function()
=======
    ex01.exercise1(tp=2, fp=3, fn=4)

    print("Exercise 02")
    ex02.exercise2()

    print("Exercise 03")
    ex03.exercise3()
>>>>>>> 00150ec31e1e7c85dc13795ce7aefc530e8a98c6
    
    print("Exercise 04")
    print(ex04.approx_sin(x=3.14, n=10))
    print(ex04.approx_cos(x=3.14, n=10))
    print(ex04.approx_sinh(x=3.14, n=10))
    print(ex04.approx_cosh(x=3.14, n=10))

    print("Exercise 05")
    print(ex05.md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1))