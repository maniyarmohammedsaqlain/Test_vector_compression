
Xfilledinputvector="0110111111111111111111111111111111101001100100111001001001000010101101000011110000111000110011000011011110101101001101110100011101100110100101100111111111111100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010001011101111111111111111111111111111111010011001001110010010010000101011010000111100001110001100110000110111101011010011011101000111011001101001011001111111111111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000110011"
def seperate(vector):
    current_pointer= vector[0]
    consecutive_count = 1
    firstarr=[]
    for digit in vector[1:]:
        if digit == current_pointer:
            consecutive_count += 1
        else:
            first=current_pointer * consecutive_count
            firstarr.append(first)
            current_pointer = digit
            consecutive_count = 1
    firstarr.append(current_pointer * consecutive_count)
    return firstarr
a=seperate(Xfilledinputvector)
def run(n):
    if len(n)==1:
        return "01"
    elif len(n)==2:
        return "001"
    elif len(n)==3:
        return "0001"
    else:
        f=len(n)//4
        m=len(n)%4
        st_mid=" "
        if m==1:
            st_mid="0"
        elif m==2:
            st_mid="00"
        elif m==3:
            st_mid="000"
    st_first=" "
    while f!=0:
        st_first+='1'
        f=f-1
    fin=st_first+st_mid+"01"
    return fin
final=[]
for i in a:
    final.append(run(i))
answer="".join(final)
answer.replace(" ","")
answerf=answer.replace(" ","")
def divide_into_parts(code, num_parts):
    divided_parts = []
    for i in range(0, len(code), num_parts):
        divided_parts.append(code[i:i+num_parts])
    return divided_parts
# long_code = "100111100101010101111111001111011100011110111011000111111010101001111011111011000011110001110000111110111001"
divided_code = divide_into_parts(answerf, 8)
mainl=[]
for i in divided_code:
    for j in range(0,8,4):
        l=[]
        l.append(i[j:j+4])
        mainl.append(l)
symbols=[]
for i in mainl:
    if i==['1111']:
        symbols.append('1')
    elif i==['0000']:
        symbols.append('0')
    else:
        symbols.append('u')
symbolslist=[]
for i in range(0,len(symbols),2):
    symbolslist.append(symbols[i]+symbols[i+1])
print(symbolslist)

newvector="";
for i in symbolslist:
    if (i=='00'):
        newvector+='0'
    elif(i=='11'):
        newvector+='10'
    elif(i=='01'):
        newvector+='11000'
    elif(i=='10'):
        newvector+='11001'
    elif(i=='1u'):
        newvector+='11010'
    elif(i=='u1'):
        newvector+='11011'
    elif(i=='0u'):
        newvector+='11100'
    elif(i=='u0'):
        newvector+='11101'
    else:
        newvector+='1111'
print(newvector)
print(len(newvector))
