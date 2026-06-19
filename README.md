AI Multi-Modal Damage Claim Verification System
HackerRank Orchestrate 2026

An Agentic AI system that automates insurance damage claim verification using image evidence, claim understanding, semantic reasoning, risk analysis, and explainable AI.

Problem Statement

Insurance claim verification is traditionally a manual process requiring human reviewers to inspect evidence, compare it with customer claims, and determine whether the claim is valid.

This process is:

Time-consuming
Expensive
Difficult to scale
Vulnerable to fraud

Our goal was to build an AI-powered system capable of analyzing damage claims automatically using both textual and visual evidence.

Solution Overview

The system combines multiple specialized AI agents to evaluate claims.

Workflow
User Claim
     ↓
Claim Agent
     ↓
Vision Agent
     ↓
Evidence Agent
     ↓
Risk Agent
     ↓
Decision Agent
     ↓
Confidence Scoring
     ↓
Fraud Scoring
     ↓
Final Decision
Agents
Claim Agent

Extracts structured information from claim text.

Example:

Input:

My car door got dented after an accident.

Output:

{
  "issue_type": "dent",
  "object_part": "door"
}
Vision Agent

Analyzes uploaded images using Gemini Vision.

Extracts:

Damage type
Damaged part
Severity
Image validity
Visibility of damage
Evidence Agent

Checks whether visual evidence satisfies the evidence requirements.

Risk Agent

Evaluates risk indicators and flags suspicious claims.

Decision Agent

Produces one of the following outcomes:

supported
contradicted
not_enough_information

The system also performs semantic matching between claim descriptions and detected damage.

Key Features
Multi-Modal AI (Vision + Text)
Agent-Based Architecture
Semantic Damage Matching
Confidence Scoring
Fraud Risk Assessment
Explainable AI
Streamlit Dashboard
Image Analysis Caching
Dashboard Features

The Streamlit dashboard provides:

Claim Overview
Claim Inspector
Evidence Viewer
Confidence Score Visualization
Fraud Risk Meter
AI Decision Explanation
Judge Demo Mode
Project Structure
code/
│
├── agents/
│   ├── claim_agent.py
│   ├── vision_agent.py
│   ├── evidence_agent.py
│   ├── risk_agent.py
│   └── decision_agent.py
│
├── cache/
├── generate_output.py
├── ui_app.py
├── output.csv
Installation

Install dependencies:

pip install -r requirements.txt
Generate Predictions
python generate_output.py

Output:

output.csv generated successfully
Launch Dashboard
streamlit run ui_app.py
Technologies Used
Python
Streamlit
Pandas
Pillow
Gemini Vision API
Future Improvements
Fine-grained severity estimation
Advanced fraud detection models
Improved semantic matching
Support for additional claim categories

Author

Anupriya Ranjan

Built for HackerRank Orchestrate 2026.