def binarySearch(alist, item):
  first = 0
  last = len(alist)-1
  found = False
 
  while first<=last and not found:
    midpoint = (first + last)//2
    if alist[midpoint] == item:
      found = True
    else:
      if item < alist[midpoint]:
        last = midpoint-1
      else:
        first = midpoint+1
  return found

def binary_search(seq, t):
    min = 0
    max = len(seq) - 1
    while True:
        if max < min:
            return -1
        m = (min + max) // 2
        if seq[m] < t:
            min = m + 1
        elif seq[m] > t:
            max = m - 1
        else:
            return m

diff = num_list[1] - num_list[0]
    geo = abs(num_list[1]) / abs(num_list[0])
    
    for i in range(len(num_list)-1):
      if (num_list[i + 1] - num_list[i]) == diff:
        return 'Arithmetic'
      elif abs(num_list[i + 1]) / abs(num_list[i]) == geo:
        return 'Geometric'
      else:
        return -1
