from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import Http404,HttpResponse
from .models import  Newsletter,patient_table
from instamojo_wrapper import Instamojo
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import nltk
from nltk.corpus import stopwords
import re
import datetime
import gensim
from gensim.models import Word2Vec
import MySQLdb
import cx_Oracle
import warnings
warnings.filterwarnings("ignore")

# nltk.download() # for downloading packages

import numpy as np
import random
import string
# Create your views here.

def index(request):
	#messages.success(request, request.session['username'])
	return render(request, 'codemania_app/index.html');
def xx(request):

	return render(request, 'codemania_app/xx.html');


conn=MySQLdb.connect(host='localhost', database='mysql',user='root',password='mysql')
def conn_disease(request):


#variable declaration
	table_name='disease'
	string_table_name="'DISEASE'"
#inpu='567890'
	table_data=[]
	column_names=[]
	flag_pid=flag_doc_id=flag_date=flag_report_link=-1
	column_name_mapping={}
	probability=0

#extracting column names from table
	cursor=conn.cursor()
	cursor.execute("desc "+table_name)
	res=cursor.fetchone()
	while res is not None:
		column_names.append(res)
		res=cursor.fetchone()
#print(column_names)

#extracting entire table data
	cursor.execute("select * from "+table_name)
	res=cursor.fetchone()
	while res is not None:
		table_data.append(res)
		res=cursor.fetchone()
#print(table_data)

#to count number of rows
	cursor.execute("select count(*) from "+table_name)
	no_of_rows=cursor.fetchone()[0]
#print(no_of_rows)

	for col_ptr in range(len(column_names)):

    #to identify pid column
		for row_ptr in range(no_of_rows):
			pattern = re.compile("^[0-9]*$")
			if pattern.search(str(table_data[row_ptr][col_ptr])):
            #print(pattern.search(str(table_data[row_ptr][col_ptr])))
				if len(table_data[row_ptr][col_ptr])==6:
					flag_id=1
					continue
				else:
					flag_id=-1
					break
		if flag_id==1:
			column_name_mapping[column_names[col_ptr]]='pid'
			flag_id=0
			col_ptr=col_ptr+1
        #print(column_name_mapping)
        #print(column_names[col_ptr])
		continue

    #to identify doc_id column
	for row_ptr in range(no_of_rows):
		pattern=re.compile("^DR[0-9]*$");
		if pattern.search(str(table_data[row_ptr][col_ptr])):
            #print(pattern.search(str(table_data[row_ptr][col_ptr])))
			if len(table_data[row_ptr][col_ptr])==6:
				flag_doc_id=1
				continue
			else:
				flag_doc_id=-1
				break
	if flag_doc_id==1:
		column_name_mapping[column_names[col_ptr]]='d_id'
		flag_doc_id=0
		col_ptr=col_ptr+1
        #print(column_name_mapping)
        #print(column_names[col_ptr]


    #to identify disease column
	for row_ptr in range(no_of_rows):
		try:
			res=abs(model1.similarity('disease',table_data[row_ptr][col_ptr].split()[0].lower()))
			if res>=0 and res<=1:
				probability+=1
			else:
				probability-=1
		except:
			pass
	if probability>=no_of_rows*0.8:
		column_name_mapping[column_names[col_ptr]]='disease'
		probability=0
		col_ptr=col_ptr+1
        #print(column_name_mapping)
        #print(column_names[col_ptr])

    #to identify date column
	for row_ptr in range(no_of_rows):
        #print(type(table_data[row_ptr][col_ptr]))
		if type(table_data[row_ptr][col_ptr]) is datetime.date:
			flag_date=1
			continue
		else:
			flag_date=-1
	if flag_date==1:
		column_name_mapping[column_names[col_ptr]]='date'
		flag_date=-1
        #print(column_name_mapping)
        #print(column_names[col_ptr])

    #to identify report column
	for row_ptr in range(no_of_rows):
		pattern=re.compile("^https:/[a-zA-Z0-9]*");
		if pattern.search(str(table_data[row_ptr][col_ptr])):
            #print(pattern.search(str(table_data[row_ptr][col_ptr])))
			flag_report_link=1
			continue
		else:
			flag_report_link=-1
	if flag_report_link==1:
		column_name_mapping[column_names[col_ptr]]='link'
		flag_report_link=0
        #print(column_name_mapping)
        #print(column_names[col_ptr])
		col_ptr=col_ptr+1


