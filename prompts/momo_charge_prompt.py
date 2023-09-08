
TARRIF_CHARGE = """
Given a transaction, determine whether the transaction is fraudulent or not. 
Agreed customer charges are given in the below: 


"""

TRANSACTION_CHARGES = """
Given a transaction, determine the type of transaction based on the following tarriff list from a mobile financial service.
[
 {
  "code": "1DC12110",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer (P2P)",
  "Minimum Value GH¢": 1,
  "Maximum Value GH¢": 50,
  "actions": "pay",
  "Charge ": 0.38,
  "currancy": "GH¢",
  "Tax Charge": 1%
 },
 {
  "code": "1DC12112",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer (P2P)",
  "Minimum Value GH¢": "Above 50",
  "Maximum Value GH¢": 1000,
  "actions": "pay",
  "Charge ": 0.75%,
  "currency": "GH¢",
  "Tax Charge": 1%
 },
 {
  "code": "1DC12114",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer (P2P)",
  "Minimum Value GH¢": "Above 1000",
  "Maximum Value GH¢": 0,
  "actions": "pay",
  "Charge ": 7.5,
  "currency": "GH¢",
  "Tax Charge": 1%
 },
 {
  "code": "1DC12116",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer(to Merchant MSISDN)",
  "Minimum Value GH¢": 1,
  "Maximum Value GH¢": 50,
  "actions": "pay",
  "Charge ": 0.5,
  "currency": "GH¢",
 },
 {
  "code": "1DC12118",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer(to Merchant MSISDN)",
  "Minimum Value GH¢": "Above 50",
  "Maximum Value GH¢": 1000,
  "actions": "pay",
  "Charge ": 1%,
  "currency": "GH¢"
 },
 {
  "code": "1DC12120",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer(to Merchant MSISDN)",
  "Minimum Value GHc": "Above 1000",
  "Maximum Value GH¢": 0,
  "actions": "pay",
  "Charge ": 10,
  "currency": "GH¢"
 },
 {
  "code": "1DC12122",
  "Transaction Point": "Subscriber",
  "Services": "MoMo Pay(Merchant ID & QR)",
  "Minimum Value GH¢": 1,
  "Maximum Value GH¢": 1000,
  "actions": "pay",
  "Charge ": 0.005,
  "currency": "GH¢",
  "Tax Charge": 0
 },
 {
  "code": "1DC12124",
  "Transaction Point": "Subscriber",
  "Services": "MoMo Pay(Merchant ID & QR)",
  "Minimum Value GH¢": "Above 1000",
  "Maximum Value GH¢": 0,
  "actions": "pay",
  "Charge ": 5,
  "currency": "GH¢"
 },
 {
  "code": "1DC12126",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer (A2C)",
  "Minimum Value GH¢": 1,
  "Maximum Value GH¢": 50,
  "actions": "pay",
  "Charge ": 1.5,
  "currency": "GH¢",
  "Tax Charge": 0
 },
 {
  "code": "1DC12128",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer (A2C)",
  "Minimum Value GH¢": "Above 50",
  "Maximum Value GH¢": 1000,
  "actions": "pay",
  "Charge ": 3%,
  "currency": "GH¢"
 },
 {
  "code": "1DC12130",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer (A2C)",
  "Minimum Value GH¢": "Above 1000",
  "Maximum Value GH¢": 0,
  "actions": "pay",
  "Charge ": 30,
  "currency": "GH¢"
 },
 {
  "code": "1DC12132",
  "Transaction Point": "Subscriber",
  "Services": "Transfer to Other networks",
  "Minimum Value GH¢": 1,
  "Maximum Value GH¢": 50,
  "actions": "pay",
  "Charge ": 0.38,
  "currency": "GH¢",
  "Tax Charge": 1%
 },
 {
  "code": "1DC12134",
  "Transaction Point": "Subscriber",
  "Services": "Transfer to Other networks",
  "Minimum Value GH¢": "Above 50",
  "Maximum Value GH¢": 1000,
  "actions": "pay",
  "Charge ": 0.75%,
  "currency": "GH¢"
 },
 {
  "code": "1DC12136",
  "Transaction Point": "Subscriber",
  "Services": "Transfer to Other networks",
  "Minimum Value GH¢": "Above 1000",
  "Maximum Value GH¢": 0,
  "actions": "pay",
  "Charge ": 7.5,
  "currency": "GH¢"
 },
]

Consider the following examples, 
[Example 1]

input : {'transaction_amount': 300, 'rate': 0.7, 'transaction_type': 'PAYMENT', 'customer_code_sender': 'C-2VH2QFJ8XFY4', 'recipient': 'C-AK72Y9EX7U9E'}
response: MoneyTransfer (P2P)

[Example 2]
input: {'transaction_amount': 300, 'rate': 0.7, 'transaction_type': 'PAYMENT', 'customer_code': 'C-2VH2QFJ8XFY4', 'recipient': 'M-AK72Y9EX7U9E'}
response: MoMo Pay(Merchant ID & QR)
"""

