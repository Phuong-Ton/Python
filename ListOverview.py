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

one line

List[0], List[1] = List[1], List[0]

'''
List = ["a","b","c"]


List.append("d")
print("List.append('d'):", List)
List.insert(1,"a2")
print("List.insert(1,'a2'):", List)
List[0], List[1] = List[1], List[0]
print("Swap List List[0], List[1] = List[1], List[0]:",List)
List.reverse()
print("List.reverse():", List)
List.sort()
print("List.sort():", List)
print("Function max(List):",max(List))
print("Function min(List):",min(List))
popItem = List.pop(1)
print("List.pop(1):", List, "- Pop item:", popItem)
print("Function len(List):",len(List))