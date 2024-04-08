
# 코사인 유사도 함수 정리

# =======================================================================================
# 거실
# =======================================================================================

# 1) 소파
def find_sofa(text):

    # 모듈 불러오기
    import pandas as pd 
    import numpy as np
    from konlpy.tag import Okt
    from konlpy.tag import Kkma
    from sklearn.feature_extraction.text import CountVectorizer

    sofaDF = pd.read_csv('./sofaDF.csv', index_col=0)
    dtm_sofa = pd.read_csv('./dtm_sofa.csv', index_col=0)

    # 코사인 유사도 : 두 벡터 사이 각도의 코사인 값 (-1 ~ 1)
    def make_cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

    kkma = Kkma()
    search_text = [text]
    strlist = kkma.nouns(search_text[0])
    search_text = [(" ".join(strlist))]

    cv = CountVectorizer()
    cv.fit_transform(sofaDF['nouns'])

    
    result = cv.transform(search_text)
    search_words = result.toarray()

    brand_list = np.array(sofaDF['brand'])
    item_list = np.array(sofaDF['item'])
    price_list = np.array(sofaDF['price'])
    image_list = np.array(sofaDF['image'])

    result_cosine = make_cosine(dtm_sofa, search_words.reshape(-1))

    result_args = result_cosine.argsort()[::-1]
    return brand_list[result_args][0], item_list[result_args][0], price_list[result_args][0], image_list[result_args][0]


# 2) 거실장
def find_tvdesk(text):

    # 모듈 불러오기
    import pandas as pd 
    import numpy as np
    from konlpy.tag import Okt
    from konlpy.tag import Kkma
    from sklearn.feature_extraction.text import CountVectorizer

    tvdeskDF = pd.read_csv('./tvdeskDF.csv', index_col=0)
    dtm_tvdesk = pd.read_csv('./dtm_tvdesk.csv', index_col=0)   

    # 코사인 유사도 : 두 벡터 사이 각도의 코사인 값 (-1 ~ 1)
    def make_cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

    kkma = Kkma()
    search_text = [text]
    strlist = kkma.nouns(search_text[0])
    search_text = [(" ".join(strlist))]

    cv = CountVectorizer()
    cv.fit_transform(tvdeskDF['nouns'])

    result = cv.transform(search_text)
    search_words = result.toarray()

    brand_list = np.array(tvdeskDF['brand'])
    item_list = np.array(tvdeskDF['item'])
    price_list = np.array(tvdeskDF['price'])
    image_list = np.array(tvdeskDF['image'])

    result_cosine = make_cosine(dtm_tvdesk, search_words.reshape(-1))

    result_args = result_cosine.argsort()[::-1]
    return brand_list[result_args][0], item_list[result_args][0], price_list[result_args][0], image_list[result_args][0]


# 3) 테이블
def find_table(text):

    # 모듈 불러오기
    import pandas as pd 
    import numpy as np
    from konlpy.tag import Okt
    from konlpy.tag import Kkma
    from sklearn.feature_extraction.text import CountVectorizer


    tableDF = pd.read_csv('./tableDF.csv', index_col=0)
    dtm_table = pd.read_csv('./dtm_table.csv', index_col=0)

    # 코사인 유사도 : 두 벡터 사이 각도의 코사인 값 (-1 ~ 1)
    def make_cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

    kkma = Kkma()
    search_text = [text]
    strlist = kkma.nouns(search_text[0])
    search_text = [(" ".join(strlist))]

    cv = CountVectorizer()
    cv.fit_transform(tableDF['nouns'])


    result = cv.transform(search_text)
    search_words = result.toarray()

    brand_list = np.array(tableDF['brand'])
    item_list = np.array(tableDF['item'])
    price_list = np.array(tableDF['price'])
    image_list = np.array(tableDF['image'])

    result_cosine = make_cosine(dtm_table, search_words.reshape(-1))

    result_args = result_cosine.argsort()[::-1]
    return brand_list[result_args][0], item_list[result_args][0], price_list[result_args][0], image_list[result_args][0]


