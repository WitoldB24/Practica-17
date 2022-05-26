list_numbers = [int(x) for x in input("Введите числа от 1 до 100, в любом порядке, через пробел: ").split()]
print(list_numbers )
while True:
    try:
        element = int(input("Введите число которое вы хотите сравнить, от 1 до 100: "))
        if element < 0 or element > 100:
            raise Exception
        break
    except ValueError:
        print("Надо ввести число")
    except Exception:
        print("Неверный диапазон")

list_numbers.append(element)
print(list_numbers)

def merge_sort(list_numbers):
    if len(list_numbers) < 2:
        return list_numbers[:]
    else:
        middle = len(list_numbers) // 2
        left = merge_sort(list_numbers[:middle])
        right = merge_sort(list_numbers[middle:])
        return merge(left, right)
        print (merge)
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

print(merge_sort(list_numbers))
list_numbers = merge_sort(list_numbers)

def binary_search(list_numbers, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if list_numbers[middle] == element:
        return middle
    elif element < list_numbers[middle]:
        return binary_search(list_numbers, element, left, middle - 1)
    else:
        return binary_search(list_numbers, element, middle + 1, right)

print(binary_search(list_numbers, element, 0,  len(list_numbers)))
