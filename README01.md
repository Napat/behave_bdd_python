[cd 01_running_tests]

Activate virtualenv เพื่อให้สามารถใช้งานคำสั่ง behave ได้

Gitbash
```
$ source venv_gitbash/Scriptes/activate
```


ทดสอบเทสฟีเจอร์ไฟล์แบบทีละไฟล์
```
$ cd "Test Group"
Test Group$ behave test_case_1.feature

    Feature: Test Cases Group 1 # test_case_1.feature:2

      Scenario: Running Test Case 1                 # test_case_1.feature:4
        Given I am the main directory               # steps\steps.py:6
        Then I should also be in the main directory # steps\steps.py:10

    1 feature passed, 0 failed, 0 skipped
    1 scenario passed, 0 failed, 0 skipped
    2 steps passed, 0 failed, 0 skipped, 0 undefined
    Took 0m0.000s
```

สามารถสั่งให้ยกเลิกการซ่อน stdout ในกรณีที่ไม่มี failed test ได้ด้วยการเพิ่ม `--no-capture` 
```
Test Group$ behave test_case_1.feature --no-capture

    Feature: Test Cases Group 1 # test_case_1.feature:2

      Scenario: Running Test Case 1                 # test_case_1.feature:4
        Given I am the main directory               # steps\steps.py:6
    ----->1
        Then I should also be in the main directory # steps\steps.py:10
    ----->2

    1 feature passed, 0 failed, 0 skipped
    1 scenario passed, 0 failed, 0 skipped
    2 steps passed, 0 failed, 0 skipped, 0 undefined
    Took 0m0.003s
```

สำหรับผู้ใช้ mac อาจมีปัญหาในการแสดงผลได้ไม่ครบหรือถูกต้อง ให้เพิ่ม option `-f plain` เข้าไป
```
Test Group$ behave test_case_2.feature --no-capture -f plain

    Feature: Test Cases Group 2 # test_case_2.feature:2

      Scenario: Running Test Case 2                 # test_case_2.feature:4
        Given I am the main directory               # steps\steps.py:6
    ----->1
        Then I should also be in the main directory # steps\steps.py:10
    ----->2

    1 feature passed, 0 failed, 0 skipped
    1 scenario passed, 0 failed, 0 skipped
    2 steps passed, 0 failed, 0 skipped, 0 undefined
    Took 0m0.000s
```

ทดสอบรันเทสในโฟลเดอร์ login จะพบว่าโปรแกรม behave สามารถมองหาโฟลเดอร์ steps ได้ถูกต้อง
แต่จะเกิด error ขึ้นในโปรแกรม .py เนื่องจากการ include path จะขึ้นอยู่กับตำแหน่งที่รันคำสั่ง behave

```
Test Group$ cd login
Test Group/login$ Test Group/login$ behave login.feature

Exception ImportError: cannot import name 'login'
Traceback (most recent call last):
...
```

ให้ทดลองแก้ไขไฟล์ step.py ดังนี้
```
# Test Group/steps/step.py
from behave import given, when, then
import login
#from login import login
...
```

ทำการทดสอบอีกครั้ง error จะหายไป
```
Test Group/login$ behave login.feature
Feature: testing login # login.feature:2

  Scenario: login test                             # login.feature:4
    Given I am in subdirectory of main directory   # ..\steps\steps.py:14
    Then I am in a Python file in the subdirectory # login.py:3

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
2 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.001s
...
```

จะเห็นว่าควรจะออกแบบโครงสร้างหรือ tree ให้เรียบร้อยก่อนเพื่อประสิทธิภาพที่ดีในการใช้งาน
