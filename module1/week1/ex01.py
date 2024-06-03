import math

#Ex1

def precision(tp, fp):
    return tp/(tp+fp)

def recall(tp, fn):
    return tp/(tp+fn)

def f1_score(tp, fp, fn):
    p = precision(tp, fp)
    r = recall(tp, fn)
    f1 = 2*(p*r)/(p+r)
    return f1

def exercise1(tp, fp, fn):
    if type(tp) is not int:
        print('tp must be int')
        return

    if type(fp) is not int:
        print('fp must be int')
        return

    if type(fn) is not int:
        print('fn must be int')
        return

    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        return
    
    p = precision(tp, fp)
    r = recall(tp, fn)
    f1 = f1_score(tp, fp, fn)

    print(f'precision is {p}')
    print(f'recall is {r}')
    print(f'f1-score is {f1}')

