"""
import calculation
result = calculation.subtract(10,20)
results = calculation.add(20,30)
print(result)
print(results)




from calculation import add
result = add(10,20)
print(result)
"""

import mypackage.calculation as c
result = c.add(10,20)
print(result)