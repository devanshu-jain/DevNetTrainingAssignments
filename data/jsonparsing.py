import json
import unittest

class TestParse(unittest.TestCase):
    def test_parse(self,result):
        expected_names = ["ACCT100","ACCT200","ACCT300"]
        expected_paid = ["60","70","0"]
        expected_due = ["100","60","0"]

        expected_list = [expected_names,expected_paid,expected_due]

        self.assertEqual(result,expected_list)


def print_json():

    names = []
    paid=[]
    due=[]

    with open('C:/Users/devajain/Downloads/DevNetTrainingAssignments-master/data/db.json') as f:
        accounts = json.load(f)

    for account in accounts:
        print("Account name is :" + account)
        print("Paid amount for account :" + str(accounts[account]["paid"]))
        print("Due amount for account :" + str(accounts[account]["due"]))
        print("------------------------------------------------------------------------")
        names.append(account)
        paid.append(str(accounts[account]["paid"]))
        due.append(str(accounts[account]["due"]))

    return [names,paid,due]


if __name__ == "__main__":

    result = print_json()

    test = TestParse()
    test.test_parse(result)

    
