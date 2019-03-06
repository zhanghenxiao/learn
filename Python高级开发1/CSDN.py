import re
"""
#正则表达式一
#findall匹配原则：匹配满足所有条件的字符
test = re.findall('abc','abcabaabc')
print(test)
#['abc', 'abc']

a = "abcaabbcc"
print(re.findall('.',a))
#['a', 'b', 'c', 'a', 'a', 'b', 'b', 'c', 'c']
print(re.findall('a+',a))
#['a', 'aa']
print(re.findall('a*',a))
#['a', '', '', 'aa', '', '', '', '', '']
print(re.findall('a?',a))
#['a', '', '', 'a', 'a', '', '', '', '', '']
"""
"""
#正则表达式二
#search匹配原则：浏览全部，匹配第一个出现的字符串。
test = (re.search('abc','abcababc')).group()
print(test)
#abc
print(re.search('a(\d+?)','a123').group())
#a1
print(re.search('a(\d*?)','a123').group())
#a
print(re.search('a(\d*?)d','a23d').group())   #a23d
#a23d

#match匹配原则：从头(第一个字母)匹配，第一个没匹配上就fail
a = '123abc456'
print(re.match('1',a).group())
#1
print(re.search('([0-9]*)([a-z]*)([0-9]*)',a).group(0))
#123abc456
print(re.match('([0-9]*)([a-z]*)([0-9]*)',a).group(1))
#123
#sub替换 ，subn得到替换次数
#sub(pattern, repl, string, count=0, flags=0)
cc = "you grt love, my got test"
print(re.sub('g.t',"have",cc))
#you have love, my have test
print(re.subn('g.t',"have","you grt love, my got test"))
#('you have love, my have test', 2)
#split分隔
test = re.compile(r'\d+')
print(test.split('one1two2three3'))
#['one', 'two', 'three', '']
print(test.split('4one1two2three3'))
#['', 'one', 'two', 'three', '']
"""
"""
#正则表达式三
#分组能满足一些特定得需求
#re.match无分组
test = "good morning this is time 10"
test1 = re.match("g\w+",test)
print(test1.group()) #good #返回匹配的所有结果
print(test1.groups()) #()#获取模型中匹配到的分组结果
print(test1.groupdict()) #()#获取模型中匹配到分组中所有执行key的组
# #re.match有分组()
test = "good morning this is time 10"
test1 = re.match("g(?P<m1>\w+)",test)
print(test1.group())  #good
print(test1.groups()) #('g', 'ood')
print(test1.groupdict()) #{'m1': 'ood'}
#re.serch无分组
test = "good morning this is time 10"
test1 = re.search("m\w+",test)
print(test1.group()) #morning
print(test1.groups())
print(test1.groupdict())
#re.serch有分组
test = "good morning this is time 10"
test1 = re.search("m(\w+).*(?P<n1>\d)$",test)
print(test1.group()) #morning this is time 10
print(test1.groups()) #('orning', '0')
print(test1.groupdict()) #{'n1': '0'}
#findall,fileiter.split
test = "good morning this is time 10"
test1 = re.findall("t(\w+)",test)
print(test1)    #['his', 'ime']
test1 = re.findall("(t)(\w+)",test)
print(test1)    #[('t', 'his'), ('t', 'ime')]
test1 = re.findall("(t)((\w+)(i))(s)",test) #[('t', 'hi', 'h', 'i', 's')]
print(test1)    #[('t', 'hi', 'h', 'i', 's')]
test2 = re.finditer("m(\w+)(ng)",test)
for i in test2:
    print(i.group(),i.groups(),i.groupdict())
print(re.split("m\w+",test)) #['good ', ' this is ti', ' 10']
print(re.split("(m\w+)",test)) #['good ', 'morning', ' this is ti', 'me', ' 10']
print(re.split("(m\w+)",test)) #['good ', 'morning', ' this is ti', 'me', ' 10']#只分割一次
"""
#正则表达式四
#应用场景
#获取IP
a="ad11.0.0.000e00qw"
print(re.search(r"(\d+(\.\d+)*)",a).group())  #11.0.0.000
#计算器原理:首先渠道
# test = '(1+2(-2+2.1*2/2（1+1）))+(2+3)'
# test1 = (re.search('\([^（)]*\)',test).group())
# print()
# a = (re.search('\([^()]*\)',test1).group())
# print(test1, a)
#test2 = (re.search('\([^()]+\)',test).group())
#print(test1,test2)
#[*/] 或乘或除
# print(re.search('\d+\.?\d+([*/]|\*\*)\d+\.?\d+',test).group())













