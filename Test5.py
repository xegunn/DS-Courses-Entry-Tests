'''
Задача 5:
Существует массив поисковых запросов, например:

search_queries = [“watch new movies”, “coffee near me”, “how to find the determinant”, “python”, 
                  “data science jobs in UK”, “courses for data science”, “taxi”, “google”, “yandex”, 
                  “bing”,”foreign exchange rates USD/BYN”, “Netflix movies watch online free”,  
                  “Statistics courses online from top universities”]

Необходимо реализовать функцию, которая принимает на вход данные массива поисковых запросов и возвращает 
распределение поисковых запросов по количеству слов в каждом из запросов в процентах. 

Результат должен выглядеть следующим образом:
1 слово : 10%
2 слова:  40%
4 слова:  45%
5 слов:    5%
'''
def calc_word(search_querries):
    words = []
    nums = []
    
    for querry in search_querries:
        words = querry.split()
        nums.append(len(words))
    
    objects = {}
    
    for num in nums:
        objects[num] = objects.get(num, 0) + 1

    for key, value in objects.items():
        print(f"{key} слов {value*100/len(nums)} %")

    

search_queries = ["watch new movies", "coffee near me", "how to find the determinant", "python",
                  "data science jobs in UK", "courses for data science", "taxi", "google", "yandex", "bing",
                  "foreign exchange rates USD/BYN", "Netflix movies watch online free", 
                  "Statistics courses online from top universities"]
calc_word(search_queries)
    



            
            
