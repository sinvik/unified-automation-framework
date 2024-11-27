### Tools

- Python:3.9
- PyCharm OR any IDE
- Create & Activate Virtual Environment [Refer script](https://gitlab.com/pythonsolutions/unified-automation-framework/-/blob/master/scripts/setup.sh?ref_type=heads)

- JDK [click here to download](https://download.visualstudio.microsoft.com/download/pr/36e84f7f-e4ab-4788-b32b-64dc0a04b7c8/bfcec69d6a817cf926e94bfd567bcd11/microsoft-jdk-11.0.23-windows-x64.zip)
  1. Set JAVA_HOME:
     1. Click "Environment Variables" at the bottom of the System Properties window.
     2. Under "System variables", click "New" to create a new environment variable:
        1. Variable name: JAVA_HOME 
        2. Variable value: C:\Program Files\Java\jdk-11 (or the path to your JDK installation).
  2. Update PATH:
     1. Find the Path variable in the "System variables" list, select it, and click "Edit".
     2. Click "New" and add the path to the bin directory of the JDK installation, e.g., C:\Program Files\Java\jdk-11\bin.
     3. Click "OK" to close all the windows.
- Allure CLI [click here to download](https://objects.githubusercontent.com/github-production-release-asset-2e65be/59838788/e2ac4c8f-7a47-4ae7-8fb9-36c6f282831a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240610%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240610T175158Z&X-Amz-Expires=300&X-Amz-Signature=48fd7fbdbaa17ac911a1ddc8ddc391cc1951bb7425b5e1f06dc4c73504d305fe&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=59838788&response-content-disposition=attachment%3B%20filename%3Dallure-2.29.0.zip&response-content-type=application%2Foctet-stream)
     1. Extract and Set Path: 
        1. Extract the ZIP file to a directory, e.g., C:\allure.
        2. Add C:\allure\bin to your PATH environment variable.
- Set ENV variables in GitLab CICD Variables [click here](https://gitlab.com/pythonsolutions/unified-automation-framework/-/blob/master/.env?ref_type=heads)