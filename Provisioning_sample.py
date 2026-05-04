hostname = ('wrt01.gru1','ert.gru1','ecs01.gru1')
n = 1
while n < 4:
    print(n)
    n = n + 1
else:
     print("n is no longer less than 6")


for x in hostname:
     print(x)

def myfunc(ipadd, mask):
     print(ipadd + ' ' + mask)

myfunc('10.0.0.0','255.255.255.0')

sw1 = 'arista'
sw2 = 'nexus'

def checksw(sw):
     if sw == sw1:
          return "the switch is " + sw1
     elif sw == sw2:
          return "The switch is " + sw2
     else:
          return "Its Big-IP"
     
print(checksw(sw2))