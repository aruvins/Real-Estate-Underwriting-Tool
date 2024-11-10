import streamlit as st
import boto3
import os
from dotenv import load_dotenv
from streamlit_cognito_auth import CognitoAuthenticator


# Initialize AWS clients
cognito_client = boto3.client('cognito-idp')
dynamodb = boto3.resource('dynamodb')
s3_client = boto3.client('s3')

load_dotenv()
# Cognito Authenticator setup
auth = CognitoAuthenticator(
    pool_id= os.getenv('COGNITO_USER_POOL_ID'),
    app_client_id= os.getenv('COGNITO_CLIENT_ID')
)

# Initialize the app
st.title("Login and Sign-up Page")

# User Authentication
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    action = st.radio("Select Action", ("Login", "Sign Up"))

    # Sign-up process
    if action == "Sign Up":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")

        if st.button("Sign Up"):
            response = cognito_client.sign_up(
                ClientId = os.getenv('COGNITO_CLIENT_ID'),
                Username=username,
                Password=password,
                UserAttributes=[{"Name": "email", "Value": email}],
            )
            
            st.success("Sign-up successful!")

    # Login process
    else:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
                try:
                    # Call the initiate_auth method from boto3 to authenticate the user
                    response = cognito_client.initiate_auth(
                        ClientId=os.getenv('COGNITO_CLIENT_ID'),
                        AuthFlow='USER_PASSWORD_AUTH',
                        AuthParameters={
                            'USERNAME': username,
                            'PASSWORD': password
                        }
                    )

                    # Check if authentication was successful by looking for the tokens
                    if 'AuthenticationResult' in response:
                        st.session_state.logged_in = True
                        st.success("Logged in successfully!")
                    else:
                        st.error("Login failed. Check your credentials.")
                
                except cognito_client.exceptions.NotAuthorizedException:
                    st.error("Incorrect username or password.")
                except cognito_client.exceptions.UserNotFoundException:
                    st.error("User not found.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

# If logged in, display project management options
if st.session_state.logged_in:
    st.title("Project Management")

    # Select project options
    project_table = dynamodb.Table("YourProjectTable")

    # Load project data from DynamoDB
    response = project_table.scan()
    projects = response.get("Items", [])

    st.write("Existing Projects")
    for project in projects:
        st.write(f"Project Name: {project['name']}, Company: {project['company']}")

    # Create a new project
    st.subheader("Create New Project")
    project_name = st.text_input("Project Name")
    company_name = st.text_input("Company Name")

    if st.button("Save Project"):
        project_table.put_item(
            Item={
                "name": project_name,
                "company": company_name,
            }
        )
        st.success("Project saved to DynamoDB!")

    # Save project data to S3
    if st.button("Save to S3"):
        s3_client.put_object(
            Bucket="your-bucket-name",
            Key=f"{project_name}.json",
            Body="Sample project data in JSON format"
        )
        st.success("Project saved to S3!")
