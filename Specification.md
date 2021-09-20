General Features:

Ability for users to sign-up, login/logout.

(done) Be able to delete account(vidhyut)

Public/private setting (Brandon)

Memorizing: 

input a markdown file and ouput flash cards. (Brandon)

Share flash cards (add to their account) (Brandon)

Categorize flashcards (Brandon)

Notes:

render markdown notes(Pranav)

convert markdown notes to pdf(Pranav)

(done) share notes with other people (add to their account)(vidhyut)

Time Management:

(done) (Dominic) Create time blocks (using markdown)

(done) (Dominic) Use pomodoro timer.

Chat:

(Dominic) Ability to create a chat room for your class. 

(Dominic) Ability to invite other students to your chat room.

Problem Assist:

(done) Ability to upload problems or questions from class with answers.(vidhyut) (made it a create class page use)

(done) Other users can access and read class problems and answers.(vidhyut) (made it a create tab for class page)


####################

### Team 2 Project

Date: 

Product Name: StudyAid 

Problem Statement: As a student, it can be difficult to schedule and manage regular study sessions. This app helps to remedy that by
giving students a way to organize their notes, a way to create flash cards and practice memorization, time blocks to help organize
their weekly schedule, and create study-sessions with other students in their class.

Non-functional Requirements: 

The app must be easy and pleasing to use, and overall give the user a satisfying experience.

The app must be usable in a browser like Firefox or Chrome.

The app must be easily navigable using a mouse and keyboard.

####################

# Use Case Description
Use Case Name: Ability for users to sign-up, login/logout.
## Summary

A login/logout system lets users access their personalized schedule and notes. 

## Actors

actor 1: User
Actor 2: Server
 
## Preconditions

* User already has an account created.
 
## Triggers

Users log themselves in.

## Primary Sequence

Step 1: User enters their username and password.
Step 2: User queries the server with their information.
Step 3: User's credentials are checked for validity by server (encryption?).
Step 4: User logs into their main page.

## Primary Postconditions

* User enters the main page of their account.

## Alternate Sequences

User does not have an account:
	Step 1: Display a warning that the username was not found, display a link to account creation page.
	Step 2: User creates an account with a username and password.
	Step 3: User gets redirected to login page.
	Step 4: User logs in with newly created account.

User entered their password incorrectly:
	Step 1: Display a warning that the password was incorrect.

### Alternate Trigger

Computer logs user in automatically (remember me feature)?

### Alternate Postconditions
	None.

##################

Use Case Name: Public/private setting

## Summary

This feature will allow the user to toggle between a public or private setting on their account. While
public, the user's account will be able to be searched. While private the user's account will not be able
to be searched. Account's will be set to default on creation.


## Actors

actor 1: Server

actor 2: User
 

## Preconditions

* First time user
 

## Triggers

Account creation.


## Primary Sequence

User creates an account an account and inputs their credentials.

Will be prompted to toggle their privacy setting.
 

## Primary Postconditions

* User enters the main page of their account.
 

## Alternate Sequences

User has already created an account and wants to toggle their privacy:

Enter user's main page.

Select options.

Select privacy and toggle accordingly.


### Alternate Trigger

User enters privacy settings.

### Alternate Postconditions

User enters the main page of their account.

####################

# Use Case Description

Use Case Name: Input a markdown file and output flash cards

## Summary

This feature will allow users to put their input into a markdown file and have it converted into an easy to read flash card.
 

## Actors

actor 1: User

actor 2: Server
 

## Preconditions

* User is logged into their account
* User is on the main page
 

## Triggers

User selects create a flash card.


## Primary Sequence

User selects create a flash card.

User puts their input into markdown file.

Markdown file is converted into easy to read flash card.

Flash card is saved to user's account.

User is prompted to create another flashcard or to quit.


## Primary Postconditions

* User enters the main page of their account.


## Alternate Sequences

User exceeds word count:
	1) Prompt user that their input exceeds the word count.
	2) (User shortens their input to appropriate size)
	3) Convert markdown file to flash card.
	4) Save flash card to account.


### Alternate Trigger
None.

### Alternate Postconditions
None.

