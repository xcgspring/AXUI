.. _`AXUI introduce`:

=========================
AXUI introduce
=========================

:Page Status: Development
:Last Reviewed: 


AXUI philosophy
=========================

Due to varies of reasons, writing and maintaining UI automation is easy to turn into a time cost/unpleasant task,
and becomes hard to reach the predefined automation goal, and eventually UI automation is give up and leave people a bad impression

Let's have a summary of these reasons:

1. UI is hard for programming, UI is a good/direct interface for people, but not a good interface for programming. On the contrary, CLI is good for programming.
   controlling UI is basically a inter process communication, typical step is:
   
   1. find the target UI with some UI special features
   2. control process/scripts send a request to UI
   3. check for response/state
   
   Potential problems in upper steps:
   
   - UI features used to find UI is not user friendly, some feature is not visible or have no meaning
   - UI control request is not user friendly, like a mouse/keyboard/touch event
   - UI could have lots of responses under different condition (UI change/no change/long time response/hang/crash), need to handle all of them

2. Tool support for UI automation is not easy to use, especially for PC platform due to there is a lot of UI frameworks on PC
   mainly problems for varies UI automation tools:
   
   - Different tool has different flavour of the programming language/style
   - Some tool is not powerful enough, but has no way to extend the function
   - There are a lot of tools, need good experience to select a proper tool to use
   
   .. note::
   
    There are a lot of good tools emerging, like `selenium <https://github.com/SeleniumHQ/selenium>`_ for web test automation, `appium <https://github.com/appium>`_ for smartphone automation

3. Testers are lack of programming skills to make test scripts robust and easy to maintain.
   Testers are responsible for test design and test execution.
   Thus, testers might not have enough coding skills to use complex libraries.
   Automation tools should be easy for testers to use, let testers focus their energy to improve test cases
      
AXUI is a collection of solutions for these problems::

1. AXUI provide a plug-in mechanism for automation guy to extend support for different UI
2. AXUI provide an unified, easy to use python interface for use in test scripts
3. AXUI separate UI logic from test scripts, make test scripts more readable and easier to maintain
4. AXUI provide mechanism to handle auto met UI automation issues, like UI response time 

  









