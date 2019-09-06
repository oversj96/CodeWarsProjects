def to_camel_case(string):
    case1 = string.replace('_', "-")
    case2 = case1.split('-')
    new_sentence = ""
    if(type(case2) is list and len(case2) > 1):
        new_sentence = case2[0]
        for w in range(1, len(case2)):
          new_sentence = new_sentence + case2[w].capitalize() 
    return new_sentence
print(to_camel_case("the_stealth-warrior"))
