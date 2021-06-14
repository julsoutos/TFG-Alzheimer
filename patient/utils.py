from principal.models import Solution
import random
from datetime import datetime


def get_solution(request, activity):
    solution = list(Solution.objects.filter(activity=activity))
    r = random.randint(0, len(solution) - 1)
    
    return solution[r]



def evaluate(request, solution, name):

    expected_solution = list(Solution.objects.filter(name = solution))[0] 
    answer = request.POST[name]
    return True if expected_solution.solution == answer else False
     
def birth(birth_date):
    return int((datetime.now().date() - birth_date).days / 365.25)