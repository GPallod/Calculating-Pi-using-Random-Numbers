Python 3.9.6 (v3.9.6:db3ff76da1, Jun 28 2021, 11:49:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> def pie(n):
	s=0
	for i in range(n):
		gcd = np.gcd(np.random.randint(1, 121, 2))
		if gcd == 1:
			s += 1
	return np.sqrt(6/(s/n))

>>> pie(100)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pie(100)
  File "<pyshell#9>", line 4, in pie
    gcd = np.gcd(np.random.randint(1, 121, 2))
ValueError: invalid number of arguments
>>> np.random.randint(1, 121, 2)
array([95, 99])
>>> np.gcd(1, 2)
1
>>> np.gcd(np.array([1, 2]))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    np.gcd(np.array([1, 2]))
ValueError: invalid number of arguments
>>> def pie(n):
	s=0
	for i in range(n):
		num1, num2 = np.random.randint(1, 121, 2)
		gcd = np.gcd(num1, num2)
		if gcd == 1:
			s += 1
	return np.sqrt(6/(s/n))

>>> pie(100)
2.9925280083228984
>>> pie(100)
3.1889640207164036
>>> pie(100000)
3.1384376195724837
>>> pie(100000)
3.1415334897403415
>>>  