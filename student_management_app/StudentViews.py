import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Count
from .forms import AnswerForm,QuestionForm


from student_management_app.models import Students, Courses, Subjects, CustomUser, \
     NotificationStudent, StudentResult, OnlineClassRoom, SessionYearModel, \
     Question,Answer,Comment,UpVote,DownVote,Staffs


def student_home(request):
    student_obj=Students.objects.get(admin=request.user.id)
    course=Courses.objects.get(id=student_obj.course_id.id)
    subjects=Subjects.objects.filter(course_id=course).count()
    subjects_data=Subjects.objects.filter(course_id=course)
    session_obj=SessionYearModel.object.get(id=student_obj.session_year_id.id)
    class_room=OnlineClassRoom.objects.filter(subject__in=subjects_data,is_active=True,session_years=session_obj)

    subject_name=[]
    data_present=[]
    data_absent=[]
    subject_data=Subjects.objects.filter(course_id=student_obj.course_id)
    for subject in subject_data:
        subject_name.append(subject.subject_name)
    return render(request,"student_template/student_home_template.html",{"subjects":subjects,"data_name":subject_name,"data1":data_present,"data2":data_absent,"class_room":class_room})

def join_class_room(request,subject_id,session_year_id):
    session_year_obj=SessionYearModel.object.get(id=session_year_id)
    subjects=Subjects.objects.filter(id=subject_id)
    if subjects.exists():
        session=SessionYearModel.object.filter(id=session_year_obj.id)
        if session.exists():
            subject_obj=Subjects.objects.get(id=subject_id)
            course=Courses.objects.get(id=subject_obj.course_id.id)
            check_course=Students.objects.filter(admin=request.user.id,course_id=course.id)
            if check_course.exists():
                session_check=Students.objects.filter(admin=request.user.id,session_year_id=session_year_obj.id)
                if session_check.exists():
                    onlineclass=OnlineClassRoom.objects.get(session_years=session_year_id,subject=subject_id)
                    return render(request,"student_template/join_class_room_start.html",{"username":request.user.username,"password":onlineclass.room_pwd,"roomid":onlineclass.room_name})

                else:
                    return HttpResponse("This Online Session is Not For You")
            else:
                return HttpResponse("This Subject is Not For You")
        else:
            return HttpResponse("Session Year Not Found")
    else:
        return HttpResponse("Subject Not Found")


def student_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    student=Students.objects.get(admin=user)
    return render(request,"student_template/student_profile.html",{"user":user,"student":student})

def student_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("student_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()

            student=Students.objects.get(admin=customuser)
            student.address=address
            student.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("student_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("student_profile"))

@csrf_exempt
def student_fcmtoken_save(request):
    token=request.POST.get("token")
    try:
        student=Students.objects.get(admin=request.user.id)
        student.fcm_token=token
        student.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

def student_all_notification(request):
    student=Students.objects.get(admin=request.user.id)
    notifications=NotificationStudent.objects.filter(student_id=student.id)
    return render(request,"student_template/all_notification.html",{"notifications":notifications})

def student_view_result(request):
    student=Students.objects.get(admin=request.user.id)
    studentresult=StudentResult.objects.filter(student_id=student.id)
    return render(request,"student_template/student_result.html",{"studentresult":studentresult})

def home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        quests=Question.objects.annotate(total_comments=Count('answer__comment')).filter(title__icontains=q).order_by('-id')
    else:
        quests=Question.objects.annotate(total_comments=Count('answer__comment')).all().order_by('-id')
    paginator=Paginator(quests,10)
    page_num=request.GET.get('page',1)
    quests=paginator.page(page_num)
    return render(request,'student_template/home.html',{'quests':quests})

# Detail
def detail(request,id):
    quest=Question.objects.get(pk=id)
    tags=quest.tags.split(',')
    answers=Answer.objects.filter(question=quest)
    answerform=AnswerForm
    if request.method=='POST':
        answerData=AnswerForm(request.POST)
        if answerData.is_valid():
            answer=answerData.save(commit=False)
            answer.question=quest
            answer.user=request.user
            answer.save()
            messages.success(request,'Answer has been submitted.')
    return render(request,'student_template/detail.html',{
        'quest':quest,
        'tags':tags,
        'answers':answers,
        'answerform':answerform
    })

# Save Comment
def save_comment(request):
    if request.method=='POST':
        comment=request.POST['comment']
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        Comment.objects.create(
            answer=answer,
            comment=comment,
            user=user
        )
        return JsonResponse({'bool':True})

# Save Upvote
def save_upvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        check=UpVote.objects.filter(answer=answer,user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            UpVote.objects.create(
                answer=answer,
                user=user
            )
            return JsonResponse({'bool':True})

# Save Downvote
def save_downvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        check=DownVote.objects.filter(answer=answer,user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            DownVote.objects.create(
                answer=answer,
                user=user
            )
            return JsonResponse({'bool':True})

# Ask Form
def ask_form(request):
    form=QuestionForm
    if request.method=='POST':
        questForm=QuestionForm(request.POST)
        if questForm.is_valid():
            questForm=questForm.save(commit=False)
            questForm.user=request.user
            questForm.save()
            messages.success(request,'Question has been added.')
    staff_count=Staffs.objects.all().count()
    staffs = Staffs.objects.all()
    staff_name_list = []
    for staff in staffs:
        subject_ids = Subjects.objects.filter(staff_id=staff.admin.id)
        staff_name_list.append(staff.admin.username)

    return render(request,'student_template/ask-question.html',{'form':form})


# Questions according to tag
def tag(request,tag):
    quests=Question.objects.annotate(total_comments=Count('answer__comment')).filter(tags__icontains=tag).order_by('-id')
    paginator=Paginator(quests,10)
    page_num=request.GET.get('page',1)
    quests=paginator.page(page_num)
    return render(request,'student_template/tag.html',{'quests':quests,'tag':tag})

def tags(request):
    quests=Question.objects.all()
    tags=[]
    for quest in quests:
        qtags=[tag.strip() for tag in quest.tags.split(',')]
        for tag in qtags:
            if tag not in tags:
                tags.append(tag)
    # Fetch Questions
    tag_with_count=[]
    for tag in tags:
        tag_data={
            'name':tag,
            'count':Question.objects.filter(tags__icontains=tag).count()
        }
        tag_with_count.append(tag_data)
    return render(request,'student_template/tags.html',{'tags':tag_with_count})
