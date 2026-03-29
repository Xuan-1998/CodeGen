# CodeGen

##  :beginner: About

## :zap: Usage

###  :electric_plug: Installation and Setup

- Environment variables:
    - Run the following commands to set up the necessary environment variables:
        - (Optional) `export RAPIDAPI_KEY='YOUR RAPID API KEY'`
        - `export OPENAI_API_KEY='YOUR OPENAI API KEY'`
        - (For Azure OPENAI) `export AZURE_OPENAI_ENDPOINT='xxx'`
        - (For Azure OPENAI) `export AZURE_OPENAI_API_KEY='xxx'`
        - (For Azure OPENAI) `export AZURE_OPENAI_DEPLOYMENT_NAME='xxx'`

- Install dependencies:
    - Run `pip install -r requirements.txt` to install the required packages.

- (Optional) [Install Ollama](https://ollama.com/download)

- (Optional) How to get a Rapid API key:
    - Follow the instructions provided in the [Rapid API documentation](https://github.com/judge0/judge0?tab=readme-ov-file#get-started) to obtain your Rapid API key.

###  :file_folder: File Structure

```bash
.
├── README.md
├── codeGen
│   ├── __init__.py
│   ├── codeGen.py
│   ├── dataset.py
│   ├── logs
│   │   ├── codeGen-INFO.log
│   │   ├── codeGen.log
│   ├── prompts.py
│   ├── results
│   │   └── tree_search
│   │       └── 63d94360
│   │           ├── code_0.py
│   │           ├── ...
│   │           ├── prob.json
│   │           └── test.json
│   ├── tests.py
│   └── utils
│       ├── __init__.py
│       ├── chatbot.py
│       ├── codeGen_logger.py
│       ├── coding.py
│       ├── logger.json
│       ├── oj_interactions.py
│       ├── problems.py
│       └── run_generated_code.py
├── data
│   ├── codechef
│   │   └── problems.jsonl
│   ├── codeforces
│   │   └── problems.jsonl
│   ├── ...
└── requirements.txt
```

- Run the codeGen: `python codeGen.py`
- Check the logs generated:
    - INFO level: `codeGen-INFO.log`
    - DEBUG level: `codeGen.log`
- Generated results: `results/{search func name}/{prob url hash}/*`
- Generate datasets: `dataset.py`
- Check the data generated: `data/{source}/problems.jsonl`
