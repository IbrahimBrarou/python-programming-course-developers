# arrays are used instead of lists for performance and in case of large sequence of numbers, no need for arrays if there is no optimization
from array import array
numbers = array("i", [1, 2, 3])
numbers[0] = 1  # 0.1 would be a problem here
numbers.remove(0)