#to print mapping of all the columns
	print(column_name_mapping)

#to close connections and cursors
	cursor.close()
	return 1;
#conn.close()
def doctor_query(request,dq):
    cursor=conn.cursor()
    cursor.execute(dq)
    res=cursor.fetchone()
    temp=[]
    while res is not None:
        temp.append(res)
        res=cursor.fetchone()
    return temp

def aadhar_query(request,aq):
    cursor=conn.cursor()
    cursor.execute(aq)
    res=cursor.fetchone()
    temp=[]
    while res is not None:
        temp.append(res)
        res=cursor.fetchone()
    return temp
conn1=''
def oracle(request,disq):
	conn1 = cx_Oracle.connect('oracle/oracle@localhost')
	cursor = conn.cursor()
	cursor.execute("select * from disease where p_id=" + disq)
	res = cursor.fetchone()
	temp = []
	while res is not None:
		temp.append(res)
		print(res)
		res = cursor.fetchone()
	conn1.close()



def disease_query(request,disq):
    cursor=conn.cursor()
    cursor.execute("select * from disease where p_id="+disq)
    res=cursor.fetchone()
    temp=[]
    while res is not None:
        res=list(res)
        res.append("Hospital A")
        temp.append(res)
        res=cursor.fetchone()
    cursor.close
    return temp


def patient_query(request,pq):
    cursor=conn.cursor()
    print(pq)
    cursor.execute("select * from patient1 where patient_id=" + str(pq))
    res=cursor.fetchone()
    temp=[]
    while res is not None:
        temp.append(res)
        res=cursor.fetchone()
    cursor.close
    return temp
def newsletter(request):
	form = Newsletter(email = request.POST['news_email']);
	form.save();
	return redirect('/');
def doctor(request):
	messages.success(request, request.session['username'])
	return render(request, 'codemania_app/doctor.html');

def form_save_internship(request):



	return render(request, 'codemania_app/doctor.html');
def doctor_display_1(request):
	messages.success(request, request.session['username'])
	x=request.POST['aadhaar']
	y=request.POST['dob']
	print("checked")
	print(x,y)
	x1 = patient_table.objects.filter(uid=x)
	print(x1)
	return render(request, 'codemania_app/doctor.html',context = {'e':x1})
def doctor_display(request):
	messages.success(request, request.session['username'])
	print("entered")
	print(request.POST['pat'])
	y=request.POST['pat']



	return render(request,'codemania_app/doctor.html')


def doctor_1(request):
	messages.success(request, request.session['username'])
	x=patient_table.objects.filter(did=request.session['username'])



	#print(request.POST['random'])
	return render(request, 'codemania_app/doctor.html',context = {'c':x})


def login(request):
	return render(request, 'codemania_app/login.html');

def register(request):
	return render(request, 'codemania_app/register.html');

def data_virt(request):
	return render(request, 'codemania_app/datav.html')
def myobj(request):
	return patient_table.objects.all()

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "hii")
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me "]
def intro_chatbot(request,flag):
	print(" My name is robo  . How can i help you?")

	user_response = request.POST['input']
	user_response = user_response.lower()
	if user_response in GREETING_INPUTS:
		return render(request, 'codemania', context={})

# Checking for greetings
def greeting(request,sentence):
    x=1
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
    if(x == 1):
        x=0
        #print(greeting(request,"hello welcome"))

