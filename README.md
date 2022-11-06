# SPM-Project-Code
SPM code 
github repo link website - https://github.com/sheryl-teo/SPM-Project-Code

# Running the code
1. Open the command terminal
2. Run ```npm install --save```
3. ```npm install --save @chakra-ui/react``` 
  a) ``` if there is react router dom error, run npm install react-router-dom --save.``` 
4. ```Run npm start```

# Fast api set up
## Executed using Command Prompt in VSCode Terminal 
1. go to spm_backend

```cd spm_backend```

2. create virtual environment

a) ```python -m venv venv```

b) ```venv\scripts\activate```

3. download required packages

```pip install -r requirements.txt```

4. run fastapi application

```uvicorn app:app --reload```
If you encounter any error after running this code, do check your directory

5. go to this link on your browser
###  `http://127.0.0.1:8000/docs#` 

# Integration Testing
### Click on the following link 'https://fastapi.tiangolo.com/tutorial/testing/' for more information regarding the commands for integration testing
1. Open the terminal
2. To use TestClient, first you install request with ``` pip install request ```
3. Import TestClient 
4. The functions can be identified as those with a name that starts with test_ , which is standard pytest conventions).
5. Next, you install pytest with ``` pip install pytest ``` if you have not done so
6. Run the test with ``` pytest ``` , it will detect the files and tests automatically, execute them, and report the results back to you.

# Circle Contineous Integration
1. Click on the following link 'https://app.circleci.com/launchpad/invited?return-to=https%3A%2F%2Fapp.circleci.com%2Fpipelines%2Fgithub%2Fsheryl-teo%2FSPM-Project-Code%3Finvite%3Dtrue&inviter=174a54c0-5833-44df-9375-54678647f3aa&invitePage=pipelines ' 
2. Sign in with your Github account and enter your Github Password.
3. Under the Project tab on the left side of the webpage, click on the SPM-Project_Code
4.  It should look like this at this point ![image](https://user-images.githubusercontent.com/65134007/200111748-404dd7ee-238d-4587-a3ad-2aea61b86a15.png)
5.  ![image](https://user-images.githubusercontent.com/65134007/200111825-5fa5d6ef-ad61-4687-9245-28c5451a8c51.png)

6.  ![image](https://user-images.githubusercontent.com/65134007/200111788-2e2a6295-24fa-422d-a03f-762bfe27950b.png)


