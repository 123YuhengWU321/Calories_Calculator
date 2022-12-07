
"""
Guan Zheng Huang
March 11
calculate calories associated with a type of fruit
"""


#return calories of object in calories
#type: type of fruit/vegeitable
#mass: mass of object, in grams
# source: calories.info
def getPrice(typee, mass):
    print("calculating calo")
    #stdType = typee.lower().strip()
    #error out if type empty or mass<0
    if (not typee or mass<0):
        return -1
    
    #defind calories per g based on data
    # value is per calories/gram
    CabbagePrice = 0.99
    BrocolliPrice = 1.99
    EggplantPrice = 1.99
    CarrotPrice= 1.49
    
    #list of all item mapped to calories
    typeList = [["Cabbage", CabbagePrice], 
                ["Broccoli", BrocolliPrice],
                ["Eggplant", EggplantPrice],
                ["Carrot", CarrotPrice]]
    
    stdType = typee
    print("cehcking", stdType)
    #find and return calclories
    for i in range(len(typeList)):
        
        print("cehcking", typeList[i][0])
        if (stdType == typeList[i][0]):
            print("retuning calo for: ", typeList[i][0])
            return mass*typeList[i][1]
        
    #if not found
    return -1
