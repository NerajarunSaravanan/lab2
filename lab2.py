def display_main_menu():
  print("Enter numbers seperate by commas:")

def getuserinput():
   numlist = input()
   splitlist = numlist.split(",")
   values = []
   for count in splitlist:
     values.append(float(count))
   return values

def calc_avg(values):
 itemcount = len(values)
 total = sum(values)
 avg = sum(values)/len(values)
 print(avg)

def sorttemp(values):
  values.sort()
  print(values)

def calc_minmaxtemp(values):
  minimum = min(values)
  maximum = max(values)
  minmaxlist = [minimum, maximum]
  print(minmaxlist)

def calc_mediantemp(values):
  values.sort()
  itemcount = len(values)
  if itemcount % 2 == 0:
    medval1 = (itemcount // 2) - 1
    medval2 = (itemcount // 2)
    median = (values[medval1] + values[medval2]) // 2
    print(median)
  
  else:
    medval = itemcount // 2
    median = values[medval]
    print(median)

def main():
 print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
 display_main_menu()
 values = getuserinput()
 calc_avg(values)
 sorttemp(values)
 calc_minmaxtemp(values)
 calc_mediantemp(values)

 return 0

if __name__ == "__main__":
 main()