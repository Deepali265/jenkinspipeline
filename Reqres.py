import requests
import pandas as pd


class SendRequest:
    def sendrequest(self):
        tuple1 = ()
        list_for_tuple = []
        self.sample = requests.get('https://reqres.in/api/users')
        test = self.sample.json()
        #print("hee", sample.json(),"\n")
        #print(type(test))
        #to store the column headings(for this keys of just one of the list item are fetched)
        list1 = test["data"][0].keys()
        list_for_tuple.append(list1)
        for i in range(len(test["data"])):
            #print(test["data"][i].values(),"\n")
            #stores values(details) of each element or user from the list of list
            k = list((test["data"][i].values()))
            list_for_tuple.append(k)
        team = pd.DataFrame(list(tuple(list_for_tuple)))
        #output to excel file
        team.to_excel("UserData.xlsx", index=False)
        #print(team)

if __name__=="__main__":
    testInstance = SendRequest()
    testInstance.sendrequest()
        
