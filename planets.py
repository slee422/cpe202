def weight_on_planets():
   # write your code here
   weight = int(input('What do you weigh on earth? '))
   Mars = weight * 0.38
   Jupiter = weight * 2.34
   print('\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds.' % (Mars, Jupiter))
   
   
   
if __name__ == '__main__':
   weight_on_planets()
