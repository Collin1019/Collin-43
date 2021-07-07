countries=["USA","India","Germany","France"]
cities=['Washington','New Delhi','Berlin','Paris']

z=zip(countries,cities)
d=dict(z)

print('{:10s}--{:10s}'.format('COUNTRY','CAPITAL'))
for k in d:
    print('{:10s}--{:10s}'.format(k,d[k]))
