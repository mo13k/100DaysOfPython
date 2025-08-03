#dictionaries intro
'''ogs = {
    'mo':'king',
    'gajan':'fat',
    'yadu':'victim'
}
ogs['waji'] = 'jacked'#to add stuff
print(ogs['mo'])'''

#nested lists
'''travels = {
    "Pakistan": {
        'visits': 10,
        'cities':["Karachi", "Islamabad", "Lahore"]
    },
    "Indonesia": ["Jakarta", "Bandung", "Bali"]
}

print(travels['Pakistan']['cities'][0])

nlist = ['a', 'b', ['c','d']]
print(nlist[2][0])'''

#silent auction
def findwinner(bids):
    return max(bids, key=bids.get)#to get the key with the max value
bids={}
bidding = True
while bidding:
    name = input("enter your name: ")
    bid = int(input("enter your bid: "))
    bids[name] = bid
    morebidders = input("are there more bidders? yes or no: ").lower()
    if morebidders == 'yes':
        print("\n"*20)
        bidding = True
    else:
        bidding = False
        print((findwinner(bids))+" won the silent auction")