
Vidhyut



General Feature

Ability for users to sign-up, login/logout.

Be able to delete account(vidhyut)

Memorizing: 

input a markdown file and ouput flash cards. (Brandon)

Share flash cards (add to their account) (Brandon)

Notes:

render markdown notes

convert markdown notes to pdf

share notes with other people (add to their account)(vidhyut)

Time Management:

(Dominic) Create time blocks (using markdown)

(Dominic) Use pomodoro timer.

Chat:

(Dominic) Ability to create a chat room for your class. 

(Dominic) Ability to invite other students to your chat room.

Problem Assist:

Ability to upload problems or questions from class with answers.(vidhyut)

Other users can access and read class problems and answers.(vidhyut)


####################

### Team 2 Project

Date: 

Product Name: StudyAid 

Problem Statement: As a student, it can be difficult to schedule and manage regular study sessions. This app helps to remedy that by
giving students a way to organize their notes, a way to create flash cards and practice memorization, time blocks to help organize
their weekly schedule, and create study-sessions with other students in their class.

Non-functional Requirements: The app must be easy and pleasing to use, and overall give the user a satisfying experience.

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

User is logged into account.

User 1 and 2 has sharing enabled (Privacy setting/visibility setting set to public on default?)

 
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
Shared notes (Where multiple people can edit)

### Alternate Postconditions
None.

