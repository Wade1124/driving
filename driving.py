country = input('請問你來自何方： ')
age = int(input('請問你今年幾歲： '))
if country == 'Macau':
	if age >= 18:
	    print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif country == 'Japan':
	if age >= 20:
	    print('你可以考駕照')
	else:
		print('你還不能考駕照')