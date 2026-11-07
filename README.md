# Python for Security and Analytics

A practical Python learning repository focused on building programming foundations and applying them to **cybersecurity (especially SOC Analyst work)** and **data analytics**.

The goal is to move beyond syntax and develop the ability to write useful scripts, investigate security logs, work with datasets, automate repetitive tasks, and explain results clearly.

## Learning Goals

### Cybersecurity and SOC
- Read, parse, filter, and summarize security logs.
- Extract and validate indicators of compromise (IOCs), such as IP addresses, domains, URLs, and file hashes.
- Automate repetitive Level 1 SOC investigation tasks.
- Work with JSON, CSV, regular expressions, timestamps, and API responses.
- Build a foundation for detection engineering and security data analysis.

### Data Analytics
- Load and clean structured datasets.
- Work with CSV, JSON, NumPy, and Pandas.
- Perform exploratory data analysis (EDA).
- Calculate descriptive statistics and identify trends.
- Prepare data for visualization and reporting.

## Learning Roadmap

### Phase 1 — Python Fundamentals

| Lesson | Topic | Status |
|---|---|---|
| 01 | Introduction and print | Completed |
| 02 | Variables and data types | Completed |
| 03 | Type conversion and input | Completed |
| 04 | Operators | Completed |
| 05 | Conditional statements | Completed |
| 06 | Loops | Completed |
| 07 | Strings and string methods | Completed |
| 08 | Lists and list methods | Completed |
| 09 | Tuples, sets, and dictionaries | Completed |
| 10 | Functions | Completed |
| 11 | File handling | Completed |
| 12 | Exception handling | Completed |
| 13 | Modules and packages | Completed |
| 14 | Debugging and testing | Completed |

Lesson notes: [Phase-1-Python-Fundamentals](./Phase-1-Python-Fundamentals/).

### Phase 2 — Core Python and Data Handling
Planned topics include debugging and testing, common data formats (CSV and JSON), comprehensions, object-oriented programming, virtual environments, dependencies, project structure, dates, paths, and command-line arguments.

### Phase 3 — Python for SOC and Cybersecurity
Planned practical areas:
- Parsing Windows, Sysmon, Linux, firewall, and authentication logs
- Detecting repeated failed logins and suspicious activity
- IOC extraction and enrichment
- Phishing email analysis
- Regular expressions for security investigations
- JSON/CSV security reports and investigation summaries
- API integration and basic automation
- Mapping findings to relevant MITRE ATT&CK techniques where appropriate

Practical exercises will use clearly labelled simulated logs or reputable public datasets. No access to a dedicated Windows machine is assumed.

### Phase 4 — Python for Data Analytics
Planned practical areas:
- NumPy fundamentals
- Pandas for data loading, cleaning, transformation, and analysis
- Data quality checks and missing-value handling
- Exploratory data analysis (EDA)
- Statistics for analytics
- Data visualization
- Business and operational analysis projects

## Mini Projects

### Mini SOC Login Detection System

A Python project that processes simulated authentication events, counts failed login attempts by IP, skips malformed records, logs processing activity, and flags IPs that meet a configurable threshold. Includes automated tests using `unittest`.

Project files: [Mini-Projects/Mini-SOC-Login-Detection](./Mini-Projects/Mini-SOC-Login-Detection/).

- [Project README](./Mini-Projects/Mini-SOC-Login-Detection/README.md)
- [Detection script](./Mini-Projects/Mini-SOC-Login-Detection/login_detection.py)
- [Unit tests](./Mini-Projects/Mini-SOC-Login-Detection/test_login_detection.py)
- [Bug documentation](./Mini-Projects/Mini-SOC-Login-Detection/bug_documentation.md)

All login events are simulated. The threshold is a learning rule and does not prove malicious activity.

## Tools and Environment

- **Python 3**
- **Google Colab** for browser-based practice
- **Visual Studio Code** for local development when needed
- **Git and GitHub** for version control and maintaining a learning portfolio
- **Splunk, Wazuh, and Microsoft Sentinel** as complementary platforms for security-log practice
- **MySQL and Power BI** as complementary tools for analytics workflows

Examples are designed to be adaptable to Google Colab and a local Python environment. If a lesson requires a file, the instructions will explain how to create or upload it.

## Repository Structure

```text
Python-for-Security-And-Analytics/
├── README.md
├── Phase-1-Python-Fundamentals/
    ├── Lesson-01-Introduction-and-Print.md
    ├── Lesson-02-Variables-and-Data-Types.md
    ├── Lesson-03-Type-Conversion-and-Input.md
    ├── Lesson-04-Operators.md
    ├── Lesson-05-Conditional-Statements.md
    ├── Lesson-05-Exercise-Answers.md
    ├── Lesson-06-Loops.md
    ├── Lesson-07-Strings-and-String-Methods.md
    ├── Lesson-08-Lists-and-List-Methods.md
    ├── Lesson-09-Tuples-Sets-and-Dictionaries.md
    ├── Lesson-10-Functions-in-Python.md
    ├── Lesson-11-File-Handling-in-Python.md
    ├── Lesson-12-Exception-Handling-in-Python.md
    ├── Lesson-12-Exercise-Answers.md
    ├── Lesson-13-Modules-and-Packages-in-Python.md
    └── Lesson-14-Debugging-and-Testing-in-Python.md
└── Mini-Projects/
    └── Mini-SOC-Login-Detection/
        ├── README.md
        ├── login_detection.py
        ├── test_login_detection.py
        └── bug_documentation.md
```

The structure will expand as new phases and projects are added.

## How to Use This Repository

1. Follow the lessons in numerical order.
2. Read the concepts and code examples carefully.
3. Run the examples yourself in Google Colab or locally.
4. Attempt the exercises before checking any answer files.
5. Modify examples and test them with your own inputs.
6. Apply the concepts to security logs and analytics datasets as the roadmap progresses.

Clone the repository for local practice:

```bash
git clone https://github.com/Gaurav7260/Python-for-Security-And-Analytics.git
cd Python-for-Security-And-Analytics
```

## Practice and Project Principles

- **Hands-on first:** concepts should lead to working code and exercises.
- **Evidence-based security analysis:** preserve relevant event details and avoid conclusions unsupported by logs.
- **Data quality matters:** handle missing, malformed, and inconsistent data.
- **Safe datasets:** use simulated or reputable public datasets; do not include private, personal, or sensitive production logs.
- **Readable code:** use clear names, comments where useful, validation, and exception handling.
- **Document results:** explain what a script does, what its output means, and its limitations.

## Progress

**Current progress:** Phase 1 lessons 01–14 completed.

**Next topic:** Phase 2 — Core Python and Data Handling.

---

This is a continuously developing learning and project repository. Topics and practical projects will be added as the learning path progresses.
