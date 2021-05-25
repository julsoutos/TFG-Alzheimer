from django.shortcuts import render
from principal.models import  Activity_Result, Activity_Training
import datetime
import json

def patient_stats(request):

    try:

        if request.method == "POST":
            
            day = request.POST['day'] 
            patient = request.GET['patient']

            context = {"day": day, "diary_stats": get_diary_stats(day, patient), "weekly_stats": get_week_stats(day, patient), "monthly_stats": get_monthly_stats(day, patient), "chart": True}
            
            return render(request, 'patient_stats.html', context)

    except:
        pass 
    
    context = {"chart": True}

    return render(request, 'patient_stats.html', context)


def get_diary_activities(date, category, patient):

    try:
        correct = (Activity_Training.objects.filter(patient_training__end_date = date, is_correct=True, activity__category = category, patient_training__patient__pk=patient),
                    Activity_Result.objects.filter(end_date = date, is_correct=True, solution__activity__category = category, patient__pk=patient))
        incorrect = (Activity_Training.objects.filter(patient_training__end_date = date, is_correct=False, is_completed=True, activity__category = category, patient_training__patient__pk=patient),
                    Activity_Result.objects.filter(end_date = date, is_correct=False, is_completed=True,solution__activity__category = category, patient__pk=patient))

        return ( (correct[0].count() + correct[1].count()) , (incorrect[0].count() + incorrect[1].count()) )
        
    except:
        return (0,0)

def get_days_activities(date, days, patient):

    try:
        stats = []

        weeks = []
        week_correct = 0
        week_incorrect = 0

        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()

        for i in range(1,days+1):
            day = datetime.timedelta(days=(days)-(i))
            correct = (Activity_Training.objects.filter(patient_training__end_date = date - day, is_correct=True, patient_training__patient__pk=patient).count() + 
                            Activity_Result.objects.filter(end_date = date - day, is_correct=True, patient__pk=patient).count())

            incorrect = (Activity_Training.objects.filter(patient_training__end_date = date - day, is_correct=False, is_completed=True, patient_training__patient__pk=patient).count() + 
                        Activity_Result.objects.filter(end_date = date - day , is_correct=False, is_completed=True, patient__pk=patient).count())

            week_correct += correct
            week_incorrect += incorrect
        
            

            if((days - i)%7 == 0):
               
                weeks.append((week_correct, week_incorrect))
                week_correct = 0
                week_incorrect = 0
            

            stats.append((correct, incorrect))
        
        return (stats, weeks)

    except:
            return (0,0)

def get_days_category_activities(date, days, category, patient):

    try:

        date1 = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        date2 = date1 - datetime.timedelta(days=days)
      

        correct = (Activity_Training.objects.filter(patient_training__end_date__range = [date2, date1], is_correct=True,  activity__category = category, patient_training__patient__pk=patient).count() + 
                        Activity_Result.objects.filter(end_date__range = [date2, date1], is_correct=True, solution__activity__category = category, patient__pk=patient).count())

        incorrect = (Activity_Training.objects.filter(patient_training__end_date__range = [date2, date1], is_correct=False, is_completed=True,  activity__category = category, patient_training__patient__pk=patient).count() + 
                    Activity_Result.objects.filter(end_date__range = [date2, date1] , is_correct=False, is_completed=True, solution__activity__category = category, patient__pk=patient).count())

        return ((correct, incorrect))

    except:
            return (0,0)




def get_diary_stats(day, patient):

    diary_memory_training = get_diary_activities(day, "Memory", patient)
    diary_calculus_training = get_diary_activities(day, "Calculus", patient)
    diary_attention_training = get_diary_activities(day, "Attention", patient)
    diary_perception_training = get_diary_activities(day, "Perception", patient)
    diary_language_training = get_diary_activities(day, "Language", patient)

    stats = {"correct_memory": json.dumps(diary_memory_training[0]), "incorrect_memory": json.dumps(diary_memory_training[1]),
                "correct_calculus": json.dumps(diary_calculus_training[0]), "incorrect_calculus": json.dumps(diary_calculus_training[1]),
                "correct_attention": json.dumps(diary_attention_training[0]), "incorrect_attention": json.dumps(diary_attention_training[1]),
                "correct_perception": json.dumps(diary_perception_training[0]), "incorrect_perception": json.dumps(diary_perception_training[1]),
                "correct_language": json.dumps(diary_language_training[0]), "incorrect_language": json.dumps(diary_language_training[1]),}

    return stats

def get_week_stats(day, patient):
    
    week_memory_training = get_days_category_activities(day, 7, "Memory", patient)
    week_calculus_training = get_days_category_activities(day, 7 ,"Calculus", patient)
    week_attention_training = get_days_category_activities(day, 7 ,"Attention", patient)
    week_perception_training = get_days_category_activities(day, 7 ,"Perception", patient)
    week_language_training = get_days_category_activities(day, 7 ,"Language", patient)

    stats = {"correct_memory": json.dumps(week_memory_training[0]), "incorrect_memory": json.dumps(week_memory_training[1]),
                "correct_calculus": json.dumps(week_calculus_training[0]), "incorrect_calculus": json.dumps(week_calculus_training[1]),
                "correct_attention": json.dumps(week_attention_training[0]), "incorrect_attention": json.dumps(week_attention_training[1]),
                "correct_perception": json.dumps(week_perception_training[0]), "incorrect_perception": json.dumps(week_perception_training[1]),
                "correct_language": json.dumps(week_language_training[0]), "incorrect_language": json.dumps(week_language_training[1]), "week_days": get_days_activities(day, 7 ,patient)[0]}

    return stats


def get_monthly_stats(day, patient):
    
    month_memory_training = get_days_category_activities(day, 28, "Memory", patient)
    month_calculus_training = get_days_category_activities(day, 28 ,"Calculus", patient)
    month_attention_training = get_days_category_activities(day, 28 ,"Attention", patient)
    month_perception_training = get_days_category_activities(day, 28 ,"Perception", patient)
    month_language_training = get_days_category_activities(day, 28 ,"Language", patient)

    stats = {"correct_memory": json.dumps(month_memory_training[0]), "incorrect_memory": json.dumps(month_memory_training[1]),
                "correct_calculus": json.dumps(month_calculus_training[0]), "incorrect_calculus": json.dumps(month_calculus_training[1]),
                "correct_attention": json.dumps(month_attention_training[0]), "incorrect_attention": json.dumps(month_attention_training[1]),
                "correct_perception": json.dumps(month_perception_training[0]), "incorrect_perception": json.dumps(month_perception_training[1]),
                "correct_language": json.dumps(month_language_training[0]), "incorrect_language": json.dumps(month_language_training[1]), "week_days": get_days_activities(day, 28 ,patient)[1]}

    return stats