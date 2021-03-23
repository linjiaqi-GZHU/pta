# 要添加一个新单元，输入 '# %%'
# 要添加一个新的标记单元，输入 '# %% [markdown]'
# %% [markdown]
# ### python练习
# %% [markdown]
# ### 第二章

# %%
# 题目1:在同一行依次输入三个值a,b,c，用空格分开，输出 b*b-4*a*c的值
a,b,c = input().split()#split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
#print(type(a)) 查看数据类型，input输出的是str类型
a,b,c = eval(a),eval(b),eval(c) #eval( )函数将字符串str当作有效的表达式来求值并返回计算结果 
d = b*b - 4*a*c
print(d)


# %%
# 题目2:输出一句短语，Python语言简单易学。
#如果包含汉字，用"print(s.encode("utf-8"))"输出.
str_a = "Python语言简单易学"
print(str_a.encode("utf-8"))


# %%
# 题目3:输入一个正整数m(20<=m<=100)，计算 11+12+13+...+m 的值。
#方法1:
m = int(input())
s = 0
for i in range(11,m+1): #range(start, stop, step);range() 函数可创建一个整数列表，一般用在 for 循环中。
    s += i
print("sum = %d"%s)


# %%
#方法2
M = int(input())
s = range(11,M+1)
print("sum = %d"%sum(s))


# %%
#
u=int(input())
if u<0:
    print("Invalid Value!")
elif u<=50:
    cost=u*0.53
    #print("cost = {:.2f}".format(cost))
    print('cost = %.2f'%cost)
else:
    cost=0.53*50+(u-50)*(0.53+0.05)
    print("cost = {:.2f}".format(cost))


# %%
#题目4：给定两个均不超过9的正整数a和n，要求编写程序求a+aa+aaa++⋯+aa⋯a（n个a）之和。
a,n = map(int,input().split()) #map() 会根据提供的函数对指定序列做映射。
c = 0
s = 0
for i in range(n):
    c = c*10 +a
    s = s+c
print('s = %d'%s)


# %%
#题目5:在一行中按照“sum = S”的格式输出部分和的值S，精确到小数点后6位。题目保证计算结果不超过双精度范围。
a = int(input())
s = 0
b = 1
for i in range(1,a+1):
    if b%2 != 0:
        s = s + 1/b
        i+= 1
    b+= 1
#print('s = %.6f'%s)
print("sum = {0:.6f}".format(s))


# %%
N=int(input())
i=su=0
b=1
while i<N:
    if b%2!=0:
      su=su+1/b
      i+=1
    b+= 1
print("sum = {0:.6f}".format(su))


# %%
n=int(input())
#a=sum([1/i if i%2==1 else -1/i for i in range(1,n+1)])
#print(a)
x=-1
sum=0
for i in range(1,n+1):
    x+=2
    sum+=1/x
print("sum = {:.6f}".format(sum))


# %%
#题目6:本题要求编写程序，计算交错序列 1-2/3+3/5-4/7+5/9-6/11+... 的前N项之和。
n = int(input())
a = b = 1
s = 0
for i in range(1,n+1):
    s = s+(a/b)*(-1)**(i+1)
    b+=2
    a+=1
print('sum = %.3f'%s)


# %%
#题目7:读入2个正整数A和B，1<=A<=9, 1<=B<=10,产生数字AA...A,一共B个A
a,b = input().split(',')
b = int(b)
c = int(a*b)
print(c)


# %%
#题目8:输入一个整数和进制，转换成十进制输出
#class int(x, base=10)
#x -- 字符串或数字。
#base -- 进制数，默认十进制。
#如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制
a,b = input().split(',')
b = int(b)
print(int(a,b))


# %%
#题目9:本题要求将输入的任意3个整数从小到大输出。
# https://blog.csdn.net/qq_43727105/article/details/107149197
#输入格式：输入在一行中给出3个整数，其间以空格分隔。  4 2 8
#输出格式：在一行中将3个整数从小到大输出，其间以“->”相连。 2->4->8

#print(*sorted(map(int,input().split())),sep="->")
a,b,c = map(int,input().split())
d = [a,b,c]
print(*sorted(d),sep="->")

#python * 的用法
'''
1.可变长参数
当我们使用函数时，需要传入不定个数的位置参数时，就可以使用号表示，即args，以元组形式传入；
需要传入不定个数的关键字参数时，使用表示，即kwargs，以字典形式传入。

2.参数解包
python中号不仅用在形参中，也可以用在实参中。当某个函数中需要不定个位置参数时，
但是我们传入的实参是一个列表或元组时，就可以在列表或者元组前面加号，python会自动为我们进行解包。
'''


