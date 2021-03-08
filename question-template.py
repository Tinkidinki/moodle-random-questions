import random
import math

# Change the following variables as needed.
# Check the Moodle docs if you want to customize other variables such as penalty, etc.
#--------------------------------------------------
quiz_no = 1
category="System Test 1" #Must already exist on Moodle
question_name = "System Test Question 1"
default_grade = 1.00 
tolerance = 0.1
num_instances = 200 #Number of copies of the question with different numerical values. Possibly useful to first upload just 1, and then upload the rest.
#--------------------------------------------------

print(fr'''<?xml version="1.0" encoding="UTF-8"?>
<quiz>
<!-- question: 0  -->
  <question type="category">
    <category>
      <text>$course$/top/Quiz {quiz_no}/{category}</text>
    </category>
    <info format="moodle_auto_format">
      <text></text>
    </info>
    <idnumber></idnumber>
  </question>

''')


for i in range(num_instances):

    # Generate the random variables. Change the variables `question_text` and `answer` to hold the correct question and computed answer.
    # `question_text` can have latex. Enclose inline latex within \(...\)
    # and newline latex within \[...\]
    # Ensure that question_text is an f-string if you want to make variable substitutions as below.
    #--------------------------------------------------------
    a = round(random.random(), 2)
    b = round(math.sqrt(1-a*a), 2)
 
    question_text = fr"Consider the quantum state {a}|0> + {b}|1>. On measuring this state in the computational basis, what is the probability that the outcome is 0?"

    answer = a*a
    #----------------------------------------------------------
    

    print(fr''' <question type="{question_type}">
        <name>
          <text>{question_name}_{i}</text>
        </name>
        <questiontext format="html">
          <text><![CDATA[<p dir="ltr" style="text-align: left;">{question_text}</p>]]></text>
        </questiontext>
        <generalfeedback format="html">
          <text></text>
        </generalfeedback>
        <defaultgrade>{default_grade}</defaultgrade>
        <penalty>{penalty}</penalty>
        <hidden>0</hidden>
        <idnumber></idnumber>
        <answer fraction="100" format="moodle_auto_format">
          <text>{answer}</text>
          <feedback format="html">
            <text></text>
          </feedback>
          <tolerance>{tolerance}</tolerance>
        </answer>
        <unitgradingtype>0</unitgradingtype>
        <unitpenalty>0.1000000</unitpenalty>
        <showunits>3</showunits>
        <unitsleft>0</unitsleft>
      </question>''')
    print()

print('</quiz>')









