
## การแสดงผล (Displaying output)

ด้วยค่าคอนฟิกเริ่มต้น ในกรณีที่เทสผ่าน behave จะไม่แสดง output จาก print statements หรือ logging statements ออกมา แต่จะแสดงผลเฉพาะ scenario ที่ทดสอบไม่ผ่านเท่านั้น  
By default for tests that pass, Behave does not print the standard output from print statements or logging statements to console,. Only test fail, all the logging of failed scenario will show. 

สามารถบังคับให้แสดงผล output ทั้งหมดได้ด้วย argument: `--no-capture`
To force command line to printing all output then use argument: `--no-capture`

