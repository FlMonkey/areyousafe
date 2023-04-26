# Are You Safe?
A website that allows a user to push a button that reports to their friends and family whether they are safe or not.

## The Issue:
Knowing if your family is safe or not is an issue that affects many people in today's world. From the war in Ukraine to just wanting to know if your family is safe when traveling abroad, getting this confirmation of saftey can be difficult. While you can use SMS it can be very repetitive to send your status to your family every couple of hours. Keeping family members updated on whether you are alive or not can be very difficult and/or inconvenient, the stress of not knowing if your family is safe is easily avoidable with a website that allows you to quickly and easily update your family on your safety.

## My Solution:
My solution to this issue is to create a user friendly, minimalistic website in order to provide the user the most simple and easy-to-use solution to this problem. In short, my website will allow users to simply choose between buttons, A ‘Safe’ button, an ‘injured’ button, and the ‘in danger’ button. Pressing these buttons updates the users status which their family members (and friends if they choose) have access too. To tackle this issue I will be using Python for the back end (using the flask module in order to allow it to communicate with the front end), HTML & CSS for the front end, and I will be using MongoDB for the database that stores the user's status along with their account. To initialize a user's account they simply need to choose a unique username and a password. The password will be encrypted using SHA256 in order to maintain high security. Once the user has an account they have the option to ‘create a family’ or to ‘join a family’. Once a family has been created, the ‘family’ generates a secret ID. In order to invite your friends and family to your ‘family’ you simply share the ID that has been generated for you. Then they click on the ‘join family’ and simply enter the password you shared with them. In case the person has multiple families or friend groups they can join multiple ‘families’. This code will use python modules such as Flask, Hashlib, MongoDB, random and potentially more. 

## Flowchart:

![Blank diagram-2](https://user-images.githubusercontent.com/75172047/226839995-26ac3c1a-7270-4f86-b5f0-2b6194084af2.png)

## Challenges that I encountered:

![image](https://user-images.githubusercontent.com/75172047/229055018-c46bdf1b-68e8-4132-81f0-f6cc4a58b9d3.png)

The part of the code that I found chalanging was setting up the MongoDB database. This wasn't inherintly dificult but it was something that I have never done before so it was a wonderfull learning experience for me. As well as learning about databases I also learned about classes which is something i've been wanting to learn for a while. To be specific about what the code above does, The get_user function searches through the database and sees if a user with the inputed username exists. The register function works as so: the first line is in charge of hashing the password that the user inputed in SHA256. The second line check if that user name already exists inside of the data base. If it doesn't exist then it creates a new user with their user name, password and it initializes their status. 

here is an image of the database interface

<img width="974" alt="Screenshot 2023-03-31 at 09 41 24" src="https://user-images.githubusercontent.com/75172047/229056133-8b5c5b48-db62-4f1e-91f5-2f712d736006.png">
