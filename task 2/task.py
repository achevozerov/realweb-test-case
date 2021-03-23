from math import factorial
def main(num, summ):

    # В случае если сумма меньше чем количество кубиков - вероятность её выпадения 0
    if summ < num:
        return 0
    # В случае если сумма больше чем количество кубиков умноженное на количество их граней - вероятность её выпадения 0    
    if summ > (num * 6):
        return 0
    # В рамках обработки простых результатов, если количество кубиков и сумма равны результатом всегда будет одинаковое значение
    if summ == num:
        return 1 / (6 * num)
    
    # В рамках обработки сложных результатов находим в англоязычном интернете формулу для решения этой задачи! (в readme в корне репозитория распишу)
    koef = int((summ - num) / 6)
    if summ > num:
        result = 0
        for i in range(koef+1):
        
            result += (-1) ** (i) * factorial(num) * factorial(summ - 6 * i - 1) / (factorial(num - i) * factorial(i) * factorial(num - 1) * factorial(summ - 6 * i - num))
        
        result = result / 6 ** (num)
        return result

if __name__ == '__main__':
    print(main(1, 6))
    print(main(1, 7))
    print(main(4, 14))