# %%
# 题目10:输入2个正整数lower和upper（lower≤upper≤100），请输出一张取值范围为[lower，upper]、且每次增加2华氏度的华氏-摄氏温度转换表。
#温度转换的计算公式：C=5×(F−32)/9，其中：C表示摄氏温度，F表示华氏温度。
a,b = map(int,input().split(','))
if a<=b:
    print('fahr celsius')
    f = a
    while f<=b:
        c = 5*(f*1-32)/9
        print('{0:d}{1:>6.1f}'.format(f,c))
        f+=2
else:
    print('Invalid')


# %%
#t=题目11:本题要求对两个正整数m和n（m≤n）编写程序，计算序列和m
m,n = map(int,input().split())

i = m
sum_1 = sum_2 = 0
while i<=n:
    sum_1 = sum_1 + i**2
    sum_2 = sum_2 + 1/i
    i+=1
s = sum_1 + sum_2
print('sum = %.6f'%s)

#sum=sum+i**2+1/i


# %%
#题目12:本题要求编写程序，根据输入的三角形的三条边a、b、c，计算并输出面积和周长。注意：在一个三角形中， 任意两边之和大于第三边。三角形面积计算公式：
#第2章-12 输出三角形面积和周长
from math import sqrt
a,b,c = map(int,input().split(','))
if ((a+b)<=c) or ((a+c)<=b) or ((b+c)<=a):
    print('These sides do not correspond to a valid triangle')
