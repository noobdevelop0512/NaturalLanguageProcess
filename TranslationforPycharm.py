from google_trans_new import google_translator

#中译英
def translate1(content, tgtlan1='en'):
    t1=google_translator(timeout=10)
    translate_result1 = t1.translate(content,tgtlan1)
    print(translate_result1)
    return translate_result1

#英回译中
def translate2(content, tgtlan2='zh-CN'):
    t2 = google_translator(timeout=10)
    translate_result2 = t2.translate(content,tgtlan2)
    print(translate_result2)
    return translate_result2

def translation(content):
    if content:
        tr1=translate1(content)
        tr2=translate2(tr1)
        