# 4) 사이드테이블
def find_sidetable(text):

    # 모듈 불러오기
    import pandas as pd 
    import numpy as np
    from konlpy.tag import Okt
    from konlpy.tag import Kkma
    from sklearn.feature_extraction.text import CountVectorizer

    sidetbDF = pd.read_csv('./sidetbDF.csv', index_col=0)
    dtm_sidetb = pd.read_csv('./dtm_sidetb.csv', index_col=0)

    # 코사인 유사도 : 두 벡터 사이 각도의 코사인 값 (-1 ~ 1)
    def make_cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

    kkma = Kkma()
    search_text = [text]
    strlist = kkma.nouns(search_text[0])
    search_text = [(" ".join(strlist))]

    cv = CountVectorizer()
    cv.fit_transform(sidetbDF['nouns'])

    result = cv.transform(search_text)
    search_words = result.toarray()

    brand_list = np.array(sidetbDF['brand'])
    item_list = np.array(sidetbDF['item'])
    price_list = np.array(sidetbDF['price'])
    image_list = np.array(sidetbDF['image'])

    result_cosine = make_cosine(dtm_sidetb, search_words.reshape(-1))

    result_args = result_cosine.argsort()[::-1]
    return brand_list[result_args][0], item_list[result_args][0], price_list[result_args][0], image_list[result_args][0]


# =======================================================================================
# 침실
# =======================================================================================

# 1) 침대
def find_bed(text):

    # 모듈 불러오기
    import pandas as pd 
    import numpy as np
    from konlpy.tag import Okt
    from konlpy.tag import Kkma
    from sklearn.feature_extraction.text import CountVectorizer

    bedDF = pd.read_csv('./bedDF.csv', index_col=0)
    dtm_bed = pd.read_csv('./dtm_bed.csv', index_col=0)

    # 코사인 유사도 : 두 벡터 사이 각도의 코사인 값 (-1 ~ 1)
    def make_cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

    kkma = Kkma()
    search_text = [text]
    strlist = kkma.nouns(search_text[0])
    search_text = [(" ".join(strlist))]

    cv = CountVectorizer()
    cv.fit_transform(bedDF['nouns'])

    result = cv.transform(search_text)
    search_words = result.toarray()

    brand_list = np.array(bedDF['brand'])
    item_list = np.array(bedDF['item'])
    price_list = np.array(bedDF['price'])
    image_list = np.array(bedDF['image'])

    result_cosine = make_cosine(dtm_bed, search_words.reshape(-1))

    result_args = result_cosine.argsort()[::-1]
    return brand_list[result_args][0], item_list[result_args][0], price_list[result_args][0], image_list[result_args][0]


# 2) 협탁
def find_nightstand(text):

    # 모듈 불러오기
    import pandas as pd 
    import numpy as np
    from konlpy.tag import Okt
    from konlpy.tag import Kkma
    from sklearn.feature_extraction.text import CountVectorizer

    nightstDF = pd.read_csv('./nightstDF.csv', index_col=0)
    dtm_nightst = pd.read_csv('./dtm_nightst.csv', index_col=0)

    # 코사인 유사도 : 두 벡터 사이 각도의 코사인 값 (-1 ~ 1)
    def make_cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

    kkma = Kkma()
    search_text = [text]
    strlist = kkma.nouns(search_text[0])
    search_text = [(" ".join(strlist))]

    cv = CountVectorizer()
    cv.fit_transform(nightstDF['nouns'])

    result = cv.transform(search_text)
    search_words = result.toarray()

    brand_list = np.array(nightstDF['brand'])
    item_list = np.array(nightstDF['item'])
    price_list = np.array(nightstDF['price'])
    image_list = np.array(nightstDF['image'])

    result_cosine = make_cosine(dtm_nightst, search_words.reshape(-1))

    result_args = result_cosine.argsort()[::-1]
    return brand_list[result_args][0], item_list[result_args][0], price_list[result_args][0], image_list[result_args][0]