####################

# Use Case Description

Use Case Name: Share flash cards (add to their account)

## Summary

A sharing system between different users for flash cards.
 

## Actors

actor 1: Server

actor 2: User 1 (Sharing)

actor 3: User 2 (Receiving)
 

## Preconditions

User 1 is logged into account.

User 1 is viewing flash cards.

User 1 and 2 have sharing enabled (Privacy setting/visibility setting set to public on default?)

 
## Triggers

User selects share notes feature.
 

## Primary Sequence

User 1 selects share notes feature.

User 1 is prompted with a search feature for other users. (Email/username/friend system)

System checks user 2's privacy/visibility settings and is set to public.

Notes are shared to user 2. (Via a "shared notes" folder)

User 2 is prompted that notes have been shared from user 1.
 

## Primary Postconditions

* User enters the main page of their account.


## Alternate Sequences

System checks user 2's privacy/visibility settings and they are set to private:
	1) User 2 will not appear in search user feature.
	2) User 1 will be prompted that user 2 could not be found.
	3) User 2 will have to find a public account or quit.

 
### Alternate Trigger
Shared notes (Where multiple people can edit?)

### Alternate Postconditions
None.


##################

# Use Case Description

Use Case Name: Categorize flashcards

## Summary

This feature will allow the user to section their flashcards into different categories.
 

## Actors

actor 1: Server

actor 2: User
 

## Preconditions

* User is logged in.

* User is on their main page.


## Triggers

User selects categorize flash cards button.

 
## Primary Sequence

User selects categorize flash cards button.

User is prompted to create category or to add to an existing one.
 
Flash card is saved to that category.


## Primary Postconditions

* User enters the main page of their account.
 

## Alternate Sequences

User tries to create an existing category:

User is prompted that such category already exist.

User is prompted to add to that existing category or input a different category.

 

### Alternate Trigger

User tries to create an existing category.


### Alternate Postconditions

User enters the main page of their account.

################

# Use Case Description
Use Case Name: Time Blocks
## Summary

Ability for users to create and view a weekly time block schedule. 

## Actors

actor 1: User
Actor 2: Server
 
## Preconditions

* User already has an account created.
 
## Triggers

User clicks on the "time block" button on the main page.

## Primary Sequence

Step 1: User clicks on the time blocks button.

Step 2: If the server has a time block on file for the user, it sends it to their client.

Step 3: User can view their weekly time block.


## Primary Postconditions

* User can view their time block.

## Alternate Sequences

User does not have a weekly time block:

Step 1: Prompt the user for a time block in a .md file, formatted so that the system can read the file.

Step 2: Store the time block .md on the server.

Step 3: Display the user's newly created time block.

User's time block is formatted incorrectly:

Display an error that the time block was not formatted correctly.

### Alternate Trigger

None.

### Alternate Postconditions

Display error message "time block not found." User continues to not have time block.


#################

# Use Case Description
Use Case Name: Pomodoro Timer
## Summary

Ability for users to utilize a pomodoro timer to help them manage study time based on certain intervals.

## Actors

actor 1: User
Actor 2: Server
 
## Preconditions

* User already has an account created.
 
## Triggers

User clicks on the "pomodoro timer" button on the main page.

## Primary Sequence

Step 1: User clicks on the "pomodoro timer" button.

Step 2: Server prompts the user for a set amount of time they would like to study for.

Step 3: User enters a time in hours and minutes.

Step 4: Server divides the amount of time into sets of 25 minutes of studying and 5 minutes of break. User can view the amount of time they have left for each stage.

Step 5: Once timer ends, website prompts user for another time.

## Primary Postconditions

* User can view the duration of their pomodoro timer.

## Alternate Sequences

User cancels their pomodoro timer early.

### Alternate Trigger

If pomodoro timer cancelled early, prompt the user for another pomodoro timer.

### Alternate Postconditions

None.

#########################

# Use Case Description
Use Case Name: Create a chatroom
## Summary

Users can create a chatroom specifically for their class which they can invite people to.
## Actors

actor 1: User
Actor 2: Server
Actor 3: Other users
 
