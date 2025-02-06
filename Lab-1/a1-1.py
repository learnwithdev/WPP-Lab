alpha = 'abcdefghijklmnopqrstuvwxyz'

l1 = [i for i in range(50)]
l2 = [j*j for j in range (1,51)]
l3 = [(i+1)*j for i,j in enumerate(alpha)]

print(f'''
{l1},

{l2},

{l3}
''')
    
        