TEMPLATES = {
    "Exercise_0_received": {
        "subject": "[TML24/25] Exercise 0 received",
        "body": """Dear {Preferred name},

We have received your submission for Exercise 0. Thank you for your hard work!

Best Wishes,
STAI
    """
    },
    "Exercise_0_not_received": {
        "subject": "[TML24/25] Exercise 0 not received",
        "body": """Dear {Preferred name},

We have not received your submission for Exercise 0 and you're not registered for the TML24/25 course.
If you have any questions or concerns, please don't hesitate to reach out to us.

Best Wishes,
STAI
    """
    },
    "Exam1_first": {
        "subject": "[TML23/24] Exam 1 grades",
        "body": """Dear {Preferred name},

Here's the summary of your performance.

Grade after Exam: {Exam1.final-grade-scheme4}
Exam 1 final score S = min(100, X + T): {Exam1.final-score} out of 100
Exam 1 score X = R x 5/9: {Exam1.score} out of 100
Exam 1 raw score R : {Exam1} out of 180
Exercise topup T = (E - 60) / 4: {Exercise-topup} out of 10
Exercise 1-3 average score E: {Exercise-scores} out of 100

Below is the breakdown of your Exam scores

B1 | Your score: {Exam1.B1} / 15 | Average score: 9.1
B2 | Your score: {Exam1.B2} / 15 | Average score: 10.6
B3 | Your score: {Exam1.B3} / 15 | Average score: 10.8
B4 | Your score: {Exam1.B4} / 15 | Average score: 9.0
B5 | Your score: {Exam1.B5} / 15 | Average score: 8.5
B6 | Your score: {Exam1.B6} / 15 | Average score: 4.1
A1 | Your score: {Exam1.A1} / 30 | Average score: 5.6
A2 | Your score: {Exam1.A2} / 30 | Average score: 15.4
A3 | Your score: {Exam1.A3} / 30 | Average score: 10.8
Sum: R = {Exam1} out of 180

Below is the breakdown of your exercise scores

Exercise 1 | Your score: {Ex1}
Exercise 2 | Your score: {Ex2}
Exercise 3 | Your score: {Ex3}
Sum: E = min(100, (Ex1 + Ex2 + Ex3) / 3) = {Exercise-scores} out of 100

Distribution of grades & conditions for the grade:
1.0: 3 (S >= 85)
1.3: 0 (S >= 80)
1.7: 8 (S >= 70)
2.0: 5 (S >= 60)
2.3: 5 (S >= 50)
2.7: 7 (S >= 40)
5.0: 5 (X < 25)

Those who failed the exam (Grade 5.0) may re-sit the exam. If you want to do so, please use the registration form https://forms.gle/RSYNjzmyHHAtFv5t5 to register for Exam 2.

You may talk to @Joon or tutors (@Arnas, @Evgenii, @Balint) to take a look at the grading together.
We will have office hours on
- Monday 19 February 11:00 - 13:00
- Friday 23 February 09:30 - 11:30
at Maria-von-Linden-Str. 6 (AI Center Building) on Floor 1 (Seong Joon Oh's office).

After 23 February 2024 (23:59 CET), the Exam 1 grades will be finalised.

Best Wishes,
STAI
"""
    },
    "Exercise0_grade": {
        "subject": "[TML24/25] Exercise 0 grades",
        "body": """Dear {Preferred name},

Here are your grades for Exercise 0: {Ex0} / 100

Here's the breakdown.

- Ex0.1: {Ex0_1} / 20
    - Ex0.1a: {Ex0_1a} / 5
    - Ex0.1b: {Ex0_1b} / 10
    - Ex0.1c: {Ex0_1c} / 5
- Ex0.2: {Ex0_2} / 20
    - Ex0.2a: {Ex0_2a} / 5
    - Ex0.2b: {Ex0_2b} / 5
    - Ex0.2c: {Ex0_2c} / 5
    - Ex0.2d: {Ex0_2d} / 5
- Ex0.3: {Ex0_3} / 20
    - Ex0.3a: {Ex0_3a} / 5
    - Ex0.3b: {Ex0_3b} / 5
    - Ex0.3c: {Ex0_3c} / 5
    - Ex0.3d: {Ex0_3d} / 5
- Ex0.4: {Ex0_4} / 40
    - Ex0.4a: {Ex0_4a} / 10
    - Ex0.4b: {Ex0_4b} / 10
    - Ex0.4c: {Ex0_4c} / 20

Recap tutorial for the exercise will be held on Thursday 31 October 2024 at 14:00-16:00 at Maria-von-Linden-Str. 6, right after the lecture.

Best Wishes,
STAI
"""
    },
    "Exam1_final": {
        "subject": "[TML23/24] Final Exam 1 grades",
        "body": """Dear {Preferred name},

Here's the summary of your performance after the grade revisions. This is the final grade for Exam 1. 

Grade after Exam: {Exam1.final-grade-scheme4}
Exam 1 final score S = min(100, X + T): {Exam1.final-score} out of 100
Exam 1 score X = R x 5/9: {Exam1.score} out of 100
Exam 1 raw score R : {Exam1} out of 180
Exercise topup T = (E - 60) / 4: {Exercise-topup} out of 10
Exercise 1-3 average score E: {Exercise-scores} out of 100

Below is the breakdown of your Exam scores

B1 | Your score: {Exam1.B1} / 15 | Average score: 9.7
B2 | Your score: {Exam1.B2} / 15 | Average score: 11.3
B3 | Your score: {Exam1.B3} / 15 | Average score: 12.1
B4 | Your score: {Exam1.B4} / 15 | Average score: 9.6
B5 | Your score: {Exam1.B5} / 15 | Average score: 9.0
B6 | Your score: {Exam1.B6} / 15 | Average score: 4.4
A1 | Your score: {Exam1.A1} / 30 | Average score: 6.0
A2 | Your score: {Exam1.A2} / 30 | Average score: 16.7
A3 | Your score: {Exam1.A3} / 30 | Average score: 11.5
Sum: R = {Exam1} out of 180

Below is the breakdown of your exercise scores

Exercise 1 | Your score: {Ex1}
Exercise 2 | Your score: {Ex2}
Exercise 3 | Your score: {Ex3}
Sum: E = min(100, (Ex1 + Ex2 + Ex3) / 3) = {Exercise-scores} out of 100

Distribution of grades & conditions for the grade:
1.0: 3 (S >= 85)
1.3: 0 (S >= 80)
1.7: 8 (S >= 70)
2.0: 5 (S >= 60)
2.3: 5 (S >= 50)
2.7: 7 (S >= 40)
5.0: 5 (X < 25)

Those who failed the exam (Grade 5.0) may re-sit the exam. If you want to do so, please use the registration form https://forms.gle/RSYNjzmyHHAtFv5t5 to register for Exam 2.

Best Wishes,
STAI
"""
    },
    "Exam2_first": {
        "subject": "[TML23/24] Exam 2 grades", 
        "body": """Dear {Preferred name},

Here's the summary of your performance.

Grade after Exam: {Exam2.final-grade-scheme}
Exam 2 final score S = min(100, X + T): {Exam2.final-score} out of 100
Exam 2 score X = R x 5/9: {Exam2.score} out of 100
Exam 2 raw score R : {Exam2} out of 180
Exercise topup T = (E - 60) / 4: {Exercise-topup} out of 10
Exercise 1-3 average score E: {Exercise-scores} out of 100

Below is the breakdown of your Exam scores

B1 | Your score: {Exam2.B1} / 15 | Average score: 11.1
B2 | Your score: {Exam2.B2} / 15 | Average score: 7.0
B3 | Your score: {Exam2.B3} / 15 | Average score: 11.1
B4 | Your score: {Exam2.B4} / 15 | Average score: 8.4
B5 | Your score: {Exam2.B5} / 15 | Average score: 11.9
B6 | Your score: {Exam2.B6} / 15 | Average score: 8.5
A1 | Your score: {Exam2.A1} / 30 | Average score: 12.4
A2 | Your score: {Exam2.A2} / 30 | Average score: 8.4
A3 | Your score: {Exam2.A3} / 30 | Average score: 15.4
Sum: R = {Exam2} out of 180

Below is the breakdown of your exercise scores

Exercise 1 | Your score: {Ex1}
Exercise 2 | Your score: {Ex2}
Exercise 3 | Your score: {Ex3}
Sum: E = min(100, (Ex1 + Ex2 + Ex3) / 3) = {Exercise-scores} out of 100

Distribution of grades & conditions for the grade:
1.0: 1 (S >= 85)
1.3: 0 (S >= 80)
1.7: 0 (S >= 70)
2.0: 3 (S >= 60)
2.3: 3 (S >= 50)
2.7: 1 (S >= 40)

You may talk to @Joon or tutors (@Arnas, @Evgenii, @Balint) to take a look at the grading together.
We will have office hours on
- Thursday 4 April 13:00 - 14:00
- Monday 8 April 13:00 - 14:00
at Maria-von-Linden-Str. 6 (AI Center Building) on Floor 1 (Seong Joon Oh's office).

After 12 April 2024 (23:59 CET), the grades will be finalised.

Best Wishes,
STAI
"""
    },
    "Exam2_final": {
        "subject": "[TML23/24] Final Exam 2 grades",
        "body": """Dear {Preferred name},

Here's the summary of your performance after the grade revisions. This is the final grade for Exam 2. 

Grade after Exam: {Exam2.final-grade-scheme}
Exam 2 final score S = min(100, X + T): {Exam2.final-score} out of 100
Exam 2 score X = R x 5/9: {Exam2.score} out of 100
Exam 2 raw score R : {Exam2} out of 180
Exercise topup T = (E - 60) / 4: {Exercise-topup} out of 10
Exercise 1-3 average score E: {Exercise-scores} out of 100

Below is the breakdown of your Exam scores

B1 | Your score: {Exam2.B1} / 15 | Average score: 11.6
B2 | Your score: {Exam2.B2} / 15 | Average score: 7.0
B3 | Your score: {Exam2.B3} / 15 | Average score: 11.1
B4 | Your score: {Exam2.B4} / 15 | Average score: 8.4
B5 | Your score: {Exam2.B5} / 15 | Average score: 11.9
B6 | Your score: {Exam2.B6} / 15 | Average score: 8.5
A1 | Your score: {Exam2.A1} / 30 | Average score: 12.4
A2 | Your score: {Exam2.A2} / 30 | Average score: 8.4
A3 | Your score: {Exam2.A3} / 30 | Average score: 15.4
Sum: R = {Exam2} out of 180

Below is the breakdown of your exercise scores

Exercise 1 | Your score: {Ex1}
Exercise 2 | Your score: {Ex2}
Exercise 3 | Your score: {Ex3}
Sum: E = min(100, (Ex1 + Ex2 + Ex3) / 3) = {Exercise-scores} out of 100

Distribution of grades & conditions for the grade:
1.0: 1 (S >= 85)
1.3: 0 (S >= 80)
1.7: 0 (S >= 70)
2.0: 3 (S >= 60)
2.3: 4 (S >= 50)
2.7: 1 (S >= 40)

Best Wishes,
STAI
"""
    },
}
