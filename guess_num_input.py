import random;

ans =random.randint(5,100)
max_count=5

print(ans)
print('i choose number in 1~100')
print('get it in', max_count,'times ')

for i in range(1,max_count+1):
    print(i,'times,ikutukana?')
    num=int(input())
    if num == ans:
        print('atari!!')
        break
    elif num >ans:
         print('mottositadayo')
    else:
         print('mottouedayo')
else:
     print('zannenn,seikaiha ',ans,'desita')
