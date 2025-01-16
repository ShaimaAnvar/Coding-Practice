# mylist = ["a", "b", "a", "c", "c"]
# mylist=dict.fromkeys(mylist);
# # mylist = list(dict.fromkeys(mylist))
# print(list(mylist));

def removeDuplicate(a):
    mylist= list(dict.fromkeys(a));
    return mylist

print(removeDuplicate([1,2,1,2,3,4]));