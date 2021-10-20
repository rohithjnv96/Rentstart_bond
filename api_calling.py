import requests

data =   {
    "data": [
  {
    "INDEX": 0,
    "DATE": "2021-05-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 1,
    "DATE": "2021-06-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 2,
    "DATE": "2021-07-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 3,
    "DATE": "2021-08-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 4,
    "DATE": "2021-09-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 5,
    "DATE": "2021-10-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 6,
    "DATE": "2021-11-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 7,
    "DATE": "2021-12-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 8,
    "DATE": "2021-01-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 9,
    "DATE": "2021-02-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 10,
    "DATE": "2021-03-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 11,
    "DATE": "2021-04-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 12,
    "DATE": "2021-05-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  }
]
}

print(data)
print()
import pandas as pd
df = pd.DataFrame(data["data"])


print(df)

print()

res = requests.post(url = "https://sose-project.herokuapp.com/", json = data)


print(res.json())
