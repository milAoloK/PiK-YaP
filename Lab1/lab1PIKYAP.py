import sys
import math

def get_coef(index, prompt):
    try:
        if len(sys.argv) > index:
            return float(sys.argv[index])
    except (IndexError, ValueError):
        pass
    
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка! Коэффициент должен быть действительным числом")

def get_biquadratic_roots(a, b, c):
    result = []

    if a == 0:
        print("В биквадратном уравнении a не может равняться 0")
        return result

    D = b*b - 4*a*c
    
    if D < 0.0:
        return result
    elif D == 0.0:
        t = -b / (2.0*a)
        if t > 0:
            root = math.sqrt(t)
            result.append(root)
            result.append(-root)
        elif t == 0:
            result.append(0.0)
    else:
        sqrt_D = math.sqrt(D)
        t1 = (-b + sqrt_D) / (2.0*a)
        t2 = (-b - sqrt_D) / (2.0*a)

        if t1 > 0:
            root = math.sqrt(t1)
            result.append(root)
            result.append(-root)
        elif t1 == 0:
            result.append(0.0)
            
        if t2 > 0:
            root = math.sqrt(t2)
            result.append(root)
            result.append(-root)
        elif t2 == 0:
            result.append(0.0)

    result = sorted(set(result))
    return result

def main():
    a = get_coef(1, 'Введите коэффициент a: ')
    b = get_coef(2, 'Введите коэффициент b: ')
    c = get_coef(3, 'Введите коэффициент c: ')
    
    roots = get_biquadratic_roots(a, b, c)
    
    len_roots = len(roots)
    if len_roots == 0:
        print('Действительных корней нет')
    elif len_roots == 1:
        print(f'Один действительный корень: {roots[0]}')
    elif len_roots == 2:
        print(f'Два действительных корня: {roots[0]} и {roots[1]}')
    elif len_roots == 3:
        print(f'Три действительных корня: {roots[0]}, {roots[1]} и {roots[2]}')
    elif len_roots == 4:
        print(f'Четыре действительных корня: {roots[0]}, {roots[1]}, {roots[2]} и {roots[3]}')
    
if __name__ == "__main__":
    main()