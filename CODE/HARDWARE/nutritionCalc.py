
"""
Guan Zheng Huang
March 11
calculate calories associated with a type of fruit
"""


#return calories of object in calories
#type: type of fruit/vegeitable
#mass: mass of object, in grams
# source: calories.info
def getCalo(typee, mass):
    print("calculating calo")
    #stdType = typee.lower().strip()
    #error out if type empty or mass<0
    if (not typee or mass<0):
        return -1
    
    #defind calories per g based on data
    # value is per calories/gram
    CabbageCalo = 12/100
    BrocolliCalo = 34/100
    EggplantCalo = 25/100
    CarrotCalo= 41/100
    
    #list of all item mapped to calories
    typeList = [["Cabbage", CabbageCalo], 
                ["Broccoli", BrocolliCalo],
                ["Eggplant", EggplantCalo],
                ["Carrot", CarrotCalo]]
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