# 3) 거울
def find_mirror(text):

    # 모듈 불러오기
    import pandas as pd 
    import numpy as np
    from konlpy.tag import Okt
    from konlpy.tag import Kkma
    from sklearn.feature_extraction.text import CountVectorizer

    mirrorDF = pd.read_csv('./mirrorDF.csv', index_col=0)
    dtm_mirror = pd.read_csv('./dtm_mirror.csv', index_col=0)

    # 코사인 유사도 : 두 벡터 사이 각도의 코사인 값 (-1 ~ 1)
    def make_cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

    kkma = Kkma()
    search_text = [text]
    strlist = kkma.nouns(search_text[0])
    search_text = [(" ".join(strlist))]

    cv = CountVectorizer()
    cv.fit_transform(mirrorDF['nouns'])

    result = cv.transform(search_text)
    search_words = result.toarray()

    brand_list = np.array(mirrorDF['brand'])
    item_list = np.array(mirrorDF['item'])
    price_list = np.array(mirrorDF['price'])
    image_list = np.array(mirrorDF['image'])

    result_cosine = make_cosine(dtm_mirror, search_words.reshape(-1))

    result_args = result_cosine.argsort()[::-1]
    return brand_list[result_args][0], item_list[result_args][0], price_list[result_args][0], image_list[result_args][0]


# 4) 수납장
def find_drawer(text):

    # 모듈 불러오기
    import pandas as pd 
    import numpy as np
    from konlpy.tag import Okt
    from konlpy.tag import Kkma
    from sklearn.feature_extraction.text import CountVectorizer

    drawerDF = pd.read_csv('./drawerDF.csv', index_col=0)
    dtm_drawer = pd.read_csv('./dtm_drawer.csv', index_col=0)

    # 코사인 유사도 : 두 벡터 사이 각도의 코사인 값 (-1 ~ 1)
    def make_cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

    kkma = Kkma()
    search_text = [text]
    strlist = kkma.nouns(search_text[0])
    search_text = [(" ".join(strlist))]

    cv = CountVectorizer()
    cv.fit_transform(drawerDF['nouns'])

    result = cv.transform(search_text)
    search_words = result.toarray()

    brand_list = np.array(drawerDF['brand'])
    item_list = np.array(drawerDF['item'])
    price_list = np.array(drawerDF['price'])
    image_list = np.array(drawerDF['image'])

    result_cosine = make_cosine(dtm_drawer, search_words.reshape(-1))

    result_args = result_cosine.argsort()[::-1]
    return brand_list[result_args][0], item_list[result_args][0], price_list[result_args][0], image_list[result_args][0]


# =======================================================================================
# 주방
# =======================================================================================

# 1) 식탁 테이블
def find_diningtb(text):

    # 모듈 불러오기
    import pandas as pd 
    import numpy as np
    from konlpy.tag import Okt
    from konlpy.tag import Kkma
    from sklearn.feature_extraction.text import CountVectorizer

    diningtbDF = pd.read_csv('./diningtbDF.csv', index_col=0)
    dtm_diningtb = pd.read_csv('./dtm_diningtb.csv', index_col=0)

    # 코사인 유사도 : 두 벡터 사이 각도의 코사인 값 (-1 ~ 1)
    def make_cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

    kkma = Kkma()
    search_text = [text]
    strlist = kkma.nouns(search_text[0])
    search_text = [(" ".join(strlist))]

    cv = CountVectorizer()
    cv.fit_transform(diningtbDF['nouns'])

    result = cv.transform(search_text)
    search_words = result.toarray()

    brand_list = np.array(diningtbDF['brand'])
    item_list = np.array(diningtbDF['item'])
    price_list = np.array(diningtbDF['price'])
    image_list = np.array(diningtbDF['image'])

    result_cosine = make_cosine(dtm_diningtb, search_words.reshape(-1))

    result_args = result_cosine.argsort()[::-1]
    return brand_list[result_args][0], item_list[result_args][0], price_list[result_args][0], image_list[result_args][0]


