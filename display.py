import time
x = 50
y = 50
displayString = ''
def display(itemList, displayString, x, y): #example for the itemList:
                                      #[['X', 50, 45], ['B', 12, 190]]
    for i in range(x):
        for j in range(y):
            for b in range(len(itemList)):
                if i == itemList[b][1] and j == itemList[b][2]: #checks for x and y position in itemList
                    displayString += itemList[b][0] #adds the symbol to the display String
                else:
                    displayString += ' '
        displayString += "\n"
    return(displayString)

if __name__ == "__main__": # only for testing :3
    
    #screen = display(itemList, displayString, x, y)
    #print(screen)
    for i in range(50):
        print(display([['X', i, i]], displayString, x, y))
        time.sleep(1/60)