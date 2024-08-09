# Entity Extraction Tool
This project is an Entity Extraction Tool built using Gradio and LangChain with GoogleGenerativeAI. It leverages the `Gemini 1.5 Pro` model to extract entities from text inputs, such as emails, and display them in a structured format using Markdown.

## Overview

The Entity Extraction Tool is designed to extract specific entities like names, locations, dates, and more from text data, with a primary focus on processing email content. The extracted entities are then displayed in a well-organized format, making it easier to analyze and utilize the information.

## Key Features

- **Entity Extraction:** Automatically identify and extract entities from the provided text.
- **User-Friendly Interface:** Simple and intuitive Gradio-based interface for easy interaction.
- **Markdown Rendering:** The extracted entities are displayed in a formatted manner using Markdown.
- **Adaptable:** While the main use case is email entity extraction, the tool can be applied to other text-based data sources as well.
  
## Use Cases
### 1. Email Entity Extraction
**Use Case:** Extracting key information from emails such as names, dates, locations, and more.

**Example:** Input an email body, and the tool will extract and display entities like sender names, dates mentioned, and any locations referenced.
### 2. Document Processing
**Use Case:** Parsing through large documents to extract essential information such as legal entities, dates, and locations.

**Example:** Input a section of a legal document to extract critical entities like company names, important dates, and referenced locations.

### 3. Customer Support Analysis
**Use Case:** Analyzing customer support emails or chat logs to identify important entities such as customer names, issue categories, and dates.

**Example:** Input a customer support email and extract details about the customer's name, issue description, and the date of the complaint.

### 4. Social Media Monitoring
**Use Case:** Extracting mentions of people, places, and events from social media posts.

**Example:** Input a social media post or tweet and extract entities like mentioned users, hashtags, locations, and event names.

## How It Works
- **Input:** The user inputs text data (e.g., an email body) into the provided Textbox.
- **Processing:** The Gemini 1.5 Pro model processes the input and extracts entities.
- **Output:** The extracted entities are displayed in a formatted manner using Markdown.
## Technology Stack
- Langchain
- Google Generative AI
- Gradio

### Try it out!!
------------------------
## [Hugging Face URL](https://huggingface.co/spaces/ahmadmac/Entity-Extraction)
