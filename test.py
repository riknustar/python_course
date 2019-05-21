from scapy.all import rdpcap
from scapy.all import *
from scapy.utils import *

pkts_list = rdpcap('/home/pythontools/Downloads/file.pcap')
#This shows the number of packets in the file
lenpkrt = len(pkts_list)
#print(lenpkrt)


#This is an example of reading a packet

#pkts_list[0].show()

#This is how you access the parameters
#srcip = pkts_list[0]['IP'].src
#print(srcip)
x=0
#this is an example of looping through and printing out a specific paramter
# while (x < lenpkrt-1):
#     print(x)
#     x= x + 1
#     srcip = pkts_list[x]['IP'].src
#     print(srcip)

#While loop is used to find a src ip in question
broj=1
while (x < lenpkrt-1):
    # print(x)
    x= x + 1
    srcip = str(pkts_list[x]['IP'].src)
    if srcip == '192.168.2.147':
         
        #This shows you what the mac address is
       #if broj==1:
        #    mac = pkts_list[1]['Ethernet'].src
        #    print("MAC ",mac)
        #This will show you the whole packet
       
        #wholePacket = pkts_list[x].show()
        
        
        #print("Host: ", host)
        
        #print (wholePacket)
        #this exits the progam as soon as a positive result is returned

        try:
            test=pkts_list[x]['Raw'].load
            
            print(test.decode('utf-8'))

        except:
           
            red=""
            novi=""
            for i in range(len(test)):
                if test[i]< 32 or test[i]> 122:
                    if len(novi) > 5:
                      
                        red=red+":"+novi
                       
                    novi=""

                novi=novi+chr(test[i])

            if len(red) > 0:
                if "krbtgt" in red:
                    print (x,">",red)
            pass
        

            

        
        

        broj+=1
print(broj)