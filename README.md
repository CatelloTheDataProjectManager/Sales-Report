## Sales Report with SQL & Pandas 📊
### Project One Overview
Welcome to my GitHub page, where I showcase my project for the portfolio a comprehensive Sales Report system. This project encompasses various stages, including Database Connection, Data Cleaning, and Data Reporting.

### Database Creation
- Entity and Property Definition (MCD)
- Associations and Relationships (MLD)
- MySQL Workbench Modeling (MPD)

[Notebook Jupyeter: Database Creation](https://github.com/CatelloTheDataProjectManager/Sales-Report/blob/main/Database_Creation.ipynb)

[MySQL EER Diagram](https://github.com/CatelloTheDataProjectManager/Sales-Report/blob/main/MySQL_EER_Diagram.png)

### Exploratory Data Analysis (EDA)

Delve into the depths of data analysis with the following components:

- SQL Queries for efficient data retrieval
- Thorough Data Cleaning procedures
- Engaging Data Visualization using Plotly
- Generate insightful PDF Reports for comprehensive presentation and analysis.

[Notebook Jupyeter: Sales Analysis](https://github.com/CatelloTheDataProjectManager/Sales-Report/blob/main/Sales_Analysis.ipynb)

Explore the code and documentation to gain a deeper understanding of the project's intricacies and its impact on enhancing data-driven decision-making. Your feedback and contributions are highly appreciated! 🚀

<img src="https://github.com/CatelloTheDataProjectManager/Sales-Report/raw/main/sales_report_image.jpg" alt="Sales Report Image" width="300">

## Sales Report with PowerBI 📈
### Project Two Overview
In this project, we will use PowerBI to create a comprehensive Sales Report system. The project encompasses various stages, including Database Connection, Data Extraction, Transformation, and Visualization.

### Database Connection and Data Import
We will establish a connection to the MySQL server, import the data, and execute SQL queries to explore the data.

### Data Extraction
We will extract data from the MySQL server to Power BI, where we will work with Power Query in Table view.

### Data Transformation
During the transformation phase, we will visualize the [Data Model ](https://github.com/CatelloTheDataProjectManager/Sales-Report/blob/main/Capture%20d%E2%80%99%C3%A9cran%202024-06-07%20131537.png) (Star Schema: Fact Table/Dimension Table) and use the [Power Query Editor/Transform Data for ETL](https://github.com/CatelloTheDataProjectManager/Sales-Report/blob/main/Capture%20d%E2%80%99%C3%A9cran%202024-06-07%20142143.png), transformation, data cleaning, data munging, and data wrangling. We will perform data filtering as in Excel and remove applied steps. We will also add columns, create conditional columns, and perform custom column transformations. We will ensure proper naming conventions for transformations and clean up columns. Finally, we will close and apply the transformations.

### Data Visualization
In this phase, we will load and visualize the data using various Power BI visualizations. We will create card visualizations and control visual properties through formatting and visual options. We will set the canvas settings to 1350x850 for optimal display. We will create stacked bar charts, selecting KPIs and formatting the X-axis and Y-axis, adding data labels, and displaying units. We will change the title and display the top N (5) values. We will also create slicers with vertical lists and format the data in table view (mmmm/yy). Finally, we will create line charts to display trends and enable cross-filtering by setting File/Options & Settings/Report Settings.

<img src="https://github.com/CatelloTheDataProjectManager/Sales-Report/blob/main/Sales_report_power_bi.png" alt="PowerBI Sales Report" width="600">

# Flask API for Data Visualization and Extraction 🕵️

This project demonstrates the automation of an API using Python and Flask to facilitate the visualization and extraction of data. The API enables users to efficiently retrieve, visualize, and analyze data.

## Installation

1. Clone the repository to your local machine.
2. Create and activate a virtual environment for dependency management.
3. Install the required dependencies listed in the `requirements.txt` file.

## Usage

1. Start the Flask application to run the API.
2. Access the API via your web browser or a tool like Postman at the provided local server URL.

## Endpoints

The API provides the following endpoints:
- `GET /data`: Fetches and displays data.
- `POST /data`: Adds new data to the database.
- `GET /visualize`: Generates a graphical visualization of the data.

![API](https://github.com/CatelloTheDataProjectManager/Sales-Report/blob/main/API.png)

# Dashboard using Streamlit 🚀

This project showcases the creation of an interactive dashboard using Streamlit for analyzing and visualizing coffee sales data. The dashboard allows users to explore sales metrics, view dynamic visualizations, and gain insights into their data effortlessly.

## Installation

1. Clone the repository to your local machine.
2. Ensure Python is installed, along with Streamlit.
3. Install the required dependencies listed in the `requirements.txt` file.

## Usage

1. Launch the dashboard by running the Streamlit application locally.
2. Access the interactive dashboard through your web browser using the provided local server URL.

## Code
You can find the code for the mortgage calculator [here](https://github.com/CatelloTheDataProjectManager/Sales-Report/blob/main/mortgage_calculator.py).

## Images
The following table includes the relevant images:

| Dashboard using Streamlit                                                                                   
|--------------------------------------------------------------------------------------------------------|
| ![Image 1](https://github.com/CatelloTheDataProjectManager/Sales-Report/blob/main/1.png) |
| ![Image 2](https://github.com/CatelloTheDataProjectManager/Sales-Report/blob/main/2.png) |
| ![Image 3](https://github.com/CatelloTheDataProjectManager/Sales-Report/blob/main/3.png) |


## Benefits of Enhancements

### Streamlit & Google Sheets: The Easiest "Database"
Integrating **Google Sheets** with Streamlit can simplify data management and serve as an easy-to-use "database." Benefits include:
- **Simplicity**: Google Sheets is intuitive and user-friendly, making it accessible for non-technical users.
- **Cloud-Based Storage**: Data is stored in the cloud, ensuring accessibility and reducing dependency on local storage.
- **Real-Time Updates**: Any edits to the Google Sheet are reflected live in the Streamlit application, allowing for seamless collaboration and data sharing.
- **Cost Efficiency**: Using Google Sheets as a lightweight database eliminates the need for more complex database setups.

### Add a User Authentication Service (Login Form) in Streamlit
Integrating a user authentication system can enhance the dashboard by:
- **Securing Data**: Ensures that only authorized users can access sensitive sales or customer data.
- **Custom User Experiences**: Allows personalized content and metrics tailored to each user after login.
- **Streamlined Access**: With a login system, users can save preferences, filters, or analysis for future sessions.
- **Ease of Implementation**: Streamlit offers libraries like `streamlit-authenticator` for quick and efficient authentication setup.

Adding these features not only increases usability but also transforms a simple dashboard into a scalable and secure tool for real-world business applications.
