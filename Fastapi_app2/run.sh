#create a venv in vscode cmd
#open the command prompt:
  -->python -m venv test
  -->.\test\Scripts\activate

#pip install -r requirements.txt   :command to install requirements.txt file under test venv

#run the file:
--->uvicorn main:app --reload
--->python main.py


# #breakpoint()
    #----->apply the breakpoint and hit the endpoint in postman to enable pdb
    #commnand inside pdb:p,n,"q to quit"
