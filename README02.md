[cd 01_running_tests]

# การรันและทดสอบหลายๆฟีเจอร์ไฟล์ในครั้งเดียว

behave สามารถค้นหาฟีเจอร์ไฟล์ในไดเร็คทอรี่ย่อยๆเพื่อทำการเทสได้
แต่มีเงื่อนไขคือโฟลเดอร์ 'steps' จะต้องอยู่ในไดเร็คทอรี่ปัจจุบันหรือไดเร็คทอรี่ก่อนหน้า(same or up level)

** Need to check **
หลักการเลือกไดเร็คทอรี่อ้างอิงในการ imports ไฟล์ของโปรแกรม python .py
- ถ้าไดเร็คทอรี่ที่เรียกใช้งาน behave มีไฟล์ .py อยู่ก็จะเลือกไดเร็คอรี่นั้นเป็นไดเร็คทอรี่อ้างอิงเลย
- ถ้าไม่มี .py จะไปค้นหาโฟลเดอร์ steps ใน level บน และใช้ level นั้นเป็นไดเร็คทอรี่อ้างอิงในการ imports ของ python

สามารถทำ package files แทนเพื่อเลี่ยงปัญหา path ที่จะใช้รันคำสั่ง behave

```
$ cd "Test Group"
Test Group$ behave
    Feature: Test Cases Group 1 # test_case_1.feature:2

      Scenario: Running Test Case 1                 # test_case_1.feature:4
        Given I am the main directory               # steps\steps.py:6
        Then I should also be in the main directory # steps\steps.py:10

    Feature: Test Cases Group 2 # test_case_2.feature:2

      Scenario: Running Test Case 2                 # test_case_2.feature:4
        Given I am the main directory               # steps\steps.py:6
        Then I should also be in the main directory # steps\steps.py:10

    Feature: testing login # login\login.feature:2

      Scenario: login test                             # login\login.feature:4
        Given I am in subdirectory of main directory   # steps\steps.py:14
        Then I am in a Python file in the subdirectory # login\login.py:3

    Feature: Negative test for login # login\login_negative\login_negative.feature:2

      Scenario: Negative testing of login      # login\login_negative\login_negative.feature:4
        Given I am negative test in main steps # steps\steps.py:18

    4 features passed, 0 failed, 0 skipped
    4 scenarios passed, 0 failed, 0 skipped
    7 steps passed, 0 failed, 0 skipped, 0 undefined
    Took 0m0.002s

```


ทดสอบเข้าไปรัน behave ในไดเร็คทอรี่ "Test Group"/login จะเกิดปัญหาการ import ขึ้น

```
Test Group/login$ behave
    Traceback (most recent call last):
      ...
      ...
      File "..\steps\steps.py", line 4, in <module>
        from login import login
    ImportError: cannot import name 'login'
    Exception ImportError: cannot import name 'login'
```

ทดสอบเข้าไปรัน behave ในไดเร็คทอรี่ "Test Group"/login/login_negative สามารถทำงานได้ปกติ

```
Test Group/login/login_negative$ behave
    Feature: Test Cases Group 1 # ..\..\test_case_1.feature:2

      Scenario: Running Test Case 1                 # ..\..\test_case_1.feature:4
        Given I am the main directory               # ..\..\steps\steps.py:6
        Then I should also be in the main directory # ..\..\steps\steps.py:10

    Feature: Test Cases Group 2 # ..\..\test_case_2.feature:2

      Scenario: Running Test Case 2                 # ..\..\test_case_2.feature:4
        Given I am the main directory               # ..\..\steps\steps.py:6
        Then I should also be in the main directory # ..\..\steps\steps.py:10

    Feature: testing login # ..\login.feature:2

      Scenario: login test                             # ..\login.feature:4
        Given I am in subdirectory of main directory   # ..\..\steps\steps.py:14
        Then I am in a Python file in the subdirectory # ..\login.py:3

    Feature: Negative test for login # login_negative.feature:2

      Scenario: Negative testing of login      # login_negative.feature:4
        Given I am negative test in main steps # ..\..\steps\steps.py:18

    4 features passed, 0 failed, 0 skipped
    4 scenarios passed, 0 failed, 0 skipped
    7 steps passed, 0 failed, 0 skipped, 0 undefined
    Took 0m0.002s
```


# การรันเทสเป็น Group
หากไม่ต้องการทอสอบทั้งหมดสามารถใช้ tags เพื่อรันเทสเป็นกรุ๊ปๆได้




