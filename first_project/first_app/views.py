from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Student
from first_app.models import Program
from django.http import HttpResponseRedirect
from django.shortcuts import render
 
from .forms import StudentForm 
clicked = 0
def index(request) :
  global clicked
  clicked += 1
  my_dict = {'count' : clicked}
  return render(request, 'index.html', my_dict)
def help(request) :
  return render(request, 'help.html')
def year_current(request) :
  return HttpResponse('<h1 style="color:blue">2023 is the current year</h1>')
def year_function(request, year) :
    if year >= 2000 and year <= 2040 :
        msg = '<h2 style="color:blue"> ' + str(year) + ' is a valid year</h2>'
    else :
        msg = '<h2 style="color:red"> ' + str(year) + ' is NOT a valid year'
 
    return HttpResponse(msg)
def uuid_function(request, id) :
    return HttpResponse('<h2 style="color:blue"> ' + str(id) + ' is a valid uuid</h2>')
def year_month_function(request, year, month) :
    return HttpResponse('<h2 style="color:blue"> ' + str(year)+'and '+str(month) + ' is a valid</h2>')

def studentsd(request) :
  students = Student.objects.all()
  return render(request, 'index.html' , { 'title': 'students enrolled', 'students' :students} )

def programsd(request) :
  programs = Program.objects.all()
  return render(request, 'index.html' , { 'title': 'programs enrolled', 'programs' :programs} )
def get_student(request):    
  if request.method == 'POST':          
    form = StudentForm(request.POST)     
    if form.is_valid():
        s_name = form.cleaned_data['name']
        s_roll = form.cleaned_data['roll']
        s_degree = form.cleaned_data['degree']        
        s_branch = form.cleaned_data['branch']
 
    return HttpResponseRedirect('/student/')
  else: 
      form =StudentForm()
      return render(request, 'StudentForm.html', {'form': form})
def get_student(request) :
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
        s_name = form.cleaned_data['name']
        s_roll = form.cleaned_data['roll']
        s_year = form.cleaned_data['year']
        s_dob = form.cleaned_data['dob']
        s_degree = form.cleaned_data['degree']
        s_branch = form.cleaned_data['branch']
        print(s_name, s_roll, s_year, s_dob, s_degree, s_branch)
        # Now insert into the model
        #p = Program.objects.filter(title=s_degree,branch=s_branch).count()
        #if p :
            #s = Student(program=p, roll_number=s_roll, name=s_name, year=s_year, dob=s_dob)
            #s.save()
        #else :
            #np = Program(title=s_degree, branch=s_branch)
            #np.save()
            #s = Student(program=np, roll_number=s_roll, name=s_name, year=s_year, dob=s_dob)
            #s.save()
    return HttpResponseRedirect('/student/')
  else:
      form = StudentForm()
      return render(request, 'StudentForm.html', {'form': form})