TRANSACTION_CHARGES_X = """
Given a transaction, determine the type of transaction, and the total charge on the transaction based on the following tarriff list from a mobile financial service.
The total charges should include all types of charges(transaction_charge, tax, etc)
[
 {
  "code": "1DC12110",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer (P2P)",
  "Minimum Value GH¢": 1,
  "Maximum Value GH¢": 50,
  "actions": "pay",
  "Charge ": 0.38,
  "currancy": "GH¢",
  "Tax Charge": 1%
 },
 {
  "code": "1DC12112",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer (P2P)",
  "Minimum Value GH¢": "Above 50",
  "Maximum Value GH¢": 1000,
  "actions": "pay",
  "Charge ": 0.75%,
  "currency": "GH¢",
  "Tax Charge": 1%
 },
 {
  "code": "1DC12114",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer (P2P)",
  "Minimum Value GH¢": "Above 1000",
  "Maximum Value GH¢": 0,
  "actions": "pay",
  "Charge ": 7.5,
  "currency": "GH¢",
  "Tax Charge": 1%
 },
 {
  "code": "1DC12116",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer(to Merchant MSISDN)",
  "Minimum Value GH¢": 1,
  "Maximum Value GH¢": 50,
  "actions": "pay",
  "Charge ": 0.5,
  "currency": "GH¢",
 },
 {
  "code": "1DC12118",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer(to Merchant MSISDN)",
  "Minimum Value GH¢": "Above 50",
  "Maximum Value GH¢": 1000,
  "actions": "pay",
  "Charge ": 1%,
  "currency": "GH¢"
 },
 {
  "code": "1DC12120",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer(to Merchant MSISDN)",
  "Minimum Value GHc": "Above 1000",
  "Maximum Value GH¢": 0,
  "actions": "pay",
  "Charge ": 10,
  "currency": "GH¢"
 },
 {
  "code": "1DC12122",
  "Transaction Point": "Subscriber",
  "Services": "MoMo Pay(Merchant ID & QR)",
  "Minimum Value GH¢": 1,
  "Maximum Value GH¢": 1000,
  "actions": "pay",
  "Charge ": 0.005,
  "currency": "GH¢",
  "Tax Charge": 0
 },
 {
  "code": "1DC12124",
  "Transaction Point": "Subscriber",
  "Services": "MoMo Pay(Merchant ID & QR)",
  "Minimum Value GH¢": "Above 1000",
  "Maximum Value GH¢": 0,
  "actions": "pay",
  "Charge ": 5,
  "currency": "GH¢"
 },
 {
  "code": "1DC12126",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer (A2C)",
  "Minimum Value GH¢": 1,
  "Maximum Value GH¢": 50,
  "actions": "pay",
  "Charge ": 1.5,
  "currency": "GH¢",
  "Tax Charge": 0
 },
 {
  "code": "1DC12128",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer (A2C)",
  "Minimum Value GH¢": "Above 50",
  "Maximum Value GH¢": 1000,
  "actions": "pay",
  "Charge ": 3%,
  "currency": "GH¢"
 },
 {
  "code": "1DC12130",
  "Transaction Point": "Subscriber",
  "Services": "MoneyTransfer (A2C)",
  "Minimum Value GH¢": "Above 1000",
  "Maximum Value GH¢": 0,
  "actions": "pay",
  "Charge ": 30,
  "currency": "GH¢"
 },
 {
  "code": "1DC12132",
  "Transaction Point": "Subscriber",
  "Services": "Transfer to Other networks",
  "Minimum Value GH¢": 1,
  "Maximum Value GH¢": 50,
  "actions": "pay",
  "Charge ": 0.38,
  "currency": "GH¢",
  "Tax Charge": 1%
 },
 {
  "code": "1DC12134",
  "Transaction Point": "Subscriber",
  "Services": "Transfer to Other networks",
  "Minimum Value GH¢": "Above 50",
  "Maximum Value GH¢": 1000,
  "actions": "pay",
  "Charge ": 0.75%,
  "currency": "GH¢"
 },
 {
  "code": "1DC12136",
  "Transaction Point": "Subscriber",
  "Services": "Transfer to Other networks",
  "Minimum Value GH¢": "Above 1000",
  "Maximum Value GH¢": 0,
  "actions": "pay",
  "Charge ": 7.5,
  "currency": "GH¢"
 },
]

Consider the following examples, 
[Example 1]

input : {'transaction_amount': 300, 'rate': 0.7, 'transaction_type': 'PAYMENT', 'customer_code_sender': 'C-2VH2QFJ8XFY4', 'recipient': 'C-AK72Y9EX7U9E'}
response: {
    transaction_type: MoneyTransfer (P2P),
    total_charge: GH¢ 5.25 (charge * transaction_amount + tax_charge * transaction_amount)
    }

[Example 2]
input: {'transaction_amount': 300, 'rate': 0.7, 'transaction_type': 'PAYMENT', 'customer_code': 'C-2VH2QFJ8XFY4', 'recipient': 'M-AK72Y9EX7U9E'}
response: {
    transaction_type: MoMo Pay(Merchant ID & QR)
    total_charge: GH¢ 1.50 ((charge * transaction_amount + tax_charge * transaction_amount))
    }
"""