#coding=utf-8
#循环和判断
# def   invest(amount,rate,time):
#     print('principle amount:'+ str(amount))
#     for i in range(1,time+1):
#         amountplus = amount *(1+rate) ** i
# #        print ('year'+ str(i)+':$' + str(amountplus))
# #       print('{}{}{}{}'.format('year',i,':$',amountplus))
#         print('year{}:${}'.format(i,amountplus))
#
# invest(100,0.05,8)


# for i in range(1,101):
#     if i % 2 == 0:
#         print(i)

#format() 字符串处理方法
# <模板字符串>.format(<逗号分隔的参数>)
# print('{}:计算机{}的CPU占用率为{}%。'.format('2016-12-31','python',10))
# print('{}{}{}'.format("圆周率是",3.1415,"..."))


#综合练习
# a_list = [1,2,3]
# print(sum(a_list))


# point1 = random.randrange(1,7)
# point2 = random.randrange(1,7)
# point3 = random.randrange(1,7)
# print (point1,point2,point3)

# # #摇骰子函数 ，考虑如果没有摇筛子怎么处理
# import  random
# def roll():
#     random1 = random.randrange(1,6)
#     random2 = random.randrange(1,6)
#     random3 = random.randrange(1,6)
#     randomResult = [random1,random2,random3]
#     return randomResult
#
# # #求和
# def jisuan(total):
#
#     if 11 <=total<= 18:
#         jisuanresult = 'big'
#     else:
#         jisuanresult = 'small'
#     return jisuanresult
#
# def main():
# #用户输入数字
#     list = ['big','small']
#     randomresult = roll()
#     total = sum(randomresult)
#     sumvalue = jisuan(total)
#     guess = input('big or small:')   #判断输入除了big或small之外的字符串怎么处理
#     if guess in list:
# #判断结果
#         if guess == sumvalue:
#             print('the points are{} you win'.format(randomresult))
#         else:
#             print('the points are{} you lose!'.format(randomresult))
#     else:
#         print('invalid word')
#         main()
# main()



# #摇骰子函数 ，考虑如果没有摇筛子怎么处理
# import  random
# def roll():
#     random1 = random.randrange(1,6)
#     random2 = random.randrange(1,6)
#     random3 = random.randrange(1,6)
#     points = [random1,random2,random3]
#     return points
#
# # #求和
# def roll_result(roll_lists):
#     total = sum(roll_lists)
#     if 11 <=total<= 18:
#         jisuanresult = 'big'
#     else:
#         jisuanresult = 'small'
#     return jisuanresult
#
# def game_start(amount):
# #用户输入数字
#     print('<<<<<<<<<<<game start!>>>>>>>>>>>>>>>>>')
#     list = ['big','small']
#     roll_list= roll()
#     sumvalue = roll_result(roll_list)
#     guess = input('big or small:')   #判断输入除了big或small之外的字符串怎么处理
#     bet = input('how much  you want  bet:')
#     if guess in list:
# #判断结果
#         if guess == sumvalue:
#             print('the points are{} you win'.format(roll_list))
#             amount = amount + int(bet)
#             print('you gained {},you have {} now'.format(bet,amount))
#         else:
#             print('the points are{} you lose!'.format(roll_list))
#             amount = amount - int(bet)
#             print('you lost {},you have {} now'.format(bet, amount))
#             if amount == 0:
#                 print('game over')
#     else:
#         print('invalid word')
#         game_start()
# game_start(1000)


# def register_phone():
#     phone_number = input('Enter your number:')
#     length = len(phone_number)
#     top3 = phone_number[0:3]
#     print(top3)
#     CN_mobile = ['123',134,136,137,138,139,150]
#     CN_union = [130,131,132,155,156,185]
#     CN_telecom = [133,153,180]
#     CN = CN_telecom + CN_mobile + CN_union
#     print(CN)
#     if length == 11:
#         if top3 in CN:
#             if top3 in CN_mobile:
#                 print('operator:china mobile')
#             elif top3 in CN_union:
#                 print('operator:china union')
#             else:
#                 print('operator:china telecom')
#         else:
#             print('No such a operator')
#             register_phone()
#     else:
#         print('invalid length,your number should be in 11 digits')
#         register_phone()
#
# register_phone()

########列表，以及增删改查
# weekday = ['monday','tuesday','wednesday','thursday']
# print(weekday[0])
#
# weekday.insert(1,'sunday') #增加多个元素使用extend
# print(weekday)
#
# weekday.remove('sunday')
# print(weekday)
#
# del weekday[0:2]
# print(weekday)

# print(weekday[-3:-1])

######字典，以及增删改查
# NASDAQ_code = {
#     'bidu':'Baidu',
#     'sina':'Sina',
#     'yoku':'Youku'
# }
# # NASDAQ_code = {
# #     'bidu':'Baidu',
# #     'bidu':'Baidu'
# # }
# #增加
# NASDAQ_code['lala'] = 'LALA'
#
# #增加多个元素
# NASDAQ_code.update({'haha':'5','bubu':'bubu'})
#
# #删除
# del NASDAQ_code['bubu']
#
# print(NASDAQ_code)
# print(NASDAQ_code['haha'])

#######元组不能修改
# letters = ('a','b','c')
# print(letters[0])

##########集合
# a_set = {1,2,3,4}
# a_set.add(5)
# a_set.discard(5)
# print(a_set)


##########排序顺序，逆序
# num_list = [6,2,7,4,1,3,5]
# print(sorted(num_list))
# print(sorted(num_list,reverse = True))

#zip函数,两个列表同步循环
# num = [1,2,3]
# str = [4,5,6]
# for a,b in zip(num,str):
#     print(b,'is',a)


# a = []
# for i in range(1,11):
#     a.append(i)
# print(a)


########推导式技巧
# a = [i**2 for i in range(1,10)]
# print(a)
# c = [j+1 for j in range(1,10)]
# print(c)
# k = [n for n in range(1,10) if n % 2 == 0]
# print(k)
# z = [letter.lower() for letter in 'ABCDEFGHIJKLMN']
# print(z)

###字典，zip函数两组字符串、数字同步循环
# d = {i:i+1 for i in range(4)}
# print(d)
# g = {i:j for i,j in zip(range(1,6),'abcde')}
# print(g)
# g = {i:j.upper() for i,j in zip(range(1,6),'abcde')}
# print(g)

#enumerate()

#综合项目
# lyric = 'the night begin to shine , the night begin to shine'
# print(lyric.split())

# import string
# path = 'C:/Users/Administrator/Desktop/Walden.txt'
# #file = open(path,'r')
# #https://www.cnblogs.com/DswCnblog/p/6126588.html  with...as使用方法
#
# with open(path, encoding='utf-8') as text:
# #     words = text.read().split()
# #     print(words)
# #     for word in words:
# #         print('{}-{} times'.format(word,words.count(word)))
#     words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]

##########类,类里面才有self
# class CocoCola:
#     formula = ['caffeine','sugar','water','soda']
#     def drink(self):
#         print('energy')

# coke_for_me = CocoCola
# coke_for_you = CocoCola
# print(CocoCola.formula)
# print(coke_for_me.formula)
# print(coke_for_you.formula)

# for element in coke_for_me.formula:
#     print(element)

# coke_for_china = CocoCola
# coke_for_china.local_logo = '可口可乐'
#
# print(coke_for_china.local_logo)
# coke_for_china.drink()