## Preconditions

* User already has an account created.
 
## Triggers

User clicks on the "chatroom" button on the main page.

## Primary Sequence

Step 1: User clicks on the "chatroom" button.

Step 2: User clicks on "create a chatroom" in chatroom page.

Step 3: User is prompted for the room name and class number.

Step 4: Server checks if a chat room for that class was already created. If not, a chat room is created.

Step 5: User is sent to chat room.

Step 6: User is given a link which can be shared to other people to join the chat room.

## Primary Postconditions

* Chat room is created.

* shareable link to chat room is created.

## Alternate Sequences

Chat room is already created: display error and link to the already created chat room.

### Alternate Trigger

None.

### Alternate Postconditions

None.

###################

# Use Case Description
Use Case Name: Talk In Chatroom
## Summary

Users can join created chat rooms, where they have the ability to send and read messages to their peers.

## Actors

actor 1: User
Actor 2: Server
Actor 3: Other users
 
## Preconditions

* User already has an account created. Chat room has been created by the server.
 
## Triggers

User clicks on the "chatroom" button on the main page.

## Primary Sequence

Step 1: User clicks on the "chatroom" button.

Step 2: User sees a list of chat rooms they are a part of. The name of the room and class number are displayed for each room.

Step 3: User clicks to join the chat room.

Step 4: User sees previously made comments.

Step 5: User sees message prompt, types in a comment and submits it.

Step 6: Server saves comment in database of comments for that chatroom, and displays it in the chatroom.

Step 7: Other users can see the message left by the user.

## Primary Postconditions

* User can chat with other users.

## Alternate Sequences

None.

### Alternate Trigger

User goes to the link for the chat room.

### Alternate Postconditions

None.

###################

# Use Case Description
Rendor Markdown Notes
## Summary

This will allow user to create notes with basic features like Heading, Subheading, Bold, etc.

## Actors

Actor 1: User

Actor 2: Server
 
## Preconditions

The user is already looged into their account.
 
## Triggers

User selects "Create a Note" option on the main page.

## Primary Sequence

Step 1: User selects "Create a Note" option.

Step 2: User enters the content to the note according to his own needs.

Step 3: User saves the note to their account with a name of their choice. 

Step 4: User is asked before quitting if he wants to make another note or not.

## Primary Postconditions

User enters in a window with all the other notes taken/shared by them.

## Alternate Sequences

User exceeds word limit:

Step 1: Prompts the user that they are on the second page.

Step 2: User saves it as one markdown file.

### Alternate Trigger

None.

### Alternate Postconditions

None.

###################

# Use Case Description
Convert markdown into pdf files
## Summary

This option converts the markdown file into a PDF file and gives the user poptions to email it to themselves.

## Actors

Actor 1: User

Actor 2: Server
 
## Preconditions

The user is already looged into their account and the note already exists in their account.
 
## Triggers

The user selects "View Notes" option.

## Primary Sequence

Step 1: The user selects "View Notes" option.

Step 2: The user clicks on "Print"/"Email the PDF"/"Share as PDF" option.

Step 3: The download of the PDF starts/message is displayed "Email sent". 

## Primary Postconditions

User is prompted with with a copy of the PDF.

## Alternate Sequences

None.

### Alternate Trigger

None.

### Alternate Postconditions

None.

## Use Case Description

Use Case Name: Delete account

## Summary

An option for the user to terminate their account. 

## Actors

Actor 1: User
Actor 2: Server
 
## Preconditions

User already has an account created.
 
## Triggers

Users select “delete account” option

## Primary Sequence

Step 1: User opens “Account Settings”.

Step 2: User selects “Delete Account” setting.

Step 3: User accepts first delete message warning with delete option instead of option to suspend the account.

Step 4: User accepts “final deletion” warning.

## Primary Postconditions

User is redirected to main page of website

## Alternate Sequences

*User wants to suspend account temporarily:

Step 1: Display a warning that the account can be suspended instead of deletion in first          
delete message warning

Step 2: User selects suspend account option

Step 3: User selects suspend time period or indefinitely suspended option

Step 4: User is logged out and redirected to home page of website

