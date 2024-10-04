'''
List build-in Menthod
List.append("new item")
List.insert(2, "new item")
Function <> Method
Swap item
List = ["a","b","c"]
temp = List[0]
List[0] = List[1]
List[1] = temp
one line List[0], List[1] = List[1], List[0]
'''

List = ["a","b","c"]
List.append("d")
print("01.List.append('d'):", List)
List.insert(1,"a2")
print("02.List.insert(1,'a2'):", List)
List[0], List[1] = List[1], List[0]
print("03.Swap List List[0], List[1] = List[1], List[0]:",List)
List.reverse()
print("04.List.reverse():", List)
List.sort()
print("05.List.sort():", List)
print("06.Function max(List):",max(List))
print("07.Function min(List):",min(List))
popItem = List.pop(1)
print("08.List.pop(1):", List, "- Pop item:", popItem)
print("09.Function len(List):",len(List))
print("10.Iterating List by 'for item in List:' ")
for item in List:
    print("iterating :", item)

print("11.Using continue to skip interating if it match with condition equal 'b'")
for item in List:
    if item == 'b':
        continue
    print("iterating :", item)

newList = List
print("12.newList = List",newList)
List[0] = 'change'
print("print(newList) after List[0] = 'change'", List)

print("13.Using enumerate to get counter 'for i, item in enumerate(List):' ")
for i, item in enumerate(List):
    print(i, item)

print("14.Using enumerate reverse List - 'for i,item in enumerate(reversed(List)):'")
for i, item in enumerate(reversed(List)):
    print(len(List) - 1 - i, item)
'''
slice List
List[start:end:step]
'''
print("15.print(List):",  List)
print("List[1:3] - include position 1 drop 3:",List[1:3])
print("List[1:] - include postion 1:",List[1:])
print("List[:3] - include positon 3:",List[:3])
print("List[1:-1] = List[1:3]:",List[1:-1])
print("16.Before del List:",List)
del List[1:-1]
print("del List[1:-1]",List)
List[0:1] = ['a','a2']
print("17.List[0:1] = ['a','a2']", List)
print("18.Finding in List 'b in List':", 'b' in List)
print("18.Finding in List 'b not in List':", 'b' not in List)
print("19.List.index(a)", List.index('a'))
print(List)
newList = ['a','b','c']
Lists = [List,newList]
print("20.Nested Lists = [List,newList]:", Lists)
print("List[1]:",List[1])
print("Lists[0][1]:",Lists[0][1])
print("21.Inline 2 for with condition")
findchar = [char for sublist in Lists for char in sublist if len(char)>1]
print(findchar)

matrix = [[j for j in range(3)] for i in range(2)]
print(matrix)
