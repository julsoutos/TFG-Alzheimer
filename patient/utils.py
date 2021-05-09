from principal.models import Activity, Solution
import random
import urllib.request


def get_solution(request, activity):
    solution = list(Solution.objects.filter(activity=activity))
    r = random.randint(0, len(solution) - 1)
    
    return solution[r]



def evaluate(request, solution):

    expected_solution = list(Solution.objects.filter(name = solution))[0] 
    answer = request.POST['answer']
    print(answer)
    return True if expected_solution.solution == answer else False
     
