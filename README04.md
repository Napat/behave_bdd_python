## การส่งต่อค่าตัวแปรจาก feature ไฟล์ไปยัง step file (Passing parameters to Steps)

```
<similar feature>
Given I am at home page
Given I am at shop page

When I add 2 items to cart
When I add 4 items to cart

Then user should receive discount
Then user should not receive the discount 
```

การเชียน feature ที่คล้ายๆกันสามารถใช้วิธีการส่งค่าพารามิเตอร์เข้าไปแทนที่จะเขียนหลายๆฟังก์ชันได้

To support many similar features can reuse the same step function 
by passing values to be parameters for the step functions.    

The default use the 'parse' module we get with Python.
The default parser is similar to string formatting(Python 3 style)

```
[Python 3 style]
>>> my_lang='Thai'
>>> str='I love {lang} language'.format(lang=my_lang)
>>> print(str)
I love Thai language
```


ข้อแนะนำ *Best practice* 

ควรใส่เครื่องหมาย single quotes หรือ double quotes คลุมค่าพารามิเตอร์ไว้ 
โดยทีมควรจะตกลงกันว่าจะเลือกใช้ quote แบบใดให้เรียบร้อย(เพื่อป้องกันปัญหาในกรณีเมื่อต้องรับค่าที่ไม่ใช่ตัวแปร string จะต้องนำพารามิเตอร์ที่ได้ไปสั่ง convert ก่อน) 
เช่น หากเลือกใช้ double quotes สามารถเขียนได้ดังนี้ `"param"`

To put the parameter in single quotes `'param'` or double quotes `"param"`, Team should select only one quote type, I am choosing double quotes style (`"param"`). 

ตัวอย่างการทดสอบฟีเจอร์การเลือกภาษาสามารถทำได้ดังนี้

Let say we have this step and we want to use different language based in the test cases.

```
Given I choose "English" version of the site
Given I choose "Thai" version of the site
```

ในส่วนของ step file จะใช้เครื่องหมาย curly braces ล้อมรอบส่วนที่เป็นพารามิเตอร์เอาไว้ `{param}`
โดยไม่ต้องสนใจว่าใน feautre file จะใช้ single qutes, double quotes หรือไม่ใช้เลยก็สามารถใช้งานได้เหมือนกัน
type ของ param ที่ได้ใน python3 จะเป็น `class 'str' และเป็น `unicode` ใน python2

Then we could define the step file using curly braces between the parameters `{param}`. 
There is no need to worrie about using single quotes, double quotes or nothing. 
Type of paramerters for python3 is `class 'str'` and be `unicode` for python2

```
@given('I choose {lang} version of the site')
def choose_lang_site(context, lang):
    print("Input lang = {}".format(lang))
    print("Input type = {}".format(lang))
    ... condition to which language site to open ...
```

ถ้าใส่ quote ชนิดใดๆเข้าไปใน step file ใน feature file จะต้องใช้ quote ชนิดนั้นๆเข้าไปด้วยเช่น

But if any quote are used in step file then need to input the same quote type in feature.

`
@given('I choose "{lang}" version of the site')
`

จะต้องเขียน feature file ด้สน double quotes ดังนี้

then double quotes require,

`
Given I choose "Thai" version of the site
`

### Tutorial 03 passing the step parameters

```
$ cd 03_step_parameters
$ behave --no-capture
Feature: Try passing parameters from feature to step file # step_parameters.fe      ature:3

  Scenario: Passing step parameters        # step_parameters.feature:5
    Given I have a new 'iPad' in my cart   # steps\definitions.py:5
Add item: 'iPad'
    And I have a new "Keyboard" in my cart # steps\definitions.py:5
Add item: "Keyboard"
    When I click on "Next"                 # steps\definitions.py:21
I am clicking the button: "Next"
    And I click on "FINISH"                # steps\definitions.py:21
I am clicking the button: "FINISH"
    Then I should see "Success"            # steps\definitions.py:26
Item added!
Checking if I see the 'success' text
PASS. I see the 'success' text

  Scenario: Add 10 participants in the call  # step_parameters.feature:13
    Given I brought "5" "lottery tickets"    # steps\definitions.py:10
The number of participants is: 5
--------------------
Original "lottery tickets" quantity 5 type <class 'str'>
Original "lottery tickets" quantity 5 type <class 'int'>
--------------------

1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
6 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.001s
```
---------------------------






