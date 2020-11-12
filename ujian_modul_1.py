### SOAL 1 ###
# p = input('Input your phone number:')
# def create_phone_number():
#     if p.isalpha():
#         print('Invalid input. No alphabet')
#     elif p == '-':
#         print('Input only positive number')
#     elif len(p) != 10:
#         print('Digits must be in length of 10, not more or less')
#     elif p.isdigit:
#         print(f'({p[0:3]}) {p[3:6]}-{p[6:]}')     
#     else:
#         print('Invalid input. No symbols')
     
# create_phone_number()

###=================================================================================###


### SOAL 2 ###

# def moveZeros(x):
#     zero = []
#     list_baru = []
#     for i in range(len(x)):
#         if x[i] == 0 or x[i] == '0' or x[i] == 0.0:
#             if type(x[i]) == str or type(x[i]) == int or type(x[i]) == float:
#                 zero.append(x[i])
#             else:
#                 list_baru.append(x[i])   
#         else:
#             list_baru.append(x[i])
#     list_baru.extend(zero)
#     print(list_baru)

# moveZeros([False, 1, 0, 1, 2, 0, 1, 3, 'a'])
# moveZeros([0, 0, 0, 'Test', 0, 3, 'a', True, False])
# moveZeros([0, True, True, False, 'a', 'b', 1, 1, 1])

###=================================================================================###

### SOAL 3 ###

class Statistic:

    def total(x):
        a = 0
        for i in x:
            a = a + i
        return a 
        
    def mean(y):
        return total(y) / len(y)
    
    def median():
        

st = Statistic()
st.mean([1,2,3,4,5])

