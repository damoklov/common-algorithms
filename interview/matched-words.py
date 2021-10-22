def find_similar(sentence_1, sentence_2):
    set_1 = set(sentence_1.split())
    set_2 = set(sentence_2.split())
    
    return sorted(list(set_1^set_2)), sorted(list(set_1&set_2))
  
