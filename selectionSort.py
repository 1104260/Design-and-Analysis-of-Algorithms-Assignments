def selection_sort(listItem):
  for i in range(len(listItem) -2):
    min = i
    for j in range(i+1, len(listItem)):
      if listItem[j] < listItem[min]:
        min = j
    temp = listItem[i]
    listItem[i] = listItem[min]
    listItem[min] = temp
  return listItem