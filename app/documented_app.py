from flask import Flask , render_template , request , jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
data = SQLAlchemy(app)

class exp(data.Model):
    """Declares the database model for storing the correct answers of the experiment.
    """
    id = data.Column(data.Integer, primary_key=True,auto_increment=True)
    word = data.Column(data.Integer)
    add_sing_dr = data.Column(data.Integer)
    delete_sing_dr = data.Column(data.Integer)
    add_plu_dr = data.Column(data.Integer)
    delete_plu_dr = data.Column(data.Integer)
    add_sing_od = data.Column(data.Integer)
    delete_sing_od = data.Column(data.Integer)
    add_plu_od = data.Column(data.Integer)
    delete_plu_od = data.Column(data.Integer)

    def __init__(self,word,add_sing_dr,delete_sing_dr,add_plu_dr,delete_plu_dr,add_sing_od,delete_sing_od,add_plu_od,delete_plu_od):
        self.word=word
        self.add_sing_dr=add_sing_dr
        self.delete_sing_dr=delete_sing_dr
        self.add_plu_dr=add_plu_dr
        self.delete_plu_dr=delete_plu_dr
        self.add_sing_od=add_sing_od
        self.delete_sing_od=delete_sing_od
        self.add_plu_od=add_plu_od
        self.delete_plu_od=delete_plu_od

class qui(data.Model):
    """Declares the database model for storing the correct answers of the quiz.
    """
    id = data.Column(data.Integer, primary_key=True,auto_increment=True)
    question = data.Column(data.String)
    option1 = data.Column(data.String)
    option2 = data.Column(data.String)
    option3 = data.Column(data.String)
    option4 = data.Column(data.String)
    answer = data.Column(data.Integer)

    def __init__(self,question,option1,option2,option3,option4,answer):
        self.question=question
        self.option1=option1
        self.option2=option2
        self.option3=option3
        self.option4=option4
        self.answer=answer

@app.route("/Experiment",methods=['POST','GET'])
def index():
   """Renders the HTML Page for 'Experiment', calls the evaluating function and displays the result on the same page.
   """
   if request.method=="GET":
      return render_template("Experiment.html",obj=[])
   if request.method=="POST":
      # def checkans():
         input_words = [ 'बच्चा', 'लड़का', 'घोड़ा', 'गधा', 'बच्ची', 'लड़की', 'नदी', 'गली', 'माला', ' लता', 'शाखा', 'गाथा', 'माली', 'जोहरी', 'कूली', 'आदमी']
         ad_list = [ 'आ', 'आओं', 'आयें', 'इयाँ', 'इयों', 'ई', 'ए', 'ओं' ]
         result = request.form
         entered=''
         entered=str(result.get('word'))   
         ans = ''
         ans=str(result.get('1'))
         ans+="."+str(result.get('2'))+"."+str(result.get('3'))+"."+str(result.get('4'))+"."+str(result.get('5'))+"."+str(result.get('6'))
         ans+="."+str(result.get('7'))+"."+str(result.get('8'))
         temp=ans.split('.')
         t=checkAnswer(entered,temp)
         jso={'first':t[0],'second':t[1],'third':t[2],'fourth':t[3],'HEAD':"Correction"}
         try :
            return render_template("Experiment.html",obj=jso)
         except Exception as e:
            return "Error has occured"

def checkAnswer(word,string):
   """Evaluates the user's answer and returns the result.
   
   Arguments:
       word {string} -- Stores the user's choice of word from the given dropdown menu.
       string {list} -- Stores the user's delete/add choices for the four different cases.
   
   """
   input_words = [ 'बच्चा', 'लड़का', 'घोड़ा', 'गधा', 'बच्ची', 'लड़की', 'नदी', 'गली', 'माला', ' लता', 'शाखा', 'गाथा', 'माली', 'जोहरी', 'कूली', 'आदमी']
   ad_list = [ 'आ', 'आओं', 'आयें', 'इयाँ', 'इयों', 'ई', 'ए', 'ओं' ]
   ans_check=[]
   data.create_all()
   ind=-1
   for i in input_words:
      ind+=1
      if i==word:
         ans_check.append(ind)
   for i in string:
      ind=-1
      for j in ad_list:
         ind+=1
         if(j==i):
            ans_check.append(ind)
   final=QueryOverDb(ans_check)
   return final
   
