#! python3
tableData = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],              
              ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    longRow = 0
    totalLongest = 0
    for list in range(len(table)):
        longest = 0
        
        for word in table[list]:
            curr = len(word)
            if (curr > longest):
                longest = curr
                
                if (longest > totalLongest):
                    totalLongest = curr
                    print('total longest: ', totalLongest)
                    longRow = list
        colWidths[list] = longest
        

    print(totalLongest)
    print (longRow)
            
        
    #printing
    #col 1:
    i=0
    j=0
    #print((table[0][0]).rjust(colWidths[0],'*'))
    for i in range(len(table)):
        rowToPrint = ""
        
        for j in range(len(table)): #range(len(table[i])) does the same thing, only difference is that this way 
            # will check each nested list individually
            #https://snakify.org/en/lessons/two_dimensional_lists_arrays/
            
        
            rowToPrint = rowToPrint + (table[0][j].rjust(totalLongest,' '))
            rowToPrint = rowToPrint + (table[1][j].rjust(totalLongest,' '))
            rowToPrint = rowToPrint + (table[2][j].rjust(totalLongest,' ')) + '\n'
            
    print(rowToPrint)
        

    



printTable(tableData)

    

