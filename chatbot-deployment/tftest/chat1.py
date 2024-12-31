import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)
'''    
FILE = "data1.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']

if cosine_similarity(pattern,msg)>=0.8:
                    print("trueee")
                else:
'''
s=["is anyone there?"]
t=['the fall of ']
#print(s)

tf=TfidfVectorizer()
tfidf=tf.fit_transform(s)
tfidf1=tf.fit_transform(t)
#cosine_similarity()
#print(tfidf)
#print(np.resize(np.arange(40), (5, 8)) )
#print(xy)
#f_names=tfidf_vectorizer.get_feature_names_out()
dense=tfidf.todense()
denselist=dense.tolist()

dense1=tfidf1.todense()
denselist1=dense1.tolist()
print(denselist)
print(denselist1)


print(cosine_similarity(denselist1,denselist))
#df=pd.DataFrame(denselist)
'''
for intent in intents['intents']:
        
    for pattern in intent['patterns']:
        tfidf1=tf.fit_transform([pattern])
        dense1=tfidf1.todense()
        denselist1=dense1.tolist()
        print(denselist1)
        #if(cosine_similarity(denselist1,denselist)>0.8):
            #print("hurray Alhamdulillah")
        
             
'''