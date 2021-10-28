from jina import Flow, Executor , requests , Document, DocumentArray
import pandas as pd
import numpy as np

df=pd.read_csv('windows_store.csv')
df= df.drop_duplicates().dropna()
# df.iloc[0]

Document(text ="text")
Document(content ="content")
Document(uri = "path" )

docs = DocumentArray()
for ind in range(df.shape[0]):
    name = df.iloc[ind,0]
    desc = df.iloc[ind,2]
#     print(name,"-",desc,"\n")
    doc = Document(text=name)
    doc.tags['description'] = desc
    docs.append(doc)

flow = (
    Flow()
    .add(uses='jinahub://SpacyTextEncoder', name="encoder", install_requirements=True)
    .add(uses='jinahub://SimpleIndexer' ,name="indexer")
#     .add().plot('f.svg')
)

with flow:
        flow.index(inputs=docs)
        query = Document(text=input("App Name:"))
        response = flow.search(inputs=query, return_results=True)

matches = response[0].data.docs[0].matches

print("Your search results")
print("-------------------\n")
i=0

for match in matches:
    
      
    i+=1
    if(i==1):
        print("Closest Match for",match.text,"Description : ", match.tags.fields['description'].string_value,"\n")
    else:
        print("Similar Query",i)
        print("-------------------\n")
        print(match.tags.fields['description'].string_value)