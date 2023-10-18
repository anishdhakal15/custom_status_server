# Jasmin SMS Gateway External API With Test

This guide provides instructions for adding callback API endpoints that will enable the storage and retrieval of batch SMS status

## Prerequisites

Before you begin, make sure you have the following prerequisites:

1. A working Jasmin SMS Gateway installation.
2. Python and pip installed on your system.

## Step 1: Start Jasmin Service

1. Start the Jasmin service .

## Step 2: Create Test User Credentials

1. Create a username "foo" and password "bar" for testing purposes. You can use these credentials for testing the Jasmin SMS Gateway.

## Step 3: Start Jasmin REST API Service

1. Start the Jasmin REST API service with the default configuration.

## Step 4: Set Up Status Server

1. Start the status_server.py script. This script accepts three GET requests:

   - `/api/success`: Accepts parameters batch_id, to, from, and statusText to save records in the database.
   - `/api/error`: Accepts parameters batch_id, to, from, and statusText to save records in the database.
   - `/api/batch`: Accepts parameters batch_id, to, and from to search and returns the status as a response.

## Step 5: Run send_request.py Script

1. Run the send_request.py script. This script allows you to change messages as needed for your testing purposes.


<!-- ## Additional Notes

- Make sure that the database setup, such as SQLite, is correctly configured and accessible by the status_server.py script.
- You can customize the status_server.py and send_request.py scripts to meet your specific requirements and configurations.

For more detailed configuration and advanced use cases, please refer to the official Jasmin SMS Gateway documentation. -->

## Required Python Modules

To run the provided scripts, you need to install the following Python modules using `pip`:

- flask
- flask_sqlalchemy

You can install them by running the following commands:

```shell
pip install flask
pip install flask_sqlalchemy
