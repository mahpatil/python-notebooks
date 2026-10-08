# Data, AI & ML Notebooks

> A hands-on collection of Jupyter notebooks exploring data, machine learning, AI, cloud services, and developer tools.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Format-Jupyter%20Notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)

Browse the notebooks by topic, open one in your preferred notebook environment, and experiment. Many notebooks are standalone explorations; check the notebook cells for any project-specific setup, packages, or credentials they require.

**[Browse the notebook index](#-notebook-index)** · **[Get started](#-get-started)**

## 🚀 Get started

### 0. Prerequisites

- Python 3.10 or later
- Jupyter support in your preferred IDE, or JupyterLab

### 1. Set up a virtual environment

Create and activate an environment from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyterlab
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Then start JupyterLab:

```bash
jupyter lab
```

You can also open the repository in an IDE with notebook support and select `.venv` as its Python interpreter. Install any additional dependencies referenced by the notebook you want to run.

### 2. Notebook setup
1. Install all pre-requisites. you can find a lot in the **init.ipynb** in the root folder
2. Most notebooks also require environment variables and use **dotenv** to load. create a .env file with the necessary variables.

## 📚 Notebook index

### AI, language models & document tools

| Notebook | Explore |
| --- | --- |
| [Bedrock summarization](bedrock/summarize.ipynb) | Summarization with Amazon Bedrock |
| [LightLLM chat](chat/lightllm.ipynb) | Chat with LightLLM |
| [Claude API requests](claude/001_requests.ipynb) | Claude requests |
| [Claude system prompts](claude/002_systemprompts.ipynb) | Claude system prompts |
| [Claude streaming](claude/003_streaming.ipynb) | Streaming responses |
| [LangChain PDF](pdf-gpt/langchain.ipynb) | PDF workflows with LangChain |
| [PDF-GPT](pdf-gpt/pdf-gpt.ipynb) | Ask questions about PDFs |
| [Resume processor](resume/resume_processor.ipynb) | Resume processing |

### Data science & analytics

| Notebook | Explore |
| --- | --- |
| [Boston dataset](linear-regression/boston-dataset.ipynb) | Linear regression |
| [Standard deviation](math/standard-dev.ipynb) | A statistical exploration |
| [Convert Excel files](excel/convert.ipynb) | Excel conversion |
| [Import XLS to Firestore](google-firestore/import-xls.ipynb) | Spreadsheet import to Firestore |
| [DuckDB 1.5 tests](duckdb/duckdb1.5-tests.ipynb) | DuckDB experiments |
| [JSON comparison](json-compare/compare-jsons.ipynb) | Compare JSON data |
| [Regex](text-comparison/regex.ipynb) | Regular expressions |
| [Text comparator](text-comparison/text-comparator.ipynb) | Compare text |

### COVID-19 & BigQuery

| Notebook | Explore |
| --- | --- |
| [COVID-19 overview](covid19-bigquery/covid_bigquery.ipynb) | COVID-19 data with BigQuery |
| [SIR model](covid19-bigquery/covid_sir_model.ipynb) | SIR model exploration |
| [Countries daily](covid19-bigquery/bigquery_countries_daily.ipynb) | Daily country data |
| [Countries detailed](covid19-bigquery/bigquery_countries_detailed.ipynb) | Detailed country data |
| [Countries forex](covid19-bigquery/bigquery_countries_forex.ipynb) | Foreign exchange data |
| [Countries summary](covid19-bigquery/bigquery_countries_summary.ipynb) | Country summaries |

### Cloud, databases & streaming

| Notebook | Explore |
| --- | --- |
| [Cassandra](cassandra/cassandra.ipynb) | Cassandra exploration |
| [Cassandra setup](cassandra/setup.ipynb) | Cassandra setup |
| [Cassandra to Kafka](cassandra/cassandra-to-kafka.ipynb) | Cassandra and Kafka |
| [Cleanup streams](cassandra/cleanup-streams.ipynb) | Stream cleanup |
| [Pinot GQL](cassandra/pinot-gql.ipynb) | Pinot and GQL |
| [Kafka 4 features](kafka/kafka4-features-test.ipynb) | Kafka 4 feature tests |

### Atlassian

| Notebook | Explore |
| --- | --- |
| [Bitbucket](atlassian/bitbucket.ipynb) | Bitbucket |
| [Bitbucket commits](atlassian/bitbucket_commits.ipynb) | Bitbucket commit data |
| [Jira and Confluence sample](atlassian/jira_confluence_sample.ipynb) | Jira and Confluence |
| [Jira epic list](atlassian/jira_epiclist.ipynb) | Jira epics |
| [Jira transition state](atlassian/jira_transitionstate.ipynb) | Jira issue transitions |

### Billing & finance

| Notebook | Explore |
| --- | --- |
| [AWS billing](billing/aws-billing.ipynb) | AWS billing data |
| [FreeAgent](billing/freeagent.ipynb) | FreeAgent |

### Diagrams & social data

| Notebook | Explore |
| --- | --- |
| [Diagrams](diagrams/root.ipynb) | Diagram generation |
| [Social media history](social-network-history/history.ipynb) | Social network history |
| [Social media letters](social-network-history/social_media_letters.ipynb) | Social media letters |

### Other

| Notebook | Explore |
| --- | --- |
| [Notebook starter](init.ipynb) | Start here |
| [Jev refund](jev/jev_refund.ipynb) | Refund-related exploration |

---

Made for learning by experimenting, one notebook at a time.
