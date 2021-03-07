# anti-plag

This is a small script for the creation of questions with the same template but varying numerical values for quizzes on Moodle. This is for numerical type questions only, and currently does not support MCQ, etc. If randomization is not involved, it might be easier to add a question directly on Moodle rather than importing a file.  

# Create a random numerical question
1. First create a category for the question on Moodle. 
    - Go to the course page, and click the gear on the right.
    - Select More -> Question Bank -> Categories
    - Select Quiz <Quiz no.> in the drop down box.
    - Type the name of the category (This can also be the name of the question).

2. Make a copy of `question-template.py`
3. Edit the file following instructions in the file.
4. Run `python3 question-template.py > file.xml`
5. Select Question Bank -> Import on Moodle
6. Select Moodle XML file format and upload file. 

# Create a quiz that includes the random numerical question
1. Create a quiz on Activity page.
2. Click on the quiz -> Edit quiz
3. Add -> a random question
4. Pick the category

