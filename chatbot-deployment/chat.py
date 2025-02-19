import random
import json
from sklearn.metrics.pairwise import cosine_similarity
import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
#print(all_words)

tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Aafhana"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
  



    X = X.reshape(1, X.shape[0])
   # print(X)
    X = torch.from_numpy(X).to(device)
    #print(X)

    output = model(X) 
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    #print(probs)
    prob = probs[0][predicted.item()]
    '''
    for intent in intents['intents']:
        for tag in intent['tag']:
            for pattern in tag['patterns']:
                if cosine_similarity(pattern,msg)>=0.8:
                    print("trueee")
                else:
'''
    if prob.item()>0.8:
       print(prob.item())
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    
    return "I do not understand..."


if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "get me doctor details"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)