def QueryOverDb(entered_value):
   """Fetches the correct answer from the database for the corresponding user's choice of word.
   
   Arguments:
       entered_value {integer} -- Stores the index of the user's input word from the dropdown menu.
   
   """
   data.create_all()
   allUsers=exp.query.all()
   final_result=[]
   ind=0
   for x in allUsers:
      ind+=1
      if(ind<=16):
         if(entered_value[0]==x.word):
            if(entered_value[1]==x.add_sing_dr and entered_value[2]==x.delete_sing_dr):
               final_result.append(1)
            else: 
               final_result.append(0)
            if(entered_value[3]==x.add_plu_dr and entered_value[4]==x.delete_plu_dr):
               final_result.append(1)
            else:
               final_result.append(0)
            if(entered_value[5]==x.add_sing_od and entered_value[6]==x.delete_sing_od):
               final_result.append(1)
            else:
               final_result.append(0)
            if(entered_value[7]==x.add_plu_od and entered_value[8]==x.delete_plu_od):
               final_result.append(1)
            else:
               final_result.append(0)
   return final_result

@app.route("/check")
def chec():
    return render_template("login.html")
    
@app.route("/view")
def view():
    data.create_all()
    allUsers=exp.query.all()
    diction = {"Questions":[]}
    for x in allUsers:
        diction["Questions"].append({"Question":x.word,"add_sing_dr":x.add_sing_dr})
    return jsonify(diction)

@app.route("/")
def mai():
   """Renders the HTML page for 'Introduction'
   
   Returns:
       HTML Page -- Returns the HTML page for 'Introduction'
   """
   try:
      return render_template('Introduction.html')
   except Exception as e:
      return render_template('error.html')

@app.route("/Introduction")
def intro():
   """Renders the HTML page for 'Introduction'
   
   Returns:
       HTML Page -- Returns the HTML page for 'Introduction'
   """
   try:
      return render_template('Introduction.html')
   except Exception as e:
      return render_template('error.html')
   
@app.route("/Theory")
def theory():
   """Renders the HTML page for 'Theory'
   
   Returns:
       HTML Page -- Returns the HTML page for 'Theory'
   """
   try:
      return render_template('Theory.html')
   except Exception as e:
      return render_template('error.html')

@app.route("/Objective")
def objective():
   """Renders the HTML page for 'Objective'
   
   Returns:
       HTML Page -- Returns the HTML page for 'Objective'
   """
   try:
      return render_template('Objective.html')
   except Exception as e:
      return render_template('error.html')

@app.route("/Experiment")
def experiment():
   """Renders the HTML page for 'Experiments'
   
   Returns:
       HTML Page -- Returns the page for 'Experiment' 
   """
   try:
      return render_template('Experiment.html')
   except Exception as e:
      return render_template('error.html')

@app.route("/Quizzes",methods=['GET','POST'])
def quizzes():
   """Renders the HTML page for 'Quizzes'
   
   The user's response is obtained in a list and the correct answers for the coressponding question
   is fetched from the database. The answers are then evaluated by comparing with the correct answers
   list. Finally, the result is displayed in an alert box.
   
   Returns:
       HTML Page -- Return the HTML page for 'Quiz'
   """
   allUser=qui.query.all()
   data_base_quiz={}
   data_base_quiz['Question1']=[]
   data_base_quiz['Question2']=[]
   data_base_quiz['Question3']=[]
   data_base_quiz['Question4']=[]
   i=0
   for user in allUser:
      i+=1
      t={}    
      t['question']=user.question
      t['answer']=user.answer
      t['option1']=user.option1
      t['option2']=user.option2
      t['option3']=user.option3
      t['option4']=user.option4
      if(i==1):
         data_base_quiz['Question1'].append(t)
      elif(i==2):
         data_base_quiz['Question2'].append(t)
      elif(i==3):
         data_base_quiz['Question3'].append(t)
      elif(i==4):
         data_base_quiz['Question4'].append(t)
   if request.method=='GET':
      try:
         return render_template('Quizzes.html',obect=data_base_quiz,ans=[],error=0)
      except Exception as e:
         return render_template('error.html')
   if request.method=='POST':
      result=request.form
      if(result.get('question1') and result.get('question2') and result.get('question3') and result.get('question4')):
         pass
      else:
         return render_template('Quizzes.html',obect=data_base_quiz,ans=[],error=1)
      user_input=[result.get('question1'),result.get('question2'),result.get('question3'),result.get('question4')]
      ans_set=[]
      if(user_input[0]==str(data_base_quiz['Question1'][0]['answer'])):
         ans_set.append(1)
      else:
         ans_set.append(0)
      if(user_input[1]==str(data_base_quiz['Question2'][0]['answer'])):
         ans_set.append(1)
      else:
         ans_set.append(0)
      if(user_input[2]==str(data_base_quiz['Question3'][0]['answer'])):
         ans_set.append(1)
      else:
         ans_set.append(0)
      if(user_input[3]==str(data_base_quiz['Question4'][0]['answer'])):
         ans_set.append(1)
      else:
         ans_set.append(0)
      try:
         return render_template('Quizzes.html',obect=data_base_quiz,ans=ans_set,error=0)
      except Exception as e:
         return render_template('error.html')

