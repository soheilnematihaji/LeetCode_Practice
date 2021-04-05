"""
a 3X3 cellphone keyword, how many different way to unlock the phone?
123
456
789
requirement:
1: at least 4 numbers
2: no duplicated numbers
3: you can go left,right, up, down and diagonal (12357-yes 1234-no)

"""

def find_pattern(G,s,visited_node,length):
    neighs=G[s]
    answers=[]
    if length>3:
        answers.append([s])
    visited_node.append(s)
    for node in neighs:
        if not node in visited_node:
            answers.extend(find_pattern(G,node,visited_node,length+1))
    visited_node.remove(s)
    for item in answers:
        item.append(s)
    return answers

visited_node=[]
s=1
G={1:[2,4,5],2:[1,3,4,6,5],3:[2,5,6],
   4:[1,2,5,7,8],5:[1,2,3,4,6,7,8,9],6:[3,2,5,8,9],7:[4,5,8],8:[7,4,5,6,9],9:[8,5,6]}
for i in range(1,10):
    list_of_items.extend(find_pattern(G,i,visited_node,1))
