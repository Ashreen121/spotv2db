# SPOTv2 
A new and improved version of SPOT


## First go to the correct directory
First we need to go to the correct directory. This is the directory where the requirements.txt file is located. Use this command to do so.

```bash
cd spotv2db
```

## Activate the Virtual Environment
Use this command to activate the virtual environment

```bash
myvenv\Scripts\activate
```

## Download dependencies from the requirements.txt file 
The requirements.txt file contains all the dependencies required for the project to run. Therefore, it need to be installed using the command below.

```bash
pip install -r requirements.txt
```

## Now we can run the project
1. Go to the directory where the settings.py file is located. You can do this by running the command below. 

```bash
cd spotdb
```

2. Use this command to run the project.

```bash
py manage.py runserver
```
## Removing .pyc files (automatically generated files)
 Some reasons you may want to remove these files are because many of these files are generated upon the running of the project. To prevent the project folder from taking up too much space, you may want to remove all these files after some development on the project.  
 
 Use this command if you want to remove all .pyc files from the project. You must be in the root directory of the project if you want to delete all the .pyc files from the project repository. 

 ```bash
git rm *.pyc
```
If the command above doesn't work, try this one:

 ```bash
git rm -f *.pyc
```

## Developers
### Front-end team
Andras Szecsenyi, Chenzhuo Gou, Yi Xiang Ngam
### Back-end team
William Wood, Ashreen Kaur, Shawq Ahmed, Chaudhry Yaqub 

