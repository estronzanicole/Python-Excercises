from functools import reduce

"""
manual_exponent(2, 3)
#> 8

manual_exponent(10, 2)
#>100
"""

def manual_exponent(num, exp):
    exp_list = [num] * exp
    return (reduce(lambda total, element: total *element, exp_list))

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))


# TEACHERS NOTES
