initial = {'first':[2,1], 'second':[2,3], 'third': [3,4]}

final = {}

final['first'] = initial['third']
final['third'] = initial['first']

final['third'].sort()

final['fourth'] = initial['second']

del initial['second']

print final