with open('life-expectancy.csv') as life_variable:
    interest = input('Enter the year of interest: ')
    next(life_variable)
    min_expec = 999
    max_expec = -1
    interest_min = 999
    interest_max = -1
    interest_year = []
    interest_expec = []
    for life in life_variable:
        life = life.strip()
        newlife_variable = life.split(',')
        entity = newlife_variable[0]
        code = newlife_variable[1]
        year = newlife_variable[2]
        expec = float(newlife_variable[3])
        expectancy_var = 0
        if expec > max_expec:
            max_expec = expec
            max_ent = entity
            max_year = year
        if expec < min_expec:
            min_expec = expec
            min_ent = entity
            min_year = year
        if interest == year:
            interest_year.append(year)
            interest_expec.append(expec)
        for intnumb in interest_expec:
            if intnumb > interest_max:
                interest_max = expec
                max_ent_int = entity
            if intnumb < interest_min:
                interest_min = expec
                min_ent_int = entity
    list_avg = sum(interest_expec) / len(interest_expec)
            

            
print()
print(f'The overall max life expectancy is: {max_expec} from {max_ent} in {max_year}')
print(f'The overall min life expectancy is: {min_expec} from {min_ent} in {min_year}')
print()
print(f'For the year {interest}:')
print(f'The average life expectancy across all countries was {list_avg:.2f}')
print(f'The max life expectancy was in {max_ent_int} with {interest_max}')
print(f'The min life expectancy was in {min_ent_int} with {interest_min}')




