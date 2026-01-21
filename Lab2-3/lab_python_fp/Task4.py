data = [1, -3, 2, -70, 12, 17, 3, 9, 0, 1]

if __name__ == '__main__':
    
    result = sorted(data, key=abs, reverse=True)
    print(result)
    
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)
