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

If any quote are used in step file then need to input the same quote type in feature.

`
@given('I choose "{lang}" version of the site')
`

จะต้องเขียน feature file ด้วย double quotes ดังนี้

Then double quotes require,

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


## การส่งข้อมูลระหว่าง step ด้วย `context` (Share data in scenario level using `context`)

โดยพื้นฐานของ Python สามารถใช้วิธีประกาศตัวแปรแบบ global เพื่อเก็บตัวแปรได้ ซึ่งวิธีดังกล่าวอาจจะใช้ได้ดีเมื่อมีเขียนไฟล์ .py แค่ไฟล์เดียว

แต่เมื่อต้องทำงานกับ .py หลายๆไฟล์หรือเริ่มเขียนโปรแกรมที่มีความซับซ้อนมากขึ้น วิธีดังกล่าวจะไม่มีประสิทธิภาพ 
ดังนั้นจึงไม่ใช่วิธีที่ดี (not good practice) ที่จะประกาศตัวแปร global เพื่อส่งค่าระหว่างแต่ละ step

Sharing information between steps could use global variable thats are only good in one file.

Declare global variables then not good practice to coding.
So Behave then provides a feature that allows us to do just that. 

เนื่องจากออปเจค `context` ซึ่งเป็นอาร์กิวเมนต์ตัวแรกของทุกๆฟังก์ชันของ behave จะถูกสร้างขึ้นและใช้ร่วมกันในแต่ละ scenario หนึ่งๆ 
ดังนั้นเราสามารถใช้เก็บและส่งค่าต่างๆไปยัง step อื่นๆ ใน scenario หนึ่งๆได้
แต่จะไม่สามารถส่งค่าข้าม scenario ผ่าน `context` ได้นะ

Argiment `context` is an instance of a class and is used to store contextual data during the **Scenario level** test run. 
Difference scenario is NOT sharing context object.

ตัวอย่างการเก็บข้อมูลที่ต้องการลงใน `context`

Below are the examples to store data value, 

```
context.name='Napat Rc'
context.email='napat_joe@hotmail.com'
```

Causion:

เนื่องจาก context จะมี attributes เก็บข้อมูลพื้นฐานที่ใช้สำหรับ behave อยู่ด้วย ดังนั้นห้ามใช้ชื่อตัวแปรที่ถูกใช้ไปแล้วเช่น  
 
Context is storing lots of information for running the test. Avoid such keywords refer to API documentation for example,

`context.feature`, `context.scenario`

สามารถดูชื่อ attributes ที่ behave ใช้งานอยู่แล้วได้จาก  (List of bahave Context attributes) 
https://pythonhosted.org/behave/api.html#detecting-that-user-code-overwrites-behave-context-attributes


### Tutorial 04 Share data in scenario level using `context`

```
$ behave --no-capture
Feature: Sharing data scenario level using context # sharingdata_scenariolevel.feature:4

  Scenario: Process refund by order id      # sharingdata_scenariolevel.feature:6
    Given I find order id from database     # steps\steps_sharingdata.py:5
Finding an order from the database....
Found an orders. Order number: 12481632
    When I issue a refund for that order id # steps\steps_sharingdata.py:14
Trying to issue a refund for order number: 12481632
Refund
    Then process payment to user            # steps\steps_sharingdata.py:26
Payment successfully processed
Payment is for refund of order number: 12481632

  Scenario: Refund should fail on a refunded item  # sharingdata_scenariolevel.feature:12
    When I issue a refund on the same order        # steps\steps_sharingdata.py:20
      Traceback (most recent call last):
        File "d:\workdir\learnbddgherkinwithpython\behave_bdd_python_git\venv_gitbash\lib\site-packages\behave\model.py", line 1456, in run
          match.run(runner.context)
        File "d:\workdir\learnbddgherkinwithpython\behave_bdd_python_git\venv_gitbash\lib\site-packages\behave\model.py", line 1903, in run
          self.func(context, *args, **kwargs)
        File "steps\steps_sharingdata.py", line 23, in issue_repeat_refund
          print("Trying to issue refund on same order: {}".format(context.order_id))
        File "d:\workdir\learnbddgherkinwithpython\behave_bdd_python_git\venv_gitbash\lib\site-packages\behave\runner.py", line 214, in __getattr__
          raise AttributeError(msg)
      AttributeError: 'Context' object has no attribute 'order_id'

    Then refund process will fail                  # None

Failing scenarios:
  sharingdata_scenariolevel.feature:12  Refund should fail on a refunded item

0 features passed, 1 failed, 0 skipped
1 scenario passed, 1 failed, 0 skipped
3 steps passed, 1 failed, 1 skipped, 0 undefined
Took 0m0.001s
```
