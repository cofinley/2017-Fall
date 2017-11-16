"""
	Connor Finley
	Advanced Python
	Regex
	2017/11/12
"""

import re

MIN_PWD_LENGTH = 8
uppercase_pat = r"([A-Z]+)"
lowercase_pat = r"([a-z]+)"
digit_pat = r"(\d+)"

operator_pat = r"\b[^0-9]"
int_pat = r"-?\d+"
nonzero_pat = r"-?[1-9]+"
fraction_pat = r"({0}\/{1})".format(int_pat, nonzero_pat)
extract_fraction_pat = r"({0})\/({1})".format(int_pat, nonzero_pat)


class BadPasswordCharacter(Exception):
    pass


class InvalidFractionExpression(Exception):
    pass


def strong_pwd(pwd_string):
	has_strong_len = len(pwd_string) >= MIN_PWD_LENGTH
	has_upper = re.search(uppercase_pat, pwd_string)
	has_lower = re.search(lowercase_pat, pwd_string)
	has_digit = re.search(digit_pat, pwd_string)
	if has_strong_len and has_upper and has_lower and has_digit:
		return True
	else:
		raise BadPasswordCharacter("Password must be at least 8 characters in length, have at least one uppercase letter, one lowercase letter, and one digit.")


def clear_whitespace(s):
	clear_s = re.sub(r"\s", "", s)
	return clear_s


def extract_from_equation(s):
	equation = clear_whitespace(s)

	fractions_raw = re.findall(fraction_pat, equation)
	for f in fractions_raw:
		equation = re.sub(f, "", equation)
	fractions = [re.findall(extract_fraction_pat, i)[0] for i in fractions_raw]
	
	if len(fractions):
		fraction_1 = fractions[0]
		numerator_1, denominator_1 = fraction_1
		if len(fractions) == 1:
			operator = None
			numerator_2 = None
			denominator_2 = None
		if len(fractions) == 2:
			fraction_2 = fractions[1]
			numerator_2, denominator_2 = fraction_2
			operator = equation
		return numerator_1, denominator_1, operator, numerator_2, denominator_2

	raise InvalidFractionExpression("Invalid fraction regex")


p1 = "P455word"
is_strong = strong_pwd(p1)
print(p1, "is a strong password\n")

s = "-25/5 +- 55/2"
n1, d1, op, n2, d2 = extract_from_equation(s)
print("Numerator 1:", n1)
print("Operator:", op)
print("Denominator 1:", d1)
print("Numerator 2:", n2)
print("Denominator 2:", d2)