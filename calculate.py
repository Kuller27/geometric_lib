import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

    '''Функция calc принимает три аргумента: fig (название фигуры), func (название метода, который нужно вызвать), и size (список аргументов для метода).
    Проверяет, что fig принадлежит списку допустимых фигур figs и func принадлежит списку funcs.
    Затем использует eval для динамического вызова метода, формируя строку вида 'circle.area(*[5])', которая выполняется как вызов circle.area(5).
    Переменная result сохраняет результат выполнения этого метода.
    Выводит результат в формате: 'area of circle is 78.53981633974483'.
    '''
	
	calc(fig, func, size)



