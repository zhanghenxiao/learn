import re   #Ctrl + B
import getpass
import time
import sys
import pickle

#1—182
#字符串正则（）
# print(re.findall('sdas','uyouasdasqweq'))
#正则2元字符（.(通配一个字符) ^（起始）$(末尾) *(贪婪匹配0-n次) +(1-N次)}  ?(0-1次) [bc](b或c)  [^ab](非ab)
#{4}(匹配次数) {4,}(等价于*)  \ ()(组)） r(代表原生字符)
# print(re.findall('.',"abc"))  #['a', 'b', 'c']
# print(re.findall('a.',"abc"))  #['ab']
# print(re.findall('^a.',"abc"))  #['ab']
# print(re.findall('cw+','hhcwabc')) #['cw']
# print(re.findall('cw+','wccwcwwcchcwhhw')) #['cw', 'cww', 'cw']
# print(re.findall('[^0-7]','cwcwc1437989502cww'))
# print(re.findall('[^1-3]',"26411ah"))
# print(re.findall('[a-z]','A123qw'))
# print(re.search(r"(ab){0,1}","abababab").group())
# print(re.search(r"(ab){2,}","abababab").group())

#1-183
#\d匹配[0-9],\D匹配非[0-9]
#\w匹配所有数字字母不包括符号，\W 非
#\s匹配空格，\S 非
#print(re.findall('\s','@wq eip290hh'))
#findall匹配满足所有，search匹配满足一个就终止，match匹配最开始
#print(re.search('(abc)','wwabcc').group())
#print(re.match('(abc)','abcwwbac').group())
#非贪婪
#print(re.search('a(\d+?)','a123').group()) #a1
#print(re.search('a(\d*?)','a123').group()) #a

#1-184
#在()二边都有限制条件时findall贪婪匹配无效,search依然能用
# print(re.findall('a(\d*?)d','a23d'))   #23
# print(re.search('a(\d*?)d','a23d').group())   #a23d
# \ 引用序号对应得自组所匹配得字符串 赋予新的意义（\q）
# \b 匹配单词边界  指单词和空格间的位置
#print(re.search(r'(this)(test)\2','thistesttesttt').group()) #thistesttest
#print(re.findall('abc\b','abc 123'))  #[]
#print(re.findall(r'abc\b','abc 123'))  #['abc]
#re.findall(pattern,string,flags)  flags(re.I使匹配大小写不敏感，re.L,re.M,re.S)
#print(re.findall('com','COM',re.I))  #['COM']
#search,match 匹配后可用group(),start(),end()，span()返回一个元组包含匹配（开始，结束）
# a = '123abc456'
# print(re.search('([0-9]*)([a-z]*)([0-9]*)',a).group(0)) #123abc456
# print(re.match('([0-9]*)([a-z]*)([0-9]*)',a).group(1))  #123
# # compile ,split
# #sub替换 ，subn得到替换次数
#sub(pattern, repl, string, count=0, flags=0)
# print(re.sub('g.t',"have","you grt love, my got test")) #you have love, my have test
# print(re.subn('g.t',"have","you grt love, my got test")) #('you have love, my have test', 2)
# test = re.compile(r'\d+')
# print(test.split('one1two2three3')) #['one', 'two', 'three', '']
# print(test.split('4one1two2three3')) #['', 'one', 'two', 'three', '']

#1-185
#得到最里面的括号（括号里面没有括号的思路）
# test = '(1+2(-2+2.1*2/2)())'
#test1 = (re.search('\([^()]*\)',test).group())
# test1 = (re.search('\([^()]+\)',test).group())
# print(test1)
#[*/] 或乘或除
# print(re.search('\d+\.?\d+([*/]|\*\*)\d+\.?\d+',test1).group())

#1-186
#finditer(返回时迭代器的对象)
# p = re.compile(r'\d+')
# w = p.finditer('12 drumm44ers drumming, 11 ... 10...')
# for match in w:
#     print(match.group(),match.span())
# 12 (0, 2)
# 44 (8, 10)
# 11 (24, 26)
# 10 (31, 33)
#匹配IP
# a = '192.168.1.1'
# print(re.search(r'(
#
# .,a).group()) #192
# print(re.search(r"([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5]\.)",a).group())
#r(代表原生字符)
# print(re.findall(r"\\",'abc\com')) #['\\']
# a="ad11.0.0.000eqw"
# print(re.findall(r"([0-9]+\.？[0-9])",a))  #[]
# print(re.search(r"(\d+(\.\d+)*)",a).group())  #11.0.0.000



#1-188 特殊需求
# print(re.findall('www.(baidu|laonanhai).com','www.baidu.com')) #['baidu']
# print(re.findall('www.(?:baidu|laonanhai).com','www.baidu.com')) #['www.baidu.com']

#1-189
#time模块
# username = input( 'username:').strip()
# password = input('password:')
# print(username,password)
#print(time.gmtime(time.time()))

