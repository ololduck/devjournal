# `devjournal`

*devjournal* is a online platform for the independent developer. It is mainly
a development log, but with some spice.

## Features

A list of (intended) features is worth a thousand words:

* A wiki for each project, with its own automatic sub-pages, such as:

    * Statistics: how much time has been spent on this project, on what
      (development, design...), which month has been more productive, and so on
    * Release history: where you can see when you released stuff
    * Commit history?
* Statistics
* Global release history
* And, of course, free creation of pages, on whatever subject you would like to
  write about.

## Idea (*pitch-my-app*)

The original idea of this project was to provide a *"framework"*, or a set of
guidelines, to write free software by passion, and keep the motivation to
maintain the written software.

The key concepts were **openness**, **transparency**, **feedback**, **documentation**

* **Openness**: I wanted to be able to show things, without being ashamed of
  it.
* **Transparency**: Most of the things public. The code, the documentation, the
  time spent, all that is public.
* **feedback**: I wanted to have metrics,  information about how my time was
  spent. That motivates me immensely.
* **Documentation**: I want it to be a place of documentation, a bit like
  pocoo.org is where every documentation created by the pocoo team.

With these concepts in mind, I wanted a software that could showcase all this,
and the projects behind.

So here's my attempt.

## Great, how do I use it?

Well, `devjournal` makes several assumptions about your workflow:

1. You should use git, with github. This project won't focus on using other
   VCS. However, in a second time, once this project is feature complete,
   support for other hosting solutions could be added.
2. In git, you use a development model where `master` is your release branch.
   All commits on this branch should be consistent. Someone who reads the log on
   the `master` branch should have a clear and concise view of what has been
   going on the project.

### How do we keep track of time?

Via a `.devjournal.yml` file, on the root of the repository.

Its syntax is as follows:

    timespent:
      - contact+trash@paulollivier.fr:
        - 15/02/2015: 2  # In hours
        - 14/02/2015: 1
      - otherdev@example.com:
        - 15/02/2015: 3

Sorry, american friends, all dates are in standard format, that is
"day/month/year".

This file may be commited in the repository, and should be updated with each
coding session.

## Keypoints

* Python
* Angular
* Wiki-like
* Custom behaviours for some pages
* showcase of your work.
* everything open (information wants to be free!)
