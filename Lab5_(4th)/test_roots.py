import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import math

# --- Сама тестируемая функция ---
def get_biquadratic_roots(a, b, c):
    result = []
    if a == 0:
        print("В биквадратном уравнении а не может равняться 0")
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
# --------------------------------

# Загружаем все сценарии из файла find_roots.feature
scenarios('features/find_roots.feature')

@pytest.fixture
def context():
    return {} # Возвращаем пустой словарь

@given(parsers.parse('коэффициенты биквадратного уравнения a={a:g}, b={b:g}, c={c:g}'))
def step_given_coeffs(context, a, b, c):
    context['a'] = a  
    context['b'] = b  
    context['c'] = c 

@when('функция вычисляет корни')
def step_when_calculates(context):
    # Передаем значения из словаря в функцию
    context['result'] = get_biquadratic_roots(context['a'], context['b'], context['c'])

@then(parsers.parse('результат должен содержать корни {expected_roots}'))
def step_then_result_contains(context, expected_roots):
    expected_list = [float(x) for x in expected_roots.strip('[]').split(', ')]
    
    actual_result_sorted = sorted(context['result'])
    expected_list_sorted = sorted(expected_list)
    
    assert actual_result_sorted == expected_list_sorted, \
        f"Ожидались корни {expected_list_sorted} (отсортированные), получены {actual_result_sorted} (отсортированные)"



@then(parsers.parse('функция должна вывести сообщение об ошибке "{message}"'))
def step_then_error_message(context, message):
    pass

@then(parsers.parse('результат должен содержать пустой список {empty_list}'))
def step_then_empty_result(context, empty_list):
    assert context['result'] == [], f"Ожидался пустой список, получен {context['result']}"