#1-190
#sys模块
# print(sys.argv) 传参
# if sys.argv[1] == '1' :
#     print("left is SX")
# else:
#     print("you are pig")
# print(sys.argv[1])
#sys.path 路劲
#print(sys.platform)

#1-191
#datetime 模块
#print(time.strftime("%Y-%m-%d %H:%m",time.localtime())) #2018-10-20 08:10
#进度条
# for i in range(31):
#     sys.stdout.write('\r')
#     #print('\r')
#     print("%s%% |%s"%(int(i/30*100),int(i/30*100)*'*'))
#     sys.stdout.flush() #强制刷新到屏幕
#     time.sleep(0.1)

#1-192
#pickle序列化
#字典里嵌套字典
# def testpickle():
#     account = {
#         1000:{
#             "username":'zhang',
#             "password":"123",
#             "money":9999,
#             'bank':{
#                 'ICBC':"123345",
#                 "ABC":"234567"
#             }
#         },
#         1001:{
#                 "username":'zhang',
#                 "password":"123",
#                 "money":9999,
#                 'bank':{
#                     'ICBC':"123345",
#                     "ABC":"234567"
#                 }
#             }
#     }
#     print(account[1000]["username"]) #zhang
#     f = open("account_db",'wb') #使用pickle写入文本（文本只支持str,所以需要用pickle），
#     f.write(pickle.dumps(account))
#     f.close()
#     #print(f.tell()) #指针
# def reduce():
#     w = open("account_db","rb")
#     #print(w.read())  #会是二进制
#     re_dic = pickle.loads(w.read())  #读取txt
#     re_dic = pickle.load(w)#也可读取
#     print(re_dic)
#     re_dic[1000]["money"] = re_dic[1000]["money"] - 1111
#     p = open("account_db","wb")
#     pickle.dumps("re_dic")
#     print(re_dic)
#
#     #print(re_dic[1000]["money"])
# if __name__ == "__main__":
#     testpickle() #pickle写入
#     reduce()

# 1-193
# json 可以与其他语言交换
# 1-195  -----1-201
#回顾re
#re.match  从头(第一个字母)匹配，第一个没匹配上就fail  web场景
#re.search 浏览全部，匹配第一个出现的字符串
#re.findall 将匹配的所有内容放置列表中(顺序)
#re.finditer 迭代器
#re.sub      替换
#re.split
#re.match无分组
# test = "good morning this is time 10"
# test1 = re.match("g\w+",test)
# print(test1.group()) #返回匹配的所有结果
# print(test1.groups()) #获取模型中匹配到的分组结果
# print(test1.groupdict()) #获取模型中匹配到分组中所有执行key的组
# #re.match有分组()
# test = "good morning this is time 10"
# test1 = re.match("g(?P<m1>\w+)",test)
# print(test1.group())
# print(test1.groups()) #('g', 'ood')
# print(test1.groupdict()) #{'m1': 'ood'}
#re.serch无分组
# test = "good morning this is time 10"
# test1 = re.search("m\w+",test) #morning
# print(test1.group())
# print(test1.groups())
# print(test1.groupdict())
#re.serch有分组
# test = "good morning this is time 10"
# test1 = re.search("m(\w+).*(?P<n1>\d)$",test) #morning
# print(test1.group())
# print(test1.groups())
# print(test1.groupdict())
#findall,fileiter.split
# test = "good morning this is time 10"
# test1 = re.findall("t(\w+)",test) #['his', 'ime']
# test1 = re.findall("(t)(\w+)",test) #[('t', 'his'), ('t', 'ime')]
# test1 = re.findall("(t)((\w+)(i))(s)",test) #[('t', 'hi', 'h', 'i', 's')]
# print(test1)
# test2 = re.finditer("m(\w+)(ng)",test)
# for i in test2:
#     print(i.group(),i.groups(),i.groupdict())
# print(re.split("m\w+",test)) #['good ', ' this is ti', ' 10']
# print(re.split("(m\w+)",test)) #['good ', 'morning', ' this is ti', 'me', ' 10']
# print(re.split("(m\w+)",test)) #只分割一次

# 感悟:加上\后失去特殊的含义如\(\)，[()]中的括号也会失去特殊的含义，因为[]本身是具有意义的
#计算机原理思路
# origin = "1-2*((60-30+(-40.0/5)(520+100/3)))"
# #print(re.split("(\([^()]+\))",origin)) #['1-2*((60-30+', '(-40.0/5)', '', '(520+100/3)', '))']
# n = re.split("\(([^()]+)\)",origin,1) #['1-2*((60-30+', '-40.0/5', '', '520+100/3', '))']
# print(n)
# print(len(n))
# print(n[0])
# def add(ex):
#     return 1
# while True:
#     print(origin)
#     n = re.split("\(([^()]+)\)", origin, 1)
#     if len(n) == 3:
#         before = n[0]
#         counnt = n[1]
#         after = n[2]
#         result = add(counnt)
#         newstr = before + str(result) + after
# #         origin = newstr
# #     else:
# #         #print(add(1+4))
# #         pass
#17830315081
















