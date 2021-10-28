
#######입력값#######
a, b = input('문자열 두 개 입력: ').split()
a = int(a)
b = int(b)
##################
c = -1 #체크 포인트
v = 1 #리스트의 들어갈 값이 저장될 변수


temp = []
result_list = [] #결과가 들어갈 리스트3
d = [] #중복 요소가 있는 리스트의 인덱스가 들어갈 리스트

while True:
    if len(temp) == b:
        if c == -1:
            break
        if temp[c] == a:
            c -= 1
            if temp[c] == a:
                continue
            temp[c] += 1
            del temp[c + 1:]
        else:
            if temp not in result_list:
                result_list.append(temp.copy())
            if temp[c] + 1 not in temp:
                temp[c] += 1
                if temp not in result_list:
                    result_list.append(temp.copy())
            else:
                temp[c] += 1
        v = 1
    else: #리스트가 덜 채워졌을 경우 없는 값으로 채우기
        if v not in temp:
            temp.append(v)
            if len(temp) == b and temp not in result_list:
                result_list.append(temp.copy())
            c += 1
        v += 1

for j in range(2, a + 1): #결과 리시트 중에서 중복 요소를 갖고 있는 리스트 제거
    for idx, i in enumerate(result_list):
        if i.count(j) > 1:
            d.append(idx)
    d.reverse()
    for i in d:
        del result_list[i]
    d.clear()

for i in result_list: #출력부분
    for j in i:
        print(j, end=' ')
    print('')
print(len(result_list))