@app.route("/Procedure")
def procedure():
   """Renders the HTML page for 'Procedure' 
   
   Returns:
       HTML Page -- Returns the HTML Page for 'Procedure'
   """
   try:
      return render_template('Procedure.html')
   except Exception as e:
      return render_template('error.html')

@app.route("/Further_Readings")
def further():
   """Renders the HTML page for 'Further Reading' 
   
   Returns:
       HTML Page -- Returns the HTML page for 'Further Readings'.
   """
   try:
      return render_template('Further_Readings.html')
   except Exception as e:
      return render_template('error.html')
   
@app.route("/Feedback")
def feedback():
   try:
      return render_template('Feedback.html')
   except Exception as e:
      return render_template('error.html')

@app.errorhandler(404)
def page_not_found(e):
   """Declaring custom error handler for the HTTP error 404.
   
   Returns:
       HTML Page -- Returns custom error page.
   """
   return render_template('error.html'),404
# Initializing the database
# def add(word,add_sing_dr,delete_sing_dr,add_plu_dr,delete_plu_dr,add_sing_od,delete_sing_od,add_plu_od,delete_plu_od):
#     data.create_all()
#     allUsers=exp.query.all()
#     new_item=exp(word,add_sing_dr,delete_sing_dr,add_plu_dr,delete_plu_dr,add_sing_od,delete_sing_od,add_plu_od,delete_plu_od)
#     data.session.add(new_item)
#     data.session.commit()

# add(0,0,0,0,6,0,6,0,7)
# add(1,0,0,0,6,0,6,0,7)
# add(2,0,0,0,6,0,6,0,7)
# add(3,0,0,0,6,0,6,0,7)
# add(4,5,5,5,3,5,5,5,4)
# add(5,5,5,5,3,5,5,5,4)
# add(6,5,5,5,3,5,5,5,4)
# add(7,5,5,5,3,5,5,5,4)
# add(8,0,0,0,2,0,0,0,1)
# add(9,0,0,0,2,0,0,0,1)
# add(10,0,0,0,2,0,0,0,1)
# add(11,0,0,0,2,0,0,0,1)
# add(12,5,5,5,5,5,5,5,4)
# add(13,5,5,5,5,5,5,5,4)
# add(14,5,5,5,5,5,5,5,4)
# add(15,5,5,5,5,5,5,5,4)

##quiz database making :
# def add(question,option1,option2,option3,option4,answer):
#     data.create_all()
#     allUsers=qui.query.all()
#     new_item=qui(question,option1,option2,option3,option4,answer)
#     data.session.add(new_item)
#     data.session.commit()
#     def _repr_(self):
#         return '<User %r>' % self.question

# add("Inflectional morphemes change a noun’s gender, grammatical mood, number, etc. without changing the meaning of the word. Identify the inflectional morphological from the options below","Sad - Sadness","Dog - Dogs","Sense - Nonsense","Quick - Quickly",2)
# add("The following is a list of words and their oblique form. Identify the incorrect pair","जेबें - जेबों","ताले - तालों","हाथी - हाथी","बिल्लियाँ - बिल्लियाँ",4)
# add("Figure out the number of morphemes in the word ‘insubordinate’","Four (4)","Five (5)","Three (3)","Six (6)",2)
# add("Choose the option which represents the incorrect standard morphological notation","ran : {run} + {-ed}","men : {man} + {-s}","Inconsistent : {in} + {consist} + {-ent}","long : {long} ",3)

print(index.__doc__)
print(checkAnswer.__doc__)
print(QueryOverDb.__doc__)

