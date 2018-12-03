
import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    mult_sum = 0
    for i in vec1 :
        if i in vec2:
            mult_sum += vec1[i] * vec2[i]
    
    cosin_sim = mult_sum / ( norm(vec1)* norm(vec2))
    
    return cosin_sim


def build_semantic_descriptors(sentences):
    
    dictionary = {}
    
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            if sentences[i][j] not in dictionary:
                dictionary[sentences[i][j]] = {}
                
            for e in sentences[i]:
                if e != sentences[i][j]:
                    
                    if e not in dictionary[sentences[i][j]]: 
                        dictionary[sentences[i][j]][e] = 1
                    else:        
                        dictionary[sentences[i][j]][e] += 1
                
    return dictionary


def build_semantic_descriptors_from_files(filenames):
        
    text = ""
    l=[]
    
    for i in range(len(filenames)):
        f = open(filenames[i],"r", encoding="utf-8")
        text += f.read().lower()

    word = text.replace("! ",".").replace(". ", ".").replace("? ", ".").replace(",", " ").replace("-", " ").replace("--", " ").replace(":", " ").replace(";", "").replace('"', ' ').replace("'", " ").replace("  "," ")

    new_word = word.split(".")

    for i in new_word:
        if i != " ":
            l.append(i.replace("\n","").split(" "))

    final_list = l[:-1]
    #part c
    #final_list = final_list[:int(0.9*len(final_list))]
    discript = build_semantic_descriptors(final_list)

    return discript


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    
    count = 0
    index = 0
    max_count = -999999999999999
    
    for i in range(len(choices)):
            if word in semantic_descriptors and choices[i] in semantic_descriptors:
                count = similarity_fn(semantic_descriptors[word], semantic_descriptors[choices[i]])

                if count > max_count :
                    max_count = count
                    index = i
                    count = 0


    if max_count == 0 :
        return -1
    else:
        return choices[index]

    

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    
    f = open(filename,"r", encoding="utf-8")
    text = f.read().lower()
    new_text = text.split("\n")[:-1]
    listerino = []
    for i in new_text:

        listerino.append(i.split(" "))
    choices = []
    currect_counter = 0
    
    for i in listerino:
 
        for j in range(len(i)):
            if j != 1:
                choices.append(i[j])
            else:
                currect_answer = i[1]
        if most_similar_word(choices[0], choices[1:], semantic_descriptors, similarity_fn) == currect_answer:
                currect_counter +=1
        choices = []
    
    percentage = currect_counter / len(new_text) *100
    return percentage
            
            
def euclidean_norm_distance (vec1,vec2):
    
    norm_vec1 = norm(vec1)
    norm_vec2= norm(vec2)
    Distancerino = 0
    for i in vec1 :
        
        if i in vec2:
            Distancerino += (vec1[i]/norm_vec1 - vec2[i]/norm_vec2)**2
            
        else:
                
            Distancerino += (vec1[i]/norm_vec1 - 0)**2
    for j in vec2:
        if j not in vec1:
             Distancerino += ( 0 - vec2[j]/norm_vec2 )**2
                
    Finalerino_distancerino = math.sqrt(Distancerino)
    return -Finalerino_distancerino
    
    
def euclidean_neg_distance(vec1, vec2):
    
    Distancerino = 0
    for i in vec1 :
        
        if i in vec2:
            Distancerino += (vec1[i] - vec2[i])**2
            
        else:
                
            Distancerino += (vec1[i] - 0)**2
    for j in vec2:
        if j not in vec1:
             Distancerino += ( 0 - vec2[j] )**2
                
    Finalerino_distancerino = math.sqrt(Distancerino)
    return -Finalerino_distancerino
    
    
    
if __name__ == '__main__':  

    #Part a:
    import time
    before_run = time.time()
    disc = build_semantic_descriptors_from_files(["/u/a/mousavib/Desktop/onerino.txt","/u/a/mousavib/Desktop/twoerino.txt"])
    print(run_similarity_test("/u/a/mousavib/Desktop/test.txt",disc,cosine_similarity))
    print("Time of Completion:",time.time() - before_run,"seconds")
    
    #Part b:
    

    before_run = time.time()
    print(run_similarity_test("/u/a/mousavib/Desktop/test.txt",disc,euclidean_norm_distance))
    print("Time of Completion:",time.time() - before_run,"seconds")
    
    before_run = time.time()
    print(run_similarity_test("/u/a/mousavib/Desktop/test.txt",disc,euclidean_neg_distance))
    print("Time of Completion:",time.time() - before_run,"seconds")
    
    
    #part c:
    
    #s[:int(.1*len(s))]
    
