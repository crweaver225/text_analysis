# text_analysis

The following project will compare two texts and analyze how similar they are. The program uses the cosine simularity algorithm, commonly used in machine learning to analyze the simularities and output a number between 0 and 1. The closer the output is to 1, the more similar the texts are. 

## How to run

There are two ways to run the program. 

### Way 1

This way requires Python 3.0 or higher on your machine to run. 

First, navigate to the Text_Analytics directory and open up the text1.txt and text2.txt files. These files will hold the two texts to compare. Add your first text to the text1.txt file and add your second text to the text2.txt file, then save both. Next, navigate to the Text_Analytics directory using a command line tool and run the following command: python text_analytics.py. 

The program will begin execution and will read from the two txt files that you edited above. When the program is complete, it will output the simularity score (between 0 and 1) onto the terminal. 


### Way 2

This way requires Python 3.0 or higher and Flask installed on your machine to run. Flask can be installed using the pip manager on a command line tool. 

Using a command line tool, navigate to the Text_Analytics directory and run the following command: python browser_text_analytics.py

The terminal should output something that lists a local url address like this: http://0.0.0.0:8000/

Copy this address and run it as a url in your browser. Your machine is now acting as a server for running the text analysis program. You should see two fields to add your two texts to compare. Simply add your texts and hit the "Compare text" button. A value should be listed below the button listing the simularity score. Repeat as needed. 
