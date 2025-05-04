# Data Science Projects with LLMs: A Complexity Guide

*Created on May 4, 2025*

This document provides a collection of data science project ideas that leverage Large Language Models (LLMs) at different complexity levels. Each project includes an example prompt to help you get started with GitHub Copilot or other LLM tools.

## Table of Contents
1. [Beginner Projects (Low Complexity)](#beginner-projects)
2. [Intermediate Projects (Medium Complexity)](#intermediate-projects)
3. [Advanced Projects (High Complexity)](#advanced-projects)

<a name="beginner-projects"></a>
## Beginner Projects (Low Complexity)

### 1. Automated Data Cleaning Pipeline

**Description**: Create a script that automatically cleans datasets by handling missing values, outliers, and standardizing formats.

**Example Prompt**:
```
Create a Python function that cleans a pandas DataFrame by:
1. Identifying and handling missing values using appropriate strategies (mean/median imputation for numerical columns, mode for categorical)
2. Detecting and handling outliers using IQR or z-score methods
3. Converting data types to appropriate formats (dates, numbers, categories)
4. Standardizing text fields (lowercase, removing special characters)

The function should take a DataFrame as input and return the cleaned DataFrame with a report of changes made.
```

### 2. Automated Exploratory Data Analysis (EDA) Report Generator

**Description**: Build a tool that automatically generates an EDA report for any dataset, including visualizations, summary statistics, and key insights.

**Example Prompt**:
```
Create a Python script that performs automated exploratory data analysis on a CSV file:
1. Load the data using pandas
2. Generate summary statistics for all columns
3. Create appropriate visualizations based on data types:
   - Histograms and box plots for numerical features
   - Bar charts for categorical features
   - Correlation heatmap for relationships between numerical features
4. Identify potential outliers and anomalies
5. Generate a formatted report with all findings using markdown

Use matplotlib and seaborn for visualizations and include an option to save the report as an HTML file.
```

### 3. Sentiment Analysis Dashboard for Customer Reviews

**Description**: Build a dashboard that analyzes sentiment from customer reviews or social media posts.

**Example Prompt**:
```
Create a Streamlit dashboard for sentiment analysis of customer reviews that:
1. Allows users to upload a CSV file containing customer reviews
2. Uses a pre-trained model or library to analyze the sentiment of each review
3. Displays sentiment distribution with visualization
4. Shows top positive and negative keywords
5. Tracks sentiment trends over time if date information is available
6. Provides filtering options by sentiment score or keywords

Make sure to include proper error handling and instructions for installing required dependencies.
```

### 4. Time Series Forecasting Tool

**Description**: Create a simple forecasting tool that predicts future values for any time series data.

**Example Prompt**:
```
Develop a Python script for time series forecasting that:
1. Takes a CSV file with time series data (date column and value column)
2. Performs necessary preprocessing (handling missing values, resampling)
3. Implements multiple forecasting methods:
   - Moving averages
   - Exponential smoothing
   - ARIMA/SARIMA
4. Evaluates each model using appropriate metrics (RMSE, MAE, MAPE)
5. Visualizes the actual vs. predicted values
6. Forecasts future values for a user-specified time period

Include option to save the model for future use and make sure to visualize prediction intervals.
```

### 5. Text Summarizer for Research Papers

**Description**: Create a tool that summarizes research papers or long documents using LLMs.

**Example Prompt**:
```
Build a Python script that summarizes research papers or long documents:
1. Accept PDF input or text files
2. Extract text content using appropriate libraries
3. Use an LLM-based approach to generate:
   - A concise abstract (100-150 words)
   - Key findings (3-5 bullet points)
   - Main methodology used (2-3 sentences)
4. Format the output in a structured way
5. Include options to adjust summary length

Make sure to handle scientific notation, references, and technical terminology appropriately.
```

<a name="intermediate-projects"></a>
## Intermediate Projects (Medium Complexity)

### 1. Intelligent Data Labeling System

**Description**: Create a semi-automated system that helps label data for machine learning by using LLMs to suggest labels and learn from human corrections.

**Example Prompt**:
```
Develop a Python application for semi-automated data labeling that:
1. Loads unlabeled data from various sources (CSV, JSON, images via paths)
2. Uses pre-trained models to suggest initial labels
3. Presents a simple UI (can use Streamlit or Gradio) for users to:
   - View the suggested labels
   - Accept, reject, or modify suggestions
   - Apply bulk actions to similar items
4. Learns from user corrections to improve future suggestions
5. Exports the labeled dataset in multiple formats
6. Tracks labeling progress and statistics

Include features for active learning, where the system prioritizes uncertain cases for human review to maximize learning efficiency.
```

### 2. Anomaly Detection System with Explainability

**Description**: Build an anomaly detection system for time series or transactional data that not only identifies anomalies but explains why they were flagged.

**Example Prompt**:
```
Create a comprehensive anomaly detection system in Python that:
1. Imports data from various sources (databases, CSV files, APIs)
2. Implements multiple anomaly detection algorithms:
   - Statistical methods (Z-score, IQR)
   - Machine learning methods (Isolation Forest, One-Class SVM)
   - Deep learning methods (Autoencoders)
3. Compares results across different methods
4. Provides detailed explanations for each detected anomaly including:
   - Deviation metrics from normal patterns
   - Contributing features ranked by importance
   - Similar historical anomalies
5. Visualizes anomalies in context with interactive plotting
6. Allows for feedback to reduce false positives

Include a configuration system to adjust sensitivity and implement real-time monitoring capabilities.
```

### 3. Multimodal Dashboard for Financial Analysis

**Description**: Create an interactive dashboard that combines financial data analysis with news sentiment and social media trends.

**Example Prompt**:
```
Develop a multimodal financial analysis dashboard using Streamlit or Dash that:
1. Fetches and integrates data from multiple sources:
   - Financial market data (stock prices, indices, etc.)
   - Company financial statements
   - News articles via API
   - Social media sentiment
2. Performs correlation analysis between news sentiment and price movements
3. Creates interactive visualizations:
   - Price charts with technical indicators
   - Sentiment trends overlaid with price action
   - Financial health indicators
   - Volume analysis
4. Implements prediction models for price movements based on multimodal data
5. Allows users to customize time periods and companies/assets to analyze
6. Provides downloadable reports of findings

Ensure the dashboard updates data in real-time or with appropriate frequency and handles API rate limits properly.
```

### 4. Automated Report Generator with Natural Language Insights

**Description**: Create a system that generates professional reports from data with natural language explanations of trends and insights.

**Example Prompt**:
```
Build a Python application that generates professional automated reports from data with natural language insights:
1. Imports data from various sources (databases, Excel, CSV)
2. Performs comprehensive data analysis:
   - Summary statistics and trend identification
   - Anomaly detection
   - Correlation analysis and potential causation flags
3. Creates publication-quality visualizations using matplotlib, seaborn, and plotly
4. Generates natural language explanations for:
   - Key trends in the data
   - Significant changes from previous periods
   - Correlations and potential causal relationships
   - Actionable recommendations based on the data
5. Compiles everything into a formatted report (PDF, HTML, or PowerPoint)
6. Allows customization of report sections and depth of analysis

Include templates for different report types (executive summary, detailed analysis, periodic reports) and make the language generation customizable by industry.
```

### 5. Interactive Text-to-SQL Assistant

**Description**: Build a tool that translates natural language questions into SQL queries and displays the results.

**Example Prompt**:
```
Create an interactive text-to-SQL assistant using Python that:
1. Connects to various database types (PostgreSQL, MySQL, SQLite)
2. Allows users to describe their query in natural language
3. Translates natural language to SQL using LLM techniques
4. Shows the generated SQL query and allows the user to edit it if needed
5. Executes the query and displays results in a formatted table
6. Supports visualization of query results when appropriate
7. Maintains history of queries for reference
8. Learns from user corrections to improve future translations

Include safety measures to prevent SQL injection and destructive operations, and implement database schema analysis to improve query accuracy.
```

<a name="advanced-projects"></a>
## Advanced Projects (High Complexity)

### 1. Autonomous Data Science Assistant

**Description**: Build a system that can perform end-to-end data science tasks from raw data to insights with minimal human intervention.

**Example Prompt**:
```
Develop an autonomous data science system using Python that:
1. Takes raw data input in various formats (CSV, JSON, databases)
2. Automatically performs and iterates through the entire data science pipeline:
   - Data cleaning and preprocessing with multiple strategies
   - Feature engineering and selection
   - Model selection from a wide range of algorithms
   - Hyperparameter optimization
   - Evaluation across multiple metrics
3. Implements reinforcement learning to improve its decision-making process
4. Generates comprehensive reports explaining:
   - All decisions made during the pipeline
   - Alternative approaches considered
   - Confidence levels in results
   - Limitations and areas for human review
5. Provides an API and user interface for interaction and configuration
6. Allows human feedback to guide and improve the system

Include a monitoring system for model drift and data distribution changes, and implement appropriate logging for all decisions and processes.
```

### 2. Multi-agent Market Simulation System

**Description**: Create a multi-agent simulation of financial or economic markets using LLMs to model agent behavior and decision-making.

**Example Prompt**:
```
Create a multi-agent market simulation system in Python that:
1. Simulates multiple economic agents (consumers, producers, investors, regulators) in a market environment
2. Uses LLMs to model agent behavior and decision-making processes based on:
   - Current market conditions
   - Historical data
   - Agent-specific goals and constraints
   - Learning from past interactions
3. Incorporates realistic economic principles and behavioral economics
4. Allows configuration of different economic scenarios and policies
5. Visualizes market dynamics and agent interactions in real-time
6. Provides analysis tools to understand emergent behaviors and system dynamics
7. Supports "what-if" scenario testing for policy evaluation

Include mechanisms to calibrate agent behavior against real-world data and implement validation methods to assess simulation realism.
```

### 3. Explainable AI Framework for Critical Decisions

**Description**: Build a framework for creating highly explainable AI models for use in critical decision-making contexts like healthcare or finance.

**Example Prompt**:
```
Develop an explainable AI framework in Python for critical decision-making domains that:
1. Implements multiple model types with inherent explainability:
   - Enhanced decision trees with natural language explanations
   - Rule-based systems with confidence metrics
   - Bayesian networks with causal relationships
   - Custom neural networks with attention visualization
2. Provides multiple layers of explanation:
   - Feature importance and contribution analysis
   - Counterfactual explanations ("what would change the outcome")
   - Natural language explanations of model reasoning
   - Confidence intervals and uncertainty quantification
3. Includes visualization tools for model interpretation
4. Implements fairness metrics and bias detection
5. Allows domain experts to incorporate prior knowledge
6. Maintains detailed audit trails of all decisions
7. Supports regulatory compliance documentation generation

Design the framework to be adaptable across domains (healthcare, finance, legal) while maintaining domain-specific best practices.
```

### 4. Knowledge Graph Construction and Reasoning System

**Description**: Create a system that automatically builds knowledge graphs from unstructured text and can perform complex reasoning tasks.

**Example Prompt**:
```
Build a knowledge graph construction and reasoning system using Python that:
1. Processes large volumes of unstructured text data from various sources
2. Extracts entities, relationships, and attributes using NLP techniques
3. Constructs and maintains a queryable knowledge graph with:
   - Entity disambiguation and resolution
   - Relationship extraction and validation
   - Confidence scoring for all extracted information
   - Temporal aspects of knowledge (valid time periods)
4. Implements reasoning capabilities:
   - Path finding and relationship inference
   - Consistency checking and contradiction detection
   - Hypothesis testing against the knowledge base
   - Answering complex multi-hop questions
5. Provides visualization of knowledge subgraphs
6. Includes an API for integration with other systems
7. Continuously updates with new information while maintaining provenance

Implement methods to handle uncertainty and conflicting information, and include specialized capabilities for specific domains like scientific research or business intelligence.
```

### 5. Multimodal Data Fusion for Predictive Analytics

**Description**: Develop a system that combines data from multiple modalities (text, images, time series, structured data) for complex predictive tasks.

**Example Prompt**:
```
Create a multimodal data fusion system for predictive analytics that:
1. Ingests and processes multiple data types:
   - Structured data (databases, CSV)
   - Text documents and articles
   - Images and video frames
   - Time series signals
   - Geospatial data
2. Implements specialized preprocessing for each modality
3. Develops joint representations using advanced fusion techniques:
   - Early fusion (feature level)
   - Late fusion (decision level)
   - Hybrid approaches with attention mechanisms
4. Builds predictive models that leverage cross-modal patterns
5. Quantifies uncertainty across modalities
6. Handles missing modalities gracefully
7. Provides interpretable results that explain contribution of each modality
8. Includes a flexible pipeline for adding new data sources

Design the system to be domain-agnostic but include examples for healthcare (combining patient records, medical images, and device readings) and environmental monitoring (combining satellite imagery, sensor data, and textual reports).
```

## How to Use This Document

1. **Choose a project** that matches your skill level and interests
2. **Copy the example prompt** as a starting point for interacting with GitHub Copilot or other LLM tools
3. **Modify the prompt** to fit your specific needs and domain
4. **Iterate on the solution** by refining your prompts based on initial outputs
5. **Implement and expand** the generated code with your own expertise

Remember that LLM outputs are starting points - always validate the code, test thoroughly, and apply your domain knowledge to enhance the solutions.

## Contributing

Feel free to expand this document with your own project ideas and improved prompts. Share your implementations and experiences to help improve this resource.

---

*Note: When implementing these projects, always comply with ethical guidelines, data privacy regulations, and ensure proper attribution for any models or data used.*