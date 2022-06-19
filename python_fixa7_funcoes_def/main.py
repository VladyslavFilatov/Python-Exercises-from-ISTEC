from datetime import datetime
import re



#1
def hey_wold():
    print("Hello world")

hey_wold()

#2
def ola_J(n):
    print(f"Ola {n}")

ola_J('Joana')

#3
def soma(a, b):
    sum = a + b
    print(sum)

soma(5,2)

#4
def soma_ret(a, b):
    return a + b

print(soma_ret(3, 4))

#5

def sobremesas(sobremesa1, sobremesa2, sobremesa3):
    print("O cliente escolher a sobremesa " + sobremesa3)
    
sobremesas(sobremesa2 = "Gelado de Lima", sobremesa3 = "Ananás",sobremesa1 = "Bolo folhado com doce de ovos")

#6
def lista(lista_a):
    print(lista_a)

lista([1,3,4])

#7
def summa(n):
    if n == 0:
        return 0
    return summa(n - 1) + n


print(summa(5))

#8
def summa_re(n):
    if n == 1:
        return 1
    else:
        return n + summa_re(n - 1)


print(summa_re(5))
#9
def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n

print(fac(5))

#10
def lista_(lista_b):
    s = sum(lista_b)
    print(s)

lista_([1,3,4])

#11
def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]

print(reverse_string("abcd"))

#12
def verif_num(n):
    if n > 1000 and n < 1000000:
        print(f"{True} "
              f"numero {n} > 1000 e < 10000000")
    else: print(False)

verif_num(1001)

#13
def str_cont_low_up(s):
    count_lower = 0
    count_upper = 0
    i = 0
    while i < len(s):
        if s[i].islower(): count_lower += 1
        if s[i].isupper(): count_upper += 1
        i += 1

    return f"letras pequenas: {count_lower} e letras grandes: {count_upper}"
    #return dict(count_lower="letras pequenas",count_upper="letras grandes")

print(str_cont_low_up("Hey"))

def str_low_up(s):
    print(f"letras grandes: {sum(map(str.isupper, s))}, letras pequenas: {sum(map(str.islower, s))}")

str_low_up("Hey")

#14
def array_same(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n


print(array_same([1,2,3,3,4,1]))

#15
def mudar_pos(l):
    l[1], l[3] = l[3], l[1]

    return l

print(mudar_pos([1,2,3,4,5]))

#16
def mudar_str(str):
    # Удаляем элемент с индексом 3
    # с помощью срезов и объединения
    res_str = str[:3] + str[4:]
    print(res_str)

mudar_str("pythonist")

#17


def printWords(s):

# split the string
    s = s.split(' ')
# iterate in words of string
    for word in s:
# if length is even
        if len(word)%2==0:
            print(word)

print(printWords("Hello World it's me"))

#18


def area(comprimento, largura):
    return comprimento * largura

def volume(altura, comprimento, largura):
    return altura * area(comprimento, largura)


print(volume(3,3,7))


#19
def time():
    current_datetime = datetime.now()
    print(current_datetime)

time()

