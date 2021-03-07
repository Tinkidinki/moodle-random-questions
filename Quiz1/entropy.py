import random
import math

# Change the following variables as needed.
# Check the Moodle docs if you want to customize other variables such as penalty, etc.
#--------------------------------------------------
quiz_no = 1
category="Entropy"
question_name = "Entropy"
default_grade = 1.00 
tolerance = 0.1
num_instances = 200 #Number of copies of the question with different numerical values. 
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
    #--------------------------------------------------------
    px1 = round(random.uniform(0.1, 0.4), 2)
    px2 = round(random.uniform(0.1, 0.4), 2)
    px3 = round(1 - (px1 + px2), 2)

    question_text = fr'''Let \(X\) be a random variable with outcomes \(x_1\), \(x_2\) and \(x_3\), which have the following probabilities:
    \[P(x_1) = {px1}\]
    \[P(x_2) = {px2}\]
    \[P(x_3) = {px3}\]
    What is the entropy of \(X\)? Use log to the base 2 when computing entropy.'''
 

    answer = - (px1*math.log2(px1) + px2*math.log2(px2) + px3*math.log2(px3))
    #----------------------------------------------------------
    

    print(fr''' <question type="numerical">
        <name>
          <text>{question_name}</text>
        </name>
        <questiontext format="html">
          <text><![CDATA[<p dir="ltr" style="text-align: left;">{question_text}</p>]]></text>
        </questiontext>
        <generalfeedback format="html">
          <text></text>
        </generalfeedback>
        <defaultgrade>{default_grade}</defaultgrade>
        <penalty>1.00</penalty>
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









