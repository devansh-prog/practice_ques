s="()"

# while '()' in s or '[]' in s or '{}'in s:
#     s=s.replace('()','')
#     s=s.replace('[]','')
#     s=s.replace('{}','')
# if len(s)==0:
#     print("y")
# else:
#     print('n')

# s="{[()]}"
# c=0
# for ch in s:
#     if ch=='(':
#         c+=1
#     elif ch==')':
#         c-=1
#     if c<0:
#         print("unbalanced")
#         break
#     if ch=='{':
#         c+=1
#     elif ch=='}':
#         c-=1
#     if c<0:
#         print("unbalanced")
#         break
#     if ch=='[':
#         c+=1
#     elif ch==']':
#         c-=1
#     if c<0:
#         print("unbalanced")
#         break
# if c==0:
#     print("valid")
# else:
#     print('not Valid')
check=[]
for c in s:
    
    if c in'{([':
        check.append(c)
    elif c in'}])':
          if not  check or(c==')'and check[-1]!='(') or (c==']'and check[-1]!='[') or(c=='}'and check[-1]!='{'):
              print(False)
              break
          check.pop()
print(True if not check else False)
