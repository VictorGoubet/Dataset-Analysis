# PythonA4

SkillCraft is a dataset composed of a lot of features of over three thousand players playing at StarCraft 2 from bronze to professional gamers. In our study we will try to predict the league index of a player considering all his others features. Thus, it is a **classification problem.**

In our notebook we have followed the next steps:
- Data exploration 
- Data engeneering
- Modeling
- Optimisation (Tunning)
- Conclusion

We obtain finally a score of **0.45** due to a significant lack of data especially for the level 8 players.
A flask API is available to make predictions on your datas if you want.

To request a prediction from our API the input must be composed of all the columns (minus the leagueIndex) and no missing data with the appropriate datatype (float or int depending on the column). Finally, it must be a dictionnary.  

To use the API you have first to launch the server: ***./venv/Scripts/python.exe .\API\Server.py***
Then you have two choices:
- You can go on your favorite browser and go on ***localhost:5000/API_form***. You will have a form to fill and you will get a prediction !
- Or, if you want to use the API as a developper, you can make a request on the ***localhost:5000/API_request*** url. A example of request is given in the ***Request_API.py*** file, you can launch this request by executing ***./venv/Scripts/python.exe .\API\Request_API.py***.

You can read the powerpoint which resume quickly the main problems, steps and reflexions we encountered.
The notebook, being well commented, is self-sufficient. 
