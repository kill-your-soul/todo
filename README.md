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
            $env:token="TOKEN_TO_YOUR_BOT";
            ```
            ```Powershell
            $env:service_file="SERVICE_FILE_FOR_GOOGLE_API";
            ```
        
        + cmd:

            ```cmd
            set token=TOKEN_TO_YOUR_BOT
            ```
            ```cmd
            set service_file="SERVICE_FILE_FOR_GOOGLE_API"
            ```

    - For Linux, MacOS:

        + Bash:

            ```shell
            export token="TOKEN_TO_YOUR_BOT"
            ```
            ```shell
            export service_file="SERVICE_FILE_FOR_GOOGLE_API"
            ```

6. Run bot

    - For Windows:

        ```shell
        cd .\src\
        ```
        ```shell
        python .\bot.py
        ```

    - For Linux, MacOS:
    
        ```shell
        cd ./src/
        ```      
        ```shell
        python3 bot.py
        ```