else:
    s = (a+b+c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    l = a+b+c
    print('area = %.2f;perimeter = %.2f'%(area,l))
#print('area = {0:.2f}; perimeter = {1:.2f}'.format(A,l))


# %%
#题目13
water_use = int(input())
if water_use <=15:
    y = 4*water_use/3
    print('%.2f'%y)
else:
    y = 2.5*water_use-17.5
    print('%.2f'%y)


# %%
#题目14
#首先顺序输出从A到B的所有整数，每5个数字占一行，每个数字占5个字符宽度，向右对齐。最后在一行中按Sum = X的格式输出全部数字的和X
a,b = map(int,input().split())
ls = list(range(a,b+1))
for index,i in enumerate(ls):  #enumerate
    index +=1
    print('%5d'%i,end='')
    if index % 5 == 0:
        if index < len(ls):
            print('')

print('\nSum = %d'%sum(ls))


# %%
#enumerate([1,3,45]) ---->   0,1  1,3   2,45

# %% [markdown]
# ### 第三章

# %%
#第一题
ls = list(map(int,input().split()))
average = sum(ls)/len(ls)
ls_av = []
for i in ls:
    if i > average:
        ls_av.append(i)
for index,v in enumerate(ls_av):
    if index < len(ls_av):
        print(v,end=' ')


# %%
#第二题
def check_id(id_n):
    weight = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    m = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
    id_n,last = id_n[:-1],id_n[-1]
#     if "X" in id_n:
#         return False
    for i in id_n:
        if i >= '0' and i <= '9':
            pass
        else:
            return False
    id_ls=list(map(int,list(id_n)))
    
    sumd = 0
    for w,i in zip(weight,id_ls):
        sumd += w*i
    check = sumd % 11
    check2 = m[check]
    if str(check2) == last:
        return True
    else:
        return False
    
    
num = int(input())
id_list = []
for i in range(num):
    id_n = input()
    id_list.append(id_n)
    
wrong = []
for i in id_list:
    is_ok = check_id(i)
    if is_ok is False:
        wrong.append(i)

if len(wrong) == 0:
    print("All passed")
else:
    for i in wrong:
        print(i)


# %%
list(map(int,list("37070419881216001X")))


# %%
for i ,v in zip([1,2,3],[4,5,6]):
    print(i,v)


# %%
# 第三
s = input()
s_1,s_2 = input().split()


# %%
s = s[::-1]
for i in range(len(s)):
    if (s_2==s[i]):
        print("{:d} {:s}".format(len(s)-i-1,s_2))
        
for i in range(len(s)):
    if (s_1 == s[i]):
        print("{:d} {:s}".format(len(s)-i-1,s_1))


# %%
check_id("37070419881216001X")


# %%
#黑体辐射
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants


# %%
def B_v(T):
    '''Function to calculate specific intensity/brightness distribution of black
    body radiation at a given temperature. T is in Kelvins and frequency 
    is in Hertz'''
    #Use Wien's displacement law to find the frequency range for given Temperature.
    # nu_max(in GHz) = 58.789*T(in Kelvin)
    nu_max = 58.79 * T
    freq = np.arange(1,2000,1)
    freq = freq * nu_max / 500.0 # Scale so that the the peak value occures at 1/4 the length of the array.
    B = (2*scipy.constants.h/scipy.constants.c**2.0)/ (np.exp((scipy.constants.h *
                                                              freq * 10**9)/(scipy.constants.k*T))-1) * (freq*10**9)**3
    #Change units for plotting to Jansky
    # 1 Jansky = 10^-26 W/m^2 Hz
    B = B * 10**26
    return B


# %%
fig,ax = plt.subplots()
T = [6000,6100,6200,6300,6400,6500,6600,6700] #In Kelvin
freq = np.arange(1,2000)
freq = freq*58.79*T[4]/500.0
for t in T:
    print(t)
    B_CMB = B_v(t)
    ax.plot(freq,B_CMB,label=str(t)+'K')
ax.legend()
ax.set_xlabel("Frequency (GHz)")
ax.set_ylabel("Specific Intensity ($Jy/sr$)")
ax.set_title("Blackbody Spectral Distribution")


# %%


def planck_formula(wavelength,      #波长
                   temperature,     #温度
                   c1=3.7414*10**8, #c1常量
                   c2=1.43879*10**4 #c2常量
                    ):
    return (c1/wavelength**5)*(1/(np.exp(c2/wavelength/temperature)-1))
#得到取样点以及输出取样点对应的值
wavelength_limit = np.linspace(0.001,100,1000)
T = [190,200,210,220,230]
for t in T:
    out = planck_formula(wavelength_limit,t)
    plot_500 = plt.plot(wavelength_limit,out,label= str(t)+'K')
# out_500 = planck_formula(wavelength_limit,500)
# out_800 = planck_formula(wavelength_limit,800)
# plot_500 = plt.plot(wavelength_limit,out_500,label='500K')
# plot_800 = plt.plot(wavelength_limit,out_800,label='800K')
#绘图
plt.xlim(3,40)
#plt.ylim(0,8000)
plt.xlabel('wavelength: μm')
plt.ylabel('spectral radiant emission: w/(cm^2 * μm)')
plt.title('Blackbody spectral radiant emission curve:')
plt.legend()
plt.show()


# %%
import numpy as np 
import matplotlib.pyplot as plt 


def planck_formula(wavelength,      #波长
                   temperature,     #温度
                   c1=3.7414*10**8, #c1常量
                   c2=1.43879*10**4 #c2常量
                    ):
    return (c1/wavelength**5)*(1/(np.exp(c2/(wavelength)/temperature)-1))
#得到取样点以及输出取样点对应的值
wavelength_limit = np.linspace(0.1,1.5,1000)
T = [5800,5900,6000,6100,6200,6300,6400,6500,6600,6700,6800,6900]
plt.figure(figsize=(15,10))
for t in T:
    out = planck_formula(wavelength_limit,t)
    plot_500 = plt.plot(wavelength_limit,out,label= str(t)+'K')
# out_500 = planck_formula(wavelength_limit,500)
# out_800 = planck_formula(wavelength_limit,800)
# plot_500 = plt.plot(wavelength_limit,out_500,label='500K')
# plot_800 = plt.plot(wavelength_limit,out_800,label='800K')
#绘图
#plt.xlim(3,50)
#plt.ylim(0,8000)
plt.xlabel('wave_length: μm',size=12)
plt.ylabel('spectral radiant emission: w/(cm^2 * μm)',size=12)
plt.title('Blackbody spectral radiant emission curve:',size=12)
plt.legend()
plt.show()


# %%
#3-4
#本题要求编写程序，从给定字符串中查找某指定的字符。


# %%
a = input()
b = input()
b = b[::-1]
if a in b:
    v = len(b)-1-b.index(a)
    print('index = %d'%v)
else:
    print('Not Found')


# %%
#3-5
#本题要求提取一个字符串中的所有数字字符（'0'……'9'），将其转换为一个整数输出。


# %%
# s = input()
# for i in s:
#     if i>='0' and i<='9':
#         print(i,end='')
s = input()
s2 =''
for i in s:
    if i>='0' and i<='9':
        s2+=i
print(int(s2))


# %%
#3-7
n = int(input())
# ls = []
# for i in range(n):
#     num = int(input())
#     ls.append(num)
ls = list(map(int,input().split()))
print(max(ls),ls.index(max(ls)))


# %%
#3-6
ls = list(map(int,input().split()))


# %%

a = ['1,2,3,4,2,3,2,3','123']
maxlabel = max(a,key=len)
print(maxlabel)


# %%
b = [1,2,4,4,4,5,6]


# %%
max(b,key=b.count)


# %%
b.count(max(b,key=b.count))


# %%
ls = list(map(int,input().split()))[1:]
max_v = max(ls,key=ls.count)
max_n = ls.count(max_v)
print(max_v,max_n)


# %%
d = [1,2,3,4,5,6,7]


# %%
def dis(v):
    return abs(v)


# %%
min(d ,key=dis)


# %%
d = [-3,-45,-1,1,0,4,5,6,4]


# %%



