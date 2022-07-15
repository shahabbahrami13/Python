SJ = """As a public figure, Johansson is a prominent brand endorser and supports various charities. She has been cited as a Hollywood sex symbol by various media outlets. She was married to Canadian actor Ryan Reynolds from 2008 to 2011, and to French businessman Romain Dauriac, with whom she has a daughter, from 2014 to 2017. In 2020, Johansson married comedian Colin Jost."""

hazfiat = ['.', ',', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in hazfiat:
  SJ = SJ.replace(i, '')

print(SJ)

SJ = SJ.replace("  ", " ")

print(SJ)

SJ = SJ.split()

SJ_list = list(SJ)

print(SJ_list)
print(len(SJ_list))

SJ_set = set(SJ_list)

print(SJ_set)
print(len(SJ_set))

SJ_dict = {"as":"به عنوان",
           "from":"از"}

SJ_per=""

for i in SJ_list:
    if i in SJ_dict:
        SJ_per+=i
    else
        
