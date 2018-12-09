import numpy as np
import tqdm

def get_aspect_terms(aspects, vocab_dict):
    aspect_terms = []
    w_notfound = []
    
    for aspect_kws in aspects:
        aspect = []
        for w in aspect_kws:
            if w in vocab_dict:
                aspect.append(w)
            else:
                w_notfound.append(w)
        aspect_terms.append(aspect)
    #We are only using one hotel review file, as we keep inceasing the number of files words not found will decrease.
    # print "Words not found in vocab:", ' '.join(w_notfound)
    return aspect_terms

def chi_sq(a,b,c,d):
    c1 = a
    c2 = b - a
    c3 = c - a
    c4 = d - b - c + a
    nc =  d
    return nc * (c1*c4 - c2*c3) * (c1*c4 - c2*c3)/((c1+c3) * (c2+c4) * (c1+c2) * (c3+c4))

def chi_sq_mat():
    global aspect_words, aspect_sent, num_words
    asp_rank = np.zeros(aspect_words.shape)
    for i in range(len(aspect_terms)):
        for j in range(len(vocab)):
            asp_rank[i][j] = chi_sq(aspect_words[i][j], num_words[j], aspect_sent[i], len(sent))
    return asp_rank

def aspect_segmentaion(review_dic,voca_freq_dic):
    #INPUT
    review_sent = [] # 문장, 단어단위로 토크나이징된 리뷰 담은 리스트
    for rev_lst in review_dic.values():
        for rev in rev_lst:
            review_sent.append(rev[1])
    
    all_ratings = []
    for rev_lst in review_dic.values():
        for rev in rev_lst:
            all_ratings.append(rev[0])

    #selection threshold
    p = 5
    
    #Iterations 
    # I = 10
    I = 1

#     #Create Vocabulary
#     #review_sent, review_actual, only_sent = parse_to_sentence(reviews)
#     #vocab, #vocab_dict = create_vocab(only_sent)

    vocab = list(voca_freq_dic.keys())
    #Assign a number corresponding to each word. Makes counting easier.
    vocab_dict = dict(zip(vocab, range(len(vocab))))

    #Aspect Keywords
    aspect_terms = get_aspect_terms(aspect_keywords,voca_freq_dic)

#     label_text = 
    # print aspect_terms

    #ALGORITHM
    review_labels = []
    k = len(aspect_terms) # k: 토픽 개수 7
    v = len(vocab) # v: 단어 개수 147119
    
    aspect_words = np.zeros((k,v))
    aspect_sent = np.zeros(k)
    num_words = np.zeros(v)
    #-----------------------------------------------------
    for i in tqdm.tqdm(range(I)):
        # print(len(review_sent)) 리뷰개수 595387
        for r in review_sent:
            labels = []
            for s in r:
                count = np.zeros(len(aspect_terms))
                i = 0
                for a in aspect_terms:
                    for w in s:
                        if w in vocab_dict:
                            num_words[vocab_dict[w]] += 1
                            if w in a:
                                count[i] += 1
                    i = i + 1
                if max(count) > 0:
                    la = np.where(np.max(count) == count)[0].tolist()
                    labels.append(la)
                    for i in la:
                        aspect_sent[i] += 1
                        for w in s:
                            if w in vocab_dict:
                                aspect_words[i][vocab_dict[w]] += 1
                else:
                    labels.append([])
                    
            review_labels.append(labels)
        
    return review_labels,review_sent
            # aspect_w_rank = chi_sq_mat()
            # new_labels = []
            # for na in aspect_w_rank:
            # 	x = np.argsort(na)[::-1][:p]
            # 	new_labels.append(x)
                # for k,v in vocab_dict.items():
                # 	if vocab_dict[k] in x:
                # 		print k
                # print 
            # sys.exit()


#     ratings_sentiment = []
#     for r in review_actual:
#         sentiment = []
#         #aspect ratings based on sentiment
#         for s in r:
#             ss = sid.polarity_scores(s)
#             sentiment.append(ss['compound'])
#         ratings_sentiment.append(sentiment)

#     #Aspect Ratings Per Review
#     aspect_ratings = []
#     for i,r in enumerate(review_labels):
#         rating = np.zeros(7)
#         count = np.zeros(7)
#         rs = ratings_sentiment[i] 
#         for j,l in enumerate(r):
#             for k in range(7):
#                 if k in l:
#                     rating[k] += rs[j]
#             for k in range(7):
#                 if count[k] != 0:
#                     rating[k] /= count[k]
#         #Map from -[-1,1] to [1,5]
#         for k in range(7):
#             if rating[k] != 0:
#                 rating[k] = int(round((rating[k]+1)*5/2))
#         aspect_ratings.append(rating)
#     return aspect_ratings, all_ratings

    # n = 0
    # print review_actual[n], '\n', review_labels[n]
    # print ratings_sentiment[n], '\n', aspect_ratings[n]
    # print len(all_ratings), len(reviews), all_ratings[0]
    # sys.exit()
    # return aspect_ratings

    # print sent[5:9], labels[5:9]
    # print zip(actual_sent, labels)[:10]
    # print zip(actual_sent, sentiment)[:10]  

