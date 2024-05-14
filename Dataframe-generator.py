import pandas as pd
import names
import random

# Setup your variabels
rows = 50
column_nams = ['name', 'gender', 'age', 'color_of_skin', 'haircolors', 'male_facial_hair', 'female_hair_style', 'car', 'car_color', 'interracial_couple']

# All data you want goes here organised into lists
gender = ['Male', 'Female']
age = [x for x in range(18, 80)]
color_of_skin = ['White', 'Black']
haircolors = ['Blonde', 'Black', 'Brown', 'Red']
male_facial_hair = ['Shaved', 'Mustache', 'Beard']
female_hair_style = ['Ponytail', 'Bun', 'Straight', 'Curled']
car = [True, False]
car_color = ['Yellow', 'Red', 'Blue', 'Green', 'Black']
interracial_couple = [True, False]

# Function to predetermine probabilities (optional)
# if you do use it, probabilites have to add up to 1
# # of probabilities  = # of items in list (when calling function)
def pick_item_with_probability(items, probabilities):
    
    # Generate a random number between 0 and 1
    rand_num = random.random()
    
    # Iterate through items and probabilities
    cumulative_prob = 0
    for item, prob in zip(items, probabilities):
        cumulative_prob += prob
        if rand_num <= cumulative_prob:
            return item
    
    # If for some reason, loop ends without picking, return last item
    return items[-1]

data = []
# Loop that creates each variable
for _ in range(rows):
    # Customize each variable with your own and a new name (I used t for temporary)
    tname = names.get_first_name()
    tgender = pick_item_with_probability(gender, [0.5, 0.5])
    tage = random.choice(age)
    tcolor_skin = pick_item_with_probability(color_of_skin, [0.67, 0.33])
    thaircolor = pick_item_with_probability(haircolors, [0.5, 0.21, 0.19, 0.1])
    tm_facialhair =  'NaN' if tgender == 'Female' else pick_item_with_probability(male_facial_hair, [0.42, 0.26, 0.31])
    tf_hairstyle = 'NaN' if tgender == 'Male' else pick_item_with_probability(female_hair_style, [0.15, 0.2, 0.35, 0.3])
    tcar = pick_item_with_probability(car, [0.9, 0.1])
    tcar_color = 'NaN' if car == 'False' else pick_item_with_probability(car_color, [0.1, 0.175, 0.3125, 0.025, 0.3875])
    tinterracial = pick_item_with_probability(interracial_couple, [0.001, 0.999])
    
    # Creates list
    temp_data = [tname, tgender, tage, tcolor_skin, thaircolor, tm_facialhair, tf_hairstyle, tcar, tcar_color, tinterracial]
    # Appends list to data (list of lists)
    data.append(temp_data)

# Transform List of lists with new name
df = pd.DataFrame(data, columns=[column_nams])
# Normal Print:
print(df)

# Only if in jupyter notebook:
# display(df)

df.to_csv('Math_Data.csv')