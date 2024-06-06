import ex01_metric
import ex02_activation_func
import ex03_loss_func
import module1.week1.ex04_approx as ex04_approx
import ex05_mean_root_error

if __name__ == "__main__":

    print("Exercise 01")
    ex01_metric.exercise1(tp=2, fp=3, fn=4)

    print("Exercise 02")
    ex02_activation_func.exercise2()

    print("Exercise 03")
    ex03_loss_func.exercise3()
    
    print("Exercise 04")
    print(ex04_approx.approx_sin(x=3.14, n=10))
    print(ex04_approx.approx_cos(x=3.14, n=10))
    print(ex04_approx.approx_sinh(x=3.14, n=10))
    print(ex04_approx.approx_cosh(x=3.14, n=10))

    print("Exercise 05")
    print(ex05_mean_root_error.md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1))