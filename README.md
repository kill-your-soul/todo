# Todo Rest API

## Prerequisites

1. [Git](https://git-scm.com/)
2. [Python](https://python.org/) version 3.8 or later
3. pip or pip3


## Build locally
### Installing requirements
1. Clone this repo 

    ```shell
    git clone https://github.com/kill-your-soul/todo.git
    ```
2. Create virtual environment 
    
    - For Windows:

        ```Powershell
        python -m venv .venv
        ```

    - For Linux, MacOS:
    
        ```shell
        python3 -m venv .venv
        ```

3. Activate virtual environment

    - For Windows:
    
        ```Powershell
        .\.venv\Scripts\activate
        ```

    - For Linux, MacOS:

        ```shell
        source ./.venv/bin/activate
        ```

4. Install requirements

    - For Windows:

        ```shell
        pip install -r requirements.txt
        ```

    - For Linux, MacOS:
    
        ```shell
        pip3 install -r requirements.txt
        ```

1. Setting environment variables

    - For Windows:

        + Powershell:

            ```Powershell
            $env:SECRET_KEY="SECRET_KEY_TO_YOUR_DJANGO_APP";
            ```
        
        + cmd:

            ```cmd
            set SECRET_KEY=SECRET_KEY_TO_YOUR_DJANGO_APP
            ```

    - For Linux, MacOS:

        + Bash:

            ```shell
            export SECRET_KEY="SECRET_KEY_TO_YOUR_DJANGO_APP"
            ```


6. Run Django server

    - For Windows:

        ```shell
        python .\manage.py runserver
        ```

    - For Linux, MacOS:
    
        ```shell
        python3 manage.py runserver
        ```