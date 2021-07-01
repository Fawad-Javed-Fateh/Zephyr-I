# Zephyr-I

## Introduction :
This is a GUI-based script developed completely in python. It follows the methods present in the book ***Numerical Anaylysis 9th Edition (Richard L.Burden and J.douglas Faire)*** in order to numerically approximate roots, integrals , derivatives and differential equations which is far more efficient than anaylytically solving for answers. 

## Salient Features :
1. GUI based design using pyQt5 inorder to streamline the UX for everytype of user
2. GUI controls streamlined and well labelled in order to smooth user experience and avoid confusion
3. Decimal Control Option added to allow for user to control accuracy and precision of his calculations, in short allowuing a more dynaminc experience for the user 
4. Methods distributed according to chapters in the mentioned textbook to allow easy access and a central menu for the user 
5. Methods listed under every chapter description to accomondate for those who arent familiar with the textbook used a guideline for design 
6. Methods such as interpolation, differentiation and integration as well as differential eqauations allow for manual points input and function input with starting points as well,catering for both type of scenarios
7. Interpolation Tables implemented using pyQt5's table widget to allow for a more comprehensive experience and one stop solution 
8. Differential Equation Tables also implemented using pyQt5's table widget to show every approximated particular solution
9. Values used for Open Newton Coates and Closed Newton Coates also displayed using the table Widget 
10. Every possible degree of polynomial answer calculated and displayed in Interpolation methods to allow for the user to verify his results for any **safe and reachable** degree he wants

## Setup And Running Instructions :

### PreRequisite Libraries:
The following libraries are required for the script to run :
1. pyQt5
2. SymPy
3. NumPy
4. Math
5. Array
6. Tkinter(not a necessity but would be required on older versions of python)
These libraries can be installed by using the following command on the powershell command line or the bash shell:
>pip install <libraryName>
 
### Running Instructions:
 After making sure that the required libraries are installed and presnet in the local machine, simply clone the repository into the machine, navigate to the **MainFiles** folder and type in the following command :
 >oython UICode.py
 
 
