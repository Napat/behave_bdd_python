
## การแสดงผล (Displaying  log output)

ด้วยค่าคอนฟิกเริ่มต้น ในกรณีที่เทสผ่าน behave จะไม่แสดง output ใดๆจาก print statements หรือ logging statements แต่จะแสดงผลออกมาเฉพาะ scenario ที่ทดสอบไม่ผ่านเท่านั้น 
 
By default for tests that pass, Behave does not print the standard output from print statements or logging statements to console,. Only test fail, all the logging of failed scenario will show. 

สามารถบังคับให้แสดงผล output ทั้งหมดได้ด้วย argument: `--no-capture`

To force command line to printing all output then use argument: `--no-capture`


## การใช้งาน Given / When / Then / And / But

การใช้งานคีย์เวริด `Given / When / Then / And / But` ควรจะใช้ตามแบบแผนดังต่อไปนี้

Best practice guidelines to use `Given / When / Then / And / But` 

 - Given
 -- ใช้เพื่อประกาศเงื่อนไขเริ่มต้น 
 -- Used for precondition
 -- ตั้งค่าเริ่มต้นเพื่อจะทำงาน 
-- Set up actions
 -- ใช้ในกรณีใดๆที่ไม่มีการติดต่อสื่อสารระหว่าง application 
 -- No interaction with the application
 - When
 -- ใช้ในกรณีใดๆที่มีการติดต่อสื่อสารระหว่าง application 
 -- Interaction with the application
 -- กระทำบางสิ่ง 
-- Act on something
 - Then
 -- การยืนยันเงื่อนไขต่างๆ 
 -- Verification
 -- ใช้เมื่อคาดหวังผลใดๆ 
-- Expectation
 - And / But
 -- ใช้เป็นตัวแทนของคีย์เวริด Given / When / Then ในกรณีที่ต้องการเงื่อนไขที่มีความซับซ้อนขึ้น 
 -- Represent the preceding key word Given / When / Then

ตัวอย่างการใช้งานใน feature file 

Feature file example

```
# sample1.feature

Feature: Buy Big Mac

Scenario: User buy Big Mac using credit card

Given I am user 
Given I am logged in 
Given I have credit card 
When I search for a Big Mac 
When I add a Big Mac to my cart 
Then Big Mac price should be calculated 
Then the tax should be calculated 
Then the subtotal should be correct 
Then the total should be correct
```
สามารถเขียนใหม่ได้ดังนี้

Should be rewrite to
```
# sample2.feature

Feature: Buy Big Mac

Scenario: User buy Big Mac using credit card

Given I am user 
And I am logged in 
And I have credit card 
When I search for a Big Mac 
And I add a Big Mac to my cart 
Then Big Mac price should be calculated 
And the tax should be calculated 
And the subtotal should be correct 
And the total should be correct
```

Note
- ใช้เครื่องหมาย # เพื่อใส่ comment ใน feature file
- Use # sign in feature file to add comment

---------------------------

### Tutorial 02 display output, And keyword and python assert failed throwing 

```
$ cd 02_displaying_output
$ behave
Feature: Demo of displaying output 2 scenarios passed but 1 failed on console # displaying_output_demo.feature:2

  Scenario: A test that will PASS (stdout demo)  # displaying_output_demo.feature:4
    Given Open browser and go to home page       # steps\home_page.py:4
    When Click on "contact us"                   # steps\home_page.py:19
    Then Should see '123/456' address            # steps\home_page.py:28

  Scenario: A test with And(Given) that will PASS (stdout demo)  # displaying_output_demo.feature:10
    Given Open browser                                           # steps\home_page.py:10
    And Go to home page                                          # steps\home_page.py:14
    When Click on "contact us"                                   # steps\home_page.py:19
    Then Should see '123/456' address                            # steps\home_page.py:28

  Scenario: A test that will FAIL by assert (stdout demo)  # displaying_output_demo.feature:17
    Given Open browser                                     # steps\home_page.py:10
    And Go to home page                                    # steps\home_page.py:14
    When Click on "my account"                             # steps\home_page.py:23
    Then Should see 'Preferences' text                     # steps\home_page.py:32
      Assertion Failed: one is not same as two
      Captured stdout:
      Open browser
      Go to home page
      I am clicking on my account
      Should see preferences

Failing scenarios:
  displaying_output_demo.feature:17  A test that will FAIL by assert (stdout demo)

0 features passed, 1 failed, 0 skipped
2 scenarios passed, 1 failed, 0 skipped
10 steps passed, 1 failed, 0 skipped, 0 undefined
Took 0m0.004s
```

