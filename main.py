import os
import random
def makeCommits (days : int):
    n = random.randint(0, 15)
    if days < 1:
        os.system('git push -f')
    else:
        dates = f"{days} days ago"
        with open('data.txt', 'a') as file:
            file.write(f'{dates} <- this was the commit for the day!!\n')
        
        # staging 
        os.system('git add data.txt')

        # commit 
        os.system('git commit --date="'+ dates +'" -m "First commit for the day!"')

        return days * makeCommits(days - n)

makeCommits(390)