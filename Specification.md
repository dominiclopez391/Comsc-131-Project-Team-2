Vidhyut



General Feature

Ability for users to sign-up, login/logout.

Be able to delete account

Memorizing: 

input a markdown file and ouput flash cards.

Share flash cards (add to their account)

Notes:

render markdown notes

convert markdown notes to pdf

share notes with other people (add to their account)

Time Management:

Create time blocks (using markdown)

Use pomodoro timer.

Chat:

Ability to create a chat room for your class.

Ability to invite other students to your chat room.

Problem Assist:

Ability to upload problems or questions from class with answers.

Other users can access and read class problems and answers.


####################

### Team 2 Project

Date: 

Product Name: 

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
