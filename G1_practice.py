# G1 Practice Questions

import random

'''
8. maybe figure out how to do a time delay of like two seconds *
'''

question_dict_answer = {1 : {
                            "question" : "In Ontario, a driver will be give 7 demerit points if he/she is covicted of :", 
                            "choices" : ["A. Following too close\nB. Failing to stop for a stopped school bus with its red alternating lights on\nC. Failing to remain at the scene of a accident\nD. Failing to obey the directions of a police officer"], 
                            "answer" : 'C'},

                        2 : {
                            "question" : "In Onatrio, a first conviction for drinking and driving can bring a minimum license suspension of:", 
                            "choices" : ["A. 6 months\nB. 12 months\nC. 24 months\nD. 48 months"], 
                            "answer" : 'B'},
                            
                        3 : {
                            "question" : "In Ontario, it is legal to turn right on red:", 
                            "choices" : ["A. Only after the vehicle has come to a complte stop yielding right of way\nB. Only from a one-way street to another one-way street\nC. Only from a two-way street to another two-way street\nD. Only from a one-way street to a two-way street"], 
                            "answer" : 'A'},

                        4 : {
                            "question" : "A streetcar is stopped to load annd unload passengers. A driver of a motor vehicle is approaching this streetcar from the rear. The driver must stop:", 
                            "choices" : ["A. 2 meters from the rear-most door at which the passengers are getting on or off\nB. 3 meters from the rear-most door at which the passengers are getting on or off\nC. 6 meters from the rear-most door at which the passengers are getting on or off\nD. 9 meters from the rear-most door at which the passengers are getting on or off"], 
                            "answer" : 'A'},

                        5 : {
                            "question" : "When approaching a level railway crossing with the gates down, the driver of a motor vehicle must:", 
                            "choices" : ["A. Stop 1 meter from the gates\nB. Stop 3 meters from the line\nC. Stop 5 meters from the first rail\nD. Stop 15 meters from the railroad crossing"], 
                            "answer" : 'C'},
                        
                        6 : {
                            "question" : "In what lane should you drive if you intend to make a ride turn?", 
                            "choices" : ["A. Close to the left of the roadway\nB. Close to the right hand side of the roadway\nC. Close to the centerline of the roadway\nD. Does not matter"], 
                            "answer" : 'B'},

                        7 : {
                            "question" : "In Ontario, there is a seat belt law:", 
                            "choices" : ["A. Yes\nB. No\nC. Only when driving on an open highway\nD. Only when driving wihtin a municipality"], 
                            "answer" : 'A'},

                        8 : {
                            "question" : "If someone is tailgating you, what should you do?", 
                            "choices" : ["A. Move into another lane when it is safe to do so\nB. Slow down slightly to increase the space in front of your car\nC. Pull over to let the tailgater pass\nD. All of the above"], 
                            "answer" : 'D'},

                        9 : {
                            "question" : "Failing to stop for a school bus that is unloading passengers will:", 
                            "choices" : ["A. Result in a one year jail sentence\nB. Cost you 6 demerit points and a fine of up to $1000\nC. Get you a warning and a fine of $100\nD. Result in retaking your road test"], 
                            "answer" : 'B'},  
                        
                        10 : {
                            "question" : "When a car is stopped to allow a pedestrian to cross the street at a marked crosswalk, you should:", 
                            "choices" : ["A. Pass the stopped car on the left\nB. Sound horn for the driver of the stopped car to drive on\nC. Pass the stopped car to the right\nD. Not pass any car stopped to allow a pedestrian to cross"], 
                            "answer" : 'D'}, 

                        11 : {
                            "question" : "When driving in heavy fog, you should use:", 
                            "choices" : ["A. Parking lights\nB. Low beam headlights\nC. Parking lights and high beam headlights\nD. High beam headlights"], 
                            "answer" : 'B'},

                        12 : {
                            "question" : "Never change lanes in traffic without:", 
                            "choices" : ["A. Giving proper signal and lookin to make sure the move can be made safely\nB. Decreasing speed and giving the correct signal\nC. Looking into the rear view mirror only\nD. Blowing your horn and looking the rear"], 
                            "answer" : 'A'},

                        13 : {
                            "question" : "What documents may a police officer require a motor vehicle owner to produce:", 
                            "choices" : ["A. If the motor vehicle is insured - a liability insurance card\nB. The motor vehicle ownership\nC. If he is operating a motor vehicle - a valid driver's license\nD. Any of the above"], 
                            "answer" : 'D'},  

                        14 : {
                            "question" : "Every accident must be reported to the police where there is personal injury or whne the damage exceeds:", 
                            "choices" : ["A. $100\nB. $150\nC. $1500\nD. $1000"], 
                            "answer" : 'D'},

                        15 : {
                            "question" : "When lights are required, drivers must use lower beam headlights when following another vehicle:", 
                            "choices" : ["A. Within 30m (100 ft.)\nB. Within 60m (200 ft.)\nC. Within 120m (400 ft.)\nD. This only applies when approaching another vehicle"], 
                            "answer" : 'B'},   

                        16 : {
                            "question" : "While travelling on a highway, the driver of a motor vehicle is not permitted to carry, in a house or boat trailer:", 
                            "choices" : ["A. Firearms\nB. Flammable material\nC. Persons (Passenger)\nD. Pets"], 
                            "answer" : 'C'},     
                        
                        17 : {
                            "question" : "When on streets designed for †wo-way traffic, you hear the siren of an emergency vehicle, what does the law require you to do?", 
                            "choices" : ["A. Speed up and get out of the way\nB. Signal the driver to pass\nC. Pull to the right as far as possible and stop\nD. Continue at the same speed"], 
                            "answer" : 'C'},

                        18 : {
                            "question" : "Which of the following has the right-of-way over all others at an intersection when the signal light is green?", 
                            "choices" : ["A. Pedestrians crossing against the light\nB. Pedestrians crossing with the light\nC. Vehicles turning right\nD. Vehicles turning left"], 
                            "answer" : 'B'},

                        19 : {
                            "question" : "To what penalties is a driver liable who is convicted of driving while disqualified?", 
                            "choices" : ["A. A fine of $500 or imprisonment for six months or both\nB. Impoundment of the motor vehicle being operated for three months\nC. An additional 6-month period of suspension of driving privilege\nD. Any of all of the above"], 
                            "answer" : 'D'},   

                        20 : {
                            "question" : "When the traffic signal-light facing you is red and you intend to go straight through the intersection, what must you do?", 
                            "choices" : ["A. Stop, give pedestrians the right-of-way, then proceed with caution\nB. Stop, proceed when the way is clear\nC. Slow down, proceed when the way is clear\nD. Stop, proceed only when the signal turns green and when the way is clear"], 
                            "answer" : 'D'},

                        21 : {
                            "question" : "If you are involved in a reportable accident, how soon must you make a report to your nearest provincial or municipal police officer?", 
                            "choices" : ["A. At once\nB. Within 24 hours\nC. Within 48 hours\nD. Within 72 hours"], 
                            "answer" : 'A'},

                        22 : {
                            "question" : "Unless otherwise posted, the maximum speed limit allowed in cities, town, villages, and built-up area is:", 
                            "choices" : ["A. 30 km/h (20 m.p.h.)\nB. 50 km/h (30 m.p.h.)\nC. 40 km/h (25 m.p.h.)\nD. 60 km/h(35 m.p.h.)"], 
                            "answer" : 'B'},

                        23 : {
                            "question" : "At an intersection where there is a flashing amber (yellow) traffic light, you must:", 
                            "choices" : ["A. Stop if making a right turn\nB. Continue at the same speed\nC. Stop if making a left turn\nD. Slow down and proceed with caution"], 
                            "answer" : 'D'},

                        24 : {
                            "question" : "Under what circumstances may a driver's license be cancelled?", 
                            "choices" : ["A. For failure to attend a re-examination\nB. For possession of an altered driver's license\nC. For failure to satisfactorily complete a driver re-examination\nD. Any or all of the above"], 
                            "answer" : 'D'},

                        25 : {
                            "question" : "As a level one (G1) driver, you must be accompanied by a class G or higher licensed driver, who has the following driving experience more than:", 
                            "choices" : ["A. Three years\nB. Four years\nC. Eight years\nD. Six years"], 
                            "answer" : 'B'},

                        26 : {
                            "question" : "As a level two (G2) driver your alcohol level must not be over:", 
                            "choices" : ["A. 0.08%\nB. 0.05%\nC. 0.02%\nD. 0.00%"], 
                            "answer" : 'D'},

                        27 : {
                            "question" : "Overdriving your headlghts at night is dangerous because:", 
                            "choices" : ["A. You are driving too fast\nB. Your headlights are too bright\nC. You cannot stop within the distance that you can see\nD. It is not good for the car battery"], 
                            "answer" : 'C'},

                        28 : {
                            "question" : "If you want to pas a motorcycle, you should:", 
                            "choices" : ["A. Honk your horn before you pass\nB. Turn on your high-beam lights before you pass\nC. Pass just as you would with another car\nD. Use half of their lane to pass"], 
                            "answer" : 'C'},

                        29 : {
                            "question" : "If you are a teenage driver aged 19 or under and in the first months of receiving your G2 license. How many passengers are you allowed to carry between midnight and 5 a.m.?", 
                            "choices" : ["A. 3 passengers aged 19 or under\nB. No passengers aged 19 or under\nC. 1 passenger aged 19 or under(no restrictions for passengers the age of 20 and over)\nD. 2 passengers aged 19 or under"], 
                            "answer" : 'C'},          





                        }

# the actual game
while True:
    question_num = list(range(1, 17))
    random.shuffle(question_num)

    for q_n in question_num:
        q_n = question_dict_answer[q_n] # q_n is the random question number
        ans = q_n.get("answer")
        print(q_n.get("question")) # prints the question corresponding to the index

        # print the possible multiple choices
        multiple_choice = ''.join(q_n.get("choices"))
        multiple_choice_lines = multiple_choice.splitlines(keepends = False)

        for line in multiple_choice_lines:
            print(line)
            
        i = input()

        if i == ans or i == ans.lower():
            print("CORRECT")
        else:
            print("INCORRECT, try again")
            i = input()
            if i == ans or ans.lower():
                print("CORRECT")
            else:
                print(f"INCORRECT, the correct answer was {ans}")
