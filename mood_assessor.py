def get_mood():
    valid_mood = {
        'happy' : 2,
        'relaxed' : 1,
        'apathetic' : 0,
        'sad' : -1,
        'angry' : -2
    }
    while True:
        mood = input("Please input your current mood")
        if mood in valid_mood :
            return valid_mood[mood]

def print_mood(file_path,mood):
    with open(file_path,'w') as m:
        m.write(f'{mood}\n')

def get_date():
    import datetime
    date_today = datetime.date.today()
    date_today = str(date_today)
    return date_today

def write_data(data_pass,date_today,mood):
    with open(data_pass, 'w') as file:
        file.write(f"{date_today},{mood}\n")

def check_date(data_pass,date_today):
    with open(data_pass, 'r') as file:
        lines = file.readlines()
        for line in lines:
            date, mood = line.strip().split(',', 1)
            if date == date_today:
                return False

def check_seven(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    if len(lines) < 7:
        return False
    
def get_recent(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    recent_mood = lines[-7:]
    return recent_mood

def calculate(moods):
    valid_mood = {
        'happy' : 2,
        'relaxed' : 1,
        'apathetic' : 0,
        'sad' : -1,
        'angry' : -2
    }
    mood_values = moods
    average_value = round(sum(mood_values) / 7)
    average_mood = valid_mood(average_value)
    happy_days = mood_values.count(3)
    sad_days = mood_values.count(1)
    apathetic_days = mood_values.count(0)
    
    if happy_days >= 5:
        diagnosis = "manic"
    elif sad_days >= 4:
        diagnosis = "depressive"
    elif apathetic_days >= 6:
        diagnosis = "schizoid"
    else:
        diagnosis = average_mood
        
    return diagnosis

def assess_mood():
    import os
    file_path = os.path.join('data','mood_diary.txt')
    data_pass = os.path.join('data','data_diary.txt')
    mood = get_mood()
    date_today = get_date()
    if check_date(data_pass,date_today) == False:
        print('Sorry, you have already entered your mood today.')
        return
    else:
        print_mood(file_path,mood)
        write_data(data_pass,date_today,mood)
        if check_seven(file_path) == False:
            return
        else:
            recent_mood = get_recent(file_path)
            diagnosis = calculate(recent_mood)
            print(f'Your diagnosis: {diagnosis}!')




assess_mood()