# 2) 식탁 의자
def find_chair(text):

    # 모듈 불러오기
    import pandas as pd 
    import numpy as np
    from konlpy.tag import Okt
    from konlpy.tag import Kkma
    from sklearn.feature_extraction.text import CountVectorizer

    chairDF = pd.read_csv('./chairDF.csv', index_col=0)
    dtm_chair = pd.read_csv('./dtm_chair.csv', index_col=0)

    # 코사인 유사도 : 두 벡터 사이 각도의 코사인 값 (-1 ~ 1)
    def make_cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

    kkma = Kkma()
    search_text = [text]
    strlist = kkma.nouns(search_text[0])
    search_text = [(" ".join(strlist))]

    cv = CountVectorizer()
    cv.fit_transform(chairDF['nouns'])

    result = cv.transform(search_text)
    search_words = result.toarray()

    brand_list = np.array(chairDF['brand'])
    item_list = np.array(chairDF['item'])
    price_list = np.array(chairDF['price'])
    image_list = np.array(chairDF['image'])

    result_cosine = make_cosine(dtm_chair, search_words.reshape(-1))

    result_args = result_cosine.argsort()[::-1]
    return brand_list[result_args][0], item_list[result_args][0], price_list[result_args][0], image_list[result_args][0]


# 3) 렌지대
def find_ovenst(text):

    # 모듈 불러오기
    import pandas as pd 
    import numpy as np
    from konlpy.tag import Okt
    from konlpy.tag import Kkma
    from sklearn.feature_extraction.text import CountVectorizer

    ovenstDF = pd.read_csv('./ovenstDF.csv', index_col=0)
    dtm_ovenst = pd.read_csv('./dtm_ovenst.csv', index_col=0)

    # 코사인 유사도 : 두 벡터 사이 각도의 코사인 값 (-1 ~ 1)
    def make_cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

    kkma = Kkma()
    search_text = [text]
    strlist = kkma.nouns(search_text[0])
    search_text = [(" ".join(strlist))]

    cv = CountVectorizer()
    cv.fit_transform(ovenstDF['nouns'])

    result = cv.transform(search_text)
    search_words = result.toarray()

    brand_list = np.array(ovenstDF['brand'])
    item_list = np.array(ovenstDF['item'])
    price_list = np.array(ovenstDF['price'])
    image_list = np.array(ovenstDF['image'])

    result_cosine = make_cosine(dtm_ovenst, search_words.reshape(-1))

    result_args = result_cosine.argsort()[::-1]
    return brand_list[result_args][0], item_list[result_args][0], price_list[result_args][0], image_list[result_args][0]


# 4) 수납장
def find_cab(text):

    # 모듈 불러오기
    import pandas as pd 
    import numpy as np
    from konlpy.tag import Okt
    from konlpy.tag import Kkma
    from sklearn.feature_extraction.text import CountVectorizer

    cabDF = pd.read_csv('./cabDF.csv', index_col=0)
    dtm_cab = pd.read_csv('./dtm_cab.csv', index_col=0)

    # 코사인 유사도 : 두 벡터 사이 각도의 코사인 값 (-1 ~ 1)
    def make_cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

    kkma = Kkma()
    search_text = [text]
    strlist = kkma.nouns(search_text[0])
    search_text = [(" ".join(strlist))]

    cv = CountVectorizer()
    cv.fit_transform(cabDF['nouns'])

    result = cv.transform(search_text)
    search_words = result.toarray()

    brand_list = np.array(cabDF['brand'])
    item_list = np.array(cabDF['item'])
    price_list = np.array(cabDF['price'])
    image_list = np.array(cabDF['image'])

    result_cosine = make_cosine(dtm_cab, search_words.reshape(-1))

    result_args = result_cosine.argsort()[::-1]
    return brand_list[result_args][0], item_list[result_args][0], price_list[result_args][0], image_list[result_args][0]