*User does not want to delete account:

Step 1: User selects option “No” in first delete warning
Step 2: User selects option to suspend in first delete warning
Step 3: User selects option “No” in final delete warning

## Alternate Trigger

User selects delete account option in account settings

## Alternate Postconditions
Account is either suspended or nothing has changed.

##################

# Use Case Description

Use Case Name: Share Class Notes

## Summary

A sharing system between different users for a particular class.
 

## Actors

actor 1: User 1 (Sharing) 

actor 2: Server (Receiving)

actor 3: User 2 (Receiving)
 

## Preconditions

User 1 is logged into account.

User 1 has created notes and is viewing the notes

User 1 and 2 have sharing enabled (Privacy setting/Visibility setting set appropriately)

 
## Triggers

User selects share notes feature.
 
## Primary Sequence

Step 1: User 1 selects share notes feature.

Step 2: User 1 is prompted with a search feature for other users (Email/username/friend system).

Step 3: System checks user 2's privacy/visibility settings and is set to public.

Step 4: Notes are shared to user 2. (Via a "shared notes" folder)

Step 5: User 2 is prompted that notes have been shared from user 1.
 

## Primary Postconditions

User enters the notes page of their account and able to view who has access to the notes.


## Alternate Sequences

*System checks user 2's privacy/visibility settings and they are set to private:

Step 1: User 2 will not appear in search user feature.
Step 2: User 1 will be prompted that user 2 could not be found.
Step 3: User 2 will have to make changes to the appropriate setting or will not be able to receive.

*User wants to share notes to the class page:

Step 1: User 1 selects share notes option
Step 2: User selects option to share to class page instead of single/multiple selected users
Step 3: Server checks if Class page can receive files
Step 4: Notes are shared to class page

*User no longer wants to share a note with others

Step 1: User 1 changes privacy setting to private


 
### Alternate Trigger

For Sequence 1: User 1 selects User 2 to share notes with

For Sequence 2: User 1 selects option to share to class page

For Sequence 3: User changes privacy setting

### Alternate Postconditions

User is directed to view the notes they have on the account and their statuses.

##################

# Use Case Description

Use Case Name: Create a Class page

## Summary

Users can create a Class page specifically for their class which they can invite people to. Class page is where they upload files related to their class 

## Actors

Actor 1: User
Actor 2: Server
Actor 3: Other users
 
## Preconditions

User already has an account created.
User is in “Classes” page
 
## Triggers

User clicks on the "Classes" button on the main page.

## Primary Sequence

Step 1: User clicks on "create a Class" in Classes page.

Step 3: User is prompted for the room name and class number.

Step 4: Server checks if a class page for that class was already created and gives user option to join the class page or continue with creation.

Step 5: User is sent to newly created Class page.

Step 6: User is given a link which can be shared to other people to join the Class page based on selected visibility settings

## Primary Postconditions

Class page is created.

Shareable link to Class page is created.

## Alternate Sequences

*Class page is already created: 

Display similar class pages and number of users in each class page and links to the already created class pages.

### Alternate Trigger

User enters already created class information.

### Alternate Postconditions:

User is added to created class page.

###################

# Use Case Description

Use Case Name: Tabs in Class Page

## Summary

Users can create a separate tab (Frequently asked questions etc.) in their created class page

## Actors

Actor 1: User
Actor 2: Server

 
## Preconditions

*User already has an account created.
*User already created a class page
*User is in “Classes” page
 
## Triggers

User clicks on the "Create tab" button on the main class page.

## Primary Sequence

Step 1: User clicks on "Create tab" in Classes page.

Step 2: User is prompted to name the tab

Step 3: User is taken to new tab

Step 4: User can upload files, type in questions and answers related to the class in the newly created tab

## Primary Postconditions

New tab is created in the Class page.

## Alternate Sequences

*User enters name for the tab that is identical to another tab that is already created:

Step 1: Display message that another tab with the same name already exists and if the user still wants to continue
Step 2: User can either continue with creation or exit process

### Alternate Trigger

User enters already created tab name.

### Alternate Postconditions:

User is taken to tab.

###################

