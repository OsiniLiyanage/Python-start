
# The results are diferent due to operator precedence: parentheses override the default BODMAS order.

result_a = 10 + 5 * 2
result_b = (10 + 5) * 2

print(result_a)
print(result_b)