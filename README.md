webctf
======

Easy example CTF server that demonstrates clientside web exploitation. It also demonstrates Information Disclosure in the later levels.

Note
----

This repository is antiquated. There are much better CTF and exploitable web apps out there than this. Use this if you like, but it's very basic.

Installation
------------

This is a simple Flask app. Ensure you have the dependencies:

-	Python 2.5 or better
-	Flask

Just `python manage.py`. Set export WERKZEUG_DEBUG_PIN=off for one of the questions that requires it.

Troubleshooting
---------------

Versioning is important. Make sure everything is up to date and matches the versions exactly as above. Honestly, it should probably just work with any version of ruby later than 2.4.1, any version of rails after 5.1.2.

If not, `gem upgrade` is useful. Read the errors if there are any. This is a simple app that runs on sqlite3, it's not meant to be that complicated.

Information
-----------

There are, so far, ten levels. Hints are provided for each level if you really need it, but no solutions. Here are the levels:

-	What is HTML?

The developer is very new to web development, especially with security. They copied an example for a login form from the internet but didn't bother to change anything.

-	What is client-side validation?

The developer is embarrassed at their mistake and wants to prove they can write their own code. They're learning JavaScript and are really enthusiastic about it, enough to write a login feature in JavaScript. The dev has also learned a small amount about hash functions to make their password verification script "better."

-	What is a cookie?

The developer is using a cookie to prevent access to all of the levels. If you need to jump forward to skip to questions, feel free to edit the cookies to access them. This is a gimme, just try it out to access the next level.

-	What is encoding?

The developer is annoyed at you now, and has made their code "unreadable" for you to exploit! It's the same code, but now it's next to impossible to understand...

-	What is editing the DOM?

The developer realises that encoding isn't enough, so they decided to write a more complicated client-side login form too. The form finally stores a hashed password on the server; it won't be possible to "reverse engineer" the stored hash from the source code any longer.

**The first set of examples during the MISC session end here.**

-	What are robots and sitemaps?

The developer has launched the site! But of course, they don't know what they're doing. You don't know really what you can exploit if it's just a simple site like this. Why don't you try to look for the next level?

-	What is a view function?

So now the developer is editing the code they are copying But they don't seem to know exactly how HTML works. You know for a fact that the view function for the login handler just returns a valid login, no validation. So what's the password?

**Hint:** In MVC, when the user visits a *url* path (or route), they call a *view function* related to that route. This view function can do processing with the HTTP object the client sends. Flask is not MVC but the concepts are pretty general: there are views and each view is associated with a URL.

**Hint:** Try logging in even if you know nothing. If you still don't get it, read the source code.

-	What is Improper Configuration?

You notice that the developer has not bothered to turn Debug mode off. What's more, it doesn't seem the configuration is in order for their Flask app. Can you access the 'secret.txt' file? What else can you do?
