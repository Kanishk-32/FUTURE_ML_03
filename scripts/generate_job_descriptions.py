"""
generate_job_descriptions.py
----------------------------
Creates a curated job_descriptions.csv for the resume screening pipeline.

Run:
    python scripts/generate_job_descriptions.py

Output:
    data/job_descriptions.csv
"""

import csv
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "job_descriptions.csv")

# ────────────────────────────────────────────────────────────────
# Each entry:  (job_id, job_title, company, category, description)
# ────────────────────────────────────────────────────────────────
JOB_DATA = [
    # ── Software Development ──────────────────────────────────
    (
        1001,
        "Senior Software Engineer",
        "TechNova Solutions",
        "INFORMATION-TECHNOLOGY",
        (
            "We are looking for a Senior Software Engineer to design and build scalable "
            "backend services. You will architect microservices, mentor junior engineers, "
            "and drive best practices across the team.\n\n"
            "Responsibilities:\n"
            "• Design, develop, and maintain high-quality software using Python and Java\n"
            "• Build RESTful APIs and microservices with Flask, FastAPI, or Spring Boot\n"
            "• Write clean, well-tested code with comprehensive unit and integration tests\n"
            "• Participate in code reviews and provide constructive feedback\n"
            "• Collaborate with product managers and designers to define features\n"
            "• Optimize application performance and troubleshoot production issues\n\n"
            "Requirements:\n"
            "• 5+ years of professional software development experience\n"
            "• Proficiency in Python and/or Java\n"
            "• Experience with SQL databases (PostgreSQL, MySQL) and NoSQL (MongoDB)\n"
            "• Familiarity with Docker, Kubernetes, and CI/CD pipelines\n"
            "• Strong understanding of data structures, algorithms, and design patterns\n"
            "• Experience with cloud platforms (AWS, Azure, or GCP)\n"
            "• Excellent communication and teamwork skills\n\n"
            "Nice to have: Experience with TypeScript, React.js, or Node.js"
        ),
    ),
    (
        1002,
        "Junior Software Developer",
        "CodeCraft Inc.",
        "INFORMATION-TECHNOLOGY",
        (
            "CodeCraft Inc. is hiring a Junior Software Developer to join our agile team. "
            "This is a great opportunity for recent graduates looking to launch their career.\n\n"
            "Responsibilities:\n"
            "• Write and maintain code in Python and JavaScript\n"
            "• Assist in building and testing web applications using React.js and Node.js\n"
            "• Fix bugs and improve existing features under senior guidance\n"
            "• Participate in daily stand-ups and sprint planning\n"
            "• Write documentation for new features and APIs\n\n"
            "Requirements:\n"
            "• Bachelor's degree in Computer Science or related field\n"
            "• Basic understanding of Python, JavaScript, HTML, and CSS\n"
            "• Familiarity with Git version control\n"
            "• Ability to work in a team and learn quickly\n"
            "• Understanding of basic data structures and algorithms\n\n"
            "Nice to have: Exposure to SQL, Django or Flask, Linux"
        ),
    ),
    (
        1003,
        "Full Stack Developer",
        "DigitalWave Technologies",
        "INFORMATION-TECHNOLOGY",
        (
            "DigitalWave Technologies is seeking a Full Stack Developer to build and maintain "
            "modern web applications from front-end to back-end.\n\n"
            "Responsibilities:\n"
            "• Develop responsive, performant web interfaces using React.js and TypeScript\n"
            "• Build scalable backends using Node.js, Express, or Django\n"
            "• Design and optimize SQL and NoSQL database schemas\n"
            "• Implement authentication, authorization, and security best practices\n"
            "• Deploy and monitor applications using Docker and cloud platforms\n"
            "• Collaborate with UX designers to implement pixel-perfect interfaces\n\n"
            "Requirements:\n"
            "• 3+ years of full stack development experience\n"
            "• Strong proficiency in JavaScript, TypeScript, HTML, CSS\n"
            "• Experience with React.js or Angular for front-end development\n"
            "• Backend experience with Node.js, Python (Django/Flask), or Java (Spring)\n"
            "• Experience with PostgreSQL, MySQL, or MongoDB\n"
            "• Familiarity with Git, Docker, and CI/CD workflows\n"
            "• Knowledge of AWS or Azure cloud services"
        ),
    ),

    # ── Data Engineering ──────────────────────────────────────
    (
        2001,
        "Data Engineer",
        "DataStream Analytics",
        "INFORMATION-TECHNOLOGY",
        (
            "DataStream Analytics is looking for a Data Engineer to build robust data "
            "pipelines and infrastructure that power our analytics platform.\n\n"
            "Responsibilities:\n"
            "• Design, build, and maintain scalable ETL/ELT data pipelines\n"
            "• Work with large-scale data processing using Python and SQL\n"
            "• Implement data warehousing solutions on cloud platforms (AWS, GCP)\n"
            "• Ensure data quality, integrity, and availability across systems\n"
            "• Optimize query performance and database schemas\n"
            "• Collaborate with data scientists and analysts to understand data needs\n\n"
            "Requirements:\n"
            "• 3+ years of data engineering experience\n"
            "• Strong SQL skills (PostgreSQL, MySQL, or similar)\n"
            "• Proficiency in Python with pandas, NumPy, and data processing libraries\n"
            "• Experience with cloud data services (AWS Redshift, GCP BigQuery, Azure Synapse)\n"
            "• Knowledge of Apache Spark, Kafka, or Airflow\n"
            "• Familiarity with Docker and Kubernetes\n"
            "• Understanding of data modeling and data warehousing concepts\n\n"
            "Nice to have: Experience with Terraform, CI/CD, dbt"
        ),
    ),
    (
        2002,
        "Senior Data Engineer",
        "CloudScale Data",
        "INFORMATION-TECHNOLOGY",
        (
            "Join CloudScale Data as a Senior Data Engineer to architect next-generation "
            "data platforms serving millions of records daily.\n\n"
            "Responsibilities:\n"
            "• Architect and implement enterprise-scale data lake and warehouse solutions\n"
            "• Build real-time streaming pipelines using Kafka and Spark Streaming\n"
            "• Lead migration of on-premise data systems to cloud-native architectures\n"
            "• Mentor junior engineers and establish data engineering best practices\n"
            "• Implement data governance, lineage tracking, and quality monitoring\n\n"
            "Requirements:\n"
            "• 6+ years in data engineering roles\n"
            "• Expert-level Python and SQL\n"
            "• Deep experience with AWS (S3, Glue, Redshift, EMR) or GCP (BigQuery, Dataflow)\n"
            "• Production experience with Apache Spark, Airflow, and Kafka\n"
            "• Strong understanding of data modeling, star schema, and dimensional modeling\n"
            "• Experience with Docker, Kubernetes, and Terraform\n"
            "• Leadership and mentoring experience"
        ),
    ),

    # ── Data Science ──────────────────────────────────────────
    (
        3001,
        "Data Scientist",
        "InsightAI Labs",
        "INFORMATION-TECHNOLOGY",
        (
            "InsightAI Labs is hiring a Data Scientist to uncover business insights "
            "through statistical analysis, machine learning, and data visualization.\n\n"
            "Responsibilities:\n"
            "• Analyze complex datasets to identify trends, patterns, and actionable insights\n"
            "• Build predictive models using machine learning and statistical techniques\n"
            "• Create compelling data visualizations using Matplotlib, Seaborn, and Tableau\n"
            "• Design and run A/B tests and experiments\n"
            "• Communicate findings to stakeholders through reports and presentations\n"
            "• Collaborate with engineering teams to deploy models to production\n\n"
            "Requirements:\n"
            "• Master's or PhD in Statistics, Mathematics, Computer Science, or related field\n"
            "• Strong proficiency in Python (pandas, NumPy, scikit-learn, SciPy)\n"
            "• Experience with machine learning algorithms: regression, classification, clustering\n"
            "• Solid foundation in statistics and probability\n"
            "• Experience with SQL and data analysis tools\n"
            "• Data visualization skills using Matplotlib, Tableau, or PowerBI\n"
            "• Excellent analytical and problem-solving skills\n\n"
            "Nice to have: Experience with deep learning (TensorFlow, PyTorch), NLP, R"
        ),
    ),
    (
        3002,
        "Senior Data Analyst",
        "MetricsPro Consulting",
        "INFORMATION-TECHNOLOGY",
        (
            "MetricsPro Consulting needs a Senior Data Analyst to drive data-driven "
            "decision making across our client portfolio.\n\n"
            "Responsibilities:\n"
            "• Perform deep-dive analyses on business data to drive strategic decisions\n"
            "• Build interactive dashboards and reports using Tableau and PowerBI\n"
            "• Write complex SQL queries to extract and transform data\n"
            "• Develop automated reporting pipelines using Python\n"
            "• Present findings and recommendations to C-level executives\n"
            "• Mentor junior analysts on best practices\n\n"
            "Requirements:\n"
            "• 5+ years of data analysis experience\n"
            "• Advanced SQL skills\n"
            "• Proficiency in Python (pandas, NumPy) or R for data analysis\n"
            "• Expert-level Tableau or PowerBI dashboard development\n"
            "• Strong knowledge of Excel with pivot tables, VBA, and advanced formulas\n"
            "• Experience with statistical analysis and hypothesis testing\n"
            "• Excellent communication and presentation skills"
        ),
    ),

    # ── Machine Learning ──────────────────────────────────────
    (
        4001,
        "Machine Learning Engineer",
        "NeuralForge AI",
        "INFORMATION-TECHNOLOGY",
        (
            "NeuralForge AI is looking for a Machine Learning Engineer to build and deploy "
            "ML models that power intelligent products.\n\n"
            "Responsibilities:\n"
            "• Design, train, and evaluate machine learning models for production use\n"
            "• Build end-to-end ML pipelines from data preprocessing to model deployment\n"
            "• Implement deep learning architectures using TensorFlow and PyTorch\n"
            "• Optimize model performance, latency, and resource utilization\n"
            "• Deploy models using Docker, Kubernetes, and cloud ML services\n"
            "• Collaborate with data engineers to ensure quality training data\n\n"
            "Requirements:\n"
            "• 3+ years of machine learning engineering experience\n"
            "• Strong Python programming with scikit-learn, TensorFlow, or PyTorch\n"
            "• Solid understanding of ML algorithms: deep learning, NLP, computer vision\n"
            "• Experience with model serving and MLOps (MLflow, Kubeflow, SageMaker)\n"
            "• Proficiency in pandas, NumPy, and data preprocessing\n"
            "• Knowledge of Docker, Kubernetes, and CI/CD for ML\n"
            "• Experience with AWS, GCP, or Azure ML services\n\n"
            "Nice to have: Published research, Kaggle competition experience, reinforcement learning"
        ),
    ),
    (
        4002,
        "NLP Engineer",
        "LinguaTech Solutions",
        "INFORMATION-TECHNOLOGY",
        (
            "LinguaTech Solutions is hiring an NLP Engineer to build state-of-the-art "
            "natural language processing systems.\n\n"
            "Responsibilities:\n"
            "• Develop and fine-tune NLP models for text classification, NER, and summarization\n"
            "• Build text preprocessing and feature engineering pipelines\n"
            "• Implement transformer-based architectures using PyTorch or TensorFlow\n"
            "• Evaluate model performance and iterate on improvements\n"
            "• Deploy NLP services as scalable REST APIs\n\n"
            "Requirements:\n"
            "• 3+ years of NLP experience\n"
            "• Strong Python programming (pandas, NumPy, scikit-learn)\n"
            "• Deep expertise in NLP libraries and frameworks\n"
            "• Experience with deep learning for NLP (transformers, BERT, GPT)\n"
            "• Knowledge of text preprocessing, tokenization, and embeddings\n"
            "• Familiarity with spaCy, NLTK, or Hugging Face Transformers\n"
            "• Experience with SQL and data management\n"
            "• Understanding of machine learning fundamentals"
        ),
    ),
    (
        4003,
        "AI Research Scientist",
        "DeepMind Innovations",
        "INFORMATION-TECHNOLOGY",
        (
            "DeepMind Innovations seeks an AI Research Scientist to push the boundaries "
            "of artificial intelligence and machine learning.\n\n"
            "Responsibilities:\n"
            "• Conduct original research in machine learning and deep learning\n"
            "• Develop novel architectures for computer vision and NLP tasks\n"
            "• Publish findings in top-tier conferences (NeurIPS, ICML, CVPR)\n"
            "• Prototype research ideas and validate through experiments\n"
            "• Collaborate with engineering teams to transfer research to products\n\n"
            "Requirements:\n"
            "• PhD in Computer Science, Machine Learning, or related field\n"
            "• Strong publication record in deep learning, NLP, or computer vision\n"
            "• Expert-level Python and PyTorch or TensorFlow\n"
            "• Deep understanding of reinforcement learning, generative models, and optimization\n"
            "• Experience with large-scale distributed training\n"
            "• Proficiency in NumPy, SciPy, and scientific computing\n"
            "• Strong mathematical foundations in linear algebra, calculus, and probability"
        ),
    ),

    # ── DevOps / Cloud ────────────────────────────────────────
    (
        5001,
        "DevOps Engineer",
        "InfraCloud Systems",
        "INFORMATION-TECHNOLOGY",
        (
            "InfraCloud Systems is seeking a DevOps Engineer to build and maintain "
            "CI/CD pipelines and cloud infrastructure.\n\n"
            "Responsibilities:\n"
            "• Design and implement CI/CD pipelines for automated testing and deployment\n"
            "• Manage cloud infrastructure on AWS using Terraform and CloudFormation\n"
            "• Containerize applications using Docker and orchestrate with Kubernetes\n"
            "• Implement monitoring, logging, and alerting systems\n"
            "• Automate operational tasks using Python and Bash scripts\n"
            "• Ensure system security, reliability, and high availability\n\n"
            "Requirements:\n"
            "• 3+ years of DevOps or SRE experience\n"
            "• Strong experience with AWS services (EC2, S3, RDS, Lambda, EKS)\n"
            "• Proficiency in Docker and Kubernetes\n"
            "• Infrastructure as Code with Terraform or CloudFormation\n"
            "• Scripting skills in Python and Bash\n"
            "• Experience with CI/CD tools (Jenkins, GitLab CI, GitHub Actions)\n"
            "• Knowledge of Linux system administration\n"
            "• Familiarity with monitoring tools (Prometheus, Grafana, CloudWatch)"
        ),
    ),
    (
        5002,
        "Cloud Solutions Architect",
        "SkyBridge Technologies",
        "INFORMATION-TECHNOLOGY",
        (
            "SkyBridge Technologies is hiring a Cloud Solutions Architect to design "
            "enterprise-grade cloud architectures.\n\n"
            "Responsibilities:\n"
            "• Design and architect scalable, secure cloud solutions on AWS and Azure\n"
            "• Lead cloud migration projects from on-premise to cloud-native\n"
            "• Define cloud governance, security policies, and cost optimization strategies\n"
            "• Evaluate and recommend cloud services for business requirements\n"
            "• Create technical documentation and architecture diagrams\n\n"
            "Requirements:\n"
            "• 7+ years of IT experience with 4+ years in cloud architecture\n"
            "• AWS Solutions Architect Professional or Azure Solutions Architect certification\n"
            "• Deep knowledge of AWS, Azure, or GCP services\n"
            "• Experience with Docker, Kubernetes, and serverless architectures\n"
            "• Strong understanding of networking, security, and compliance\n"
            "• Experience with Terraform and Infrastructure as Code\n"
            "• Excellent communication and stakeholder management skills"
        ),
    ),

    # ── Cybersecurity ─────────────────────────────────────────
    (
        6001,
        "Cybersecurity Analyst",
        "SecureNet Corp",
        "INFORMATION-TECHNOLOGY",
        (
            "SecureNet Corp is hiring a Cybersecurity Analyst to protect our organization's "
            "digital assets and infrastructure.\n\n"
            "Responsibilities:\n"
            "• Monitor security systems and analyze threat intelligence\n"
            "• Conduct vulnerability assessments and penetration testing\n"
            "• Investigate security incidents and perform forensic analysis\n"
            "• Implement and manage firewall, IDS/IPS, and SIEM solutions\n"
            "• Develop security policies and incident response procedures\n"
            "• Conduct security awareness training for employees\n\n"
            "Requirements:\n"
            "• 3+ years of cybersecurity experience\n"
            "• Knowledge of network security, firewalls, and encryption\n"
            "• Experience with SIEM tools and log analysis\n"
            "• Scripting skills in Python and Bash for automation\n"
            "• Understanding of OWASP Top 10 and common vulnerabilities\n"
            "• Familiarity with Linux system administration\n"
            "• Relevant certifications (CEH, CISSP, CompTIA Security+) preferred"
        ),
    ),

    # ── Mobile Development ────────────────────────────────────
    (
        7001,
        "Android Developer",
        "AppForge Studios",
        "INFORMATION-TECHNOLOGY",
        (
            "AppForge Studios is looking for an Android Developer to build world-class "
            "mobile applications.\n\n"
            "Responsibilities:\n"
            "• Design and develop Android applications using Kotlin and Java\n"
            "• Implement modern UI patterns with Jetpack Compose\n"
            "• Integrate RESTful APIs and third-party SDKs\n"
            "• Write unit tests and ensure app quality and performance\n"
            "• Publish and maintain apps on the Google Play Store\n"
            "• Collaborate with iOS team to ensure consistent cross-platform experience\n\n"
            "Requirements:\n"
            "• 3+ years of Android development experience\n"
            "• Proficiency in Kotlin and Java\n"
            "• Experience with Android SDK, Jetpack libraries, and Material Design\n"
            "• Understanding of MVVM/MVP architecture patterns\n"
            "• Experience with Git version control\n"
            "• Knowledge of SQL databases and data persistence\n"
            "• Familiarity with Firebase and cloud services"
        ),
    ),
    (
        7002,
        "iOS Developer",
        "AppForge Studios",
        "INFORMATION-TECHNOLOGY",
        (
            "We are hiring an iOS Developer to create beautiful, performant mobile "
            "applications for the Apple ecosystem.\n\n"
            "Responsibilities:\n"
            "• Develop iOS applications using Swift and SwiftUI\n"
            "• Implement complex UI designs with smooth animations\n"
            "• Integrate RESTful APIs and manage local data persistence\n"
            "• Write comprehensive unit and UI tests\n"
            "• Optimize app performance, memory usage, and battery consumption\n\n"
            "Requirements:\n"
            "• 3+ years of iOS development experience\n"
            "• Strong proficiency in Swift\n"
            "• Experience with SwiftUI and UIKit frameworks\n"
            "• Understanding of MVC, MVVM, and clean architecture patterns\n"
            "• Experience with Core Data, Realm, or similar persistence frameworks\n"
            "• Knowledge of Git, CI/CD, and Agile methodologies\n"
            "• App Store submission and release management experience"
        ),
    ),

    # ── Web Development ───────────────────────────────────────
    (
        8001,
        "Frontend Developer",
        "PixelPerfect Design",
        "INFORMATION-TECHNOLOGY",
        (
            "PixelPerfect Design is looking for a Frontend Developer who is passionate "
            "about creating beautiful, accessible web experiences.\n\n"
            "Responsibilities:\n"
            "• Build responsive, performant web interfaces using React.js and TypeScript\n"
            "• Implement pixel-perfect designs from Figma mockups\n"
            "• Write clean, reusable, and well-tested component code\n"
            "• Optimize web performance (Core Web Vitals, lazy loading, code splitting)\n"
            "• Ensure cross-browser compatibility and accessibility (WCAG)\n"
            "• Collaborate with backend developers on API integration\n\n"
            "Requirements:\n"
            "• 3+ years of frontend development experience\n"
            "• Expert-level JavaScript, TypeScript, HTML, and CSS\n"
            "• Strong experience with React.js and state management (Redux, Zustand)\n"
            "• Understanding of responsive design and mobile-first development\n"
            "• Experience with Git, npm/yarn, and modern build tools\n"
            "• Knowledge of web accessibility standards\n"
            "• Familiarity with REST APIs and GraphQL"
        ),
    ),
    (
        8002,
        "Backend Developer",
        "ServerStack Solutions",
        "INFORMATION-TECHNOLOGY",
        (
            "ServerStack Solutions needs a Backend Developer to build robust, scalable "
            "server-side applications and APIs.\n\n"
            "Responsibilities:\n"
            "• Design and implement RESTful APIs using Python (Django/Flask) or Node.js\n"
            "• Build and optimize database schemas with PostgreSQL and MongoDB\n"
            "• Implement authentication, caching, and rate limiting\n"
            "• Write comprehensive tests and maintain high code coverage\n"
            "• Deploy applications using Docker and cloud services\n"
            "• Participate in on-call rotation for production support\n\n"
            "Requirements:\n"
            "• 3+ years of backend development experience\n"
            "• Strong Python (Django, Flask, or FastAPI) or Node.js\n"
            "• Solid SQL experience with PostgreSQL or MySQL\n"
            "• Experience with NoSQL databases (MongoDB, Redis)\n"
            "• Knowledge of Docker, CI/CD, and cloud platforms (AWS)\n"
            "• Understanding of API security and authentication (OAuth, JWT)\n"
            "• Experience with Git and agile development practices"
        ),
    ),

    # ── Quality Assurance ─────────────────────────────────────
    (
        9001,
        "QA Automation Engineer",
        "QualityFirst Tech",
        "INFORMATION-TECHNOLOGY",
        (
            "QualityFirst Tech is hiring a QA Automation Engineer to build and maintain "
            "our automated testing infrastructure.\n\n"
            "Responsibilities:\n"
            "• Design and implement automated test frameworks for web and API testing\n"
            "• Write and maintain automated test scripts using Python and Selenium\n"
            "• Integrate tests into CI/CD pipelines for continuous testing\n"
            "• Perform performance and load testing\n"
            "• Report bugs with clear reproduction steps and track resolution\n"
            "• Collaborate with development teams to improve code quality\n\n"
            "Requirements:\n"
            "• 3+ years of QA automation experience\n"
            "• Proficiency in Python with testing frameworks (pytest, unittest)\n"
            "• Experience with Selenium WebDriver and browser automation\n"
            "• Knowledge of API testing tools (Postman, REST Assured)\n"
            "• Experience with CI/CD integration (Jenkins, GitHub Actions)\n"
            "• Understanding of SQL for database validation\n"
            "• Familiarity with Git and agile/scrum methodologies"
        ),
    ),

    # ── Systems / Network ─────────────────────────────────────
    (
        10001,
        "Systems Administrator",
        "NetCore Infrastructure",
        "INFORMATION-TECHNOLOGY",
        (
            "NetCore Infrastructure seeks a Systems Administrator to manage and maintain "
            "enterprise IT infrastructure.\n\n"
            "Responsibilities:\n"
            "• Manage and maintain Linux and Windows server environments\n"
            "• Configure and monitor network infrastructure (switches, routers, firewalls)\n"
            "• Implement backup, disaster recovery, and business continuity plans\n"
            "• Automate administrative tasks using Bash and Python scripts\n"
            "• Manage Active Directory, DNS, DHCP, and email systems\n"
            "• Provide tier-3 technical support and troubleshooting\n\n"
            "Requirements:\n"
            "• 4+ years of systems administration experience\n"
            "• Strong Linux administration (RHEL, Ubuntu, CentOS)\n"
            "• Experience with Windows Server and Active Directory\n"
            "• Knowledge of networking protocols (TCP/IP, DNS, HTTP, SSL)\n"
            "• Scripting skills in Bash and Python\n"
            "• Experience with virtualization (VMware, Hyper-V)\n"
            "• Familiarity with cloud platforms (AWS, Azure)"
        ),
    ),

    # ── Product / Project Management ──────────────────────────
    (
        11001,
        "Technical Project Manager",
        "AgileOps Group",
        "INFORMATION-TECHNOLOGY",
        (
            "AgileOps Group is hiring a Technical Project Manager to lead software "
            "development projects from inception to delivery.\n\n"
            "Responsibilities:\n"
            "• Manage end-to-end software project lifecycle using Agile/Scrum\n"
            "• Plan sprints, track progress, and remove blockers for development teams\n"
            "• Define project scope, timelines, and resource allocation\n"
            "• Communicate project status to stakeholders and leadership\n"
            "• Identify and mitigate project risks\n"
            "• Drive continuous improvement in team processes\n\n"
            "Requirements:\n"
            "• 5+ years of technical project management experience\n"
            "• PMP or Certified Scrum Master (CSM) certification\n"
            "• Understanding of software development lifecycle and technologies\n"
            "• Experience with JIRA, Confluence, and project management tools\n"
            "• Strong communication, leadership, and organizational skills\n"
            "• Familiarity with Python, SQL, or basic programming concepts\n"
            "• Experience managing cross-functional teams"
        ),
    ),

    # ── Database Administration ───────────────────────────────
    (
        12001,
        "Database Administrator",
        "DataVault Systems",
        "INFORMATION-TECHNOLOGY",
        (
            "DataVault Systems needs a Database Administrator to ensure the performance, "
            "security, and reliability of our database systems.\n\n"
            "Responsibilities:\n"
            "• Administer and optimize PostgreSQL, MySQL, and MongoDB databases\n"
            "• Implement database backup, recovery, and replication strategies\n"
            "• Monitor database performance and tune queries for optimal execution\n"
            "• Design and implement database security policies and access controls\n"
            "• Plan and execute database migrations and upgrades\n"
            "• Automate routine DBA tasks using Python and SQL scripts\n\n"
            "Requirements:\n"
            "• 4+ years of database administration experience\n"
            "• Expert-level SQL skills\n"
            "• Strong experience with PostgreSQL and/or MySQL\n"
            "• Knowledge of NoSQL databases (MongoDB, Redis)\n"
            "• Experience with database replication, clustering, and high availability\n"
            "• Scripting skills in Python or Bash\n"
            "• Understanding of cloud database services (AWS RDS, Azure SQL)"
        ),
    ),

    # ── Business Intelligence ─────────────────────────────────
    (
        13001,
        "Business Intelligence Developer",
        "InsightDriven Analytics",
        "INFORMATION-TECHNOLOGY",
        (
            "InsightDriven Analytics is looking for a BI Developer to build data-driven "
            "reporting and analytics solutions.\n\n"
            "Responsibilities:\n"
            "• Design and develop interactive dashboards using Tableau and PowerBI\n"
            "• Build ETL pipelines to transform raw data into analytics-ready datasets\n"
            "• Write complex SQL queries for data extraction and analysis\n"
            "• Create automated reports and KPI tracking systems\n"
            "• Collaborate with business stakeholders to understand reporting needs\n"
            "• Maintain data models and ensure data accuracy\n\n"
            "Requirements:\n"
            "• 3+ years of BI development experience\n"
            "• Expert-level Tableau and/or PowerBI\n"
            "• Strong SQL skills for complex queries and data modeling\n"
            "• Experience with Python for data analysis (pandas, NumPy)\n"
            "• Knowledge of data warehousing concepts and star schemas\n"
            "• Advanced Excel skills with pivot tables and macros\n"
            "• Excellent data visualization and storytelling skills"
        ),
    ),

    # ── Embedded / IoT ────────────────────────────────────────
    (
        14001,
        "Embedded Systems Engineer",
        "IoTech Devices",
        "INFORMATION-TECHNOLOGY",
        (
            "IoTech Devices is hiring an Embedded Systems Engineer to develop firmware "
            "and software for IoT devices.\n\n"
            "Responsibilities:\n"
            "• Develop embedded firmware in C and C++ for microcontrollers\n"
            "• Design and implement communication protocols (MQTT, BLE, Wi-Fi)\n"
            "• Interface with sensors, actuators, and peripheral hardware\n"
            "• Write Python scripts for testing, automation, and data analysis\n"
            "• Debug hardware-software integration issues\n"
            "• Collaborate with hardware engineers on PCB design reviews\n\n"
            "Requirements:\n"
            "• 3+ years of embedded development experience\n"
            "• Strong C and C++ programming\n"
            "• Experience with ARM Cortex microcontrollers\n"
            "• Knowledge of RTOS, Linux embedded, and bare-metal programming\n"
            "• Familiarity with Python for testing and tooling\n"
            "• Understanding of digital electronics and communication protocols\n"
            "• Experience with Git and version control"
        ),
    ),

    # ── Additional varied roles ───────────────────────────────
    (
        15001,
        "Site Reliability Engineer",
        "ReliableOps Inc.",
        "INFORMATION-TECHNOLOGY",
        (
            "ReliableOps Inc. is seeking a Site Reliability Engineer to ensure our "
            "services maintain 99.99% uptime.\n\n"
            "Responsibilities:\n"
            "• Design and implement infrastructure for high availability and fault tolerance\n"
            "• Build monitoring, alerting, and incident response systems\n"
            "• Automate deployments and infrastructure using Terraform and Ansible\n"
            "• Conduct capacity planning and performance optimization\n"
            "• Participate in on-call rotations and incident post-mortems\n"
            "• Develop runbooks and standard operating procedures\n\n"
            "Requirements:\n"
            "• 4+ years of SRE or DevOps experience\n"
            "• Strong Linux administration and troubleshooting skills\n"
            "• Proficiency in Python and Bash scripting\n"
            "• Experience with Docker, Kubernetes, and container orchestration\n"
            "• Knowledge of AWS or GCP cloud infrastructure\n"
            "• Experience with monitoring tools (Prometheus, Grafana, PagerDuty)\n"
            "• Understanding of SLOs, SLIs, and error budgets"
        ),
    ),
    (
        15002,
        "Software Architect",
        "ArchitectNow Consulting",
        "INFORMATION-TECHNOLOGY",
        (
            "ArchitectNow Consulting seeks a Software Architect to design scalable, "
            "maintainable software systems for enterprise clients.\n\n"
            "Responsibilities:\n"
            "• Define system architecture for complex enterprise applications\n"
            "• Evaluate and select appropriate technologies, frameworks, and platforms\n"
            "• Create architecture decision records and technical design documents\n"
            "• Lead proof-of-concept development for new technologies\n"
            "• Ensure architectures meet non-functional requirements (performance, security, scalability)\n"
            "• Mentor development teams on architectural patterns and best practices\n\n"
            "Requirements:\n"
            "• 10+ years of software development experience\n"
            "• 5+ years in architecture and system design roles\n"
            "• Deep expertise in Python, Java, or C#\n"
            "• Experience with microservices, event-driven, and serverless architectures\n"
            "• Strong knowledge of cloud platforms (AWS, Azure, GCP)\n"
            "• Experience with Docker, Kubernetes, and CI/CD\n"
            "• Excellent communication and stakeholder management"
        ),
    ),
    (
        16001,
        "Python Developer",
        "PyTech Solutions",
        "INFORMATION-TECHNOLOGY",
        (
            "PyTech Solutions is hiring a Python Developer to build automation tools, "
            "backend services, and data processing systems.\n\n"
            "Responsibilities:\n"
            "• Develop backend services and REST APIs using Django and FastAPI\n"
            "• Build data processing pipelines with pandas and NumPy\n"
            "• Write reusable Python packages with comprehensive documentation\n"
            "• Implement automated testing using pytest\n"
            "• Optimize application performance and memory usage\n"
            "• Deploy services using Docker and AWS\n\n"
            "Requirements:\n"
            "• 3+ years of professional Python development\n"
            "• Experience with Django, Flask, or FastAPI\n"
            "• Proficiency in SQL (PostgreSQL or MySQL)\n"
            "• Knowledge of pandas, NumPy, and data processing\n"
            "• Experience with Docker and Linux\n"
            "• Familiarity with Git, CI/CD, and agile workflows\n"
            "• Understanding of software design patterns and clean code principles"
        ),
    ),
    (
        17001,
        "Computer Vision Engineer",
        "VisualAI Corp",
        "INFORMATION-TECHNOLOGY",
        (
            "VisualAI Corp is looking for a Computer Vision Engineer to develop "
            "image and video analysis systems.\n\n"
            "Responsibilities:\n"
            "• Develop computer vision models for object detection, segmentation, and tracking\n"
            "• Train and optimize deep learning models using PyTorch and TensorFlow\n"
            "• Build data annotation and augmentation pipelines\n"
            "• Deploy vision models on edge devices and cloud platforms\n"
            "• Evaluate model accuracy, latency, and runtime performance\n\n"
            "Requirements:\n"
            "• 3+ years of computer vision experience\n"
            "• Strong Python programming with PyTorch or TensorFlow\n"
            "• Deep understanding of CNNs, transformers, and detection architectures\n"
            "• Experience with OpenCV and image processing libraries\n"
            "• Knowledge of deep learning optimization and model compression\n"
            "• Proficiency in NumPy, pandas, and matplotlib\n"
            "• Experience with AWS or GCP for model training and deployment"
        ),
    ),
    (
        18001,
        "Blockchain Developer",
        "ChainLogic Labs",
        "INFORMATION-TECHNOLOGY",
        (
            "ChainLogic Labs is seeking a Blockchain Developer to build decentralized "
            "applications and smart contracts.\n\n"
            "Responsibilities:\n"
            "• Develop and deploy smart contracts on Ethereum and Solana\n"
            "• Build Web3 frontend interfaces using React.js and ethers.js\n"
            "• Implement security best practices for smart contract development\n"
            "• Design tokenomics and decentralized protocol architectures\n"
            "• Write comprehensive tests for smart contracts\n\n"
            "Requirements:\n"
            "• 2+ years of blockchain development experience\n"
            "• Proficiency in Solidity and/or Rust\n"
            "• Strong JavaScript and TypeScript skills\n"
            "• Experience with React.js and Node.js\n"
            "• Understanding of DeFi protocols and blockchain security\n"
            "• Knowledge of Git and CI/CD pipelines\n"
            "• Familiarity with Python for scripting and data analysis"
        ),
    ),
    (
        19001,
        "Technical Support Engineer",
        "SupportTech Global",
        "INFORMATION-TECHNOLOGY",
        (
            "SupportTech Global is hiring a Technical Support Engineer to provide "
            "expert-level support for our software products.\n\n"
            "Responsibilities:\n"
            "• Diagnose and resolve complex technical issues for enterprise customers\n"
            "• Analyze application logs, database queries, and system configurations\n"
            "• Create and maintain knowledge base articles and troubleshooting guides\n"
            "• Collaborate with engineering teams to report and track product bugs\n"
            "• Automate common support tasks using Python scripts\n\n"
            "Requirements:\n"
            "• 2+ years of technical support experience\n"
            "• Strong troubleshooting and analytical skills\n"
            "• Basic programming knowledge in Python or Bash\n"
            "• Understanding of SQL databases and query debugging\n"
            "• Experience with Linux command line\n"
            "• Knowledge of networking fundamentals (TCP/IP, DNS, HTTP)\n"
            "• Excellent written and verbal communication skills"
        ),
    ),
    (
        20001,
        "Data Warehouse Developer",
        "WarehouseLogic Inc",
        "INFORMATION-TECHNOLOGY",
        (
            "WarehouseLogic Inc is hiring a Data Warehouse Developer to design and "
            "build enterprise data warehousing solutions.\n\n"
            "Responsibilities:\n"
            "• Design and implement dimensional data models (star, snowflake schemas)\n"
            "• Build ETL/ELT pipelines using Python, SQL, and cloud-native tools\n"
            "• Optimize query performance and storage efficiency in data warehouses\n"
            "• Implement data quality checks and monitoring\n"
            "• Support analytics teams with data access and reporting needs\n\n"
            "Requirements:\n"
            "• 4+ years of data warehousing experience\n"
            "• Expert-level SQL and data modeling\n"
            "• Experience with cloud data warehouses (Redshift, BigQuery, Snowflake)\n"
            "• Proficiency in Python for ETL development\n"
            "• Knowledge of pandas, NumPy, and data processing\n"
            "• Experience with dbt, Airflow, or similar orchestration tools\n"
            "• Understanding of data governance and data quality frameworks"
        ),
    ),
    # ── Additional ML/AI roles ────────────────────────────────
    (
        21001,
        "MLOps Engineer",
        "ModelServe AI",
        "INFORMATION-TECHNOLOGY",
        (
            "ModelServe AI is looking for an MLOps Engineer to bridge the gap between "
            "machine learning research and production deployment.\n\n"
            "Responsibilities:\n"
            "• Build and maintain ML model training and serving infrastructure\n"
            "• Implement CI/CD pipelines for machine learning workflows\n"
            "• Deploy and monitor ML models using Kubernetes and cloud services\n"
            "• Automate model retraining, evaluation, and A/B testing\n"
            "• Manage feature stores and experiment tracking systems\n\n"
            "Requirements:\n"
            "• 3+ years of MLOps or DevOps experience\n"
            "• Strong Python programming with scikit-learn and ML libraries\n"
            "• Experience with Docker, Kubernetes, and container orchestration\n"
            "• Knowledge of MLflow, Kubeflow, or Weights & Biases\n"
            "• Experience with AWS SageMaker, GCP Vertex AI, or Azure ML\n"
            "• Proficiency in Terraform and Infrastructure as Code\n"
            "• Understanding of machine learning model lifecycle"
        ),
    ),
    (
        22001,
        "Data Analytics Engineer",
        "AnalyticsBridge",
        "INFORMATION-TECHNOLOGY",
        (
            "AnalyticsBridge is hiring a Data Analytics Engineer to build the data "
            "infrastructure that powers our analytics platform.\n\n"
            "Responsibilities:\n"
            "• Build and optimize data transformation pipelines using dbt and SQL\n"
            "• Design data models that support self-service analytics\n"
            "• Create automated data quality testing and monitoring\n"
            "• Collaborate with analysts to understand data requirements\n"
            "• Implement metrics layers and semantic models\n\n"
            "Requirements:\n"
            "• 3+ years of analytics engineering or data engineering experience\n"
            "• Expert-level SQL and data modeling\n"
            "• Experience with Python (pandas, NumPy) for data analysis\n"
            "• Knowledge of dbt, Airflow, or similar tools\n"
            "• Experience with cloud data warehouses (Snowflake, BigQuery)\n"
            "• Understanding of data visualization tools (Tableau, PowerBI)\n"
            "• Strong analytical and problem-solving skills"
        ),
    ),
    (
        23001,
        "Platform Engineer",
        "PlatformX Technologies",
        "INFORMATION-TECHNOLOGY",
        (
            "PlatformX Technologies is seeking a Platform Engineer to build internal "
            "developer platforms and tooling.\n\n"
            "Responsibilities:\n"
            "• Design and build internal developer platforms and self-service tools\n"
            "• Implement service meshes, API gateways, and platform abstractions\n"
            "• Create developer documentation and onboarding workflows\n"
            "• Build and maintain shared libraries and infrastructure components\n"
            "• Drive platform adoption across engineering teams\n\n"
            "Requirements:\n"
            "• 4+ years of platform or infrastructure engineering experience\n"
            "• Strong Python, Go, or Java programming skills\n"
            "• Deep experience with Docker and Kubernetes\n"
            "• Knowledge of AWS, GCP, or Azure cloud services\n"
            "• Experience with Terraform, Helm, and GitOps workflows\n"
            "• Understanding of microservices architecture patterns\n"
            "• Excellent documentation and communication skills"
        ),
    ),
    (
        24001,
        "Automation Engineer",
        "AutomatePro Systems",
        "INFORMATION-TECHNOLOGY",
        (
            "AutomatePro Systems is hiring an Automation Engineer to streamline business "
            "processes through intelligent automation.\n\n"
            "Responsibilities:\n"
            "• Design and implement process automation solutions using Python\n"
            "• Build robotic process automation (RPA) workflows\n"
            "• Automate data collection, transformation, and reporting tasks\n"
            "• Create automated testing and monitoring frameworks\n"
            "• Document automation workflows and maintain runbooks\n\n"
            "Requirements:\n"
            "• 3+ years of automation engineering experience\n"
            "• Strong Python programming with scripting and automation libraries\n"
            "• Experience with web scraping (BeautifulSoup, Selenium)\n"
            "• Knowledge of SQL and database automation\n"
            "• Experience with Excel automation and data processing (pandas)\n"
            "• Familiarity with Git, CI/CD, and Linux\n"
            "• Understanding of RESTful APIs and integration patterns"
        ),
    ),
    # ── A few more specialized roles ──────────────────────────
    (
        25001,
        "Game Developer",
        "PixelForge Games",
        "INFORMATION-TECHNOLOGY",
        (
            "PixelForge Games is seeking a Game Developer to create engaging gaming "
            "experiences across multiple platforms.\n\n"
            "Responsibilities:\n"
            "• Develop game mechanics, UI systems, and gameplay features\n"
            "• Write efficient, optimized code in C++ and C#\n"
            "• Implement physics, AI behaviors, and rendering systems\n"
            "• Debug and profile game performance issues\n"
            "• Collaborate with artists and designers to bring creative visions to life\n\n"
            "Requirements:\n"
            "• 3+ years of game development experience\n"
            "• Strong C++ and/or C# programming\n"
            "• Experience with Unity or Unreal Engine\n"
            "• Understanding of 3D mathematics, physics, and rendering\n"
            "• Knowledge of data structures and algorithms for game optimization\n"
            "• Experience with Git version control\n"
            "• Python scripting for tools and automation is a plus"
        ),
    ),
    (
        26001,
        "API Developer",
        "ConnectAPI Solutions",
        "INFORMATION-TECHNOLOGY",
        (
            "ConnectAPI Solutions needs an API Developer to design and build robust "
            "API platforms serving thousands of developers.\n\n"
            "Responsibilities:\n"
            "• Design and implement RESTful and GraphQL APIs\n"
            "• Build API authentication, rate limiting, and versioning systems\n"
            "• Write comprehensive API documentation using OpenAPI/Swagger\n"
            "• Implement API monitoring, logging, and analytics\n"
            "• Ensure API security and compliance with best practices\n\n"
            "Requirements:\n"
            "• 3+ years of API development experience\n"
            "• Strong Python (Flask, FastAPI, Django REST Framework) or Node.js\n"
            "• Experience with PostgreSQL, MongoDB, and Redis\n"
            "• Knowledge of API security (OAuth 2.0, JWT, API keys)\n"
            "• Experience with Docker and cloud deployment (AWS, GCP)\n"
            "• Understanding of REST principles and API design patterns\n"
            "• Familiarity with CI/CD and automated testing"
        ),
    ),
    (
        27001,
        "Big Data Engineer",
        "ScaleData Corp",
        "INFORMATION-TECHNOLOGY",
        (
            "ScaleData Corp is hiring a Big Data Engineer to process and analyze "
            "petabyte-scale datasets.\n\n"
            "Responsibilities:\n"
            "• Build distributed data processing pipelines using Apache Spark\n"
            "• Design data lake architectures on AWS S3 or GCP Cloud Storage\n"
            "• Implement real-time streaming solutions with Kafka and Flink\n"
            "• Optimize data processing for performance and cost efficiency\n"
            "• Develop data quality frameworks and monitoring dashboards\n\n"
            "Requirements:\n"
            "• 4+ years of big data engineering experience\n"
            "• Strong Python and Scala programming\n"
            "• Expert-level Apache Spark (PySpark, Spark SQL)\n"
            "• Experience with Apache Kafka, Airflow, and Hive\n"
            "• Deep knowledge of AWS (EMR, S3, Glue) or GCP (Dataproc, BigQuery)\n"
            "• Proficiency in SQL and data modeling\n"
            "• Experience with Docker, Kubernetes, and Terraform"
        ),
    ),
    (
        28001,
        "IT Consultant",
        "TechAdvisors Group",
        "INFORMATION-TECHNOLOGY",
        (
            "TechAdvisors Group is looking for an IT Consultant to provide strategic "
            "technology guidance to enterprise clients.\n\n"
            "Responsibilities:\n"
            "• Assess client technology infrastructure and recommend improvements\n"
            "• Design solutions for cloud migration, security, and digital transformation\n"
            "• Create technical proposals, roadmaps, and implementation plans\n"
            "• Lead workshops and training sessions for client teams\n"
            "• Stay current with industry trends and emerging technologies\n\n"
            "Requirements:\n"
            "• 5+ years of IT consulting or enterprise technology experience\n"
            "• Broad knowledge of cloud platforms (AWS, Azure, GCP)\n"
            "• Understanding of Python, SQL, and modern development practices\n"
            "• Experience with data analytics and visualization tools\n"
            "• Strong presentation and client-facing communication skills\n"
            "• Knowledge of cybersecurity, networking, and infrastructure\n"
            "• Relevant certifications (AWS, Azure, ITIL) preferred"
        ),
    ),
    # ── Deep Learning / Research roles ────────────────────────
    (
        29001,
        "Deep Learning Engineer",
        "CortexAI Research",
        "INFORMATION-TECHNOLOGY",
        (
            "CortexAI Research is hiring a Deep Learning Engineer to develop cutting-edge "
            "neural network models for real-world applications.\n\n"
            "Responsibilities:\n"
            "• Design, implement, and train deep neural networks using PyTorch\n"
            "• Develop models for NLP, computer vision, and multimodal applications\n"
            "• Optimize training pipelines for distributed GPU clusters\n"
            "• Implement model quantization and optimization for deployment\n"
            "• Conduct experiments and report results with rigorous methodology\n\n"
            "Requirements:\n"
            "• 3+ years of deep learning experience\n"
            "• Expert-level Python and PyTorch or TensorFlow\n"
            "• Strong understanding of deep learning architectures (CNNs, RNNs, Transformers)\n"
            "• Experience with machine learning, NLP, and computer vision\n"
            "• Proficiency in NumPy, pandas, matplotlib, and scipy\n"
            "• Knowledge of scikit-learn and classical ML algorithms\n"
            "• Experience with Docker, Kubernetes, and cloud GPU instances (AWS, GCP)"
        ),
    ),
    (
        30001,
        "Software Development Engineer in Test",
        "TestDriven Technologies",
        "INFORMATION-TECHNOLOGY",
        (
            "TestDriven Technologies is seeking an SDET to ensure software quality through "
            "comprehensive testing strategies.\n\n"
            "Responsibilities:\n"
            "• Design and implement automated testing frameworks and strategies\n"
            "• Write integration, end-to-end, and performance tests\n"
            "• Develop custom testing tools and utilities in Python\n"
            "• Analyze test results and provide detailed quality reports\n"
            "• Collaborate with developers to establish testing best practices\n\n"
            "Requirements:\n"
            "• 3+ years of SDET or test automation experience\n"
            "• Strong Python programming with pytest and unittest\n"
            "• Experience with Selenium, Playwright, or Cypress\n"
            "• Knowledge of REST API testing and contract testing\n"
            "• Familiarity with CI/CD pipelines (Jenkins, GitHub Actions)\n"
            "• Understanding of SQL and database testing\n"
            "• Experience with Git and agile development methodologies"
        ),
    ),
]


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["job_id", "job title", "company", "category", "job description"])
        for job_id, title, company, category, description in JOB_DATA:
            writer.writerow([job_id, title, company, category, description])

    print(f"[OK] Generated {len(JOB_DATA)} job descriptions -> {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
