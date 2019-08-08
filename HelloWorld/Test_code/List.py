pow2 = [2 ** x for x in range(1, 11) if x < 4]
print(pow2)
lang = [x+y for x in ['Python ','C '] for y in ['Language','Programming']]
# ['Python Language', 'Python Programming', 'C Language', 'C Programming']
print(lang)