from statistics import mean 


def total_salary(path):
    salaries=[]
    with open(path, 'r') as file:
        for line in file:
            name, salary = line.strip().split(',')
            salaries.append(int(salary)) 
            

    

    return sum(salaries),mean(salaries)

def get_cats_info(path):
    cats_info = {}
    to_return = []
    with open(path , 'r') as file:
        for line in file:
            id, name, age = line.strip().split(',')
            print(id, name, age)
            cats_info['name'] = name
            cats_info['age'] = age
            cats_info['id'] = id
            to_return.append(cats_info)
    return to_return

cats_info = get_cats_info("cats.txt")
print(cats_info)