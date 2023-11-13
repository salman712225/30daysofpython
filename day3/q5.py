b=[{'title':'Le Père Goriot','author': 'Honoré de Balzac' ,'year':1835},{'title':' David Copperfield ','author':'Charles Dickens','year':1849},{'title':'Madame Bovary','author':'Gustave Flaubert','year':1856}]
for i in b:
    for j in i:
        if j=='title':
            print(i[j])
