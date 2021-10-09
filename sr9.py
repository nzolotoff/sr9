def proga (a,b,c) :
	if a < b and b < c :
		return ('Выполняется A<B<C')
	elif a > b and b > c :
		return ('Выполняется A>B>C')
	elif a == b and b == c :
		return ('Ух ты! A=B=C! Но никакое из двух неравенств не выполняется :(')
	else :
		return ('Никакое из двух неравенств не выполняется :(')
try :
	a = float(input('Введите значение A\n'))
	b = float(input('Введите значение B\n'))
	c = float(input('Введите значение C\n'))
except ValueError : 
	print("Это не правильный ввод. Это не число вообще! Это строка, попробуйте еще раз.")
else :
	print (proga(a,b,c))