def patient(request):
	try:
		greeting(request,"hiii")
		is_private = request.POST.get('set', False)
		print("check ")
		d=''
		if(is_private=="check the data"):
			id=request.session['username']
			records=disease_query(request,id)
			conn.close()
			print("addd")
			print(records)
			conn1 = cx_Oracle.connect('oracle/oracle@localhost')
			print("1")
			cursor = conn1.cursor()
			print("2")
			cursor.execute("select * from disease where p_id=" +str(789890))
			print("3")
			res = cursor.fetchone()
			temp = []
			while res is not None:
				res=list(res)
				res.append("Hospital B")
				temp.append(res)
				res = cursor.fetchone()
			cursor.close

			for q in temp:
				records.append(q)
			print(records)
		#records.append(disease_query(request,id))

		#conn1.close()
			print(len(records))
			print("q1")
			cursor = cursor.execute("select P_ID,P_NAME from patient where P_ID="+str(id))
			print("q2")
			temp1 = []
			res=cursor.fetchone()
			while res is not None:
				temp1.append(res);
				break;
			cursor.close
			print("adithya")
			print(temp1)
			cursor = cursor.execute("select D_ID,D_NAME from doctor where D_ID in (select D_ID from disease where p_id=" +str(id)+')')
			temp2 = []
			res=cursor.fetchone()
			while res is not None:
				temp2.append(res);
				break;

			conn1.close()
			cursor.close

			print("temp")
			print(temp1)
			print(temp2)

			for i in range(len(records)):

				l=['']*7
				myf=0
				print("atdttt")
				for j in range(len(records[i])):
					l[j]=records[i][j]
					print("dsdshfd")

			#print(l[3])
			#b = datetime.datetime(2011, 5, 21)
			#print(l[3].strftime("%Y/%m/%d"))




				print(l[j])
				print(l,temp1[0][1]);
				print(temp2[0][1])
				aqq = patient_table(pid = l[0],did =l[1],diseasename = l[2],date =datetime.date(2016,3,5) ,linkreport = l[4],uid=l[5],pname=temp1[0][1],dname=temp2[0][1],hname=l[6])

				for j in patient_table.objects.all():
			# print(aqq.pid, j.pid)
			# print(aqq.did, j.did)
			# print(aqq.diseasename, j.diseasename)
			# print(aqq.date,j.date)
			# print(aqq.linkreport,j.linkreport)
					if ( aqq.uid == j.uid and aqq.pid == j.pid and aqq.did == j.did and aqq.diseasename == j.diseasename and aqq.linkreport == j.linkreport):
						myf = 1
						break;
				if (myf == 0):
					aqq.save()
				print(myf)

			'''if(request.POST['but']=='Search here'):
				x=patient_table.objects.filter(disease='%'+request.POST['search']+'%')
				return render(request, 'codemania_app/datav.html', context={'c':x })'''

			d = patient_table.objects.all()

			print(len(d))
	except Exception:
		print('xx')
		#xx=request.session['value']
		u=myobj(request)

		messages.success(request, request.session['username'])
		return render(request, 'codemania_app/datav.html', context={'c': u, 'pri': is_private})


	messages.success(request,request.session['username'])
	return render(request, 'codemania_app/datav.html',context = {'c':d,'pri':is_private})







def user_auth(request):
	#print("*"*10,request, "*"*10)
	#print(User.objects.get(email='test@gmail.com'))
	var=False;
	fl=None
	user=authenticate(username=request.POST['name'],password=request.POST['password'])


	print(user)
	if user:
		request.session['username']=request.POST['name']
		for i in User.objects.all():
			if (request.POST['name'] == i.username):
				print("valid")
				var = i.is_staff;
				break;
		print(var)
		print(fl)


		#rint(request.session['username'])
		#print(messages)
		messages.success(request, request.session['username'])

		if(var==False):
			return redirect('/')
		else:
			return redirect('/xx')

	else:
		return redirect('/login');

def register_auth(request):
	print('_'*10, request,'_'*10)
	name = request.POST['name1'];
	email = request.POST['email'];
	pass1 = request.POST['password1'];
	pass2 = request.POST['password2'];
	usertype=request.POST['designation']
	print(usertype)
	is_staff=''
	if usertype=='Doctor':
		is_staff=True
	else:
		is_staff=False

	if pass1 == pass2:
		print('Name', name)
		user = User.objects.create_user(username=name, email=email, password=pass1,is_staff=is_staff);
		user.save();
		return redirect('/');
	else:
		return redirect('/register');
def logout(request):
	del request.session['username']
	return  redirect('/')
def forgot_psw(request):
	return render(request, 'codemania_app/resetpassword.html');
