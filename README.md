# Password_Manager_With_Encryption
A password manager made in python that encrypts passwords using Fernet then saves them to a file. User can add, delete and view passwords.

******* HOW TO RUN *******
clone git repo
in the CLI, go to the folder with the python script

(IF PYTHON IS NOT INSTALLED) -> brew install python3 or scoop install python3 or sudo apt install python3

`pip3 install cryptography (This installs the fernet cryptography library)`
  
`pwd (Trust me we will need this later)`
  
`python3 Main.py`
  

You'll be greeted with this

`******* Password Manager *********`
  
`******* Version 1.0 **************`
  
`Add password(1)`
  
`Delete Password(2)`
  
`View Password(3)`
  
`Exit(4)`
  
`Select an option: `
  

Lets say you want to add a password -> 

Input the file path: 

Copy and paste the pwd output from earlier, then add /passwords.txt at the end


**** EXAMPLE *****

`******* Password Manager *********`
  
`******* Version 1.0 **************`
  
`Add password(1)`
  
`Delete Password(2)`
  
`View Password(3)`
  
`Exit(4)`
  
`Select an option: 1`
  
`Input the file path: GitHub/Password_Manager_With_Encryption/passwords.txt`
  
`Application: Apple`
  
`Password: SuperSecurePass123`
  
`Apple password saved. `
  
`Add password(1)`
  
`Delete Password(2)`
  
`View Password(3)`
  
`Exit(4)`
  
`Select an option: 3`
  
`Input the file path: GitHub/Password_Manager_With_Encryption/passwords.txt`
  

` ----- Saved Passwords ------`
  
`Apple : SuperSecurePass123`

What the passwords.txt file will look like, top three are unencrypted just for the example, the whole file should look like the bottom one.

`Apple : SuperSecurePass123 `
  
`Apple : SuperSecurePass123! `
  
` Google : NotSecurePass12332 `
  
`Steam : gAAAAABpO2DjliUV0_YZB038t5mCqH5GT5lFcg5z4sLZJT3yfdODz2UAoOkcPrG85SaGAcxMF1PXbY2x74ihIuD8OJlit01bpTfHLVkfPYj7NajIGhnHRyo= `
  
  

