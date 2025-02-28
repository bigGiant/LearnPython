def most_frequent(list):
  return max(set(list), key=list.count)

mylist = [1,1,2,3,4,5,6,6,2,2]
print("出现次数最多的元素是:", most_frequent(mylist))
