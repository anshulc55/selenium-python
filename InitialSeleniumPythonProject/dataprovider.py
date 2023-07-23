
# Login Test Case
def getData(userName, password, browser):
    dataList = [userName, password, browser]
    return dataList

def getData1():
    dataList = []
    data1 = {"user1": "value1", "browser": "Chrome"}
    data2 = {"user2": "value2"}
    data3 = {"user3": "value3"}
    data4 = {"user4": "value4"}
    dataList.append(data1)
    dataList.append(data2)
    dataList.append(data3)
    dataList.append(data4)
    return dataList

def getData2():
    dataList = []
    data1 = {"user11": "value11", "browser": "Chrome"}
    data2 = {"user22": "value22"}
    data3 = {"user33": "value33"}
    data4 = {"user44": "value44"}
    dataList.append(data1)
    dataList.append(data2)
    dataList.append(data3)
    dataList.append(data4)
    return dataList

def getData3(testcase_Name):
    dataList = []
    data1 = {"user11": "value11", "browser": "Chrome"}
    data2 = {"user22": "value22"}
    data3 = {"user33": "value33"}
    data4 = {"user44": "value44"}
    if testcase_Name == "test1":
        dataList.append(data1)
        dataList.append(data2)
    elif testcase_Name == "test2":
        dataList.append(data3)
        dataList.append(data4)
    else:
        print("No data defined for this test, Returning empty....")
    return dataList