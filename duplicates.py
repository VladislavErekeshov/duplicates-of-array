# Если массив содержит дубликаты, вункция выводит True,  если нет, то False

list = [1, 2, 3, 4, 2]
def dup(list):
    a = set(list)

    if len(a) == len(list):
        return "False"
    else:
        return "True"

print(dup(list))