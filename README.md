clientside
==========

Easy example CTF server that demonstrates clientside web exploitation. It also demonstrates Information Disclosure in the later levels.

Installation
------------

This is a typical rails app. Ensure you have the dependencies using `rvm` or similar:

-	Ruby 2.4.1
-	Bundler 1.15.3
-	Rails 5.1.2

Just ensure your ruby and bundler versions are up to date and run:

```sh
$ bundle install
$ rails s
```

This will start a server on 0.0.0.0:3000.

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

The developer is embarrassed at their mistake and wants to prove they can write their own code. They're learning JavaScript and are really enthusiastic about it, enough to write a login feature in JavaScript. The dev has also learned a small amount about hash functions, too...

-	What is encoding?

The developer is annoyed at you now, and has made their code "unreadable" for you to exploit! It's the same code, but now it's next to impossible to understand...

-	What is editing the DOM?

The developer realises that encoding isn't enough, so they decided to write a more complicated client-side login form too. The form finally stores a hashed password on the server; it won't be possible to "reverse engineer" the stored hash from the source code any longer.

**The first set of examples during the MISC session end here.**

-	What are robots and sitemaps?

The developer has launched the site! But of course, they don't know what they're doing. You don't know really what you can exploit if it's just a simple site like this. Why don't you try to look for the next level?

-	What is a view function?

So now the developer is editing the code they are copying But they don't seem to know exactly how HTML works. You know for a fact that the view function for the login handler just returns a valid login, no validation. So what's the password?

**Hint:** When the user visits a *url* path (or route), they call a *view function* related to that route. This view function can do processing with the HTTP object the client sends. You might want to look up "MVC" if you're interested.

**Hint:** Try logging in even if you know nothing.

-	What is Using Components with Known Vulnerabilities? Also, what is Improper Configuration?

The developer is using an outdated version of Flask, justifying themselves that things would break should they upgrade. This developer is also unsure about how Python and Flask works, leaving Debug set to True in production.

-	What is error handling?

The server now does all validation on the server. The developer has learned their lesson. But they seem to have left full error message displays on.

-	What are HTTP status codes?

The developer has learned their lesson and the errors returned are now much more general. Logging in might not be as easy as it was before. But you don't need to log in, you just need to find out which one of the following users actually exists on the server: andyh, maxw, alicec, bobl, daven, carols, eveo, frankz.

-	What is a time-based attack?

Now the developer has wised up and has almost had enough of you. Their last design has generalised 200-status error messages, and your job again is to find the user on the list that exists.

**Hint:** The password is hashed repeatedly (about 10,000 times) using an algorithm that is designed to make brute force cracking infeasible. Would this take a long time? Could we avoid this processing somehow unless it was completely necessary? *Should* we?
