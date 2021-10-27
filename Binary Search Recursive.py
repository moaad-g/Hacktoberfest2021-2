def RecursiveBinarySearch (prohibited_list, list_length, list_rear, word_input): 
    if list_rear >= list_length: 
        mid = int(list_length + (list_rear - list_length)/2)
        print (prohibited_list[mid])
        if prohibited_list[mid] == word_input: 
            return True 
        elif prohibited_list[mid] > word_input: 
            return RecursiveBinarySearch(prohibited_list, list_length, mid-1, word_input) 
        else: 
            return RecursiveBinarySearch(prohibited_list, mid+1, list_rear, word_input) 
    else: 
        return False

word_input = str(input("gern:"))
print(len(word_input))
with open("Prohibited_Words.txt","r") as Prohibited_File:
    prohibited_list_1 = Prohibited_File.readlines()
    print (prohibited_list_1)
    prohibited_list = []
    for x in range (0,(len(prohibited_list_1)-1)):
        word = (prohibited_list_1[x][0:(len(prohibited_list_1[x])-1)])
        prohibited_list.append(word)
        
    print(prohibited_list) 
    result = RecursiveBinarySearch(prohibited_list,0,len(prohibited_list)-1,word_input)

if result == True:
    print("The item is in the list")

else:
    print("Item not in the list.")
