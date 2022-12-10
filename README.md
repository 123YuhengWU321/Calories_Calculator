# Calories_Calculator
This is a calories calculator made in April 2022

Our project has two different modes, one is a calories calculator, other being a CV based check out station. For the calories calculator, the user places a fruit/vegetable on the platform, the calories of the fruit is displayed one the website, associated LCD, and history is stored in a file.
The second function is a self checkout, the user takes turns placing products on the platform, the system identifies the product type, records and calculates the price and finally provides a receipt for the purchase.
The project have the following key features

## Modes: 
the system can be on, off or in sleep mode to save power
on: system is fully functional and parse/transfer data with highest speed possible. The system is in this state by default
sleep(save power): system is partially functional with only weighting enabled. The system enters this state when it is idle for too long (~20sec without software, hardware, or weight change on scale). The system leaves this state when there is weight change on scale or hardware interaction.
off: system is off, user needs to turn on power switch to start system. In this mode only previous data is recorded and is available for download
Smart object identification: the object identification supports items in all angles, multiple items of the same type, item in a near-clear bag or container. This means the user can drop an entire bag of objects on the platform and expect the correct result to be returned. This is enabled as well as collecting and labelling most of the data ourselves, so we can choose any angle/count for the best training result.
Website: the hardware is connected to a vm where the website is running on, this enables hardware interaction between the hardware and website (read, write). The website also supports downloading data as text files (history/receipt). 
Multiple station support: multiple stations are supported in parallel. This means multiple users can use different “check out” stations at the same time. All of the features include scale number, file download, signals are independent, so everything can be controlled in parallel on different devices/windows. (Due to the price of pi we are only able to have one physical device, however each device is identical. Code for each machine is uploaded on github)
System casing:  The system is contained in the casing so no cables are exposed. It is smoothly crafted for the best user experience and appearance.
Indicator light: two led lights indicate the state of the system. The red LED indicates system status (LED on= system on, LED flash=system sleep, LED off=system off). The green LED indicates server interaction, everytime interaction is made, a flash is made (actually green being on means the interaction is happening right now).
LCD screen display: A LCD display is connected to the system which is used to display information such as the price or mass of each item. The LCD screen could be used to show the system's status (running, sleeping, logged out, etc).
RFID module: A RFID module is included in the system to increase flexibility. It is able to recognize registered RFID tags which are stored in the VM. When the system is used as a self checkout machine. This module could be used as an identity verification check during the process where loyalty cards could be swiped to identify different users.
