def dollar_to_euro(dollar_value):
	return dollar_value * 0.89

def euro_to_yen(euro_value):
	return euro_value * 124.15

####### ↓ YOUR CODE BELOW ↓ #######

enEuros = dollar_to_euro(137)
enYen=euro_to_yen(enEuros)
print(enYen)