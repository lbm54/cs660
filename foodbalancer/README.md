# foodbalancer

FoodBalancer is a basic implementation of Nutri-Educ by me, Lee Martin, lbm13@uab.edu.  All of the relevant code in this project was written by me (found in the lib folder).  Balances meals around calories, macronutrients and whether there's a vegetable in a given meal.

## Installation

First of all, this project can be run from an ios or an android emulator by downloading Flutter and referencing your emulator with "flutter run <emulator_id>".

Please see the instructions, here: https://docs.flutter.dev/get-started/install/macos

Naturally, that might be too much work, so, alternatively, you can find an apk I've built under build/app/outputs/flutter-apk/app-release.apk.  Feel free to plug in your phone (or an emulator) and copy and paste that apk to install and launch.  Is that too much work?  I'm sorry it's a bit of a hassle.  Let me know if you ever need an ios build.

## Description of Files

Source code files are in the lib folder:

Models:
--This folder houses descriptions of what a balanced meal should look like (for comparison), what an individual food item should be (say bread or spaghetti) and then what a meal (or a combination of food items) should look like.  

Widgets:
--Various Ui components for rendering the models on the screen.

Food_list:
--A list of 20 items for use in building a meal.

Main:
--Builds the scaffolding for the UI and renders the widgets on the screen.

Meal Balancer:
--Houses the priority queue and does the algorithm's heavy lifting.

Again, if there's any questions or any other way I can offer assistance, please let me know!
