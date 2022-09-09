def StringManipulation(str):

    a=list(input())
    for i in range (len(a)):
        n=ord(a[i])
        if(n>=65 and n<90):
            n=n+1
            a[i]=chr(n)
        elif(n>=97 and n<122):
            n=n+1
            a[i]=chr(n)
        elif(n==90):
            n=65
            a[i]="A"
        elif(n==122):
            a[i]="a"
    
    for i in range(len(a)):
        output1 = print(a[i],end='')

    print(output1)

    new1 = output1
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for x in new1:
        if x in vowels_list:
            new1 = new1.replace(x,"")

    def reverse(word):
        word = "".join(reversed(word))
        return word

    output2 = new1
    print(reverse(output2))

    print(a[::2]) 
    y = print(a[::2]) 
    z = ' '.join(y)
    print(z)

StringManipulation()
