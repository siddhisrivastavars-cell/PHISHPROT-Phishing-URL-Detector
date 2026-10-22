from flask import Flask,render_template,request
app=Flask(__name__)

def check_phishing(url):
    url=url.lower()
    c=0 #counts the suspicion count in the url entered by the user
    suspicions=[]
    
    if '@' in url :
       suspicions.append("Found @ sysmbol")
       c+=1
    if ".gov" not in url and ".com" not in url and ".in" not in url :
       suspicions.append("No Valide Domain")
       c+=1
    if url.count('.')>2 :
       suspicions.append("Too Many '.'")
       c+=1
    if "http://" in url:
       suspicions.append("http not https")
       c+=1
    if len(url)>40 :
       suspicions.append("Exceeding Length")
       c+=1
    if "free" in url or "link" in url or "login" in url or "verify" in  url or "LOGIN" in url :
       suspicions.append("")
       c+=1
    if url.count('-')>1 :
       suspicions.append("Found @ sysmbol")
       c+=1
    if url.count("//")>2 :
       suspicions.append("Found @ sysmbol")
       c+=1

    is_phishing=c>2
    return is_phishing,c,suspicions

@app.route('/',methods=['GET','POST'])
def home():
    result=None
    if request.method=='POST' :
        url=request.form.get('url')
        is_phishing,c,suspicions=check_phishing(url)
        result={
            'url':url,
            'c':c,
            'suspicions':suspicions,
            'is_phishing':is_phishing
        }
    return render_template('index.html',result=result)

if __name__=='__main__' :
    app.run(debug=True)
    
        
    
