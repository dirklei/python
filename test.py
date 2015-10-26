# import sys
# __author__ = 'yulei'
# print __author__
# list=dir(sys)
# # for i in range(len(dir(sys))):
# #    print(list[i])
#
# print type(__author__)
# test=dir(list)
# for i in range(len(test)):
#     test.pop();
# print len(test)
# test.append("i have a new paramter")
# print test
# test += ["2", "test plus"]
# print test
# test.insert(1, ["aaa", "what can i do?", "to explain this"])
# print test
# test.insert(10, "where did you insert")
# print test
#
# import whois;
# w = whois.whois("www.baidu.com");
# print type(w);
# import sys
# import random
#
# ans = True
#
# while ans:
#     question = raw_input("Ask the magic 8 ball a question: (press enter to quit) ")
#
#     answers = random.randint(1, 8)
#     answers1 = random.randint(7, 10)
#     answers2 = random.randint(3, 10)
#
#     if question == "":
#
#         sys.exit()
#
#     elif answers == 1:
#         print "It is certain"
#
#     elif answers == 2:
#         print "Outlook good"
#
#     elif answers == 3:
#         print "You may rely on it"
#
#     elif answers == 4:
#         print "Ask again later"
#
#     elif answers == 5:
#         print "Concentrate and ask again"
#
#     elif answers == 6:
#         print "Reply hazy, try again"
#
#     elif answers == 7:
#         print "My reply is no"
#
#     elif answers == 8:
#         print "My sources say no"
#     elif answers == 9:
#         print "this is new add option"
#     else:
#         print("out of range,system exit")
#
# ab={    'Swaroop'   :   'swaroopch@byteofpython.info',
#         'Larry'     :   'larry@eall.org',
#         'Matsumoto' :   'matz@ruby-lang.org',
#         'Spammer'   :   'spammer@hotmail.com'   #The last para has no ','
#     }
#
# for i in ab.iterkeys():
#
#     print  i + "'s address is %s" % ab[i]
#
#
# ab['yulei'] = 'yulei@belink.com'
#
# print ab.items();
# print [1,2,3,4,5][::2]
#Filename:001.py
# cnt = 0#count the sum of result
# rangeEnd = 10
# for i in range(1,rangeEnd):
#     for j in range(1,rangeEnd):
#         for k in range(1,rangeEnd):
#             if i!=j and i!=k and j!=k:
#                 #print i*100+j*10+k
#                 cnt+=1
# print cnt

#Filename:002.py
i = int(raw_input('Enter the profit:'))
arr = [80000,55000,35000,9000,4500,0]
rat = [0.45,0.35,0.30,0.25,0.20,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print (i-arr[idx])*rat[idx]
        i=arr[idx]
print r
