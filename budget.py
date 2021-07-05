class Category:
  def __init__(self, name):
    self.name = name;
    self.ledger = []
  
  def deposit(self, mons, *desc):
    if(desc != ()):
      self.ledger.append({"amount":float(mons), "description":desc[0]})
    else:
      self.ledger.append({"amount":float(mons), "description":""})
  def withdraw(self, mons, *desc):
    if(self.check_funds(mons)):
      if(desc != ()):
        self.ledger.append({"amount":float(mons * -1), "description":desc[0]})
      else:
        self.ledger.append({"amount":float(mons * -1), "description":""})
      return True
    else:
      return False
      

  def get_balance(self):
    total = 0
    for i in self.ledger:
      total = total + i.get("amount")
    return total
  
  def transfer(self, mons, other):
    if(self.check_funds(mons)):
      self.withdraw(float(mons), "Transfer to " + other.name)
      other.deposit(float(mons), "Transfer from " + self.name)
      return True
    else:
      return False
  
  def check_funds(self, mons):
    if(self.get_balance() >= mons):
      return True
    else:
      return False

  def __str__(self):
    s = '{:*^30}'.format(self.name) + "\n"
    for i in self.ledger:
      #print(i.get("description"))
      if(len(i.get("description")) > 23):
        s = s + '{:<23}'.format(i.get("description")[0:23]) + '{:>7}'.format("{:.2f}".format(i.get("amount"))) + '\n'

      else:
        s = s + '{:<23}'.format(i.get("description")) + '{:>7}'.format("{:.2f}".format(i.get("amount"))) + '\n'
    
    s = s + "Total: " + str(self.get_balance())
    return s



def create_spend_chart(categories):
  s = "Percentage spent by category\n"
  total = 0;
  lis = [];
  per = [];
  names = []
  for i in categories:
    cattot = 0;
    names.append(i.name)
    for w in i.ledger:
      if(w.get("amount") < 0):
        cattot = cattot + w.get("amount") * -1
        total = total + w.get("amount") * -1
    lis.append(cattot)
  
  #print(lis)
  #print("Total: " +str(total))
  
  for i in lis:
    per.append(int(i/total * 100))

  #print(per)
  
  for i in range(100, -1, -10):
    space = " "
    s = s + '{:>4}'.format(str(i) + "|")
    count = 0;
    for p in per:
      if(count == per.index(p)):
        if(p >= i):
          space = space + "o  "
        else:
          space = space + "   "
        count += 1;
    if(i == 100):
      s = s + space[1:] + "\n"
    else:
      s = s + space + "\n"



  s = s + " "*4 + "-"*((len(lis) * 3)+1) + "\n" 
  #print(names)

  x = ""
  for i in range(len(max(names, key=len))):
    new_s = "     "
    for n in names:
      if(i < len(n)):
          new_s = new_s + n[i] + "  "
      else:
        new_s = new_s + "   "
    new_s = new_s + "\n"
    x = x + new_s

  s = s + x[0: len(x)-1]
  return s

    