----Lab 1-- assignment----

This assignment was about creating a grade evaluation system that calculates a student's final academic standing based on a pre-existing 
CSV file of course grades. It contains two files 1. grade-evaluator.py which is a python engine to evaluate student's grades. 
2.organizer.sh file which is a shell scripting file that checks if the grades.csv file exists, if it doesnt exist it creates it. and then after 
it archives it into archive/ folder and create a log file.

--how to run---

To run this program, if you don't already have a .csv file first run organizer.sh file to create a new .csv file to store students grades, to 
run it you can use:

	bash organizer.sh

to run the grade-evaluator.py file you can use:

	python3 grade-evaluator.py

after running the python file, it will check if there is any .csv file, and check if its empty, if the .csv file is empty it will tell you to 
record student's grades data, and then proceed accordingly.
