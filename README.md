# FastAPI
# Always use Command Prompt as a Terminal to run the commands in vscode

# Tutorial Link:--->FastAPI
       # ---->##### 4:02:55 hr ----> Link:https://www.youtube.com/watch?v=7t2alSnE2-I&ab_channel=Bitfumes

# Steps to run the command: 


1.) C:\Users\AmanKumar\OneDrive - GyanSys Inc\Desktop\Github\FastAPI>cd Fastapi_app2

# activate the env-variable(fastapi-env)
2.) C:\Users\AmanKumar\OneDrive - GyanSys Inc\Desktop\Github\FastAPI\Fastapi_app2>fastapi-env\Scripts\activate

3.) C:\Users\AmanKumar\OneDrive - GyanSys Inc\Desktop\Github\FastAPI\Fastapi_app2>cd blog

# now we are under virtual env then we can run the fastapi app using below command
(fastapi-env) C:\Users\AmanKumar\OneDrive - GyanSys Inc\Desktop\Github\FastAPI\Fastapi_app2\blog>uvicorn main:app --reload


# list down username ans password of git
       # write the below command in git bash
            ---> $ git config --list
            ---> $ git config user.name
            ---> $ git config user.email

# using below command to set project attributes:
     --->$ git init        :.git file will be created in file location
     ---->$ git add .  "or"  git add <filename>
     ---->$ git commit -m "msg"
     ----->git pull origin dev3.5
     ------>git push origin aman-dev


# routing is used to make a path and return something
     --->but in our case we were writing all the logic inside 'blog/routers/blog.py' or 'blog/routers/user.py'
     --->to overcome this issue we are exporting our logic in repository folder by creating 2 folders blog.py and user.py in order to write the logic(function) inside it.