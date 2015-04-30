import glob

def getListProduct(numList):
	product = 1
	for i in numList:
		i = int(i)
		product = product*i
	return product

def partition(numList,n):
	length = len(numList)
	g = 0
	newList = []
	subList = []
	while g+2 != (length): 
		newList.append(numList[g:g+n])
		g = g+1
	return newList

def getLargestPartition(numList,n):
	new = partition(numList,n)
	maxprod = 0
	dict_n = []
	for sub in new:
		prod = getListProduct(sub)
		if prod > maxprod:
			dict_n = [sub,prod]
			maxprod

	return tuple(dict_n)

def getLargestProduct():
	prod = 0
	maxprod = 0
	dic = []
	new_1 = []
	with open("./Number Grid.txt") as f:
		for line in f:
			new = line.split()
			i = 0
			while i < 20:
				new_1.append(new[i])
				i = i+1
			prod = getLargestPartition(new_1,4)
			new_1 = []
			if(prod[1] > maxprod):
				maxprod = prod
				dic = [prod[0],prod[1],'H']

	return tuple(dic)

def getDirectory():
    report_list = glob.glob("./reports/*") # creates a list of files in ./reports/ directory
    id_to_name_dict = {}                    # creates an empty dictionary

    # following segment reads users.text and creates a dictionary mapping id to first,last name
    with open("./users.txt") as f:
       	for line in f:
		new = line.split()
        f.readline()
        for line in f:  # read each required line
            temp_list = line.split()    # spit line into a list
            id_to_name_dict[ temp_list[3] ] = temp_list[1] + " " + temp_list[0][:-1] # obtain first name last name value

    name_to_unit_cost_dict = {} # create empty dictionary that must be returned

    for key in id_to_name_dict.keys():  # basically, for each user - id
        no_units = 0
        total_spending = 0.0

        for each_report in report_list: # read each report for each user
            with open(each_report) as f:
                user_id = f.readline().split()[2]
                if key == user_id:      # if the user is the creator of the report
                    f.readline()        # then add to no_units and total_spending the values in this file
                    f.readline()
                    f.readline()
                    for line in f:
                        line_list = line.split()
                        no_units += int(line_list[2])
                        total_spending += float(line_list[3][1:])

        name_to_unit_cost_dict[ id_to_name_dict[key] ] = (no_units, total_spending) # add values as tuple to dictionary
        # print("id: ", key, "name: ", id_to_name_dict[key], "units: ", no_units, "cost: ", total_spending)
    return name_to_unit_cost_dict


def generateReportForAllViruses():
    report_list = glob.glob("./reports/*")
    virusName_to_unit_cost_dict = {}
    for report in report_list:  # read each report
        with open(report) as f:
            f.readline();f.readline();f.readline();f.readline() # skip unwanted lines
            for line in f:                  # in the remaining lines
                line_list = line.split()    # split each line into a list
                virusName = line_list[1]    # obtain virus name , unit value and the cost in specified types
                unit = int(line_list[2])
                cost = float(line_list[3][1:])
                if virusName not in virusName_to_unit_cost_dict:    # if virus not already seen before
                    virusName_to_unit_cost_dict[virusName] = [unit, cost]   # create new instance of the virus
                else:   # otherwise, add cost and unit number to the instance of the virus that is already present
                    virusName_to_unit_cost_dict[virusName] = [ virusName_to_unit_cost_dict[virusName][0] + unit , virusName_to_unit_cost_dict[virusName][0] + cost ]

    dict_in_tuple_form = {}
    for key in virusName_to_unit_cost_dict: # run a loop to convert our string:[int,float] dictionary into a string:(int,float) type
        dict_in_tuple_form[key] = (virusName_to_unit_cost_dict[key][0],virusName_to_unit_cost_dict[key][1])

    return dict_in_tuple_form


def getUsersWithoutReports():
    report_list = glob.glob("./reports/*")
    id_to_name_dict = {}

    # following segment reads users.text and creates a dictionary mapping id to first,last name
    with open("./users.txt") as f:
        f.readline()
        f.readline()    # read unwanted lines
        for line in f:
            temp_list = line.split()
            id_to_name_dict[ temp_list[3] ] = temp_list[1] + " " + temp_list[0][:-1]    # add to list FirstName LastName

    for report in report_list:
        with open(report) as f:     # open and read through each report
            ID = f.readline().split()[2]
            if ID in id_to_name_dict:   # if ID is present in dictionary (which it will be), change name to "None"
                id_to_name_dict[ID] = "None"
    list_names = []
    for key in id_to_name_dict.keys():
        if id_to_name_dict[key] != "None":  # fom dictionary, add all names that are not equal to "None" we set above
            list_names.append(id_to_name_dict[key])
    setc = set(list_names)  # create a set out of the list that we have
    return setc


def getTotalSpending():
    report_list = glob.glob("./reports/*")
    sum = 0.0
    for report in report_list:
        with open(report) as f:
            f.readline()
            f.readline()
            f.readline()
            f.readline()    # skip all unwanted lines
            for line in f:  # for each of the remaining lines
                sum += float(line.split()[3][1:])   # we convert value to float and add it ti sum
    return sum # which is then returned


if __name__ == "__main__":
    #print("Hi");
    #f1_dict = generateReportForAllUsers()
    prod = getListProduct([1,2,3,4])
    print prod 
    prod = partition([1,2,3,4,5,6],3)
    print prod
    prod = getLargestProduct()
    print prod
