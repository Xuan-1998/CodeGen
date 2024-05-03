correct_prob = (1/(2**n)) * reduce(lambda x,y: x*(y[0]/total_probs)**y[0]*((1-y[0])/total_probs)**(y[1]-y[0]), probs, 1)
