# Overview

This is my first experiment with NoSQL cloud database. It is meant to be a simple sandbox prototype for testing python integration of Google's firebase.

This is a mock database for my wife's Etsy products.

I wrote this to practice working with cloud storage and manipulation.

[Software Demo Video](https://youtu.be/wLsL5hb8UdU)

# Cloud Database

This program is using Google's Firebase for it's cloud storage solution.

The Database is structured in a simple one table design. The table is "products" and each row has three attributes: name, price, and description.

# Development Environment

I developed this program using Visual Studio Code on Pop!_OS.

The program is written in python using google's firebase-admin module.

# Useful Websites

* [Official Firebase Documentation](https://firebase.google.com/docs/firestore/)

# Future Work

* Deleting rows from the DB (Bug fix)
* Modifying rows in the DB (Bug fix)
* A graphical UI would be better than text (Add Feature)