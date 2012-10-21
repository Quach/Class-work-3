# -*- coding: utf-8 -*-
"class practice work 3"

#def sum(e, z, a = 4, b = 3):
#	"Bla bla"
#	return a + b

def get_params(func):
	"Get info fucn"

	print "Name: ", func.func_name
	print "Docs: ", func.func_doc
	print "Count args: ", func.func_code.co_argcount
	print "Args: ", func.func_code.co_varnames
	print "Defaults: ", func.func_defaults
	return 

def my_filter(func, iterator):
	"Map"

	res = []
	for i in iterator:
		 if func(i):
		 	res.append(i)
	return res

def gh(param):
	"If more than 3"

	return param > 3

def my_reduce(func, sequence):
	"Reduce"

	if len(sequence) < 2:
		return None
	temp = sequence[0]
	for val in sequence[1:]:
		temp = func(temp, val)

	return temp

def my_sum(a, b):
	return a + b

def func1():
	def func2():
		pass
	return func2

def haskell(*funcs):
	def fC(x):
		for f in funcs[::-1]:
			x = f(x)
		return x
	return fC

def main():
    "main"

    temp_fc = haskell(gh, sum)
    assert temp_fc([1,10]) == True
    assert my_filter(gh, (1, 2, 3, 4, 5, 6)) == [4, 5, 6]
    assert my_reduce(my_sum, (1,1,1,1,1,1,4)) == 10
    assert (func1() is func1()) == False
    print "TEST OK!"
    raw_input()
    return 0

if __name__ == "__main__":    
	exit(main())
