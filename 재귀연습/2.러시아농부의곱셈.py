def farmer(expression):
    result = []
    expression = expression.split(' x ')
    left = int(expression[0])
    right = int(expression[1])
    recursion(left, right, result)
    return sum(result)


def recursion(left, right, result):
    if left % 2 == 1:
        result.append(right)
    if left < 2:
        return result
    return recursion(left//2, right*2, result)


print(123 * 12)
print(farmer('123 x 12'))
print('-'*20)
print(61 * 24)
print(farmer('61 x 24'))
print('-'*20)
print(30 * 48)
print(farmer('30 x 48'))
print('-'*20)
print(15 * 96)
print(farmer('15 x 96'))
print('-'*20)
print(7 * 192)
print(farmer('7 x 192'))
print('-'*20)
print(3 * 384)
print(farmer('3 x 384'))
print('-'*20)
print(1 * 768)
print(farmer('1 x 768'))
